# 🔥 COINGLASS LIQUIDATION HEATMAP AUTOMATION - VINCENT'S WORKFLOW

**LAST UPDATED**: October 27, 2025
**PURPOSE**: Comprehensive automated capture and annotation of ALL BTC liquidation heatmap timeframes
**USAGE**: Just tell Claude: "Run the CoinGlass heatmap workflow" and reference this doc

---

## 🎯 THE MISSION

Automate the complete capture, analysis, and annotation of CoinGlass BTC liquidation heatmaps across ALL timeframes for social media posting and API validation.

---

## 📋 EXACT WORKFLOW STEPS

### **PHASE 1: NAVIGATION & SETUP**

1. **Navigate to CoinGlass**
   - URL: `https://www.coinglass.com/pro/futures/LiquidationHeatMapNew`
   - Wait for page load (3-5 seconds)
   - Verify heatmap is visible

2. **Switch to Symbol View**
   - Click the **"Symbol"** tab (NOT "Pair")
   - Reason: Symbol view shows individual assets, Pair shows trading pairs
   - Verify BTC chart loads by default

3. **Confirm BTC Selected**
   - Check dropdown shows "BTC" selected
   - If not, select BTC from the crypto dropdown

---

### **PHASE 2: TIMEFRAME ITERATION**

Iterate through **ALL 10 timeframes** in this exact order:

```javascript
const timeframes = [
  '12 hour',
  '24 hour',   // Default view
  '48 hour',
  '3 day',
  '1 week',
  '2 week',
  '1 month',
  '3 month',
  '6 month',
  '1 Year'
];
```

**For EACH timeframe:**

#### Step 1: Select Timeframe
- Click the timeframe dropdown (shows "24 hour" by default)
- Select the target timeframe from the dropdown menu
- Wait 2-3 seconds for heatmap to render

#### Step 2: Capture Screenshot
- Take full-resolution screenshot of the heatmap area
- Include:
  - The heatmap visualization (purple/blue/cyan/yellow/green gradient)
  - The price chart overlay (pink line)
  - Y-axis price levels (right side: 115000, 120000, 125000, etc.)
  - X-axis time labels
  - Legend showing "Liquidation Leverage" and "Supercharts"
- Save as: `BTC_liquidation_heatmap_[timeframe]_raw.png`
- Example: `BTC_liquidation_heatmap_24hour_raw.png`

#### Step 3: Extract Yellow Zone Values
**Yellow zones = HIGH liquidation concentration areas**

Method A: **Hover Detection**
- Move mouse over yellow/bright green areas
- Wait for tooltip to appear (format: "27 Oct 2025, 22:05 | Price: 116932.2 | Liquidation Leverage: 25.31M")
- Extract values:
  - Price level
  - Liquidation leverage amount (in millions)
  - Timestamp

Method B: **Click & Read**
- Click on yellow zone
- If tooltip persists, screenshot it
- Extract same values as Method A

Method C: **Browser Script Extraction** (most reliable)
```javascript
// Execute in Chrome DevTools or via browser script
(function() {
  const dataPoints = [];

  // Find all high-leverage zones (yellow/green in heatmap)
  const zones = document.querySelectorAll('[data-liquidation]');

  zones.forEach(zone => {
    const price = zone.getAttribute('data-price');
    const leverage = zone.getAttribute('data-leverage');
    const timestamp = zone.getAttribute('data-time');

    if (parseFloat(leverage) > 20000000) { // > 20M liquidations
      dataPoints.push({
        price: parseFloat(price),
        leverage_millions: (parseFloat(leverage) / 1000000).toFixed(2),
        timestamp: timestamp
      });
    }
  });

  return JSON.stringify(dataPoints, null, 2);
})()
```

**Record ALL yellow zones found:**
```
Timeframe: 24 hour
Yellow Zones:
  1. Price: 116932.2 | Leverage: 25.31M | Time: Oct 27 22:05
  2. Price: 115500.0 | Leverage: 28.45M | Time: Oct 27 18:30
  3. Price: 118200.0 | Leverage: 22.10M | Time: Oct 27 23:15
  ... (continue for all yellow zones)
```

---

### **PHASE 3: IMAGE ANNOTATION WITH IMAGESORCERY**

For EACH captured screenshot, annotate using ImageSorcery MCP tools:

#### Annotation 1: Draw Rectangles Around Yellow Zones
```markdown
Use: mcp__imagesorcery-mcp__draw_rectangles

For each yellow zone:
- Draw RED rectangle with 3px thickness
- Coordinates: Identify yellow cluster location
- Color: [0, 0, 255] (BGR red)
- No fill (outline only)

Example:
{
  "input_path": "/Users/vincentortegajr/screenshots/BTC_liquidation_heatmap_24hour_raw.png",
  "rectangles": [
    {
      "x1": 450, "y1": 250,
      "x2": 650, "y2": 350,
      "color": [0, 0, 255],
      "thickness": 3,
      "filled": false
    }
  ],
  "output_path": "/Users/vincentortegajr/screenshots/BTC_liquidation_heatmap_24hour_annotated_step1.png"
}
```

#### Annotation 2: Add Arrows Pointing to Key Zones
```markdown
Use: mcp__imagesorcery-mcp__draw_arrows

- Draw GREEN arrows from empty space to yellow zones
- Arrow start: Above or to the side of zone (clear space)
- Arrow end: Center of yellow zone
- Color: [0, 255, 0] (BGR green)
- Thickness: 4px
- Tip length: 0.2 (20% of arrow length)

Example:
{
  "input_path": "/Users/vincentortegajr/screenshots/BTC_liquidation_heatmap_24hour_annotated_step1.png",
  "arrows": [
    {
      "x1": 350, "y1": 200,
      "x2": 550, "y2": 300,
      "color": [0, 255, 0],
      "thickness": 4,
      "tip_length": 0.2
    }
  ],
  "output_path": "/Users/vincentortegajr/screenshots/BTC_liquidation_heatmap_24hour_annotated_step2.png"
}
```

#### Annotation 3: Label Values with Text
```markdown
Use: mcp__imagesorcery-mcp__draw_texts

For each yellow zone, add text label:
- Format: "$[PRICE] - [LEVERAGE]M"
- Example: "$116,932 - 25.31M"
- Position: Near the arrow or above rectangle
- Color: WHITE [255, 255, 255] with black outline
- Font: FONT_HERSHEY_SIMPLEX
- Size: 1.5
- Thickness: 3

Example:
{
  "input_path": "/Users/vincentortegajr/screenshots/BTC_liquidation_heatmap_24hour_annotated_step2.png",
  "texts": [
    {
      "text": "$116,932 - 25.31M",
      "x": 380,
      "y": 180,
      "font_scale": 1.5,
      "color": [255, 255, 255],
      "thickness": 3,
      "font_face": "FONT_HERSHEY_SIMPLEX"
    }
  ],
  "output_path": "/Users/vincentortegajr/screenshots/BTC_liquidation_heatmap_24hour_annotated_step3.png"
}
```

#### Annotation 4: Add Header/Title
```markdown
Use: mcp__imagesorcery-mcp__draw_texts

Add title at top of image:
- Text: "BTC LIQUIDATION HEATMAP - [TIMEFRAME]"
- Position: Top center (x: 500, y: 50)
- Color: Yellow [0, 255, 255]
- Font size: 2.0
- Thickness: 4

Add subtitle with current BTC price:
- Text: "Current Price: $116,932 | 24h Liquidations: 25.31M"
- Position: Below title (x: 400, y: 90)
- Color: White [255, 255, 255]
- Font size: 1.2
- Thickness: 2

Example:
{
  "input_path": "/Users/vincentortegajr/screenshots/BTC_liquidation_heatmap_24hour_annotated_step3.png",
  "texts": [
    {
      "text": "BTC LIQUIDATION HEATMAP - 24 HOUR",
      "x": 500, "y": 50,
      "font_scale": 2.0,
      "color": [0, 255, 255],
      "thickness": 4
    },
    {
      "text": "Current Price: $116,932 | Total Liquidations: 25.31M",
      "x": 400, "y": 90,
      "font_scale": 1.2,
      "color": [255, 255, 255],
      "thickness": 2
    }
  ],
  "output_path": "/Users/vincentortegajr/screenshots/BTC_liquidation_heatmap_24hour_FINAL.png"
}
```

#### Annotation 5: Add Watermark (Optional)
```markdown
Use: mcp__imagesorcery-mcp__draw_texts

Bottom right corner:
- Text: "Data: CoinGlass.com | Analysis: Vincent Ortega Jr"
- Position: (x: 900, y: 750)
- Color: Gray [128, 128, 128]
- Font size: 0.8
- Thickness: 1

Example:
{
  "text": "Data: CoinGlass.com | @VincentOrtegaJr",
  "x": 900, "y": 750,
  "font_scale": 0.8,
  "color": [128, 128, 128],
  "thickness": 1
}
```

