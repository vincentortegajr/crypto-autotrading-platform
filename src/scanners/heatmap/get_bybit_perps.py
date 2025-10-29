"""Bybit Perpetuals List Fetcher

Fetches the complete list of USDT perpetual contracts from Bybit API.
This list is used by all heatmap scanners to know which coins to scan.

Flow: call Bybit API → parse response → return clean coin list (BTC, ETH, SOL, etc.)
"""

import asyncio
import logging
from typing import List

import aiohttp

logger = logging.getLogger(__name__)

BYBIT_INSTRUMENTS_URL = "https://api.bybit.com/v5/market/instruments-info"


async def get_bybit_perps() -> List[str]:
    """Fetch all USDT perpetual contract symbols from Bybit.

    Returns:
        List of base symbols (e.g., ["BTC", "ETH", "SOL", ...])
    """
    try:
        async with aiohttp.ClientSession() as session:
            params = {
                "category": "linear",  # Linear perpetuals
                "status": "Trading"     # Only active contracts
            }

            async with session.get(BYBIT_INSTRUMENTS_URL, params=params, timeout=aiohttp.ClientTimeout(total=30)) as response:
                response.raise_for_status()
                data = await response.json()

                if data.get("retCode") != 0:
                    logger.error(f"❌ Bybit API error: {data.get('retMsg')}")
                    return []

                # Extract USDT perps only
                instruments = data.get("result", {}).get("list", [])
                usdt_perps = []

                for instrument in instruments:
                    symbol = instrument.get("symbol", "")
                    if symbol.endswith("USDT") and ":" not in symbol:  # Exclude inverse and dated contracts
                        base_symbol = symbol.replace("USDT", "")
                        usdt_perps.append(base_symbol)

                logger.info(f"✅ Found {len(usdt_perps)} Bybit USDT perpetual contracts")
                return sorted(usdt_perps)

    except Exception as exc:
        logger.error(f"❌ Failed to fetch Bybit perps: {exc}")
        return []


async def main():
    """Test the Bybit perps fetcher."""
    logging.basicConfig(level=logging.INFO)

    coins = await get_bybit_perps()
    print(f"\n📊 Total Bybit USDT Perpetuals: {len(coins)}")
    print(f"\n🪙 First 20 coins: {coins[:20]}")
    print(f"\n🪙 Sample popular coins:")
    for coin in ["BTC", "ETH", "SOL", "XRP", "DOGE"]:
        if coin in coins:
            print(f"   ✅ {coin}")
        else:
            print(f"   ❌ {coin} NOT FOUND")


if __name__ == "__main__":
    asyncio.run(main())
