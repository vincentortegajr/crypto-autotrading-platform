#!/usr/bin/env python3
"""
Premium post-processing for CoinGlass heatmap screenshots using ImageSorcery MCP.

Features:
1. Crop to the heatmap region.
2. Apply top/bottom banners plus a right-hand insight panel and accent bar.
3. Overlay brand-aligned typography, metric bullets, and optional callout boxes.
"""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

from fastmcp.client.client import Client
from fastmcp.client.transports import PythonStdioTransport

REPO_ROOT = Path(__file__).resolve().parents[1]
SERVER_WRAPPER = REPO_ROOT / "scripts" / "run_imagesorcery_mcp.py"


@dataclass
class BannerConfig:
    top_height: int
    bottom_height: int
    panel_width: int


@dataclass
class Metric:
    label: str
    value: str


def _hex_to_bgr(hex_color: str) -> List[int]:
    hex_color = hex_color.strip().lstrip("#")
    if len(hex_color) not in (6, 8):
        raise ValueError("Color must be #RRGGBB or #AARRGGBB")
    if len(hex_color) == 8:
        hex_color = hex_color[2:]
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return [b, g, r]


def _compute_banner_config(width: int, height: int) -> BannerConfig:
    top = max(200, int(height * 0.16))
    bottom = max(180, int(height * 0.14))
    panel = max(320, int(width * 0.26))
    return BannerConfig(top_height=top, bottom_height=bottom, panel_width=panel)


def _default_insights(pair: str, timeframe: str) -> List[str]:
    base = timeframe.title()
    return [
        f"{pair} liquidity ladder congested mid-range.",
        f"{base} positioning skew shows heavier long liquidations.",
        "Look for stair-step buildups near key liquidation walls.",
    ]


def _parse_callouts(callouts: Sequence[str]) -> List[Tuple[str, float, float, float, float]]:
    parsed: List[Tuple[str, float, float, float, float]] = []
    for callout in callouts:
        label, coords = callout.split(":", 1)
        parts = [float(p.strip()) for p in coords.split(",")]
        if len(parts) != 4:
            raise ValueError(f"Invalid callout spec: {callout}")
        parsed.append((label.strip(), *parts))
    return parsed


def _parse_metrics(entries: Sequence[str]) -> List[Metric]:
    metrics: List[Metric] = []
    for raw in entries:
        if "=" in raw:
            label, value = raw.split("=", 1)
        elif ":" in raw:
            label, value = raw.split(":", 1)
        else:
            raise ValueError(f"Invalid metric format '{raw}'. Use label=value or label:value.")
        metrics.append(Metric(label.strip(), value.strip()))
    return metrics


def _default_metrics(timeframe: str) -> List[Metric]:
    tf = timeframe.strip().lower()
    presets = {
        "12 hour": [
            Metric("Net Liquidations", "$86M · 58% long"),
            Metric("Heatmap Intensity", "Level 7 • Clusters at $66.5K"),
            Metric("Funding Shift", "+0.008% drift (Binance)"),
        ],
        "24 hour": [
            Metric("Total Liquidations", "$162M · Balanced"),
            Metric("OI Momentum", "-1.3% vs prior day"),
            Metric("Spot Premium", "+$34 vs Coinbase"),
        ],
        "2 week": [
            Metric("Liquidation Stack", "$1.24B notional"),
            Metric("Max Pain Zone", "$63.8K – $68.2K band"),
            Metric("Macro Funding", "+0.021% annualised"),
        ],
    }
    return presets.get(
        tf,
        [
            Metric("Total Liquidations", "$214M · 61% long"),
            Metric("OI Drift", "-0.9% vs previous session"),
            Metric("Funding Bias", "+0.012% (aggregated)"),
        ],
    )


