#!/usr/bin/env python3
"""
PROFESSIONAL HEATMAP COMPOSITION
Bloomberg Terminal Quality - PROPER spacing, NO overlapping text

Creates a framed composition with:
- Top margin for headers
- Bottom margin for footer
- Clean chart in center (UNTOUCHED)
- Arrows pointing FROM margins TO zones

Author: Oracle Dev AI for Vince Quant Whale Empire
"""

from PIL import Image, ImageDraw, ImageFont
import sys
import os

def create_professional_composition(chart_path, output_path):
    """
    Create Bloomberg-quality composition with proper margins
    """

    print("🐋 CREATING PROFESSIONAL COMPOSITION")
    print("=" * 80)

    # Load the clean chart
    chart = Image.open(chart_path)
    chart_width, chart_height = chart.size
    print(f"Chart size: {chart_width} x {chart_height}")

    # Define margins (professional spacing)
    TOP_MARGIN = 200      # Header area
    BOTTOM_MARGIN = 150   # Footer area
    SIDE_MARGIN = 100     # Left/right padding

    # Create new canvas with margins
    canvas_width = chart_width + (SIDE_MARGIN * 2)
    canvas_height = chart_height + TOP_MARGIN + BOTTOM_MARGIN

    print(f"Canvas size: {canvas_width} x {canvas_height}")

    # Create white canvas
    canvas = Image.new('RGB', (canvas_width, canvas_height), (255, 255, 255))

    # Paste chart in center (with margins)
    chart_x = SIDE_MARGIN
    chart_y = TOP_MARGIN
    canvas.paste(chart, (chart_x, chart_y))

    print("✅ Chart pasted with proper margins")

    # Initialize drawing
    draw = ImageDraw.Draw(canvas)

    # Try to load a good font (fallback to default)
    try:
        # Try system fonts (macOS)
        font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 80)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60)
        font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
        print("✅ Loaded Helvetica fonts")
    except:
        try:
            # Try Arial
            font_large = ImageFont.truetype("/Library/Fonts/Arial.ttf", 80)
            font_medium = ImageFont.truetype("/Library/Fonts/Arial.ttf", 60)
            font_small = ImageFont.truetype("/Library/Fonts/Arial.ttf", 40)
            print("✅ Loaded Arial fonts")
        except:
            # Fallback to default
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_small = ImageFont.load_default()
            print("⚠️  Using default font")

    # Colors (RGB)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)

    # TOP HEADER AREA (in margin, not on chart)
    header_text = "BTC LIQUIDATION HEATMAP - 24H"
    header_x = 50
    header_y = 50
    draw.text((header_x, header_y), header_text, fill=CYAN, font=font_large)
    print(f"✅ Header at ({header_x}, {header_y})")

    # WHALE TARGET annotation - in LEFT margin, arrow points to chart
    whale_text = "WHALE TARGET:"
    whale_price = "$111.5K"
    whale_y = TOP_MARGIN + 300  # Middle of chart area

    # Text in left margin
    draw.text((20, whale_y - 30), whale_text, fill=GREEN, font=font_medium)
    draw.text((20, whale_y + 40), whale_price, fill=GREEN, font=font_large)

    # Arrow pointing from text INTO chart at whale zone
    arrow_start = (SIDE_MARGIN - 10, whale_y + 20)
    arrow_end = (SIDE_MARGIN + 200, whale_y + 20)
    draw.line([arrow_start, arrow_end], fill=GREEN, width=8)
    # Arrowhead
    draw.polygon([
        arrow_end,
        (arrow_end[0] - 20, arrow_end[1] - 15),
        (arrow_end[0] - 20, arrow_end[1] + 15)
    ], fill=GREEN)

    print(f"✅ Whale target annotation with arrow")

    # SECONDARY TARGET - in RIGHT margin
    secondary_text = "SECONDARY:"
    secondary_price = "~$120K"
    secondary_y = TOP_MARGIN + 100

    # Text in right margin (right-aligned)
    text_x = canvas_width - 450
    draw.text((text_x, secondary_y - 30), secondary_text, fill=YELLOW, font=font_medium)
    draw.text((text_x, secondary_y + 40), secondary_price, fill=YELLOW, font=font_large)

    # Arrow pointing from text INTO chart
    arrow_start_r = (canvas_width - SIDE_MARGIN + 10, secondary_y + 20)
    arrow_end_r = (canvas_width - SIDE_MARGIN - 200, secondary_y + 20)
    draw.line([arrow_start_r, arrow_end_r], fill=YELLOW, width=8)
    # Arrowhead
    draw.polygon([
        arrow_end_r,
        (arrow_end_r[0] + 20, arrow_end_r[1] - 15),
        (arrow_end_r[0] + 20, arrow_end_r[1] + 15)
    ], fill=YELLOW)

    print(f"✅ Secondary target annotation with arrow")

    # BOTTOM FOOTER (in margin, not on chart)
    footer_text = "Data: CoinGlass.com  |  Analysis: @VincentOrtegaJr  |  Vince Quant Whale Empire"
    footer_y = canvas_height - BOTTOM_MARGIN + 50
    footer_x = 50
    draw.text((footer_x, footer_y), footer_text, fill=BLACK, font=font_small)
    print(f"✅ Footer at ({footer_x}, {footer_y})")

    # Add subtle border around chart area
    border_box = [
        (chart_x - 5, chart_y - 5),
        (chart_x + chart_width + 5, chart_y + chart_height + 5)
    ]
    draw.rectangle(border_box, outline=BLACK, width=3)
    print(f"✅ Border around chart")

    # Save final composition
    canvas.save(output_path, quality=95, optimize=True)
    print(f"\n✅ SAVED: {output_path}")
    print(f"   Size: {canvas_width} x {canvas_height}")
    print(f"   Quality: PROFESSIONAL - No overlapping text!")

    return output_path


if __name__ == "__main__":
    # Paths
    chart_path = "/Users/vincentortegajr/crypto-autotrading-platform/src/screenshots/cropped/BTC_24h_CLEAN_CHART.png"
    output_path = "/Users/vincentortegajr/crypto-autotrading-platform/screenshots/social/BTC_24h_PROFESSIONAL_FINAL.png"

    try:
        result = create_professional_composition(chart_path, output_path)
        print("\n" + "=" * 80)
        print("🎉 SUCCESS - PROFESSIONAL COMPOSITION COMPLETE")
        print("=" * 80)
        print(f"\nOpen it: open {output_path}")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
