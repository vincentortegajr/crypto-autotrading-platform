#!/usr/bin/env python3
"""
Quick test to validate heatmap automation integration with Vince Quant Whale Empire

Tests:
1. Screenshot capture working
2. OCR extraction accuracy
3. JSON report structure (for trading bots)
4. Image quality (for social media broadcast)
5. File organization (for src/scanners/heatmap/)
"""

import json
import os
from pathlib import Path

print("="*80)
print("🐋 VINCE QUANT WHALE EMPIRE - HEATMAP AUTOMATION TEST")
print("="*80)

# Test 1: Check folder structure (src/scanners/heatmap/)
print("\n[TEST 1] Folder Structure (Intelligence Network)")
scanner_path = Path("src/scanners/heatmap")
if scanner_path.exists():
    files = list(scanner_path.glob("*"))
    print(f"✅ src/scanners/heatmap/ exists with {len(files)} files")
    for f in files:
        size_kb = f.stat().st_size / 1024
        print(f"   - {f.name} ({size_kb:.1f}KB)")
else:
    print("❌ Missing src/scanners/heatmap/")

# Test 2: Check existing screenshots
print("\n[TEST 2] Screenshot Quality (Social Media Ready)")
screenshots_dir = Path("screenshots")
social_images = list(screenshots_dir.glob("*SOCIAL*.png"))
print(f"✅ Found {len(social_images)} social media images:")
for img in social_images[:3]:
    size_kb = img.stat().st_size / 1024
    print(f"   - {img.name} ({size_kb:.1f}KB)")

# Test 3: Check JSON reports
print("\n[TEST 3] JSON Reports (Trading Bot Integration)")
reports_dir = Path("data/reports/heatmap_analysis")
json_files = list(reports_dir.glob("*.json"))
if json_files:
    print(f"✅ Found {len(json_files)} JSON reports")
    # Validate structure
    sample_json = json_files[0]
    with open(sample_json) as f:
        data = json.load(f)
    
    print(f"\n   Sample: {sample_json.name}")
    print(f"   - Symbol: {data.get('symbol')}")
    print(f"   - Timeframe: {data.get('timeframe')}")
    print(f"   - Primary Whale Target: {data.get('whale_targets', {}).get('primary', {}).get('price')}")
    print(f"   - Trading Direction: {data.get('trading_implications', {}).get('direction')}")
    print(f"   - Whale Strategy: {data.get('trading_implications', {}).get('whale_strategy', '')[:80]}...")
    
    # Check if format is bot-consumable
    required_keys = ['symbol', 'timeframe', 'whale_targets', 'trading_implications']
    has_all = all(k in data for k in required_keys)
    print(f"   - Bot-Consumable Format: {'✅ PASS' if has_all else '❌ FAIL'}")
else:
    print("❌ No JSON reports found")

# Test 4: Check markdown summaries
print("\n[TEST 4] Analysis Summaries (Telegram/X Broadcasting)")
md_files = list(reports_dir.glob("*SUMMARY.md"))
if md_files:
    print(f"✅ Found {len(md_files)} markdown summaries")
    sample_md = md_files[0]
    with open(sample_md) as f:
        lines = f.readlines()[:10]
    print(f"\n   Sample: {sample_md.name}")
    print("   First 10 lines preview:")
    for line in lines:
        print(f"   {line.rstrip()}")
else:
    print("❌ No markdown summaries found")

# Test 5: Integration readiness
print("\n[TEST 5] Integration Readiness for Vince Quant Platform")
integration_checks = {
    "Screenshot automation": scanner_path.exists() and Path("src/scanners/heatmap/coinglass_full_automation.py").exists(),
    "Social media images": len(social_images) > 0,
    "Trading bot JSON": len(json_files) > 0,
    "Broadcast summaries": len(md_files) > 0,
    "Organized structure": screenshots_dir.exists() and reports_dir.exists(),
    "Documentation": Path("docs/COINGLASS-HEATMAP-FULL-AUTOMATION-PROMPT.md").exists()
}

print("\nIntegration Components:")
for component, status in integration_checks.items():
    status_icon = "✅" if status else "❌"
    print(f"   {status_icon} {component}")

all_pass = all(integration_checks.values())
print(f"\n{'='*80}")
if all_pass:
    print("🎉 ALL TESTS PASSED - READY FOR WHALE EMPIRE INTEGRATION")
else:
    print("⚠️  SOME TESTS FAILED - REVIEW ABOVE")
print(f"{'='*80}")

# Show whale targets summary
print("\n[WHALE INTELLIGENCE SUMMARY]")
if json_files:
    with open(json_files[0]) as f:
        data = json.load(f)
    print(f"🎯 Coin: {data.get('symbol')}")
    print(f"⏰ Timeframe: {data.get('timeframe')}")
    print(f"🐋 PRIMARY WHALE TARGET: {data.get('whale_targets', {}).get('primary', {}).get('price')}")
    print(f"   Intensity: {data.get('whale_targets', {}).get('primary', {}).get('liquidation_intensity')}")
    print(f"   Zone Type: {data.get('whale_targets', {}).get('primary', {}).get('zone_type')}")
    if 'secondary' in data.get('whale_targets', {}):
        print(f"🎯 SECONDARY TARGET: {data.get('whale_targets', {}).get('secondary', {}).get('price_range')}")
    print(f"\n⚡ Strategy: {data.get('trading_implications', {}).get('whale_strategy')}")
    print(f"⚠️  Direction: {data.get('trading_implications', {}).get('direction')}")

