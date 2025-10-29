"""CoinGlass REST API Client - Universal Interface

Provides unified access to all CoinGlass REST endpoints for liquidation heatmaps,
open interest, volume, and aggregated data across all exchanges.

Flow: ENV key → HTTP client → parse response → return clean data
"""

import asyncio
import logging
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone

import aiohttp

from src.utils.config_utils import get_config
from src.utils.error_utils import retry_on_failure

logger = logging.getLogger(__name__)

AGENT_NAME = "coinglass_rest"
BASE_URL = "https://open-api-v4.coinglass.com/api/futures"


class CoinGlassAPIError(RuntimeError):
    """Raised when CoinGlass returns a non-success response."""

    def __init__(self, message: str, code: Optional[str] = None):
        super().__init__(message)
        self.code = code

# Available endpoints
ENDPOINTS = {
    "heatmap_model1": "/liquidation/aggregated-heatmap/model1",
    "heatmap_model2": "/liquidation/aggregated-heatmap/model2",
    "heatmap_model3": "/liquidation/aggregated-heatmap/model3",
    "aggregated_map": "/liquidation/aggregated-map",
    "liquidation_history": "/liquidation/aggregated/history",
    "open_interest_history": "/openInterest/ohlc-aggregated-history",
}

# Timeframe options (called "range" in CoinGlass API)
TIMEFRAMES = {
    "12h": "12h",
    "24h": "24h",
    "3d": "3d",
    "7d": "7d",
    "30d": "30d",
    "90d": "90d",
    "180d": "180d",
    "1y": "1y",
}


