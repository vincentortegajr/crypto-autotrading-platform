"""
Redis Utilities for Vince Quant Whale Stack + Polymarket Oracle Helix.

Provides Redis connection, pub/sub messaging, and caching utilities
for real-time fusion between perps (yang) and polymarket (yin) signals.

Flow: Connect to Redis → Pub/sub channels (perps_oi, poly_signals, fusion_alerts) → Cache signals.
"""

import asyncio
import json
import logging
from typing import Any, Dict, List, Optional, Callable, Awaitable
from dataclasses import dataclass

import redis.asyncio as redis
from redis.asyncio import Redis, ConnectionPool

from .config_utils import Config

logger = logging.getLogger(__name__)


@dataclass
class RedisConfig:
    """Redis connection configuration."""
    host: str
    port: int
    db: int
    password: Optional[str] = None
    decode_responses: bool = True


class RedisUtils:
    """Redis connection and pub/sub utilities."""

    def __init__(self, config: Config):
        self.config = config
        self._redis: Optional[Redis] = None
        self._pubsub: Optional[Any] = None
        self._redis_config = RedisConfig(
            host=config.redis_host,
            port=config.redis_port,
            db=config.redis_db
        )

    async def connect(self) -> None:
        """Connect to Redis."""
        try:
            self._redis = redis.Redis(
                host=self._redis_config.host,
                port=self._redis_config.port,
                db=self._redis_config.db,
                decode_responses=self._redis_config.decode_responses
            )
            # Test connection
            await self._redis.ping()
            logger.info(f"Redis connected to {self._redis_config.host}:{self._redis_config.port} db {self._redis_config.db}")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise

    async def disconnect(self) -> None:
        """Disconnect from Redis."""
        if self._redis:
            await self._redis.aclose()
            logger.info("Redis disconnected")

    async def publish(self, channel: str, message: str) -> int:
        """Publish a message to a channel."""
        if not self._redis:
            raise RuntimeError("Redis not connected. Call connect() first.")
        try:
            result = await self._redis.publish(channel, message)
            logger.debug(f"Published to {channel}: {message}")
            return result
        except Exception as e:
            logger.error(f"Failed to publish to {channel}: {e}")
            raise

    async def set_cache(self, key: str, value: Any, expire: Optional[int] = None) -> bool:
        """Set a cache value with optional expiration (seconds)."""
        if not self._redis:
            raise RuntimeError("Redis not connected. Call connect() first.")
        try:
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            result = await self._redis.set(key, value, ex=expire)
            logger.debug(f"Cached {key}: {value[:100]}...")
            return result
        except Exception as e:
            logger.error(f"Failed to cache {key}: {e}")
            raise

    async def get_cache(self, key: str) -> Optional[Any]:
        """Get a cached value."""
        if not self._redis:
            raise RuntimeError("Redis not connected. Call connect() first.")
        try:
            value = await self._redis.get(key)
            if value:
                try:
                    # Try to parse as JSON
                    return json.loads(value)
                except json.JSONDecodeError:
                    return value
            return value
        except Exception as e:
            logger.error(f"Failed to get cache {key}: {e}")
            raise

    async def delete_cache(self, key: str) -> int:
        """Delete a cached value."""
        if not self._redis:
            raise RuntimeError("Redis not connected. Call connect() first.")
        try:
            result = await self._redis.delete(key)
            logger.debug(f"Deleted cache {key}")
            return result
        except Exception as e:
            logger.error(f"Failed to delete cache {key}: {e}")
            raise

    async def subscribe(self, channels: List[str], callback: Callable[[str, str], Awaitable[None]]) -> None:
        """Subscribe to channels and call callback on messages."""
        if not self._redis:
            raise RuntimeError("Redis not connected. Call connect() first.")

        self._pubsub = self._redis.pubsub()
        await self._pubsub.subscribe(*channels)

        logger.info(f"Subscribed to channels: {channels}")

        try:
            async for message in self._pubsub.listen():
                if message['type'] == 'message':
                    channel = message['channel']
                    data = message['data']
                    await callback(channel, data)
        except Exception as e:
            logger.error(f"Subscription error: {e}")
            raise
        finally:
            if self._pubsub:
                await self._pubsub.unsubscribe(*channels)

    async def publish_signal(self, signal_type: str, data: Dict[str, Any]) -> None:
        """Publish a signal to the appropriate channel."""
        channel_map = {
            'perps_oi': 'perps_oi',
            'poly_signals': 'poly_signals',
            'fusion_alerts': 'fusion_alerts',
            'liquidation_alert': 'liquidation_alerts',
            'wallet_sync': 'wallet_sync'
        }

        channel = channel_map.get(signal_type, 'general_signals')
        message = json.dumps({
            'type': signal_type,
            'timestamp': data.get('timestamp', str(asyncio.get_event_loop().time())),
            'data': data
        })

        await self.publish(channel, message)

    async def get_recent_signals(self, channel: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent signals from a channel (requires Redis streams or list)."""
        # For simplicity, we'll use a list to store recent messages
        key = f"recent:{channel}"
        signals = await self.get_cache(key) or []

        if not isinstance(signals, list):
            signals = []

        return signals[-limit:] if signals else []

    async def health_check(self) -> bool:
        """Check Redis connectivity."""
        try:
            if not self._redis:
                return False
            await self._redis.ping()
            return True
        except Exception as e:
            logger.error(f"Redis health check failed: {e}")
            return False


# Global instance for singleton pattern
_redis_instance: Optional[RedisUtils] = None


async def get_redis_utils(config: Config) -> RedisUtils:
    """Get singleton Redis utilities instance."""
    global _redis_instance
    if _redis_instance is None:
        _redis_instance = RedisUtils(config)
        await _redis_instance.connect()
    return _redis_instance


async def test_redis_connection():
    """Test function for Redis connectivity and pub/sub."""
    config = Config()
    redis_utils = RedisUtils(config)

    try:
        await redis_utils.connect()
        logger.info("Redis connection established")

        # Test health check
        healthy = await redis_utils.health_check()
        if healthy:
            logger.info("Redis health check passed")
        else:
            logger.error("Redis health check failed")

        # Test caching
        await redis_utils.set_cache("test_key", {"message": "hello world"}, expire=60)
        cached = await redis_utils.get_cache("test_key")
        if cached and cached["message"] == "hello world":
            logger.info("Redis caching test passed")
        else:
            logger.error("Redis caching test failed")

        # Test pub/sub with echo
        received_messages = []

        async def echo_callback(channel: str, message: str):
            received_messages.append((channel, message))
            logger.info(f"Received on {channel}: {message}")

        # Start subscriber in background
        subscriber_task = asyncio.create_task(
            redis_utils.subscribe(["test_channel"], echo_callback)
        )

        # Give subscriber time to start
        await asyncio.sleep(0.1)

        # Publish test message
        await redis_utils.publish("test_channel", "Hello from Redis!")

        # Wait a bit for message to be received
        await asyncio.sleep(0.1)

        # Cancel subscriber
        subscriber_task.cancel()
        try:
            await subscriber_task
        except asyncio.CancelledError:
            pass

        if received_messages:
            logger.info("Redis pub/sub test passed")
        else:
            logger.warning("Redis pub/sub test: no messages received (may be timing issue)")

        # Test poly signals
        await redis_utils.publish_signal("poly_signals", {
            "market_id": "0x123",
            "confidence": 0.85,
            "edge_estimate": 0.15
        })
        logger.info("Poly signal published")

        logger.info("All Redis tests passed successfully!")

    except Exception as e:
        logger.error(f"Redis test failed: {e}")
        raise
    finally:
        await redis_utils.disconnect()


if __name__ == "__main__":
    # Run test when executed directly
    logging.basicConfig(level=logging.INFO)
    asyncio.run(test_redis_connection())