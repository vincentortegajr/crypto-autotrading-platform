#!/usr/bin/env python3
"""
Capture the CoinGlass liquidation heatmap via Microsoft's Playwright MCP server.

Automates navigation, consent dismissal, timeframe selection, and saves a full
page screenshot for comparison against the Chrome DevTools MCP capture.
"""

import argparse
import asyncio
import re
import shutil
from pathlib import Path
from typing import Tuple

from fastmcp.client.client import Client
from fastmcp.client.transports import NodeStdioTransport

REPO_ROOT = Path(__file__).resolve().parents[1]
PLAYWRIGHT_SCRIPT = (REPO_ROOT / "node_modules" / "@playwright" / "mcp" / "cli.js").resolve()
TARGET_URL = "https://www.coinglass.com/pro/futures/LiquidationHeatMapNew"


def _parse_viewport(value: str) -> Tuple[int, int]:
    try:
        width, height = value.lower().split("x", 1)
        return int(width), int(height)
    except Exception as exc:  # pragma: no cover - defensive parsing
        raise argparse.ArgumentTypeError(f"Invalid viewport '{value}', expected WIDTHxHEIGHT") from exc


def _build_timeframe_regex(label: str) -> str:
    escaped = re.escape(label.strip())
    return escaped.replace("\\ ", "\\s*")


async def capture(timeframe: str, viewport: Tuple[int, int], output_path: Path, timeout_ms: int) -> None:
    timeframe = timeframe.strip()
    width, height = viewport
    output_path = output_path.resolve()

    transport = NodeStdioTransport(
        PLAYWRIGHT_SCRIPT,
        args=[
            "--headless",
            "--browser",
            "chromium",
            "--isolated",
            "--user-agent",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "--viewport-size",
            f"{width}x{height}",
            "--timeout-action",
            str(timeout_ms),
            "--timeout-navigation",
            str(timeout_ms),
        ],
    )
    client = Client(transport)

    async with client:
        await client.call_tool(
            "browser_navigate",
            {
                "url": TARGET_URL,
            },
        )

        await client.call_tool(
            "browser_wait_for",
            {
                "time": 5,
            },
        )

        consent_result = await client.call_tool(
            "browser_evaluate",
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
                "browser_wait_for",
                {
                    "text": timeframe,
                },
            )
        except Exception:
            try:
                await client.call_tool(
                    "browser_wait_for",
                    {
                        "text": "24 hour",
                    },
                )
            except Exception:
                await asyncio.sleep(1.0)

        dropdown_click = await client.call_tool(
            "browser_click",
            {
                "element": "timeframe dropdown",
                "ref": "e86",
            },
        )
        print("Dropdown:", dropdown_click.data or dropdown_click.structured_content or dropdown_click.content)

        await client.call_tool("browser_wait_for", {"time": 1})

        regex = _build_timeframe_regex(timeframe)
        option_result = await client.call_tool(
            "browser_evaluate",
            {
                "function": f"""
() => {{
  const option = Array.from(document.querySelectorAll('[role="option"], button'))
    .find((el) => /{regex}/i.test(el.textContent || ''));
  if (option) {{
    option.click();
    return 'option-selected';
  }}
  return 'option-missing';
}}
                """,
            },
        )
        print("Timeslot:", option_result.data or option_result.structured_content or option_result.content)

        try:
            await client.call_tool(
                "browser_wait_for",
                {
                    "text": timeframe,
                },
            )
        except Exception:
            # If the exact casing differs, fall back to a short delay.
            await asyncio.sleep(2.0)

        await asyncio.sleep(3.0)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        screenshot_result = await client.call_tool(
            "browser_take_screenshot",
            {
                "fullPage": True,
                "filename": str(output_path.relative_to(REPO_ROOT)),
            },
        )
        text_block = next((c for c in screenshot_result.content if getattr(c, "type", "") == "text"), None)
        tmp_path = None
        if text_block:
            match = re.search(r"saved it as ([^\s]+\.png)", text_block.text)
            if match:
                tmp_path = Path(match.group(1)).expanduser()
        if tmp_path and tmp_path.exists():
            output_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(tmp_path, output_path)
            print(f"Screenshot copied to {output_path}")
        else:
            print("Screenshot response:", screenshot_result.content)


def main() -> None:
    parser = argparse.ArgumentParser(description="Capture CoinGlass heatmap via Playwright MCP.")
    parser.add_argument(
        "--timeframe",
        default="2 week",
        help="Label of the timeframe option to select (e.g. '24 hour', '2 week', '1 month').",
    )
    parser.add_argument(
        "--viewport",
        default="1600x900",
        type=_parse_viewport,
        help="Viewport size in WIDTHxHEIGHT format (default: 1600x900).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=300000,
        help="Action/navigation timeout in milliseconds passed to @playwright/mcp (default: 300000).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output PNG path. Defaults to artifacts/heatmap_playwright_mcp_<timeframe>.png",
    )
    args = parser.parse_args()

    timeframe_slug = re.sub(r"[^a-z0-9]+", "-", args.timeframe.lower()).strip("-") or "heatmap"
    output_path = (args.output or (REPO_ROOT / "artifacts" / f"heatmap_playwright_mcp_{timeframe_slug}.png")).resolve()

    asyncio.run(capture(args.timeframe, args.viewport, output_path, args.timeout))


if __name__ == "__main__":
    main()
