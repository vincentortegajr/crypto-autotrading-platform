# 🔥 COINGLASS HEATMAP MEGA-AUTOMATION - COMPLETE PROMPT INJECTION

YOU ARE AN AI AGENT WITH ZERO CONTEXT. FOLLOW THESE INSTRUCTIONS EXACTLY.

## 🎯 OBJECTIVE
Generate professional social media ready liquidation heatmap images for [COIN] across ALL 10 timeframes with full annotations, data extraction, and deliverables.

## 🛠️ TOOLS AVAILABLE
1. **Chrome DevTools MCP** - Browser automation (navigate, click, screenshot)
   - `mcp__chrome-devtools__navigate_page` - Navigate to URL
   - `mcp__chrome-devtools__take_snapshot` - Get page elements with UIDs
   - `mcp__chrome-devtools__click` - Click element by UID
   - `mcp__chrome-devtools__take_screenshot` - Capture screenshot

2. **ImageSorcery MCP** - Image processing (all tools use BGR color format)
   - `mcp__imagesorcery-mcp__get_metainfo` - Get image dimensions
   - `mcp__imagesorcery-mcp__crop` - Crop image (x1, y1, x2, y2)
   - `mcp__imagesorcery-mcp__ocr` - Extract text via OCR
   - `mcp__imagesorcery-mcp__draw_rectangles` - Draw rectangles
   - `mcp__imagesorcery-mcp__draw_arrows` - Draw arrows
   - `mcp__imagesorcery-mcp__draw_texts` - Add text labels
   - `mcp__imagesorcery-mcp__resize` - Resize image
   - `mcp__imagesorcery-mcp__overlay` - Overlay logo/watermark

## 📋 STEP-BY-STEP EXECUTION WORKFLOW

### STEP 1: NAVIGATE TO COINGLASS
```
Use: mcp__chrome-devtools__navigate_page
URL: https://www.coinglass.com/pro/futures/LiquidationHeatMapNew
Timeout: 15000
```

### STEP 2: GET PAGE SNAPSHOT (TO FIND CLICKABLE ELEMENTS)
```
Use: mcp__chrome-devtools__take_snapshot
Purpose: Find UIDs for Symbol dropdown and timeframe selector
```

### STEP 3: CLICK SYMBOL TAB
```
Use: mcp__chrome-devtools__take_snapshot
Find: Element with text "Symbol"
Extract: UID for Symbol tab
Use: mcp__chrome-devtools__click
Click: Symbol tab UID
```

### STEP 4: SELECT [COIN] FROM DROPDOWN
```
Use: mcp__chrome-devtools__take_snapshot
Find: Dropdown/search box for coin selection
Extract: UID
Use: mcp__chrome-devtools__click or mcp__chrome-devtools__fill
Input: [COIN] (e.g., "BTC", "ETH", "SOL")
```

### STEP 5: ITERATE THROUGH ALL 10 TIMEFRAMES
**Timeframes to process:** 12h, 24h, 48h, 3d, 1w, 2w, 1m, 3m, 6m, 1y

FOR EACH TIMEFRAME:

#### 5.1: SELECT TIMEFRAME
```
Use: mcp__chrome-devtools__take_snapshot
Find: Timeframe dropdown element
Extract: UID
Use: mcp__chrome-devtools__click
Select: [TIMEFRAME]
Wait: 3 seconds for heatmap to reload
```

#### 5.2: CAPTURE FULL PAGE SCREENSHOT
```
Use: mcp__chrome-devtools__take_screenshot
Parameters:
  fullPage: true
  format: "png"
  filePath: "/Users/vincentortegajr/crypto-autotrading-platform/screenshots/raw/[COIN]_[TIMEFRAME]_raw.png"
```

#### 5.3: GET IMAGE METADATA
```
Use: mcp__imagesorcery-mcp__get_metainfo
Input: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/raw/[COIN]_[TIMEFRAME]_raw.png
Extract: width, height, dimensions
```

#### 5.4: CROP TO HEATMAP CHART ONLY
```
Use: mcp__imagesorcery-mcp__crop
Input: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/raw/[COIN]_[TIMEFRAME]_raw.png
Crop coordinates (adjust based on metadata):
  x1: 250 (left edge, remove sidebar)
  y1: 1030 (top edge, remove header)
  x2: 2250 (right edge, keep chart)
  y2: 2300 (bottom edge, keep x-axis)
Output: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/cropped/[COIN]_[TIMEFRAME]_cropped.png
```