class CoinGlassRestClient:
    """Universal REST client for CoinGlass API."""

    def __init__(self, config: Any):
        self.config = config
        self.api_key = config.coinglass_api_key
        self.session: Optional[aiohttp.ClientSession] = None

    async def initialize(self) -> None:
        """Initialize HTTP session."""
        self.session = aiohttp.ClientSession(
            headers={"CG-API-KEY": self.api_key, "accept": "application/json"},
            timeout=aiohttp.ClientTimeout(total=30)
        )
        logger.info(f"✅ {AGENT_NAME}: HTTP session initialized")

    async def close(self) -> None:
        """Close HTTP session."""
        if self.session:
            await self.session.close()
            logger.info(f"✅ {AGENT_NAME}: HTTP session closed")

    @retry_on_failure(max_retries=3, delay=2)
    async def _request(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make authenticated request to CoinGlass API."""
        if not self.session:
            raise RuntimeError("Session not initialized. Call initialize() first.")

        url = f"{BASE_URL}{endpoint}"

        try:
            async with self.session.get(url, params=params) as response:
                response.raise_for_status()
                data = await response.json()

                # Check CoinGlass response code
                if data.get("code") != "0":
                    error_msg = data.get("msg", "Unknown error")
                    logger.error(f"❌ {AGENT_NAME}: API error: {error_msg}")
                    raise CoinGlassAPIError(error_msg, data.get("code"))

                logger.debug(f"✅ {AGENT_NAME}: {endpoint} request successful")
                return data

        except aiohttp.ClientError as e:
            logger.error(f"❌ {AGENT_NAME}: Request failed: {e}")
            raise CoinGlassAPIError(str(e))

    async def get_liquidation_heatmap(
        self,
        symbol: str,
        timeframe: str = "7d",
        model: int = 1
    ) -> Dict[str, Any]:
        """Get liquidation heatmap data for a symbol.

        Args:
            symbol: Trading pair (e.g., "BTC", "ETH", "SOL")
            timeframe: One of: 12h, 24h, 3d, 7d, 30d, 90d, 180d, 1y
            model: Heatmap model (1, 2, or 3)

        Returns:
            Dict with NORMALIZED keys: y_axis (prices), liquidation_leverage_data, price_candlesticks
        """
        if timeframe not in TIMEFRAMES:
            raise ValueError(f"Invalid timeframe: {timeframe}. Must be one of {list(TIMEFRAMES.keys())}")

        endpoint_key = f"heatmap_model{model}"
        if endpoint_key not in ENDPOINTS:
            raise ValueError(f"Invalid model: {model}. Must be 1, 2, or 3")

        params = {
            "symbol": symbol,
            "range": timeframe
        }

        response = await self._request(ENDPOINTS[endpoint_key], params)
        raw_data = response.get("data", {})

        # Normalize response structure (Model 2 uses different keys for 180d/1y)
        return self._normalize_heatmap_response(raw_data)

    def _normalize_heatmap_response(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize heatmap response to consistent structure.

        CoinGlass Model 2 returns different key names for 180d/1y timeframes:
        - Standard (12h-90d): y_axis, liquidation_leverage_data, price_candlesticks
        - Long timeframes (180d-1y): y, liq, prices
        """
        if not data:
            return {}

        # Check if this is the alternate structure (180d/1y format)
        if "y" in data and "liq" in data and "prices" in data:
            return {
                "y_axis": data.get("y", []),
                "liquidation_leverage_data": data.get("liq", []),
                "price_candlesticks": data.get("prices", []),
                # Preserve additional fields
                "precision": data.get("precision"),
                "rangeLow": data.get("rangeLow"),
                "rangeHigh": data.get("rangeHigh"),
                "instrument": data.get("instrument")
            }

        # Already in standard format
        return data

    async def get_open_interest(
        self,
        symbol: str,
        exchange: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get current open interest for a symbol.

        Args:
            symbol: Trading pair (e.g., "BTC", "ETH", "SOL")
            exchange: Optional exchange filter (e.g., "Bybit", "Binance")

        Returns:
            Dict with current OI data across exchanges
        """
        params = {"symbol": symbol}
        if exchange:
            params["exchange"] = exchange

        response = await self._request(ENDPOINTS["open_interest"], params)
        return response.get("data", {})

    async def get_open_interest_history(
        self,
        symbol: str,
        timeframe: str = "7d"
    ) -> Dict[str, Any]:
        """Get historical open interest data.

        Args:
            symbol: Trading pair (e.g., "BTC", "ETH", "SOL")
            timeframe: One of: 1d, 7d

        Returns:
            Dict with historical OI data
        """
        if timeframe not in ["1d", "7d"]:
            raise ValueError("Timeframe must be '1d' or '7d' for OI history")

        params = {
            "symbol": symbol,
            "time_type": timeframe
        }

        response = await self._request(ENDPOINTS["open_interest_history"], params)
        return response.get("data", {})

    async def get_funding_rate(self, symbol: str) -> Dict[str, Any]:
        """Get current funding rates across exchanges.

        Args:
            symbol: Trading pair (e.g., "BTC", "ETH", "SOL")

        Returns:
            Dict with funding rate data
        """
        params = {"symbol": symbol}
        response = await self._request(ENDPOINTS["funding_rate"], params)
        return response.get("data", {})

    async def get_long_short_ratio(self, symbol: str) -> Dict[str, Any]:
        """Get long/short account ratio.

        Args:
            symbol: Trading pair (e.g., "BTC", "ETH", "SOL")

        Returns:
            Dict with long/short ratio data
        """
        params = {"symbol": symbol}
        response = await self._request(ENDPOINTS["long_short_ratio"], params)
        return response.get("data", {})


async def test_coinglass_api():
    """Test CoinGlass REST API with live key."""
    config = get_config()
    client = CoinGlassRestClient(config)

    try:
        await client.initialize()
        logger.info(f"🚀 {AGENT_NAME}: Testing CoinGlass REST API...")

        # Test 1: Liquidation Heatmap Model 1
        logger.info(f"📊 {AGENT_NAME}: Testing liquidation heatmap model 1...")
        heatmap = await client.get_liquidation_heatmap("BTC", timeframe="7d", model=1)
        y_axis = heatmap.get('yAxis', [])
        liq_data = heatmap.get('liquidationLeverageData', [])
        candles = heatmap.get('priceCandlesticks', [])
        logger.info(f"✅ {AGENT_NAME}: Heatmap received - {len(y_axis)} price levels, {len(liq_data)} data points, {len(candles)} candles")

        # Test 2: Different symbols
        for symbol in ["ETH", "SOL"]:
            logger.info(f"📊 {AGENT_NAME}: Testing {symbol}...")
            data = await client.get_liquidation_heatmap(symbol, timeframe="3d", model=1)
            logger.info(f"✅ {AGENT_NAME}: {symbol} data received")

        logger.info(f"✅ {AGENT_NAME}: All API tests passed!")

    except Exception as e:
        logger.error(f"❌ {AGENT_NAME}: Test failed: {e}")
        raise
    finally:
        await client.close()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    asyncio.run(test_coinglass_api())
