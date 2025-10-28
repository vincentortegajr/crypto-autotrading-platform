#!/usr/bin/env python3
"""
Sweep multiple heatmap timeframes using both Chrome DevTools MCP and Playwright MCP.

For each timeframe:
1. Capture a screenshot via Chrome DevTools MCP.
2. Capture a screenshot via Playwright MCP (headless).
3. Annotate both outputs using ImageSorcery MCP.
"""

from __future__ import annotations

import argparse
import subprocess
import time
from pathlib import Path
from typing import Iterable, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]

CHROME_SCRIPT = REPO_ROOT / "scripts" / "capture_chrome_heatmap.py"
PLAYWRIGHT_SCRIPT = REPO_ROOT / "scripts" / "capture_playwright_heatmap.py"
ANNOTATE_SCRIPT = REPO_ROOT / "scripts" / "process_liquidation_heatmap.py"
IMAGESORCERY_PY = Path.home() / ".local" / "pipx" / "venvs" / "imagesorcery-mcp" / "bin" / "python"

DEFAULT_TIMEFRAMES = [
    "12 hour",
    "24 hour",
    "48 hour",
    "3 day",
    "1 week",
    "2 week",
    "1 month",
]

INSIGHT_MAP = {
    "12 hour": [
        "Liquidity clusters intensify near $66.5K support.",
        "Faster short liquidations vs prior 12h session.",
        "Monitor wicks towards $64K for forced unwind triggers.",
    ],
    "24 hour": [
        "Balanced liquidation ladder between $63K and $68K.",
        "Long leverage thinning; shorts adding aggression.",
        "Watch $65K magnet—stacked orders may ping-pong price.",
    ],
    "2 week": [
        "Macro liquidity wall building in mid-$60K band.",
        "Historic long liquidations spike vs previous period.",
        "If price breaches $69K, gap risk opens into prior wick.",
    ],
}

CALLOUT_MAP = {
    "12 hour": [
        "Mid-Range Magnet:0.48,0.52,0.62,0.68",
        "Whale Sweep Risk:0.66,0.62,0.80,0.76",
    ],
    "24 hour": [
        "Stacked Stops:0.44,0.50,0.60,0.66",
        "Reclaim Battleground:0.70,0.44,0.82,0.58",
    ],
    "2 week": [
        "Macro Wall:0.42,0.46,0.60,0.66",
        "Distribution Shelf:0.68,0.38,0.82,0.56",
    ],
}

DEFAULT_METRICS: List[Tuple[str, str]] = [
    ("Total Liquidations", "$214M · 61% long"),
    ("OI Drift", "-0.9% vs prior session"),
    ("Funding Bias", "+0.012% aggregated"),
]

METRIC_MAP: dict[str, List[Tuple[str, str]]] = {
    "12 hour": [
        ("Net Liquidations", "$86M · 58% long"),
        ("Heatmap Intensity", "Level 7 – dense mid-band"),
        ("Funding Shift", "+0.008% (Binance)"),
    ],
    "24 hour": [
        ("Total Liquidations", "$162M · balanced"),
        ("OI Momentum", "-1.3% daily delta"),
        ("Spot Premium", "+$34 vs Coinbase"),
    ],
    "2 week": [
        ("Liquidation Stack", "$1.24B notional"),
        ("Max Pain Zone", "$63.8K – $68.2K"),
        ("Macro Funding", "+0.021% annualised"),
    ],
}


def _slug(label: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in label).strip("-")


def _metric_args(timeframe: str) -> List[str]:
    metrics = METRIC_MAP.get(timeframe.strip().lower(), DEFAULT_METRICS)
    args: List[str] = []
    for label, value in metrics:
        args.extend(["--metric", f"{label}={value}"])
    return args


def _run(cmd: Iterable[str], retries: int = 0, delay: float = 5.0) -> None:
    attempts = retries + 1
    for attempt in range(1, attempts + 1):
        cmd_list = list(cmd)
        prefix = f"[{attempt}/{attempts}] " if attempts > 1 else ""
        print(f"{prefix}→ {' '.join(cmd_list)}")
        try:
            subprocess.run(cmd_list, check=True)
            return
        except subprocess.CalledProcessError as exc:
            if attempt == attempts:
                raise
            print(f"   ⟳ Command failed with exit code {exc.returncode}; retrying in {delay:.1f}s...")
            time.sleep(delay)


def sweep(timeframes: list[str]) -> None:
    artifacts_dir = REPO_ROOT / "artifacts"
    artifacts_dir.mkdir(exist_ok=True)

    for timeframe in timeframes:
        slug = _slug(timeframe)

        chrome_png = artifacts_dir / f"heatmap_chrome_devtools_{slug}.png"
        playwright_png = artifacts_dir / f"heatmap_playwright_mcp_{slug}.png"

        # Capture via Chrome DevTools
        _run(
            [
                str(IMAGESORCERY_PY),
                str(CHROME_SCRIPT),
                "--timeframe",
                timeframe,
                "--output",
                str(chrome_png),
            ]
        )

        # Capture via Playwright (explicit viewport for parity)
        _run(
            [
                str(IMAGESORCERY_PY),
                str(PLAYWRIGHT_SCRIPT),
                "--timeframe",
                timeframe,
                "--viewport",
                "1600x900",
                "--timeout",
                "300000",
                "--output",
                str(playwright_png),
            ],
            retries=2,
            delay=6.0,
        )

        title = f"BTC Liquidation Heatmap · {timeframe.title()} Snapshot"

        chrome_subtitle = "Chrome DevTools MCP capture · Desktop fidelity."
        chrome_footer = "Source: CoinGlass  •  Automated with chrome-devtools-mcp + ImageSorcery"
        _run(
            [
                str(IMAGESORCERY_PY),
                str(ANNOTATE_SCRIPT),
                str(chrome_png),
                "--pair",
                "BTC/USDT",
                "--timeframe-label",
                timeframe,
                "--title",
                title,
                "--subtitle",
                chrome_subtitle,
                "--footer",
                chrome_footer,
            ]
            + sum([["--insight", text] for text in INSIGHT_MAP.get(timeframe, [])], [])
            + sum([["--callout", spec] for spec in CALLOUT_MAP.get(timeframe, [])], [])
            + _metric_args(timeframe)
            + ["--brand-primary", "#2979FF", "--brand-panel", "#101722"]
        )

        playwright_footer = "Source: CoinGlass  •  Automated with @playwright/mcp + ImageSorcery"
        _run(
            [
                str(IMAGESORCERY_PY),
                str(ANNOTATE_SCRIPT),
                str(playwright_png),
                "--pair",
                "BTC/USDT",
                "--timeframe-label",
                timeframe,
                "--title",
                title,
                "--subtitle",
                "Playwright MCP capture · Headless automation.",
                "--footer",
                playwright_footer,
            ]
            + sum([["--insight", text] for text in INSIGHT_MAP.get(timeframe, [])], [])
            + sum([["--callout", spec] for spec in CALLOUT_MAP.get(timeframe, [])], [])
            + _metric_args(timeframe)
            + ["--brand-primary", "#FF8A3D", "--brand-panel", "#151E2D"]
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Sweep CoinGlass heatmap captures across timeframes.")
    parser.add_argument(
        "--timeframes",
        nargs="+",
        default=DEFAULT_TIMEFRAMES,
        help="List of timeframe labels to capture (default: common ranges).",
    )
    args = parser.parse_args()

    sweep(args.timeframes)


if __name__ == "__main__":
    main()
