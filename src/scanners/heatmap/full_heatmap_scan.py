"""Complete Liquidation Heatmap Scanner - ALL MODELS, ALL TIMEFRAMES, ALL COINS

Scans EVERY Bybit perpetual across ALL 3 CoinGlass models and ALL 8 timeframes.
This is the PRIMARY data collector for the liquidation hunting strategy.

SCOPE:
- 435+ Bybit USDT perpetuals (dynamically fetched)
- 3 models (model1, model2, model3)
- 8 timeframes (12h, 24h, 3d, 7d, 30d, 90d, 180d, 1y)
- Total: ~10,440 API calls per scan cycle

Flow: fetch coin list → loop all combinations → store in DB → publish to Redis
"""

import asyncio
import json
import logging
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from src.scanners.heatmap.coinglass_rest import CoinGlassRestClient, CoinGlassAPIError
from src.scanners.heatmap.get_bybit_perps import get_bybit_perps
from src.utils.config_utils import get_config
from src.utils.redis_utils import get_redis_utils
from src.utils.timescale_utils import get_db_utils

logger = logging.getLogger(__name__)

AGENT_NAME = "full_heatmap_scan"
SCAN_INTERVAL = 300  # 5 minutes between full cycles
TIMEFRAMES = ["12h", "24h", "3d", "7d", "30d", "90d", "180d", "1y"]  # ALL 8 timeframes
MODELS = [1, 2, 3]  # ALL 3 models
REQUESTS_PER_SECOND = 2  # Rate limiting: 2 requests/sec = 120/min = safe buffer under Professional plan limits
INTERNAL_ERROR_THRESHOLD = 15  # after this many in a row, pause
INTERNAL_ERROR_COOLDOWN = 60  # seconds to wait when CoinGlass keeps failing


