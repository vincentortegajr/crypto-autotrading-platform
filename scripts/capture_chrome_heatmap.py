#!/usr/bin/env python3
"""
Capture the CoinGlass liquidation heatmap via the Chrome DevTools MCP server.

Uses FastMCP's NodeStdioTransport to launch chrome-devtools-mcp locally,
automates the consent dismissal and timeframe switch, then saves a full-page
PNG screenshot for comparison against the Playwright MCP flow.
"""

import argparse
import asyncio
import re
from pathlib import Path

from fastmcp.client.client import Client
from fastmcp.client.transports import NodeStdioTransport

REPO_ROOT = Path(__file__).resolve().parents[1]
CHROME_SCRIPT = (REPO_ROOT / "node_modules" / "chrome-devtools-mcp" / "build" / "src" / "index.js").resolve()
TARGET_URL = "https://www.coinglass.com/pro/futures/LiquidationHeatMapNew"


def _build_timeframe_regex(label: str) -> str:
    escaped = re.escape(label.strip())
    return escaped.replace("\\ ", "\\s*")


async def capture(timeframe: str, output_path: Path, wait_timeout: int) -> None:
    timeframe = timeframe.strip()
    output_path = output_path.resolve()
    transport = NodeStdioTransport(CHROME_SCRIPT)
    client = Client(transport)

    async with client:
        await client.call_tool(
            "new_page",
            {
                "url": TARGET_URL,
                "timeout": 0,
            },
        )

        # Allow initial UI to settle
        await asyncio.sleep(5.0)

        consent_result = await client.call_tool(
            "evaluate_script",
            {
                "function": """
() => {
  const btn = document.querySelector('.fc-button.fc-cta-consent, .fc-button.fc-data-preferences-accept-all');
  if (btn) {
    btn.click();
    return 'consent-clicked';
  }
  return 'consent-absent';
}
                """,
            },
        )
        print("Consent:", consent_result.data or consent_result.structured_content or consent_result.content)

        try:
            await client.call_tool(
                "wait_for",
                {
                    "text": timeframe,
                    "timeout": wait_timeout,
                },
            )
        except Exception:
            await client.call_tool(
                "wait_for",
                {
                    "text": "24 hour",
                    "timeout": wait_timeout,
                },
            )

        dropdown_result = await client.call_tool(
            "evaluate_script",
            {
                "function": f"""
() => {{
  const dropdown = Array.from(document.querySelectorAll('button'))
    .find((el) => /24\\s*hour/i.test(el.textContent || ''));
  if (dropdown) {{
    dropdown.click();
    return 'dropdown-opened';
  }}
  return 'dropdown-missing';
}}
                """,
            },
        )
        print("Dropdown:", dropdown_result.data or dropdown_result.structured_content or dropdown_result.content)

        await asyncio.sleep(1.0)

        timeframe_regex = _build_timeframe_regex(timeframe)
        select_result = await client.call_tool(
            "evaluate_script",
            {
                "function": f"""
() => {{
  const option = Array.from(document.querySelectorAll('[role="option"], button'))
    .find((el) => /{timeframe_regex}/i.test(el.textContent || ''));
  if (option) {{
    option.click();
    return 'option-selected';
  }}
  return 'option-missing';
}}
                """,
            },
        )
        print("Timeslot:", select_result.data or select_result.structured_content or select_result.content)

        await asyncio.sleep(5.0)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        await client.call_tool(
            "take_screenshot",
            {
                "fullPage": True,
                "filePath": str(output_path),
            },
        )
        print(f"Screenshot saved to {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Capture CoinGlass heatmap via Chrome DevTools MCP.")
    parser.add_argument(
        "--timeframe",
        default="2 week",
        help="Label of the timeframe option to select (e.g. '24 hour', '2 week', '1 month').",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output PNG path. Defaults to artifacts/heatmap_chrome_devtools_<timeframe>.png",
    )
    parser.add_argument(
        "--wait-timeout",
        type=int,
        default=45_000,
        help="Timeout (ms) for waiting on text elements (default: 45000).",
    )
    args = parser.parse_args()

    timeframe_slug = re.sub(r"[^a-z0-9]+", "-", args.timeframe.lower()).strip("-") or "heatmap"
    output_path = args.output or (REPO_ROOT / "artifacts" / f"heatmap_chrome_devtools_{timeframe_slug}.png")

    asyncio.run(capture(args.timeframe, output_path, args.wait_timeout))


if __name__ == "__main__":
    main()