#### 5.5: OCR TEXT EXTRACTION (GET PRICE LEVELS + LIQUIDATION VALUES)
```
Use: mcp__imagesorcery-mcp__ocr
Input: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/cropped/[COIN]_[TIMEFRAME]_cropped.png
Language: "en"
Extract: All visible text (price levels on Y-axis, dates on X-axis, leverage values)
Store: In memory for JSON report
```

#### 5.6: IDENTIFY YELLOW-GREEN LIQUIDATION ZONES
**CRITICAL:** Analyze the cropped heatmap image visually to identify:
- Bright yellow horizontal bands (MASSIVE liquidation zones)
- Green/cyan horizontal bands (secondary targets)
- Record approximate Y-axis positions and corresponding price levels

Example zones to look for:
- Bottom 1/3 of chart = Lower liquidation zone
- Middle section = Mid-range targets
- Top section = Upper resistance zones

#### 5.7: ANNOTATE WITH RED RECTANGLES (WHALE TARGET BOXES)
```
Use: mcp__imagesorcery-mcp__draw_rectangles
Input: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/cropped/[COIN]_[TIMEFRAME]_cropped.png
Rectangles (adjust Y coordinates based on identified zones):
  [
    {
      "x1": 200,
      "y1": [ZONE_1_TOP],
      "x2": 1700,
      "y2": [ZONE_1_BOTTOM],
      "color": [0, 0, 255],
      "thickness": 8,
      "filled": false
    },
    {
      "x1": 200,
      "y1": [ZONE_2_TOP],
      "x2": 1700,
      "y2": [ZONE_2_BOTTOM],
      "color": [0, 0, 255],
      "thickness": 8,
      "filled": false
    }
  ]
Output: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/annotated/[COIN]_[TIMEFRAME]_step1.png
```

#### 5.8: ADD GREEN ARROWS POINTING TO WHALE ZONES
```
Use: mcp__imagesorcery-mcp__draw_arrows
Input: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/annotated/[COIN]_[TIMEFRAME]_step1.png
Arrows (point from right side to zones):
  [
    {
      "x1": 1800,
      "y1": [ZONE_1_CENTER_Y],
      "x2": 1680,
      "y2": [ZONE_1_CENTER_Y],
      "color": [0, 255, 0],
      "thickness": 12,
      "tip_length": 0.2
    },
    {
      "x1": 1800,
      "y1": [ZONE_2_CENTER_Y],
      "x2": 1680,
      "y2": [ZONE_2_CENTER_Y],
      "color": [0, 255, 0],
      "thickness": 12,
      "tip_length": 0.2
    }
  ]
Output: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/annotated/[COIN]_[TIMEFRAME]_step2.png
```

#### 5.9: ADD TEXT LABELS (HEADER + ZONE LABELS + FOOTER)
```
Use: mcp__imagesorcery-mcp__draw_texts
Input: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/annotated/[COIN]_[TIMEFRAME]_step2.png
Texts:
  [
    {
      "text": "[COIN] LIQUIDATION HEATMAP - [TIMEFRAME]",
      "x": 220,
      "y": 100,
      "font_scale": 3.0,
      "color": [0, 255, 255],
      "thickness": 7,
      "font_face": "FONT_HERSHEY_DUPLEX"
    },
    {
      "text": "WHALE TARGET: $[ZONE_1_PRICE]",
      "x": 230,
      "y": [ZONE_1_LABEL_Y],
      "font_scale": 2.3,
      "color": [0, 255, 255],
      "thickness": 6,
      "font_face": "FONT_HERSHEY_DUPLEX"
    },
    {
      "text": "LIQUIDATION: [ZONE_1_LEVERAGE]M",
      "x": 230,
      "y": [ZONE_1_LABEL_Y + 40],
      "font_scale": 1.8,
      "color": [255, 255, 255],
      "thickness": 4,
      "font_face": "FONT_HERSHEY_SIMPLEX"
    },
    {
      "text": "SECONDARY TARGET: $[ZONE_2_PRICE]",
      "x": 230,
      "y": [ZONE_2_LABEL_Y],
      "font_scale": 2.0,
      "color": [0, 255, 255],
      "thickness": 5,
      "font_face": "FONT_HERSHEY_DUPLEX"
    },
    {
      "text": "Data: CoinGlass.com | Analysis: @VincentOrtegaJr",
      "x": 220,
      "y": 1220,
      "font_scale": 1.5,
      "color": [255, 255, 255],
      "thickness": 4,
      "font_face": "FONT_HERSHEY_SIMPLEX"
    }
  ]
Output: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/final/[COIN]_liquidation_heatmap_[TIMEFRAME]_FINAL.png
```