class FullHeatmapScanner:
    """Scans ALL liquidation heatmap data across all models, timeframes, and coins."""

    def __init__(self, config: Any):
        self.config = config
        self.coinglass_client = CoinGlassRestClient(config)
        self.db_utils = None
        self.redis_utils = None
        self.running = False
        self.coin_list: List[str] = []
        self.internal_error_streak = 0

    async def initialize(self) -> None:
        """Initialize all connections and fetch coin list."""
        await self.coinglass_client.initialize()
        self.db_utils = await get_db_utils(self.config)
        self.redis_utils = await get_redis_utils(self.config)

        # Fetch complete Bybit perps list
        self.coin_list = await get_bybit_perps()
        logger.info(f"✅ {AGENT_NAME}: Initialized with {len(self.coin_list)} coins")

    async def _scan_single_combination(
        self, symbol: str, timeframe: str, model: int
    ) -> Optional[Dict[str, Any]]:
        """Pull heatmap data for ONE combination (symbol + timeframe + model)."""
        try:
            heatmap = await self.coinglass_client.get_liquidation_heatmap(
                symbol=symbol,
                timeframe=timeframe,
                model=model
            )

            if not heatmap:
                logger.debug(f"⚠️ {AGENT_NAME}: No data for {symbol} {timeframe} model{model}")
                return None

            # Parse heatmap structure (API returns snake_case keys)
            y_axis = heatmap.get('y_axis', [])
            liq_data = heatmap.get('liquidation_leverage_data', [])
            candles = heatmap.get('price_candlesticks', [])

            if not liq_data:
                logger.debug(f"⚠️ {AGENT_NAME}: Empty data for {symbol} {timeframe} model{model}")
                return None

            # reset internal error streak on success
            self.internal_error_streak = 0

            return {
                "symbol": symbol,
                "timeframe": timeframe,
                "model": model,
                "y_axis": y_axis,
                "liquidation_data": liq_data,
                "candles": candles,
                "timestamp": datetime.now(timezone.utc)
            }

        except CoinGlassAPIError as exc:
            message = str(exc).lower()
            if "internal error" in message:
                self.internal_error_streak += 1
                if self.internal_error_streak >= INTERNAL_ERROR_THRESHOLD:
                    logger.warning(
                        f"⚠️ {AGENT_NAME}: CoinGlass internal errors hit {self.internal_error_streak}. "
                        f"Cooling down for {INTERNAL_ERROR_COOLDOWN}s."
                    )
                    await asyncio.sleep(INTERNAL_ERROR_COOLDOWN)
                    self.internal_error_streak = 0
                else:
                    await asyncio.sleep(1)  # brief pause to avoid hammering
            else:
                logger.error(
                    f"❌ {AGENT_NAME}: API failure {symbol} {timeframe} model{model}: {exc}"
                )
            return None
        except Exception as exc:
            logger.error(f"❌ {AGENT_NAME}: Failed {symbol} {timeframe} model{model}: {exc}")
            return None

    async def _store_heatmap(self, data: Dict[str, Any]) -> None:
        """Store heatmap data in TimescaleDB."""
        if not self.db_utils:
            return

        try:
            query = """
                INSERT INTO liquidation_data_raw (
                    symbol, timeframe, timestamp, y_axis, liquidation_data, candles, metadata
                )
                VALUES ($1, $2, $3, $4, $5, $6, $7)
                ON CONFLICT (symbol, timeframe, timestamp) DO NOTHING
            """

            metadata = {
                "source": AGENT_NAME,
                "model": f"model{data['model']}",
                "num_levels": len(data["y_axis"]),
                "num_points": len(data["liquidation_data"]),
                "num_candles": len(data["candles"])
            }

            # Store with model number in timeframe to differentiate
            timeframe_key = f"{data['timeframe']}_m{data['model']}"

            await self.db_utils.execute_command(
                query,
                data["symbol"],
                timeframe_key,
                data["timestamp"],
                json.dumps(data["y_axis"]),
                json.dumps(data["liquidation_data"]),
                json.dumps(data["candles"]),
                json.dumps(metadata)
            )

        except Exception as exc:
            logger.error(f"❌ {AGENT_NAME}: Failed to store heatmap: {exc}")

    async def _publish_heatmap(self, data: Dict[str, Any]) -> None:
        """Publish heatmap to Redis for real-time consumption."""
        if not self.redis_utils:
            return

        try:
            payload = {
                "symbol": data["symbol"],
                "timeframe": data["timeframe"],
                "model": data["model"],
                "timestamp": data["timestamp"].isoformat().replace("+00:00", "Z"),
                "num_levels": len(data["y_axis"]),
                "num_points": len(data["liquidation_data"]),
                "source": AGENT_NAME
            }

            await self.redis_utils.publish("heatmap_updates", json.dumps(payload))

        except Exception as exc:
            logger.error(f"❌ {AGENT_NAME}: Failed to publish heatmap: {exc}")

    async def scan_all_combinations(self) -> None:
        """Scan ALL coins × ALL timeframes × ALL models (full universe)."""
        total_combinations = len(self.coin_list) * len(TIMEFRAMES) * len(MODELS)
        logger.info(
            f"🔄 {AGENT_NAME}: Starting FULL scan - "
            f"{len(self.coin_list)} coins × {len(TIMEFRAMES)} timeframes × {len(MODELS)} models "
            f"= {total_combinations} combinations"
        )

        scanned = 0
        stored = 0
        failed = 0

        for symbol in self.coin_list:
            for model in MODELS:
                for timeframe in TIMEFRAMES:
                    heatmap_data = await self._scan_single_combination(symbol, timeframe, model)

                    if heatmap_data:
                        await self._store_heatmap(heatmap_data)
                        await self._publish_heatmap(heatmap_data)
                        stored += 1
                    else:
                        failed += 1

                    scanned += 1

                    # Rate limiting: wait between requests
                    await asyncio.sleep(1 / REQUESTS_PER_SECOND)

                    # Progress logging every 100 combinations
                    if scanned % 100 == 0:
                        progress = (scanned / total_combinations) * 100
                        logger.info(
                            f"📊 {AGENT_NAME}: Progress {progress:.1f}% "
                            f"({scanned}/{total_combinations}) - "
                            f"✅ {stored} stored, ❌ {failed} failed"
                        )

        logger.info(
            f"✅ {AGENT_NAME}: Scan cycle complete - "
            f"{scanned} scanned, {stored} stored, {failed} failed"
        )

    async def run(self) -> None:
        """Main run loop - continuous scanning every 5 minutes."""
        if not self.db_utils or not self.redis_utils:
            await self.initialize()

        self.running = True
        logger.info(f"🚀 {AGENT_NAME}: Starting continuous full heatmap scanning...")

        while self.running:
            try:
                await self.scan_all_combinations()
                logger.info(f"⏳ {AGENT_NAME}: Waiting {SCAN_INTERVAL}s before next cycle...")
                await asyncio.sleep(SCAN_INTERVAL)

            except asyncio.CancelledError:
                logger.info(f"🛑 {AGENT_NAME}: Cancelled")
                break
            except Exception as exc:
                logger.error(f"❌ {AGENT_NAME}: Scan cycle failed: {exc}")
                await asyncio.sleep(30)  # Wait 30s on error before retry

    async def stop(self) -> None:
        """Stop the scanner gracefully."""
        self.running = False
        if self.coinglass_client:
            await self.coinglass_client.close()
        logger.info(f"🛑 {AGENT_NAME}: Stopped")


async def main() -> None:
    """Test entry point - run single scan cycle."""
    config = get_config()
    scanner = FullHeatmapScanner(config)

    try:
        await scanner.initialize()
        logger.info(f"🧪 {AGENT_NAME}: Running single test scan cycle...")
        await scanner.scan_all_combinations()
        logger.info(f"✅ {AGENT_NAME}: Test scan complete")
    except Exception as exc:
        logger.error(f"❌ {AGENT_NAME}: Test failed: {exc}")
        raise
    finally:
        await scanner.stop()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    asyncio.run(main())