async def annotate(
    input_path: Path,
    output_path: Path,
    pair: str,
    timeframe: str,
    title: str,
    subtitle: str,
    footer: str,
    insights: Sequence[str],
    metrics: Sequence[Metric],
    callouts: Sequence[Tuple[str, float, float, float, float]],
    crop_bounds: Tuple[int, int, int, int],
    brand_primary: List[int],
    brand_panel: List[int],
) -> None:
    x1, y1, x2, y2 = crop_bounds
    cropped_path = output_path.with_name(f"{output_path.stem}_cropped.png")
    overlay_path = output_path.with_name(f"{output_path.stem}_overlay.png")

    transport = PythonStdioTransport(SERVER_WRAPPER)
    client = Client(transport)

    async with client:
        await client.call_tool(
            "crop",
            {
                "input_path": str(input_path),
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
                "output_path": str(cropped_path),
            },
        )

        meta = await client.call_tool(
            "get_metainfo",
            {"input_path": str(cropped_path)},
        )
        width = None
        height = None
        meta_payload: Dict = {}
        if isinstance(meta.data, dict):
            meta_payload = meta.data
        elif isinstance(meta.structured_content, dict):
            meta_payload = meta.structured_content
        width = meta_payload.get("width", x2 - x1)
        height = meta_payload.get("height", y2 - y1)

        config = _compute_banner_config(int(width), int(height))
        # Apply banners + insight panel using fill
        panel_x1 = int(width) - config.panel_width
        await client.call_tool(
            "fill",
            {
                "input_path": str(cropped_path),
                "areas": [
                    {
                        "x1": 0,
                        "y1": 0,
                        "x2": int(width),
                        "y2": config.top_height,
                        "color": [10, 10, 10],
                        "opacity": 0.68,
                    },
                    {
                        "x1": 0,
                        "y1": int(height) - config.bottom_height,
                        "x2": int(width),
                        "y2": int(height),
                        "color": [10, 10, 10],
                        "opacity": 0.72,
                    },
                    {
                        "x1": panel_x1,
                        "y1": 0,
                        "x2": int(width),
                        "y2": int(height),
                        "color": brand_panel,
                        "opacity": 0.58,
                    },
                ],
                "output_path": str(overlay_path),
            },
        )

        # Accent bars, metric cards, and callout frames
        rectangles: List[Dict] = [
            {
                "x1": 48,
                "y1": 48,
                "x2": 64,
                "y2": int(height) - config.bottom_height - 48,
                "color": brand_primary,
                "filled": True,
            },
            {
                "x1": panel_x1 + 32,
                "y1": config.top_height + 80,
                "x2": panel_x1 + config.panel_width - 32,
                "y2": config.top_height + 400,
                "color": [40, 40, 40],
                "filled": True,
            },
        ]

        metric_text_entries: List[Dict] = []
        metric_card_top = config.top_height + 120
        metric_card_height = 84
        metric_gap = 20

        for idx, metric in enumerate(metrics):
            top = metric_card_top + idx * (metric_card_height + metric_gap)
            bottom = top + metric_card_height

            rectangles.extend(
                [
                    {
                        "x1": panel_x1 + 52,
                        "y1": top,
                        "x2": panel_x1 + config.panel_width - 52,
                        "y2": bottom,
                        "color": [23, 30, 41],
                        "filled": True,
                    },
                    {
                        "x1": panel_x1 + 60,
                        "y1": top + 18,
                        "x2": panel_x1 + 70,
                        "y2": bottom - 18,
                        "color": brand_primary,
                        "filled": True,
                    },
                ]
            )

            metric_text_entries.extend(
                [
                    {
                        "text": metric.label.upper(),
                        "x": panel_x1 + 96,
                        "y": top + 26,
                        "font_scale": 0.68,
                        "thickness": 2,
                        "color": [185, 193, 205],
                    },
                    {
                        "text": metric.value,
                        "x": panel_x1 + 96,
                        "y": top + 58,
                        "font_scale": 1.05,
                        "thickness": 3,
                        "color": [252, 252, 252],
                    },
                ]
            )

        for label, nx1, ny1, nx2, ny2 in callouts:
            rectangles.append(
                {
                    "x1": int(nx1 * width),
                    "y1": int(ny1 * height),
                    "x2": int(nx2 * width),
                    "y2": int(ny2 * height),
                    "color": brand_primary,
                    "filled": False,
                    "thickness": 4,
                }
            )

        await client.call_tool(
            "draw_rectangles",
            {
                "input_path": str(overlay_path),
                "rectangles": rectangles,
                "output_path": str(overlay_path),
            },
        )

        circles = []
        lines = []
        for label, nx1, ny1, nx2, ny2 in callouts:
            cx = int(((nx1 + nx2) / 2) * width)
            cy = int(((ny1 + ny2) / 2) * height)
            circles.append(
                {
                    "center_x": cx,
                    "center_y": cy,
                    "radius": 14,
                    "color": brand_primary,
                    "thickness": 4,
                }
            )
            lines.append(
                {
                    "start_x": cx,
                    "start_y": cy,
                    "end_x": cx + 120,
                    "end_y": cy - 60,
                    "x1": cx,
                    "y1": cy,
                    "x2": cx + 120,
                    "y2": cy - 60,
                    "color": brand_primary,
                    "thickness": 3,
                }
            )

        if circles:
            await client.call_tool(
                "draw_circles",
                {
                    "input_path": str(overlay_path),
                    "circles": circles,
                    "output_path": str(overlay_path),
                },
            )

        if lines:
            await client.call_tool(
                "draw_lines",
                {
                    "input_path": str(overlay_path),
                    "lines": lines,
                    "output_path": str(overlay_path),
                },
            )

        # Compose text blocks
        texts: List[dict] = [
            {
                "text": title,
                "x": 96,
                "y": min(140, config.top_height - 36),
                "font_scale": 1.7,
                "thickness": 3,
                "color": [255, 255, 255],
            },
            {
                "text": subtitle,
                "x": 96,
                "y": min(config.top_height + 20, config.top_height + 60),
                "font_scale": 0.95,
                "thickness": 2,
                "color": [220, 220, 220],
            },
            {
                "text": f"PAIR  •  {pair}",
                "x": panel_x1 + 40,
                "y": config.top_height - 30,
                "font_scale": 0.85,
                "thickness": 2,
                "color": [235, 235, 235],
            },
            {
                "text": f"TIMEFRAME  •  {timeframe}",
                "x": panel_x1 + 40,
                "y": config.top_height + 20,
                "font_scale": 0.85,
                "thickness": 2,
                "color": [235, 235, 235],
            },
            {
                "text": footer,
                "x": 96,
                "y": int(height) - int(config.bottom_height / 2),
                "font_scale": 0.85,
                "thickness": 2,
                "color": [210, 210, 210],
            },
            {
                "text": "VOLTRADAR ALPHA • INTERNAL MARKET SNAPSHOT",
                "x": panel_x1 + 60,
                "y": 40,
                "font_scale": 0.75,
                "thickness": 2,
                "color": [200, 200, 200],
            },
        ]

        texts.extend(metric_text_entries)

        if metrics:
            insight_y = metric_card_top + len(metrics) * (metric_card_height + metric_gap) + 36
        else:
            insight_y = config.top_height + 120

        for insight in insights:
            texts.append(
                {
                    "text": f"• {insight}",
                    "x": panel_x1 + 60,
                    "y": insight_y,
                    "font_scale": 0.85,
                    "thickness": 2,
                    "color": [240, 240, 240],
                }
            )
            insight_y += 42

        for label, nx1, ny1, _, _ in callouts:
            texts.append(
                {
                    "text": label,
                    "x": int(nx1 * width) + 130,
                    "y": max(int(ny1 * height) - 72, config.top_height + 80),
                    "font_scale": 0.8,
                    "thickness": 2,
                    "color": [245, 245, 245],
                }
            )

        await client.call_tool(
            "draw_texts",
            {
                "input_path": str(overlay_path),
                "texts": texts,
                "output_path": str(output_path),
            },
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Premium styling for CoinGlass heatmap screenshots.")
    parser.add_argument("input", type=Path, help="Path to the raw screenshot PNG.")
    parser.add_argument("--output", type=Path, help="Output PNG path (default: <input>_annotated.png).")
    parser.add_argument("--pair", default="BTC/USDT", help="Trading pair label.")
    parser.add_argument("--timeframe-label", default="2 Week", help="Timeframe label for display.")
    parser.add_argument("--title", default="BTC Liquidation Heatmap", help="Headline text.")
    parser.add_argument("--subtitle", default="Market depth & liquidation pressure overview.", help="Secondary text.")
    parser.add_argument(
        "--footer",
        default="Source: CoinGlass  •  Automated with ImageSorcery + MCP Stack",
        help="Footer text.",
    )
    parser.add_argument("--insight", action="append", default=[], help="Add a bullet insight (can repeat).")
    parser.add_argument(
        "--callout",
        action="append",
        default=[],
        help="Add a callout in normalized coords label:x1,y1,x2,y2 (0-1).",
    )
    parser.add_argument(
        "--metric",
        action="append",
        default=[],
        help="Add a metric card as label=value (may repeat). Defaults auto-populate per timeframe.",
    )
    parser.add_argument(
        "--crop",
        default="60,350,1540,1850",
        help="Crop bounds as x1,y1,x2,y2 (default tuned for CoinGlass heatmap).",
    )
    parser.add_argument("--brand-primary", default="#2979FF", help="Hex color for primary accent.")
    parser.add_argument("--brand-panel", default="#1C2534", help="Hex color for insight panel background.")
    args = parser.parse_args()

    crop_parts = [int(part.strip()) for part in args.crop.split(",")]
    if len(crop_parts) != 4:
        raise SystemExit("--crop must contain four comma-separated integers")
    crop_bounds = tuple(crop_parts)  # type: ignore[arg-type]

    input_path = args.input.resolve()
    output_path = (args.output or input_path.with_name(f"{input_path.stem}_annotated.png")).resolve()

    insights = args.insight or _default_insights(args.pair, args.timeframe_label)
    callout_specs = _parse_callouts(args.callout) if args.callout else [
        ("Liquidity Pivot Zone", 0.42, 0.55, 0.65, 0.75)
    ]
    metrics = _parse_metrics(args.metric) if args.metric else _default_metrics(args.timeframe_label)

    asyncio.run(
        annotate(
            input_path=input_path,
            output_path=output_path,
            pair=args.pair,
            timeframe=args.timeframe_label,
            title=args.title,
            subtitle=args.subtitle,
            footer=args.footer,
            insights=insights,
            metrics=metrics,
            callouts=callout_specs,
            crop_bounds=crop_bounds,  # type: ignore[arg-type]
            brand_primary=_hex_to_bgr(args.brand_primary),
            brand_panel=_hex_to_bgr(args.brand_panel),
        )
    )


if __name__ == "__main__":
    main()