#### 5.10: RESIZE FOR SOCIAL MEDIA (OPTIONAL)
```
Use: mcp__imagesorcery-mcp__resize
Input: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/final/[COIN]_liquidation_heatmap_[TIMEFRAME]_FINAL.png
Width: 1920 (Twitter/X optimal)
Height: null (preserve aspect ratio)
Output: /Users/vincentortegajr/crypto-autotrading-platform/screenshots/social/[COIN]_[TIMEFRAME]_SOCIAL.png
```

### STEP 6: GENERATE DATA REPORT (JSON + MARKDOWN)

#### 6.1: CREATE JSON DATA FILE
```
File: /Users/vincentortegajr/crypto-autotrading-platform/data/reports/heatmap_analysis/[COIN]_[TIMEFRAME]_data.json

Structure:
{
  "coin": "[COIN]",
  "timeframe": "[TIMEFRAME]",
  "analysis_timestamp": "2025-10-28T00:30:34Z",
  "whale_targets": [
    {
      "zone": "primary",
      "price_level": "$XXX,XXX",
      "liquidation_leverage": "XXX.XXM",
      "zone_type": "massive_yellow",
      "coordinates": {"x1": 200, "y1": XXX, "x2": 1700, "y2": XXX}
    },
    {
      "zone": "secondary",
      "price_level": "$XXX,XXX-$XXX,XXX",
      "liquidation_leverage": "XXX.XXM",
      "zone_type": "cyan_band",
      "coordinates": {"x1": 200, "y1": XXX, "x2": 1700, "y2": XXX}
    }
  ],
  "ocr_extracted_text": [ALL_OCR_RESULTS],
  "files_generated": {
    "raw_screenshot": "/path/to/raw.png",
    "cropped_chart": "/path/to/cropped.png",
    "final_annotated": "/path/to/FINAL.png",
    "social_optimized": "/path/to/SOCIAL.png"
  }
}
```

#### 6.2: CREATE MARKDOWN SUMMARY
```
File: /Users/vincentortegajr/crypto-autotrading-platform/data/reports/heatmap_analysis/[COIN]_[TIMEFRAME]_SUMMARY.md

Content:
# 🐋 [COIN] Liquidation Heatmap Analysis - [TIMEFRAME]

**Analysis Date:** October 28, 2025
**Timeframe:** [TIMEFRAME]
**Data Source:** CoinGlass.com

## 🎯 Whale Targets Identified

### Primary Target Zone
- **Price Level:** $XXX,XXX
- **Liquidation Leverage:** XXX.XXM
- **Zone Type:** Massive Yellow Band (High Concentration)
- **Status:** Critical whale hunting ground

### Secondary Target Zone
- **Price Level:** $XXX,XXX - $XXX,XXX
- **Liquidation Leverage:** XXX.XXM
- **Zone Type:** Cyan Band (Moderate Concentration)
- **Status:** Secondary resistance/support

## 📊 Trading Implications
- Whales are targeting liquidation clusters at identified levels
- Expect price manipulation toward yellow zones
- Monitor volume spikes near these levels

## 📁 Files Generated
- **Raw Screenshot:** `screenshots/raw/[COIN]_[TIMEFRAME]_raw.png`
- **Cropped Chart:** `screenshots/cropped/[COIN]_[TIMEFRAME]_cropped.png`
- **Final Annotated:** `screenshots/final/[COIN]_liquidation_heatmap_[TIMEFRAME]_FINAL.png`
- **Social Optimized:** `screenshots/social/[COIN]_[TIMEFRAME]_SOCIAL.png`
- **Data JSON:** `data/reports/heatmap_analysis/[COIN]_[TIMEFRAME]_data.json`

## 🔗 Social Media Ready
✅ Image is professional, branded, and ready to post
✅ Includes CoinGlass attribution
✅ Contains @VincentOrtegaJr branding
✅ Optimized for Twitter/X, Telegram, Instagram

---
*Generated by CoinGlass Heatmap Automation System*
```

### STEP 7: REPEAT FOR ALL 10 TIMEFRAMES
Loop through: 12h, 24h, 48h, 3d, 1w, 2w, 1m, 3m, 6m, 1y