---

### **PHASE 4: DATA COMPILATION**

After processing ALL 10 timeframes, create a comprehensive data report:

#### Output Format: JSON
```json
{
  "capture_date": "2025-10-27T22:05:00Z",
  "btc_current_price": 116932.2,
  "timeframes_analyzed": 10,
  "data": [
    {
      "timeframe": "12 hour",
      "yellow_zones": [
        {
          "price": 116932.2,
          "liquidation_leverage_usd": 25310000,
          "liquidation_leverage_display": "25.31M",
          "timestamp": "2025-10-27T22:05:00Z",
          "zone_intensity": "high"
        }
      ],
      "total_liquidations_usd": 25310000,
      "screenshot_path": "/Users/vincentortegajr/screenshots/BTC_liquidation_heatmap_12hour_FINAL.png"
    },
    {
      "timeframe": "24 hour",
      "yellow_zones": [...],
      "total_liquidations_usd": 45200000,
      "screenshot_path": "/Users/vincentortegajr/screenshots/BTC_liquidation_heatmap_24hour_FINAL.png"
    }
    // ... repeat for all 10 timeframes
  ],
  "summary": {
    "total_yellow_zones_identified": 47,
    "highest_liquidation_zone": {
      "timeframe": "1 week",
      "price": 118500.0,
      "leverage": "78.92M"
    },
    "api_validation_ready": true
  }
}
```

Save as: `BTC_liquidation_heatmap_data_[date].json`

#### Output Format: Markdown Report
```markdown
# BTC LIQUIDATION HEATMAP ANALYSIS REPORT
**Date**: October 27, 2025 22:05
**Current BTC Price**: $116,932.20
**Timeframes Analyzed**: 10 (12h → 1 Year)

---

## 📊 SUMMARY

- **Total Yellow Zones Identified**: 47
- **Highest Liquidation Zone**: $118,500 with 78.92M leverage (1 Week timeframe)
- **Most Volatile Timeframe**: 1 Week (12 yellow zones)
- **Least Volatile Timeframe**: 12 Hour (2 yellow zones)

---

## 🔥 KEY LIQUIDATION LEVELS (ALL TIMEFRAMES)

### 12 HOUR
- **$116,932** - 25.31M liquidations
- **$115,500** - 18.42M liquidations

### 24 HOUR
- **$118,200** - 32.15M liquidations
- **$116,932** - 25.31M liquidations
- **$114,800** - 21.90M liquidations

### 48 HOUR
[Continue for all timeframes...]

---

## 📸 ANNOTATED IMAGES

All images saved to: `/Users/vincentortegajr/screenshots/`

1. `BTC_liquidation_heatmap_12hour_FINAL.png` ✅
2. `BTC_liquidation_heatmap_24hour_FINAL.png` ✅
3. `BTC_liquidation_heatmap_48hour_FINAL.png` ✅
... (10 total)

---

## ✅ SOCIAL MEDIA READY

All images are:
- ✅ High resolution (1920x1080+)
- ✅ Annotated with red rectangles
- ✅ Labeled with exact values
- ✅ Green arrows pointing to zones
- ✅ Header with timeframe
- ✅ Watermark with attribution
- ✅ Ready to post on Twitter/Telegram/Discord

---

## 🔗 API VALIDATION

This data is ready for comparison against CoinGlass API:
- Endpoint: `/api/futures/liquidation/heatmap`
- Symbol: BTC
- Validate: Price levels, leverage amounts, timestamps

Next step: Run API comparison script
```

Save as: `BTC_liquidation_heatmap_report_[date].md`

---

## 🎨 EXAMPLE FINAL IMAGE

**What the annotated heatmap should look like:**

