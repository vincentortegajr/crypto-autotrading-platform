# 🪄 IMAGESORCERY MCP - COMPLETE OVERVIEW

**Last Updated**: October 27, 2025
**Version**: Latest (Python 3.10+)
**Official Site**: [imagesorcery.net](https://imagesorcery.net)
**Purpose**: Computer vision-based local image processing for Vincent's Quant Whale Empire

---

## 🎯 WHAT IT ACTUALLY DOES

ImageSorcery MCP is a **LOCAL image processing powerhouse** that empowers AI assistants with computer vision capabilities:

### ✅ **WHAT IT CAN DO:**
- ✅ **Crop, resize, rotate** images with precision
- ✅ **Remove backgrounds** using AI
- ✅ **Draw text, shapes, arrows** on images
- ✅ **Add logos and watermarks**
- ✅ **Detect objects** using YOLO AI models
- ✅ **Extract text** from images with OCR (80+ languages)
- ✅ **Find objects by description** ("find yellow button")
- ✅ **Blur areas** or backgrounds
- ✅ **All processing happens LOCALLY** - no cloud uploads

### ❌ **WHAT IT CANNOT DO:**
- ❌ Navigate websites or browse the web
- ❌ Click UI elements or buttons
- ❌ Take screenshots (need OS tools or Terminator MCP)
- ❌ Control applications or browsers
- ❌ Real-time video processing

---

## 🔥 WHY THIS MATTERS FOR YOUR VISION

From `z-PRD-VISION-AND-BUILD-DOC-NO-POLYMARKET-YET.md`:

> **Your Mission**: Build the world's first transparent, whale-tracking, AI-powered crypto quant fund that:
> 1. Tracks liquidation heatmaps across ALL timeframes
> 2. Predicts whale targets by analyzing patterns
> 3. Broadcasts signals to Telegram, X, email, SMS
> 4. Turns followers into affiliates and investors

### **ImageSorcery's Role in Your Empire:**

```
WORKFLOW: CoinGlass Heatmap → Social Media Empire
══════════════════════════════════════════════════════════

STEP 1: CAPTURE (Manual or Terminator MCP)
├── Navigate to coinglass.com/liquidation-heatmap
├── Screenshot BTC heatmaps: 12h, 24h, 48h, 3d, 1w, 1m, 3m, 6m, 1y
└── Save to: data/images/heatmaps/raw/

STEP 2: ANALYZE (ImageSorcery MCP) ⭐ THIS IS WHERE MAGIC HAPPENS
├── OCR: Extract "Price: $116,932", "Liquidation Leverage: 25.31M"
├── Detect: Find yellow liquidation zones using YOLO AI
├── Find: Locate UI elements ("24 hour dropdown", "Symbol button")
├── Get coordinates of high-risk zones for whale targeting
└── Output: JSON with prices, leverage, coordinates

STEP 3: ANNOTATE (ImageSorcery MCP)
├── Draw red rectangles around yellow zones
├── Add green arrows pointing to key levels
├── Label exact values: "$116,932 - 25.31M Liquidations"
├── Add header: "BTC LIQUIDATION HEATMAP - 24 HOUR"
├── Overlay watermark: "CoinGlass + @VincentOrtegaJr"
└── Save to: data/images/heatmaps/annotated/

STEP 4: BROADCAST (Your Telegram/X APIs)
├── Post annotated images to Telegram channels
├── Tweet with CoinGlass affiliate link
├── Build social proof + commission revenue
└── Flywheel: Followers → Affiliates → Fund Investors
```

---

## 💻 INSTALLATION & SETUP

### **System Requirements:**
```bash
# Operating System
- macOS (M4 Max - your setup)
- Ubuntu/Debian Linux
- Windows (with WSL recommended)

# Python
- Python 3.10 or higher

# System Libraries (for OpenCV)
- ffmpeg
- libsm6
- libxext6
- libgl1-mesa-glx
```

### **Install System Dependencies:**

**macOS (your M4 Max):**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y ffmpeg libsm6 libxext6 libgl1-mesa-glx
```

### **Install ImageSorcery MCP (Recommended Method - pipx):**

```bash
# 1. Install pipx (if not already installed)
brew install pipx  # macOS

# 2. Install ImageSorcery MCP
pipx install imagesorcery-mcp

# 3. Run post-installation (CRITICAL - downloads models)
imagesorcery-mcp --post-install
```

**What `--post-install` does:**
- Creates `config.toml` configuration file
- Creates `models/` directory for AI models
- Downloads YOLO models (object detection):
  - `yoloe-11l-seg-pf.pt` (large, high accuracy)
  - `yoloe-11s-seg-pf.pt` (small, faster)
  - `yoloe-11l-seg.pt`
  - `yoloe-11s-seg.pt`
- Downloads CLIP model (text-based object finding)
- Creates `models/model_descriptions.json`

### **Configure MCP Server:**

Edit `~/.claude/global-mcp.json`:

```json
{
  "mcpServers": {
    "imagesorcery-mcp": {
      "command": "imagesorcery-mcp",
      "transportType": "stdio",
      "timeout": 100,
      "autoApprove": [
        "blur", "change_color", "config", "crop", "detect",
        "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles",
        "draw_texts", "fill", "find", "get_metainfo", "ocr",
        "overlay", "resize", "rotate"
      ]
    }
  }
}
```

**Restart Claude after adding this configuration.**

---

## 📂 FILE STRUCTURE (YOUR PROJECT INTEGRATION)

From your PRD, ImageSorcery integrates with these folders:

```
vince-quant-stack/
│
├── data/images/
│   ├── heatmaps/
│   │   ├── raw/                       # Screenshots from CoinGlass
│   │   │   ├── BTC_12h_2025-10-27.png
│   │   │   ├── BTC_24h_2025-10-27.png
│   │   │   └── ...
│   │   │
│   │   └── annotated/                 # ImageSorcery outputs ⭐
│   │       ├── BTC_12h_FINAL.png      # Social media ready
│   │       ├── BTC_24h_FINAL.png
│   │       └── ...
│   │
│   ├── agent_screenshots/             # AutoTrader captures
│   ├── tg_broadcasts/                 # Telegram-ready images
│   ├── x_broadcasts/                  # Twitter-ready images
│   ├── tutorials/                     # Strategy visual guides
│   └── strategy_visuals/              # Trading setup diagrams
│
├── data/processed/
│   └── heatmap_analysis/              # OCR + detection JSON
│       ├── BTC_12h_ocr.json          # Text extracted
│       ├── BTC_12h_zones.json        # Detected liquidation zones
│       └── ...
│
└── config/
    └── imagesorcery_config.toml       # ImageSorcery settings
```

---

## 🛠️ AVAILABLE AI MODELS

ImageSorcery comes with multiple pre-trained models:

### **Object Detection (YOLO)**
Downloaded automatically during `--post-install`:

- **`yoloe-11l-seg-pf.pt`** - Large segmentation model
  - Highest accuracy
  - Slower processing
  - Best for production/final outputs

- **`yoloe-11s-seg-pf.pt`** - Small segmentation model
  - Faster processing
  - Lower accuracy
  - Good for testing/iteration

- **`yoloe-11l-seg.pt`** - Large standard segmentation
- **`yoloe-11s-seg.pt`** - Small standard segmentation

### **Text-Based Detection (CLIP)**
- Installed via `--post-install`
- Allows finding objects by description:
  - "find yellow button"
  - "find Submit text"
  - "find red warning icon"

### **OCR (EasyOCR)**
- Supports 80+ languages
- Default: English (`en`)
- Available: `ru`, `fr`, `zh`, `ja`, `es`, `de`, etc.

### **Download Additional Models:**
```bash
# Download specific YOLO model from Ultralytics
download-yolo-models --ultralytics yoloe-11l-seg

# Download from Hugging Face
download-yolo-models --huggingface ultralytics/yolov8:yolov8m.pt

# Download specialized model (e.g., form field detection)
download-yolo-models --huggingface foduucom/web-form-ui-field-detection
```

---

## ⚙️ CONFIGURATION

ImageSorcery uses `config.toml` for default settings.

**Location**: Created in current directory during `--post-install`

**Example `config.toml`:**
```toml
[detection]
confidence_threshold = 0.75  # Minimum confidence (0.0 to 1.0)
default_model = "yoloe-11l-seg-pf.pt"

[find]
confidence_threshold = 0.75
default_model = "yoloe-11l-seg.pt"

[blur]
strength = 15  # Blur intensity (must be odd number)

[text]
font_scale = 1.0  # Default font size

[drawing]
color = [0, 0, 0]  # Default color (BGR format) - black
thickness = 1  # Default line thickness

[ocr]
language = "en"  # Default OCR language

[resize]
interpolation = "linear"  # Options: nearest, linear, area, cubic, lanczos

[telemetry]
enabled = false  # Anonymous usage stats (opt-in only)
```

**Modify defaults at runtime:**
```python
# Set detection confidence to 0.8
config(action="set", key="detection.confidence_threshold", value=0.8)

# Change default model
config(action="set", key="detection.default_model", value="yoloe-11s-seg-pf.pt")
```

---

## 🎯 INTEGRATION WITH YOUR STACK

### **With TimescaleDB (from your PRD):**

```python
# src/scanners/heatmap/heatmap_ocr_scanner.py
"""
Extract text from CoinGlass heatmap screenshots and store in TimescaleDB.
"""
import os
from datetime import datetime
from src.utils.config_utils import get_config
from src.utils.timescale_utils import execute_query

AGENT_NAME = "heatmap_ocr_scanner"

def scan_heatmap_ocr(image_path, symbol, timeframe):
    """Extract text from heatmap screenshot."""
    config = get_config()

    # Use ImageSorcery OCR
    ocr_results = imagesorcery_ocr(image_path, language="en")

    # Store in TimescaleDB
    for segment in ocr_results["text_segments"]:
        execute_query(
            """
            INSERT INTO heatmap_ocr
            (agent, symbol, timeframe, image_path, text_content, confidence, bbox, extracted_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
            """,
            (
                AGENT_NAME,
                symbol,
                timeframe,
                image_path,
                segment["text"],
                segment["confidence"],
                segment["bbox"]
            )
        )

    print(f"✅ {AGENT_NAME}: Extracted {len(ocr_results['text_segments'])} text segments")
    return ocr_results
```

### **With Redis Pub/Sub (from your PRD):**

```python
# src/scanners/heatmap/zone_detector.py
"""
Detect yellow liquidation zones and publish to Redis.
"""
from src.utils.redis_utils import publish_signal

AGENT_NAME = "liquidation_zone_detector"

def detect_liquidation_zones(image_path, symbol, timeframe):
    """Detect high-risk liquidation zones in heatmap."""

    # Use ImageSorcery to find yellow zones
    zones = imagesorcery_find(
        image_path,
        description="yellow liquidation zone",
        confidence=0.75,
        return_all_matches=True
    )

    # Publish each zone to Redis
    for zone in zones:
        signal = {
            "agent": AGENT_NAME,
            "symbol": symbol,
            "timeframe": timeframe,
            "zone_coordinates": zone["bbox"],
            "confidence": zone["confidence"],
            "detected_at": datetime.now().isoformat()
        }

        publish_signal("liquidation_zones", signal)

    return zones
```

### **With Telegram Broadcasting (from your PRD):**

```python
# src/agents/broadcast/heatmap_broadcaster.py
"""
Annotate heatmap and broadcast to Telegram.
"""
from src.agents.broadcast.telegram import send_telegram_photo

AGENT_NAME = "heatmap_broadcaster"

def broadcast_annotated_heatmap(raw_image_path, symbol, timeframe, zones):
    """Create annotated heatmap and send to Telegram."""

    # 1. Annotate image
    annotated_path = raw_image_path.replace("raw", "annotated").replace(".png", "_FINAL.png")

    # Draw red rectangles around zones
    for zone in zones:
        draw_rectangles(
            raw_image_path,
            rectangles=[{
                "x1": zone["bbox"][0],
                "y1": zone["bbox"][1],
                "x2": zone["bbox"][2],
                "y2": zone["bbox"][3],
                "color": [0, 0, 255],  # Red
                "thickness": 3
            }],
            output_path=annotated_path
        )

    # Add header text
    draw_texts(
        annotated_path,
        texts=[{
            "text": f"{symbol} LIQUIDATION HEATMAP - {timeframe}",
            "x": 50,
            "y": 50,
            "font_scale": 2.0,
            "color": [0, 255, 255],  # Yellow
            "thickness": 4
        }]
    )

    # 2. Send to Telegram
    caption = f"🔥 {symbol} Liquidation Zones Detected - {timeframe} Timeframe\\n\\nData: CoinGlass.com | Analysis: @VincentOrtegaJr"
    send_telegram_photo(annotated_path, caption)

    print(f"✅ {AGENT_NAME}: Broadcast {symbol} {timeframe} to Telegram")
```

---

## 🚨 IMPORTANT NOTES

### **Privacy & Security:**
- ✅ All processing happens **LOCALLY** on your M4 Max
- ✅ No images uploaded to cloud servers
- ✅ No API keys required (unlike cloud OCR services)
- ✅ Telemetry is **disabled by default** (opt-in only)

### **Performance Tips:**
- **Large models** (yoloe-11l) → Highest accuracy, slower (use for final outputs)
- **Small models** (yoloe-11s) → Faster, lower accuracy (use for testing)
- **OCR on high-res images** → Can be slow, consider resizing first
- **Batch processing** → Process multiple images in sequence for efficiency

### **File Path Requirements:**
- ✅ Always use **ABSOLUTE paths**: `/Users/vincentortegajr/...`
- ❌ NOT relative paths: `~/...` or `./...`
- ✅ Example: `/Users/vincentortegajr/crypto-autotrading-platform/data/images/heatmaps/BTC_24h.png`

### **Color Format (BGR not RGB):**
ImageSorcery uses OpenCV which uses **BGR** color format:
- Red: `[0, 0, 255]`
- Green: `[0, 255, 0]`
- Blue: `[255, 0, 0]`
- Yellow: `[0, 255, 255]`
- White: `[255, 255, 255]`
- Black: `[0, 0, 0]`

---

## 🔗 RESOURCES & PROMPTS

### **Resources:**
- `models://list` - Lists all available models in models directory

**Usage:**
```
"Which models are available in ImageSorcery?"
```

### **Prompts:**
- `remove-background` - Guided workflow for background removal

**Usage:**
```
"Use the remove-background prompt to remove the background from my photo 'portrait.jpg', keeping only the person"
```

---

## 📚 NEXT STEPS

1. **Read**: `tools.md` - Detailed documentation of all 17 tools
2. **Read**: `commands.md` - Copy/paste command snippets for your use cases
3. **Test**: Run OCR on a test image to verify installation
4. **Integrate**: Build your heatmap annotation pipeline

---

## 🤝 SUPPORT & DOCUMENTATION

- **Official Website**: [imagesorcery.net](https://imagesorcery.net)
- **GitHub**: [sunriseapps/imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp)
- **Tool Docs**: `/src/imagesorcery_mcp/tools/README.md`
- **Resource Docs**: `/src/imagesorcery_mcp/resources/README.md`
- **Prompt Docs**: `/src/imagesorcery_mcp/prompts/README.md`

---

**ImageSorcery MCP = Your local computer vision powerhouse for the Vince Quant Whale Empire** 🐋💎🚀