Total files generated per coin: 10 timeframes × 5 files = 50 files

### STEP 8: CREATE MASTER INDEX
```
File: /Users/vincentortegajr/crypto-autotrading-platform/data/reports/heatmap_analysis/[COIN]_MASTER_INDEX.md

Content:
# 🐋 [COIN] Complete Heatmap Analysis - All Timeframes

**Generated:** October 28, 2025
**Coin:** [COIN]
**Timeframes Analyzed:** 10

## 📊 Quick Access

| Timeframe | Whale Target (Primary) | Social Image | Data Report |
|-----------|------------------------|--------------|-------------|
| 12h | $XXX,XXX | [View](screenshots/social/[COIN]_12h_SOCIAL.png) | [JSON](data/reports/[COIN]_12h_data.json) |
| 24h | $XXX,XXX | [View](screenshots/social/[COIN]_24h_SOCIAL.png) | [JSON](data/reports/[COIN]_24h_data.json) |
| 48h | $XXX,XXX | [View](screenshots/social/[COIN]_48h_SOCIAL.png) | [JSON](data/reports/[COIN]_48h_data.json) |
| 3d | $XXX,XXX | [View](screenshots/social/[COIN]_3d_SOCIAL.png) | [JSON](data/reports/[COIN]_3d_data.json) |
| 1w | $XXX,XXX | [View](screenshots/social/[COIN]_1w_SOCIAL.png) | [JSON](data/reports/[COIN]_1w_data.json) |
| 2w | $XXX,XXX | [View](screenshots/social/[COIN]_2w_SOCIAL.png) | [JSON](data/reports/[COIN]_2w_data.json) |
| 1m | $XXX,XXX | [View](screenshots/social/[COIN]_1m_SOCIAL.png) | [JSON](data/reports/[COIN]_1m_data.json) |
| 3m | $XXX,XXX | [View](screenshots/social/[COIN]_3m_SOCIAL.png) | [JSON](data/reports/[COIN]_3m_data.json) |
| 6m | $XXX,XXX | [View](screenshots/social/[COIN]_6m_SOCIAL.png) | [JSON](data/reports/[COIN]_6m_data.json) |
| 1y | $XXX,XXX | [View](screenshots/social/[COIN]_1y_SOCIAL.png) | [JSON](data/reports/[COIN]_1y_data.json) |

## 📁 Complete File Structure
```
screenshots/
├── raw/
│   ├── [COIN]_12h_raw.png
│   ├── [COIN]_24h_raw.png
│   └── ... (10 total)
├── cropped/
│   ├── [COIN]_12h_cropped.png
│   └── ... (10 total)
├── annotated/
│   ├── [COIN]_12h_step1.png
│   ├── [COIN]_12h_step2.png
│   └── ... (20 total)
├── final/
│   ├── [COIN]_liquidation_heatmap_12h_FINAL.png
│   └── ... (10 total)
└── social/
    ├── [COIN]_12h_SOCIAL.png
    └── ... (10 total)

data/reports/heatmap_analysis/
├── [COIN]_12h_data.json
├── [COIN]_12h_SUMMARY.md
├── ... (20 total)
└── [COIN]_MASTER_INDEX.md
```
```

## 🎯 FINAL DELIVERABLES

### Per Timeframe (10×):
1. ✅ Raw screenshot (full page)
2. ✅ Cropped heatmap chart
3. ✅ Professional annotated image with:
   - Red rectangles around whale zones
   - Green arrows pointing to targets
   - Yellow header with coin + timeframe
   - White text labels with price + leverage
   - Footer with CoinGlass + @VincentOrtegaJr branding
4. ✅ Social media optimized version (1920px width)
5. ✅ JSON data report (whale targets + OCR data)
6. ✅ Markdown summary (trading analysis)

### Master Deliverables:
1. ✅ Master index with all 10 timeframes
2. ✅ Complete file structure listing
3. ✅ Total: 50 files per coin

---

## 📋 USAGE EXAMPLES

### Example 1: Analyze BTC
```
Execute COINGLASS-HEATMAP-FULL-AUTOMATION-PROMPT.md for BTC
```

### Example 2: Analyze ETH
```
Execute COINGLASS-HEATMAP-FULL-AUTOMATION-PROMPT.md for ETH
```

### Example 3: Analyze SOL
```
Execute COINGLASS-HEATMAP-FULL-AUTOMATION-PROMPT.md for SOL
```

---

## ⚠️ CRITICAL REMINDERS