```
┌─────────────────────────────────────────────────────────────┐
│  BTC LIQUIDATION HEATMAP - 24 HOUR                         │
│  Current Price: $116,932 | Total Liquidations: 25.31M      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  126,327 ─────────────────────────────────────────────────  │
│           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      │
│  125,000 ─────────────────────────────────────────────────  │
│           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      │
│  120,000 ─────────────────────────────────────────────────  │
│           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░██████░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓      │
│           ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░██████░░░░░░░░░▓▓▓▓▓▓▓▓      │
│  115,000 ─────────────────────────────────────────────────  │
│           ▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓      │
│           ▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓      │
│  110,000 ─────────────────────────────────────────────────  │
│           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      │
│                                                             │
│  Legend: █ Yellow Zone (High Risk)  ░ Green (Medium)       │
│          ▓ Purple/Blue (Low)        ~ Price Chart          │
│                                                             │
│  🔴 RED RECTANGLES around yellow zones                      │
│  ➡️ GREEN ARROWS pointing to zones                          │
│  📝 WHITE TEXT LABELS: "$116,932 - 25.31M"                  │
│                                                             │
│                    Data: CoinGlass.com | @VincentOrtegaJr  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 EXECUTION COMMAND

**To run this entire workflow, just tell me:**

```
"Run the CoinGlass heatmap automation workflow"
```

Or be specific:

```
"Execute the full CoinGlass BTC liquidation heatmap capture:
- Navigate to CoinGlass liquidation heatmap
- Click Symbol tab
- Capture all 10 timeframes (12h through 1 Year)
- Extract yellow zone values
- Annotate with rectangles, arrows, and text
- Generate the data report and markdown summary
- Save all images ready for social media"
```

---

## 📂 OUTPUT FILE STRUCTURE

After running, you'll have:

```
/Users/vincentortegajr/screenshots/
├── BTC_liquidation_heatmap_12hour_raw.png
├── BTC_liquidation_heatmap_12hour_FINAL.png
├── BTC_liquidation_heatmap_24hour_raw.png
├── BTC_liquidation_heatmap_24hour_FINAL.png
├── BTC_liquidation_heatmap_48hour_raw.png
├── BTC_liquidation_heatmap_48hour_FINAL.png
├── BTC_liquidation_heatmap_3day_raw.png
├── BTC_liquidation_heatmap_3day_FINAL.png
├── BTC_liquidation_heatmap_1week_raw.png
├── BTC_liquidation_heatmap_1week_FINAL.png
├── BTC_liquidation_heatmap_2week_raw.png
├── BTC_liquidation_heatmap_2week_FINAL.png
├── BTC_liquidation_heatmap_1month_raw.png
├── BTC_liquidation_heatmap_1month_FINAL.png
├── BTC_liquidation_heatmap_3month_raw.png
├── BTC_liquidation_heatmap_3month_FINAL.png
├── BTC_liquidation_heatmap_6month_raw.png
├── BTC_liquidation_heatmap_6month_FINAL.png
├── BTC_liquidation_heatmap_1year_raw.png
├── BTC_liquidation_heatmap_1year_FINAL.png
├── BTC_liquidation_heatmap_data_2025-10-27.json
└── BTC_liquidation_heatmap_report_2025-10-27.md

Total: 22 files (20 images + 2 data files)
```

---

## ⏱️ ESTIMATED TIME

- **Navigation & Setup**: 30 seconds
- **Per Timeframe**: 15-20 seconds (select, wait, capture, extract)
- **Per Annotation**: 30 seconds (4-5 ImageSorcery operations)
- **Data Compilation**: 1 minute

**Total Time**: ~8-10 minutes for complete workflow

---

## ✅ SUCCESS CRITERIA

The workflow is successful when:

1. ✅ All 10 timeframes captured
2. ✅ All yellow zones identified and values extracted
3. ✅ All images annotated with:
   - Red rectangles around yellow zones
   - Green arrows pointing to zones
   - White text labels with exact values
   - Title/header with timeframe
   - Watermark attribution
4. ✅ JSON data file generated
5. ✅ Markdown report generated
6. ✅ All 22 files saved to screenshots folder
7. ✅ Images ready for immediate social media posting

---

## 🔄 FUTURE ENHANCEMENTS

V2 of this workflow could include:
- [ ] Automatic posting to Twitter/Telegram
- [ ] API validation and discrepancy detection
- [ ] Historical comparison (compare today vs. last week)
- [ ] Alert system for extreme liquidation zones
- [ ] Video generation showing heatmap evolution
- [ ] Multi-asset support (ETH, SOL, etc.)

---

## 🎯 WHY THIS MATTERS

**For Trading:**
- Identifies high-risk liquidation zones
- Helps avoid getting liquidated
- Shows where market could move violently
- Validates API data accuracy

**For Social Media:**
- Professional annotated images
- Clear value labels
- Ready to post with one click
- Builds authority and credibility

**For Automation:**
- Repeatable workflow
- No manual clicking required
- Consistent output format
- Saves hours of manual work

---

**LAST UPDATED**: October 27, 2025
**VERSION**: 1.0
**NEXT RUN**: Just tell me "Run CoinGlass workflow" 🚀
