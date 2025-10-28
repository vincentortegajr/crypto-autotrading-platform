"""
TimescaleDB utilities for Vince Quant Whale Stack + Polymarket Oracle Helix.

Provides connection pooling, query execution, and data insertion functions
for both perps (yang) and polymarket (yin) verticals. Supports hypertables
for time-series data and fusion hooks for hybrid signals.

Author: Vince Quant Whale Stack
"""

import asyncio
import logging
from typing import Any, Dict, List, Optional, Tuple, Union
from contextlib import asynccontextmanager
from dataclasses import dataclass
import datetime

import asyncpg
from asyncpg import Pool, Connection
from asyncpg.exceptions import PostgresError

from .config_utils import Config

logger = logging.getLogger(__name__)


@dataclass
class DBConfig:
    """Database configuration for TimescaleDB connections."""
    host: str
    port: int
    database: str
    user: str
    password: str
    min_size: int = 5
    max_size: int = 20
    command_timeout: float = 60.0


class TimescaleUtils:
    """TimescaleDB connection and query utilities."""

    def __init__(self, config: Config):
        self.config = config
        self._pool: Optional[Pool] = None
        self._db_config = DBConfig(
            host=config.timescale_db_host,
            port=config.timescale_db_port,
            database=config.timescale_db_name,
            user=config.timescale_db_user,
            password=config.timescale_db_pass,
            min_size=5,  # Default since not in config
            max_size=20,  # Default
            command_timeout=60.0  # Default
        )

    async def initialize_pool(self) -> None:
        """Initialize the asyncpg connection pool."""
        try:
            self._pool = await asyncpg.create_pool(
                host=self._db_config.host,
                port=self._db_config.port,
                database=self._db_config.database,
                user=self._db_config.user,
                password=self._db_config.password,
                min_size=self._db_config.min_size,
                max_size=self._db_config.max_size,
                command_timeout=self._db_config.command_timeout
            )
            logger.info(f"TimescaleDB pool initialized with {self._db_config.min_size}-{self._db_config.max_size} connections")
        except Exception as e:
            logger.error(f"Failed to initialize TimescaleDB pool: {e}")
            raise

    async def close_pool(self) -> None:
        """Close the connection pool."""
        if self._pool:
            await self._pool.close()
            logger.info("TimescaleDB pool closed")

    @asynccontextmanager
    async def get_connection(self):
        """Context manager for getting a database connection."""
        if not self._pool:
            raise RuntimeError("Database pool not initialized. Call initialize_pool() first.")

        conn = await self._pool.acquire()
        try:
            yield conn
        finally:
            await self._pool.release(conn)

    async def execute_query(self, query: str, *args, **kwargs) -> List[asyncpg.Record]:
        """Execute a SELECT query and return results."""
        async with self.get_connection() as conn:
            try:
                return await conn.fetch(query, *args, **kwargs)
            except PostgresError as e:
                logger.error(f"Query execution failed: {query} - {e}")
                raise

    async def execute_command(self, command: str, *args, **kwargs) -> str:
        """Execute a command (INSERT, UPDATE, DELETE) and return status."""
        async with self.get_connection() as conn:
            try:
                result = await conn.execute(command, *args, **kwargs)
                return result
            except PostgresError as e:
                logger.error(f"Command execution failed: {command} - {e}")
                raise

    async def execute_many(self, command: str, args_list: List[Tuple]) -> None:
        """Execute a command with multiple parameter sets."""
        async with self.get_connection() as conn:
            try:
                await conn.executemany(command, args_list)
            except PostgresError as e:
                logger.error(f"Execute many failed: {command} - {e}")
                raise

    # Perps (Yang) data insertion functions

    async def insert_liquidation_data(self, symbol: str, timestamp: str, price: float,
                                    leverage: float, side: str, amount_usd: float,
                                    vertical: str = 'perps') -> None:
        """Insert liquidation data into hypertable."""
        query = """
        INSERT INTO liquidations (symbol, timestamp, price, leverage, side, amount_usd, vertical)
        VALUES ($1, $2, $3, $4, $5, $6, $7)
        """
        await self.execute_command(query, symbol, timestamp, price, leverage, side, amount_usd, vertical)

    async def insert_ohlcv_data(self, symbol: str, timestamp: str, open_price: float,
                              high_price: float, low_price: float, close_price: float,
                              volume: float, vertical: str = 'perps') -> None:
        """Insert OHLCV data into hypertable."""
        query = """
        INSERT INTO ohlcv (symbol, timestamp, open, high, low, close, volume, vertical)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
        """
        await self.execute_command(query, symbol, timestamp, open_price, high_price,
                                 low_price, close_price, volume, vertical)

    async def insert_trade_data(self, symbol: str, timestamp: str, price: float,
                              amount: float, side: str, vertical: str = 'perps') -> None:
        """Insert trade data into hypertable."""
        query = """
        INSERT INTO trades (symbol, timestamp, price, amount, side, vertical)
        VALUES ($1, $2, $3, $4, $5, $6)
        """
        await self.execute_command(query, symbol, timestamp, price, amount, side, vertical)

    # Polymarket (Yin) data insertion functions

    async def insert_poly_wallet(self, wallet_address: str, timestamp: str,
                               balance_usd: float, pnl_24h: float,
                               market_count: int, vertical: str = 'poly') -> None:
        """Insert polymarket wallet data into hypertable."""
        query = """
        INSERT INTO polymarket_wallets (wallet_address, timestamp, balance_usd, pnl_24h, market_count, vertical)
        VALUES ($1, $2, $3, $4, $5, $6)
        """
        await self.execute_command(query, wallet_address, timestamp, balance_usd,
                                 pnl_24h, market_count, vertical)

    async def insert_poly_signal(self, market_id: str, timestamp: str,
                               signal_type: str, confidence: float,
                               edge_estimate: float, vertical: str = 'poly') -> None:
        """Insert polymarket signal data into hypertable."""
        query = """
        INSERT INTO polymarket_signals (market_id, timestamp, signal_type, confidence, edge_estimate, vertical)
        VALUES ($1, $2, $3, $4, $5, $6)
        """
        await self.execute_command(query, market_id, timestamp, signal_type,
                                 confidence, edge_estimate, vertical)

    # Query functions for both verticals

    async def get_recent_liquidations(self, symbol: str, hours: int = 24) -> List[Dict[str, Any]]:
        """Get recent liquidation data for a symbol."""
        query = """
        SELECT * FROM liquidations
        WHERE symbol = $1 AND timestamp > NOW() - INTERVAL '%s hours'
        ORDER BY timestamp DESC
        """ % hours
        records = await self.execute_query(query, symbol)
        return [dict(record) for record in records]

    async def get_ohlcv_data(self, symbol: str, start_time: str, end_time: str) -> List[Dict[str, Any]]:
        """Get OHLCV data for a symbol within a time range."""
        query = """
        SELECT * FROM ohlcv
        WHERE symbol = $1 AND timestamp BETWEEN $2 AND $3
        ORDER BY timestamp ASC
        """
        records = await self.execute_query(query, symbol, start_time, end_time)
        return [dict(record) for record in records]

    async def get_poly_wallets_by_balance(self, min_balance: float = 1000.0) -> List[Dict[str, Any]]:
        """Get polymarket wallets above minimum balance."""
        query = """
        SELECT * FROM polymarket_wallets
        WHERE balance_usd >= $1
        ORDER BY balance_usd DESC
        """
        records = await self.execute_query(query, min_balance)
        return [dict(record) for record in records]

    async def get_poly_signals_by_confidence(self, min_confidence: float = 0.7) -> List[Dict[str, Any]]:
        """Get polymarket signals above minimum confidence."""
        query = """
        SELECT * FROM polymarket_signals
        WHERE confidence >= $1
        ORDER BY confidence DESC, timestamp DESC
        """
        records = await self.execute_query(query, min_confidence)
        return [dict(record) for record in records]

    # Fusion query functions (hybrid yang + yin)

    async def get_fusion_signals(self, oi_threshold: float = 0.7) -> List[Dict[str, Any]]:
        """Get hybrid signals where perps OI spikes align with poly signals."""
        query = """
        SELECT
            ps.*,
            l.symbol,
            l.amount_usd as liquidation_amount,
            l.timestamp as liq_timestamp
        FROM polymarket_signals ps
        JOIN liquidations l ON l.timestamp > ps.timestamp - INTERVAL '1 hour'
            AND l.timestamp < ps.timestamp + INTERVAL '1 hour'
        WHERE ps.confidence >= $1
            AND l.amount_usd > (SELECT AVG(amount_usd) * 1.5 FROM liquidations WHERE timestamp > NOW() - INTERVAL '24 hours')
        ORDER BY ps.confidence DESC, l.amount_usd DESC
        """
        records = await self.execute_query(query, oi_threshold)
        return [dict(record) for record in records]

    # Utility functions

    async def create_hypertables_if_not_exist(self) -> None:
        """Create hypertables for time-series data if they don't exist."""
        tables = [
            ("liquidations", "timestamp"),
            ("ohlcv", "timestamp"),
            ("trades", "timestamp"),
            ("polymarket_wallets", "timestamp"),
            ("polymarket_signals", "timestamp")
        ]

        for table_name, time_column in tables:
            # First create regular table if not exists
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL,
                symbol VARCHAR(50),
                timestamp TIMESTAMPTZ NOT NULL,
                price DECIMAL(20,8),
                leverage DECIMAL(10,2),
                side VARCHAR(10),
                amount_usd DECIMAL(20,2),
                open DECIMAL(20,8),
                high DECIMAL(20,8),
                low DECIMAL(20,8),
                close DECIMAL(20,8),
                volume DECIMAL(20,8),
                amount DECIMAL(20,8),
                wallet_address VARCHAR(100),
                balance_usd DECIMAL(20,2),
                pnl_24h DECIMAL(20,2),
                market_count INTEGER,
                market_id VARCHAR(100),
                signal_type VARCHAR(50),
                confidence DECIMAL(5,4),
                edge_estimate DECIMAL(10,4),
                vertical VARCHAR(10) NOT NULL DEFAULT 'perps'
            );
            """
            await self.execute_command(create_table_query)

            # Convert to hypertable if not already
            hypertable_query = f"""
            SELECT create_hypertable('{table_name}', '{time_column}', if_not_exists => TRUE);
            """
            try:
                await self.execute_command(hypertable_query)
                logger.info(f"Hypertable {table_name} created or already exists")
            except PostgresError as e:
                if "already a hypertable" not in str(e):
                    logger.warning(f"Could not create hypertable {table_name}: {e}")

    async def health_check(self) -> bool:
        """Check database connectivity and basic functionality."""
        try:
            result = await self.execute_query("SELECT 1 as health_check")
            return len(result) > 0 and result[0]['health_check'] == 1
        except Exception as e:
            logger.error(f"Database health check failed: {e}")
            return False


# Global instance for singleton pattern
_db_instance: Optional[TimescaleUtils] = None


async def get_db_utils(config: Config) -> TimescaleUtils:
    """Get singleton database utilities instance."""
    global _db_instance
    if _db_instance is None:
        _db_instance = TimescaleUtils(config)
        await _db_instance.initialize_pool()
    return _db_instance


async def test_db_connection():
    """Test function for database connectivity."""
    config = Config()
    db = TimescaleUtils(config)

    try:
        await db.initialize_pool()
        logger.info("Database pool initialized successfully")

        # Test health check
        healthy = await db.health_check()
        if healthy:
            logger.info("Database health check passed")
        else:
            logger.error("Database health check failed")

        # Create hypertables
        await db.create_hypertables_if_not_exist()
        logger.info("Hypertables created successfully")

        # Test insertions
        await db.insert_liquidation_data(
            symbol="BTCUSDT",
            timestamp=datetime.datetime.fromisoformat("2024-01-01T12:00:00+00:00"),
            price=45000.0,
            leverage=25.0,
            side="long",
            amount_usd=100000.0
        )
        logger.info("Test liquidation data inserted")

        await db.insert_poly_wallet(
            wallet_address="0x1234567890abcdef",
            timestamp=datetime.datetime.fromisoformat("2024-01-01T12:00:00+00:00"),
            balance_usd=50000.0,
            pnl_24h=2500.0,
            market_count=15
        )
        logger.info("Test poly wallet data inserted")

        logger.info("All database tests passed successfully!")

    except Exception as e:
        logger.error(f"Database test failed: {e}")
        raise
    finally:
        await db.close_pool()


if __name__ == "__main__":
    # Run test when executed directly
    logging.basicConfig(level=logging.INFO)
    asyncio.run(test_db_connection())