### 1. Color Format: BGR not RGB
```
Red = [0, 0, 255]
Green = [0, 255, 0]
Yellow = [0, 255, 255]
White = [255, 255, 255]
Cyan = [255, 255, 0]
```

### 2. Absolute Paths Always
```
✅ /Users/vincentortegajr/crypto-autotrading-platform/screenshots/...
❌ screenshots/... (relative paths will fail)
```

### 3. Professional Quality Requirements
- Text must be readable at social media size
- Boxes must precisely outline liquidation zones
- Labels must clearly identify price levels
- No half-assed annotations
- Every pixel matters for $1M+ brand image

### 4. Wait for Page Loads
After selecting timeframe, wait 3-5 seconds before taking screenshot to ensure heatmap fully renders

### 5. Create Required Folders First
```bash
mkdir -p /Users/vincentortegajr/crypto-autotrading-platform/screenshots/{raw,cropped,annotated,final,social}
mkdir -p /Users/vincentortegajr/crypto-autotrading-platform/data/reports/heatmap_analysis
```

### 6. ImageSorcery Font Options
```
FONT_HERSHEY_SIMPLEX - Clean, simple (use for footer)
FONT_HERSHEY_DUPLEX - Professional, bold (use for headers)
FONT_HERSHEY_COMPLEX - Elegant
FONT_HERSHEY_TRIPLEX - Extra bold
```

### 7. Screenshot Quality Settings
```
Format: PNG (lossless)
Full page: true
Window size: 2560x1440 minimum
DPI: Native (no scaling)
```

---

## 🚀 AUTOMATION INTEGRATION (FUTURE)

This prompt will become the foundation for:

**File:** `src/scanners/heatmap/auto_heatmap_broadcaster.py`

**Cron Schedule:**
```
# Every 6 hours for top 10 coins
0 */6 * * * python src/scanners/heatmap/auto_heatmap_broadcaster.py BTC
0 */6 * * * python src/scanners/heatmap/auto_heatmap_broadcaster.py ETH
0 */6 * * * python src/scanners/heatmap/auto_heatmap_broadcaster.py SOL
```

**Integration Points:**
- TimescaleDB: Store whale target data
- Redis: Publish signals when new zones detected
- Telegram: Auto-post to channel
- Twitter/X: Auto-post with affiliate link
- Email: Send to premium subscribers

---

## 📊 EXPECTED PERFORMANCE METRICS

**Per Coin Processing Time:**
- Navigation + screenshots: ~2-3 minutes per timeframe
- OCR + analysis: ~30 seconds per timeframe
- Annotation + rendering: ~1 minute per timeframe
- **Total per coin: ~35-45 minutes for all 10 timeframes**

**Resource Usage:**
- Chrome RAM: ~500MB per instance
- Image processing: ~200MB per timeframe
- Disk space: ~50MB per coin (all files)

**Quality Standards:**
- OCR accuracy: >95% for price levels
- Zone identification: Manual verification required
- Annotation precision: ±5px tolerance
- Social media compliance: All platforms

---

## 🔧 TROUBLESHOOTING

### Issue: Screenshot captures popup/modal
**Solution:** Add `wait_for` step after navigation to ensure popups are dismissed

### Issue: OCR extracts wrong values
**Solution:** Increase crop precision to isolate text areas better

### Issue: Annotations don't align with zones
**Solution:** Verify Y-axis coordinates by reading actual pixel positions from OCR data

### Issue: Social media image looks pixelated
**Solution:** Use higher resolution base screenshot (3840x2160) before cropping

### Issue: Timeframe selector doesn't work
**Solution:** Use `take_snapshot` to find correct UID, may have changed since last run

---

## 📝 CHANGELOG

**v1.0.0 (Oct 28, 2025)**
- Initial comprehensive automation prompt
- All 10 timeframes supported
- Full ImageSorcery integration
- Professional annotation standards
- Complete deliverables specification

---

## 📄 LICENSE & ATTRIBUTION

**Created by:** Vincent Ortega Jr
**Purpose:** CoinGlass liquidation heatmap automation for social media marketing
**Platform:** Vince Quant Whale Empire
**Data Source:** CoinGlass.com (with attribution)

All generated images MUST include:
- CoinGlass.com attribution
- @VincentOrtegaJr branding
- Affiliate tracking links (when posted)

---

**END OF AUTOMATION PROMPT**

🐋💎 NOW EXECUTE FOR: [COIN]
