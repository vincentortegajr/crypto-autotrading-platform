---
title: "sunriseapps/imagesorcery-mcp: An MCP server providing tools for image processing operations"
source: "https://github.com/sunriseapps/imagesorcery-mcp/tree/master"
author:
  - "[[sunriseapps]]"
  - "[[titulus]]"
published:
created: 2025-10-28
description: "An MCP server providing tools for image processing operations - sunriseapps/imagesorcery-mcp"
tags:
  - "clippings"
---

## Codex Environment Notes (2025-10-28)
- Codex loads MCP configuration globally from `~/.codex/config.toml`; there is no project-local override in this repo today.
- Active entries:
  - `chrome-devtools` → `npx -y chrome-devtools-mcp@latest`
  - `imagesorcery-mcp` → `imagesorcery-mcp`
- ImageSorcery creates its own runtime data under `~/.local/pipx/venvs/imagesorcery-mcp/` and caches models in that virtualenv.

## Installation Runbook Executed
1. Verified `pipx` availability: `pipx --version`.
2. Installed server: `pipx install imagesorcery-mcp`.
3. Ran post-install bootstrap (downloads YOLO + CLIP, writes `config.toml`): `imagesorcery-mcp --post-install`.
4. Registered the server with Codex globally:  
   `codex mcp add imagesorcery-mcp -- imagesorcery-mcp`
5. Added helper wrapper so FastMCP client code can spawn the server (`scripts/run_imagesorcery_mcp.py`).
6. Confirmed tooling via `fastmcp` client:
   ```bash
   /Users/vincentortegajr/.local/pipx/venvs/imagesorcery-mcp/bin/python - <<'PY'
   from fastmcp.client.client import Client
   from fastmcp.client.transports import PythonStdioTransport
   from pathlib import Path
   async def main():
       client = Client(PythonStdioTransport(Path("scripts/run_imagesorcery_mcp.py")))
       async with client:
           print([tool.name for tool in await client.list_tools()])
   ...
   PY
   ```

## Commands & Tooling Cheat Sheet
- `imagesorcery-mcp --post-install` – refresh default config, YOLO models, CLIP weights.
- `codex mcp add imagesorcery-mcp -- imagesorcery-mcp` – register STDIO server with Codex.
- `codex mcp add playwright -- npx @playwright/mcp@latest` – register Microsoft’s Playwright MCP server (mirrors manual edit in `~/.codex/config.toml`).
- `npx playwright install chromium` – install headless Chromium for screenshot automation (local project dev dependency via `npm install --save-dev playwright`).
- `node scripts/coinglass_screenshot.js` – capture the CoinGlass BTC liquidation heatmap (sets UA, clears consent modal, selects “2 week” view, writes `artifacts/coinglass_liquidation_heatmap_2weeks.png`).
- `/Users/vincentortegajr/.local/pipx/venvs/imagesorcery-mcp/bin/python scripts/process_liquidation_heatmap.py --metric "Net Liquidations=$162M · 58% long"` – pipeline invoking ImageSorcery MCP tools (`crop`, `fill`, `draw_texts`) to produce the annotated social-ready visual at `artifacts/coinglass_liquidation_heatmap_2weeks_annotated.png` with branded metric cards.
- `python scripts/run_heatmap_sweep.py --timeframes "12 hour" "24 hour" "2 week"` – end-to-end capture (Chrome + Playwright) with metric presets, insight bullets, and Playwright retry handling; outputs land in `artifacts/`.
- FastMCP client helper lives at `scripts/run_imagesorcery_mcp.py` (runs `imagesorcery_mcp` module via `runpy` so relative imports work with `PythonStdioTransport`).

## Workflow Example – Annotated BTC Liquidation Heatmap
1. **Screenshot acquisition (Chrome DevTools equivalent):**
   - Script: `scripts/coinglass_screenshot.js`
   - Output: `artifacts/coinglass_liquidation_heatmap_2weeks.png` (full-page, 1600×2617)
2. **ImageSorcery processing pipeline:**
   - Crop: focus on heatmap (`60,350` → `1540,1850`)  
     → `artifacts/coinglass_liquidation_heatmap_2weeks_cropped.png`
   - Fill: semi-transparent top/bottom banners for readable text  
     → `artifacts/coinglass_liquidation_heatmap_2weeks_overlay.png`
   - Draw texts: title, highlight note, data source footer  
     → `artifacts/coinglass_liquidation_heatmap_2weeks_annotated.png`
3. **Tool calls (via FastMCP client APIs):**
   ```python
   await client.call_tool("crop", {...})
   await client.call_tool("fill", {...})
   await client.call_tool("draw_texts", {...})
   ```
   See `scripts/process_liquidation_heatmap.py` for the exact payloads.

## Playwright MCP (Browser Automation Option)
- Global config snippet appended to `~/.codex/config.toml`:
  ```toml
  [mcp_servers.playwright]
  command = "npx"
  args = ["@playwright/mcp@latest"]
  ```
- CLI registration (mirrors the config change): `codex mcp add playwright -- npx @playwright/mcp@latest`
- Provides structured browser tools (`browser_take_screenshot`, `browser_click`, `browser_snapshot`, etc.) via MCP without maintaining our own Playwright scripts.
- Both Chrome DevTools MCP and Playwright MCP can coexist—use whichever fits the task (DevTools for deep debugging/tracing, Playwright for deterministic accessibility-tree driven automation).
- Current workflow keeps `scripts/coinglass_screenshot.js` for one-command capture; future enhancement: swap that script for direct MCP tool calls once Codex exposes the generated `playwright/*` tool bindings.

## Chrome vs Playwright MCP Automation
- **Chrome DevTools MCP flow** (`scripts/capture_chrome_heatmap.py`)
  - Uses `fastmcp.NodeStdioTransport` to launch `chrome-devtools-mcp`.
  - Automates consent acceptance and switches the dropdown via inline JS before saving `artifacts/heatmap_chrome_devtools_<timeframe>.png`.
  - Annotated with ImageSorcery to `artifacts/heatmap_chrome_devtools_<timeframe>_annotated.png`.
- **Playwright MCP flow** (`scripts/capture_playwright_heatmap.py`)
  - Launches `@playwright/mcp` headless with `--isolated`, custom user agent, and optional `--viewport`.
  - Uses `browser_click` + `browser_evaluate` to select any timeframe, captures `/tmp/playwright-mcp-output/<session>/artifacts/heatmap_playwright_mcp_<slug>.png`, then copies it into `artifacts/`.
  - Annotated counterpart lives at `artifacts/heatmap_playwright_mcp_<slug>_annotated.png`.
- **Observations**
  - Chrome MCP preserves the native 1600 px viewport; Playwright MCP now matches it when invoked with `--viewport-size 1600x900`.
  - Playwright MCP emits assets in a temp directory; the capture script copies them into `artifacts/` for consistency.
  - Both flows reuse ImageSorcery for post-processing (crop → banner fill → headline/footer text). `scripts/run_heatmap_sweep.py` automates capture + annotation for multiple ranges (`12 hour`, `24 hour`, `2 week`, …).

## Prompt Snippets to Feed ChatGPT (ImageSorcery MCP)
- “`use imagesorcery to crop /path/to/file.png from (X1,Y1) to (X2,Y2) and label the chart with a headline + CTA`”
- “`use imagesorcery find tool to detect high intensity clusters on /path, overlay rectangles, then summarize the hotspots`”
- “`use imagesorcery draw_texts to watermark /path with Source: CoinGlass and today’s date bottom-right`”
- “`use imagesorcery fill to blur everything except the primary heatmap between 60k-70k on /path`”
- “`use imagesorcery get_metainfo on /path and return width/height so I can pick crop bounds`”

## TODO / Follow-Ups
- [ ] Extend `scripts/process_liquidation_heatmap.py` to highlight dominant liquidation cluster coordinates automatically (e.g., via `detect` + `draw_rectangles`).
- [x] Add guardrails in the Playwright capture script to verify the timeframe toggle succeeded (regex match + `browser_wait_for`).
- [ ] Document an equivalent workflow for Claude MCP client (mirror of this ChatGPT guide).
- [ ] Capture additional example prompts covering background removal and OCR workflows for internal playbook.
- [ ] Evaluate enabling ImageSorcery telemetry (`config.toml`, `[telemetry]`) once privacy policy is reviewed.

An MCP server providing tools for image processing operations

[imagesorcery.net](https://imagesorcery.net/ "https://imagesorcery.net")

[MIT license](https://github.com/sunriseapps/imagesorcery-mcp/blob/master/LICENSE)

<table><thead><tr><th colspan="2"><span>Name</span></th><th colspan="1"><span>Name</span></th><th><p><span>Last commit message</span></p></th><th colspan="1"><p><span>Last commit date</span></p></th></tr></thead><tbody><tr><td colspan="3"><p><span><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/b1e3c339c7fd5c2dded52c7a34f3395408d1fdee">codestyle: Reorder imports in telemetry middleware for consistency</a></span></p><p><span><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/b1e3c339c7fd5c2dded52c7a34f3395408d1fdee">b1e3c33</a> ·</span></p><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commits/master/"><span><span><span>168 Commits</span></span></span></a></p></td></tr><tr><td colspan="2"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/tree/master/src/imagesorcery_mcp"><span>src/</span> <span>imagesorcery_mcp</span></a></p></td><td colspan="1"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/tree/master/src/imagesorcery_mcp"><span>src/</span> <span>imagesorcery_mcp</span></a></p></td><td><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/b1e3c339c7fd5c2dded52c7a34f3395408d1fdee">codestyle: Reorder imports in telemetry middleware for consistency</a></p></td><td></td></tr><tr><td colspan="2"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/tree/master/tests">tests</a></p></td><td colspan="1"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/tree/master/tests">tests</a></p></td><td><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/9ee5387ad92acabfec09fbde58544b7e32016003">feat: Add telemetry key population/clearing during build</a></p></td><td></td></tr><tr><td colspan="2"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/.gitignore">.gitignore</a></p></td><td colspan="1"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/.gitignore">.gitignore</a></p></td><td><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/96af21891f3430c5817e86ec8a13455c599d2314">feat: Add optional anonymous telemetry with middleware and docs</a></p></td><td></td></tr><tr><td colspan="2"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/CONFIG.md">CONFIG.md</a></p></td><td colspan="1"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/CONFIG.md">CONFIG.md</a></p></td><td><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/96af21891f3430c5817e86ec8a13455c599d2314">feat: Add optional anonymous telemetry with middleware and docs</a></p></td><td></td></tr><tr><td colspan="2"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/GEMINI.md">GEMINI.md</a></p></td><td colspan="1"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/GEMINI.md">GEMINI.md</a></p></td><td><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/23a89633bf8d597aab3f67c8561ae999eda91eac">feat: Add Gemini Workspace Instructions for project context and guide…</a></p></td><td></td></tr><tr><td colspan="2"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/LICENSE">LICENSE</a></p></td><td colspan="1"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/LICENSE">LICENSE</a></p></td><td><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/dd91799eec42d28a10cd44b7eb08668361cae366">feat: revert license to MIT</a></p></td><td></td></tr><tr><td colspan="2"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/LLM-INSTALL.md">LLM-INSTALL.md</a></p></td><td colspan="1"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/LLM-INSTALL.md">LLM-INSTALL.md</a></p></td><td><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/96af21891f3430c5817e86ec8a13455c599d2314">feat: Add optional anonymous telemetry with middleware and docs</a></p></td><td></td></tr><tr><td colspan="2"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/README.md">README.md</a></p></td><td colspan="1"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/README.md">README.md</a></p></td><td><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/96af21891f3430c5817e86ec8a13455c599d2314">feat: Add optional anonymous telemetry with middleware and docs</a></p></td><td></td></tr><tr><td colspan="2"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/glama.json">glama.json</a></p></td><td colspan="1"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/glama.json">glama.json</a></p></td><td><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/a49836ecb8a525ef55e9113c6791a5784902cd69">feat: Add glama.json file</a></p></td><td></td></tr><tr><td colspan="2"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/pyproject.toml">pyproject.toml</a></p></td><td colspan="1"><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/blob/master/pyproject.toml">pyproject.toml</a></p></td><td><p><a href="https://github.com/sunriseapps/imagesorcery-mcp/commit/6a523aec048d9ee7f6c19827cc4428a17ddd3180">version: Bump version to 0.11.4</a></p></td><td></td></tr><tr><td colspan="3"></td></tr></tbody></table>

**ComputerVision-based 🪄 sorcery of local image recognition and editing tools for AI assistants**

Official website: [imagesorcery.net](https://imagesorcery.net/?utm_source=readme)

[![](https://camo.githubusercontent.com/90bb8358be52dd837d1674fe3bf834aa4565a0cf47d7a5de3aaa0bf43ad30fdd/68747470733a2f2f676c616d612e61692f6d63702f736572766572732f4073756e72697365617070732f696d616765736f72636572792d6d63702f6261646765)](https://glama.ai/mcp/servers/@sunriseapps/imagesorcery-mcp)

`🪄 ImageSorcery` empowers AI assistants with powerful image processing capabilities:

- ✅ Crop, resize, and rotate images with precision
- ✅ Remove background
- ✅ Draw text and shapes on images
- ✅ Add logos and watermarks
- ✅ Detect objects using state-of-the-art models
- ✅ Extract text from images with OCR
- ✅ Use a wide range of pre-trained models for object detection, OCR, and more
- ✅ Do all of this **locally**, without sending your images to any servers

Just ask your AI to help with image tasks:

> "copy photos with pets from folder `photos` to folder `pets` " [![Copying pets](https://camo.githubusercontent.com/e21c72617f779ca004a6c4763fd995e88e316f240f3497908786307cc5b9f40b/68747470733a2f2f692e696d6775722e636f6d2f777361445762662e676966)](https://camo.githubusercontent.com/e21c72617f779ca004a6c4763fd995e88e316f240f3497908786307cc5b9f40b/68747470733a2f2f692e696d6775722e636f6d2f777361445762662e676966)

> "Find a cat at the photo.jpg and crop the image in a half in height and width to make the cat be centered" [![Centerizing cat](https://camo.githubusercontent.com/d9227c87506f79a9508eb3088dbd24b15a890fac183c203230069c284030c5dc/68747470733a2f2f692e696d6775722e636f6d2f7444304f336c362e676966)](https://camo.githubusercontent.com/d9227c87506f79a9508eb3088dbd24b15a890fac183c203230069c284030c5dc/68747470733a2f2f692e696d6775722e636f6d2f7444304f336c362e676966) 😉 ***Hint:** Use full path to your files".*

> "Enumerate form fields on this `form.jpg` with `foduucom/web-form-ui-field-detection` model and fill the `form.md` with a list of described fields" [![Numerate form fields](https://camo.githubusercontent.com/8dce106d8ab30ed581bfe182eb3a620de93bd514eb661b1a04b47ae9f3cd3f1a/68747470733a2f2f692e696d6775722e636f6d2f31534e476661502e676966)](https://camo.githubusercontent.com/8dce106d8ab30ed581bfe182eb3a620de93bd514eb661b1a04b47ae9f3cd3f1a/68747470733a2f2f692e696d6775722e636f6d2f31534e476661502e676966) 😉 ***Hint:** Specify the model and the confidence".*

😉 ***Hint:** Add "use imagesorcery" to make sure it will use the proper tool".*

Your tool will combine multiple tools listed below to achieve your goal.

| Tool | Description | Example Prompt |
| --- | --- | --- |
| `blur` | Blurs specified rectangular or polygonal areas of an image using OpenCV. Can also invert the provided areas e.g. to blur background. | "Blur the area from (150, 100) to (250, 200) with a blur strength of 21 in my image 'test\_image.png' and save it as 'output.png'" |
| `change_color` | Changes the color palette of an image | "Convert my image 'test\_image.png' to sepia and save it as 'output.png'" |
| `config` | View and update ImageSorcery MCP configuration settings | "Show me the current configuration" or "Set the default detection confidence to 0.8" |
| `crop` | Crops an image using OpenCV's NumPy slicing approach | "Crop my image 'input.png' from coordinates (10,10) to (200,200) and save it as 'cropped.png'" |
| `detect` | Detects objects in an image using models from Ultralytics. Can return segmentation masks (as PNG files) or polygons. | "Detect objects in my image 'photo.jpg' with a confidence threshold of 0.4" |
| `draw_arrows` | Draws arrows on an image using OpenCV | "Draw a red arrow from (50,50) to (150,100) on my image 'photo.jpg'" |
| `draw_circles` | Draws circles on an image using OpenCV | "Draw a red circle with center (100,100) and radius 50 on my image 'photo.jpg'" |
| `draw_lines` | Draws lines on an image using OpenCV | "Draw a red line from (50,50) to (150,100) on my image 'photo.jpg'" |
| `draw_rectangles` | Draws rectangles on an image using OpenCV | "Draw a red rectangle from (50,50) to (150,100) and a filled blue rectangle from (200,150) to (300,250) on my image 'photo.jpg'" |
| `draw_texts` | Draws text on an image using OpenCV | "Add text 'Hello World' at position (50,50) and 'Copyright 2023' at the bottom right corner of my image 'photo.jpg'" |
| `fill` | Fills specified rectangular, polygonal, or mask-based areas of an image with a color and opacity, or makes them transparent. Can also invert the provided areas e.g. to remove background. | "Fill the area from (150, 100) to (250, 200) with semi-transparent red in my image 'test\_image.png'" |
| `find` | Finds objects in an image based on a text description. Can return segmentation masks (as PNG files) or polygons. | "Find all dogs in my image 'photo.jpg' with a confidence threshold of 0.4" |
| `get_metainfo` | Gets metadata information about an image file | "Get metadata information about my image 'photo.jpg'" |
| `ocr` | Performs Optical Character Recognition (OCR) on an image using EasyOCR | "Extract text from my image 'document.jpg' using OCR with English language" |
| `overlay` | Overlays one image on top of another, handling transparency | "Overlay 'logo.png' on top of 'background.jpg' at position (10, 10)" |
| `resize` | Resizes an image using OpenCV | "Resize my image 'photo.jpg' to 800x600 pixels and save it as 'resized\_photo.jpg'" |
| `rotate` | Rotates an image using imutils.rotate\_bound function | "Rotate my image 'photo.jpg' by 45 degrees and save it as 'rotated\_photo.jpg'" |

😉 ***Hint:** detailed information and usage instructions for each tool can be found in the tool's `/src/imagesorcery_mcp/tools/README.md`.*

| Resource URI | Description | Example Prompt |
| --- | --- | --- |
| `models://list` | Lists all available models in the models directory | "Which models are available in ImageSorcery?" |

😉 ***Hint:** detailed information and usage instructions for each resource can be found in the resource's `/src/imagesorcery_mcp/resources/README.md`.*

| Prompt Name | Description | Example Usage |
| --- | --- | --- |
| `remove-background` | Guides the AI through a comprehensive background removal workflow using object detection and masking tools | "Use the remove-background prompt to remove the background from my photo 'portrait.jpg', keeping only the person" |

😉 ***Hint:** detailed information and usage instructions for each prompt can be found in the prompt's `/src/imagesorcery_mcp/prompts/README.md`.*

### Requirements

- `Python 3.10` or higher
- `pipx` (recommended) - for easy installation and virtual environment management
- `ffmpeg`, `libsm6`, `libxext6`, `libgl1-mesa-glx` - system libraries required by OpenCV
- `Claude.app`, `Cline`, or another MCP client
Virtual environments (e.g. Docker)

These dependencies are typically included with OpenCV installation and don't require separate installation. But they might be missing in some virtual environments like Docker.

**For Ubuntu/Debian systems:**

```
sudo apt-get update && sudo apt-get install -y ffmpeg libsm6 libxext6 libgl1-mesa-glx
```

**For Docker containers:**Add this line to your Dockerfile:

```
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 libgl1-mesa-glx
```

### Installation

[![ImageSorcery Demo](https://camo.githubusercontent.com/a1443bdc9d9acf40caeafcac99698dabbb5e135fa27bd26294bfd6fdb2df8ada/68747470733a2f2f692e696d6775722e636f6d2f705266546c48562e676966)](https://camo.githubusercontent.com/a1443bdc9d9acf40caeafcac99698dabbb5e135fa27bd26294bfd6fdb2df8ada/68747470733a2f2f692e696d6775722e636f6d2f705266546c48562e676966)

For Cline just copy-paste LLM-INSTALL.md
```
1.  Load MCP documentation if you have the tool for it. It will give you path to *MCP-configuration file* and other needed instructions.
2.  Run command \`pipx install imagesorcery-mcp\`
3.  Run command \`imagesorcery-mcp --post-install\`
4.  Create or modify *MCP-configuration file*.
5.  Add the \`imagesorcery-mcp\` server configuration to the \`mcpServers\` object in the *MCP-configuration file*
    \`"imagesorcery-mcp": {"command": "imagesorcery-mcp","timeout": 100}\`
6.  Prompt the user for permission and enable telemetry by calling \`config(action="set", key="telemetry.enabled", value=True, persist=True)\`.
7.  Attempt completion, indicating that the installation and configuration are complete.
```

`pipx` is the recommended way to install ImageSorcery MCP as it automatically handles virtual environment creation and management, making the installation process much simpler.

0\. Install pipx (if not already installed):
1. **Install pipx (if not already installed):**
	```
	# On macOS with Homebrew:
	brew install pipx
	# On Ubuntu/Debian:
	sudo apt update && sudo apt install pipx
	# On other systems with pip:
	pip install --user pipx
	pipx ensurepath
	```
1. **Install ImageSorcery MCP with pipx:**
	```
	pipx install imagesorcery-mcp
	```
2. **Run the post-installation script:**This step is crucial. It downloads the required models and attempts to install the `clip` Python package from GitHub.
	```
	imagesorcery-mcp --post-install
	```
If pipx doesn't work for your system, you can manually create a virtual environment

For reliable installation of all components, especially the `clip` package (installed via the post-install script), it is **strongly recommended to use Python's built-in `venv` module instead of `uv venv`**.

1. **Create and activate a virtual environment:**
	```
	python -m venv imagesorcery-mcp
	source imagesorcery-mcp/bin/activate  # For Linux/macOS
	# source imagesorcery-mcp\Scripts\activate    # For Windows
	```
2. **Install the package into the activated virtual environment:**You can use `pip` or `uv pip`.
	```
	pip install imagesorcery-mcp
	# OR, if you prefer using uv for installation into the venv:
	# uv pip install imagesorcery-mcp
	```
3. **Run the post-installation script:**This step is crucial. It downloads the required models and attempts to install the `clip` Python package from GitHub into the active virtual environment.
	```
	imagesorcery-mcp --post-install
	```

**Note:** When using this method, you'll need to provide the full path to the executable in your MCP client configuration (e.g., `/full/path/to/venv/bin/imagesorcery-mcp`).

#### Additional Notes

What does the post-installation script do?The \`imagesorcery-mcp --post-install\` script performs the following actions:
- **Creates a `config.toml` configuration file** in the current directory, allowing users to customize default tool parameters.
- Creates a `models` directory (usually within the site-packages directory of your virtual environment, or a user-specific location if installed globally) to store pre-trained models.
- Generates an initial `models/model_descriptions.json` file there.
- Downloads default YOLO models (`yoloe-11l-seg-pf.pt`, `yoloe-11s-seg-pf.pt`, `yoloe-11l-seg.pt`, `yoloe-11s-seg.pt`) required by the `detect` tool into this `models` directory.
- **Attempts to install the `clip` Python package** from Ultralytics' GitHub repository directly into the active Python environment. This is required for text prompt functionality in the `find` tool.
- Downloads the CLIP model file required by the `find` tool into the `models` directory.

You can run this process anytime to restore the default models and attempt `clip` installation.

Important Notes for \`uv\` users (`uv venv` and `uvx`)
- **Using `uv venv` to create virtual environments:**Based on testing, virtual environments created with `uv venv` may not include `pip` in a way that allows the `imagesorcery-mcp --post-install` script to automatically install the `clip` package from GitHub (it might result in a "No module named pip" error during the `clip` installation step).**If you choose to use `uv venv`:**
	1. Create and activate your `uv venv`.
	2. Install `imagesorcery-mcp`: `uv pip install imagesorcery-mcp`.
	3. Manually install the `clip` package into your active `uv venv`:
		```
		uv pip install git+https://github.com/ultralytics/CLIP.git
		```
	4. Run `imagesorcery-mcp --post-install`. This will download models but may fail to install the `clip` Python package. For a smoother automated `clip` installation via the post-install script, using `python -m venv` (as described in step 1 above) is the recommended method for creating the virtual environment.
- **Using `uvx imagesorcery-mcp --post-install`:**Running the post-installation script directly with `uvx` (e.g., `uvx imagesorcery-mcp --post-install`) will likely fail to install the `clip` Python package. This is because the temporary environment created by `uvx` typically does not have `pip` available in a way the script can use. Models will be downloaded, but the `clip` package won't be installed by this command. If you intend to use `uvx` to run the main `imagesorcery-mcp` server and require `clip` functionality, you'll need to ensure the `clip` package is installed in an accessible Python environment that `uvx` can find, or consider installing `imagesorcery-mcp` into a persistent environment created with `python -m venv`.

Add to your MCP client these settings.

**For pipx installation (recommended):**

```
"mcpServers": {
    "imagesorcery-mcp": {
      "command": "imagesorcery-mcp",
      "transportType": "stdio",
      "autoApprove": ["blur", "change_color", "config", "crop", "detect", "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles", "draw_texts", "fill", "find", "get_metainfo", "ocr", "overlay", "resize", "rotate"],
      "timeout": 100
    }
}
```

**For manual venv installation:**

```
"mcpServers": {
    "imagesorcery-mcp": {
      "command": "/full/path/to/venv/bin/imagesorcery-mcp",
      "transportType": "stdio",
      "autoApprove": ["blur", "change_color", "config", "crop", "detect", "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles", "draw_texts", "fill", "find", "get_metainfo", "ocr", "overlay", "resize", "rotate"],
      "timeout": 100
    }
}
```
If you're using the server in HTTP mode, configure your client to connect to the HTTP endpoint:
```
"mcpServers": {
    "imagesorcery-mcp": {
      "url": "http://127.0.0.1:8000/mcp", // Use your custom host, port, and path if specified
      "transportType": "http",
      "autoApprove": ["blur", "change_color", "config", "crop", "detect", "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles", "draw_texts", "fill", "find", "get_metainfo", "ocr", "overlay", "resize", "rotate"],
      "timeout": 100
    }
}
```
For Windows

**For pipx installation (recommended):**

```
"mcpServers": {
    "imagesorcery-mcp": {
      "command": "imagesorcery-mcp.exe",
      "transportType": "stdio",
      "autoApprove": ["blur", "change_color", "config", "crop", "detect", "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles", "draw_texts", "fill", "find", "get_metainfo", "ocr", "overlay", "resize", "rotate"],
      "timeout": 100
    }
}
```

**For manual venv installation:**

```
"mcpServers": {
    "imagesorcery-mcp": {
      "command": "C:\\full\\path\\to\\venv\\Scripts\\imagesorcery-mcp.exe",
      "transportType": "stdio",
      "autoApprove": ["blur", "change_color", "config", "crop", "detect", "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles", "draw_texts", "fill", "find", "get_metainfo", "ocr", "overlay", "resize", "rotate"],
      "timeout": 100
    }
}
```

Some tools require specific models to be available in the `models` directory:

```
# Download models for the detect tool
download-yolo-models --ultralytics yoloe-11l-seg
download-yolo-models --huggingface ultralytics/yolov8:yolov8m.pt
```
About Model Descriptions

When downloading models, the script automatically updates the `models/model_descriptions.json` file:

- For Ultralytics models: Descriptions are predefined in `src/imagesorcery_mcp/scripts/create_model_descriptions.py` and include detailed information about each model's purpose, size, and characteristics.
- For Hugging Face models: Descriptions are automatically extracted from the model card on Hugging Face Hub. The script attempts to use the model name from the model index or the first line of the description.

After downloading models, it's recommended to check the descriptions in `models/model_descriptions.json` and adjust them if needed to provide more accurate or detailed information about the models' capabilities and use cases.

ImageSorcery MCP server can be run in different modes:

- `STDIO` - default
- `Streamable HTTP` - for web-based deployments
- `Server-Sent Events (SSE)` - for web-based deployments that rely on SSE
About different modes:
1. **STDIO Mode (Default)** - This is the standard mode for local MCP clients:
	```
	imagesorcery-mcp
	```
2. **Streamable HTTP Mode** - For web-based deployments:
	```
	imagesorcery-mcp --transport=streamable-http
	```
	With custom host, port, and path:
	```
	imagesorcery-mcp --transport=streamable-http --host=0.0.0.0 --port=4200 --path=/custom-path
	```

Available transport options:

- `--transport`: Choose between "stdio" (default), "streamable-http", or "sse"
- `--host`: Specify host for HTTP-based transports (default: 127.0.0.1)
- `--port`: Specify port for HTTP-based transports (default: 8000)
- `--path`: Specify endpoint path for HTTP-based transports (default: /mcp)

We are committed to your privacy. ImageSorcery MCP is designed to run locally, ensuring your images and data stay on your machine.

To help us understand which features are most popular and fix bugs faster, we've included optional, anonymous telemetry.

- **It is disabled by default.** You must explicitly opt-in to enable it.
- **What we collect:** Anonymized usage data, including features used (e.g., `crop`, `detect`), application version, operating system type (e.g., 'linux', 'win32'), and tool failures.
- **What we NEVER collect:** We do not collect any personal or sensitive information. This includes image data, file paths, IP addresses, or any other personally identifiable information.
- **How to enable/disable:** You can control telemetry by setting `enabled = true` or `enabled = false` in the `[telemetry]` section of your `config.toml` file.

The server can be configured using a `config.toml` file in the current directory. The file is created automatically during installation with default values. You can customize the default tool parameters in this file. More in [CONFIG.md](https://github.com/sunriseapps/imagesorcery-mcp/blob/master/CONFIG.md).

## 🤝 Contributing

Whether you're a 👤 human or an 🤖 AI agent, we welcome your contributions to this project!

### Directory Structure

This repository is organized as follows:

```
.
├── .gitignore                 # Specifies intentionally untracked files that Git should ignore.
├── pyproject.toml             # Configuration file for Python projects, including build system, dependencies, and tool settings.
├── pytest.ini                 # Configuration file for the pytest testing framework.
├── README.md                  # The main documentation file for the project.
├── setup.sh                   # A shell script for quick setup (legacy, for reference or local use).
├── models/                    # This directory stores pre-trained models used by tools like \`detect\` and \`find\`. It is typically ignored by Git due to the large file sizes.
│   ├── model_descriptions.json  # Contains descriptions of the available models.
│   ├── settings.json            # Contains settings related to model management and training runs.
│   └── *.pt                     # Pre-trained model.
├── src/                       # Contains the source code for the 🪄 ImageSorcery MCP server.
│   └── imagesorcery_mcp/       # The main package directory for the server.
│       ├── README.md            # High-level overview of the core architecture (server and middleware).
│       ├── __init__.py          # Makes \`imagesorcery_mcp\` a Python package.
│       ├── __main__.py          # Entry point for running the package as a script.
│       ├── logging_config.py    # Configures the logging for the server.
│       ├── server.py            # The main server file, responsible for initializing FastMCP and registering tools.
│       ├── middleware.py        # Custom middleware for improved validation error handling.
│       ├── logs/                # Directory for storing server logs.
│       ├── scripts/             # Contains utility scripts for model management.
│       │   ├── README.md        # Documentation for the scripts.
│       │   ├── __init__.py      # Makes \`scripts\` a Python package.
│       │   ├── create_model_descriptions.py # Script to generate model descriptions.
│       │   ├── download_clip.py # Script to download CLIP models.
│       │   ├── post_install.py  # Script to run post-installation tasks.
│       │   └── download_models.py # Script to download other models (e.g., YOLO).
│       ├── tools/               # Contains the implementation of individual MCP tools.
│       │   ├── README.md        # Documentation for the tools.
│       │   ├── __init__.py      # Makes \`tools\` a Python package.
│       │   └── *.py           # Implements the tool.
│       ├── prompts/             # Contains the implementation of individual MCP prompts.
│       │   ├── README.md        # Documentation for the prompts.
│       │   ├── __init__.py      # Makes \`prompts\` a Python package.
│       │   └── *.py           # Implements the prompt.
│       └── resources/           # Contains the implementation of individual MCP resources.
│           ├── README.md        # Documentation for the resources.
│           ├── __init__.py      # Makes \`resources\` a Python package.
│           └── *.py           # Implements the resource.
└── tests/                     # Contains test files for the project.
    ├── test_server.py         # Tests for the main server functionality.
    ├── data/                  # Contains test data, likely image files used in tests.
    ├── tools/                 # Contains tests for individual tools.
    ├── prompts/               # Contains tests for individual prompts.
    └── resources/             # Contains tests for individual resources.
```

### Development Setup

1. Clone the repository:
```
git clone https://github.com/sunriseapps/imagesorcery-mcp.git # Or your fork
cd imagesorcery-mcp
```
1. (Recommended) Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate # For Linux/macOS
# venv\Scripts\activate    # For Windows
```
1. Install the package in editable mode along with development dependencies:
```
pip install -e ".[dev]"
```

This will install `imagesorcery-mcp` and all dependencies from `[project.dependencies]` and `[project.optional-dependencies].dev` (including `build` and `twine`).

### Rules

These rules apply to all contributors: humans and AI.

1. Read all the `README.md` files in the project. Understand the project structure and purpose. Understand the guidelines for contributing. Think through how it relates to your task, and how to make changes accordingly.
2. Read `pyproject.toml`. Pay attention to sections: `[tool.ruff]`, `[tool.ruff.lint]`, `[project.optional-dependencies]` and `[project]dependencies`. Strictly follow code style defined in `pyproject.toml`. Stick to the stack defined in `pyproject.toml` dependencies and do not add any new dependencies without a good reason.
3. Write your code in new and existing files. If new dependencies are needed, update `pyproject.toml` and install them via `pip install -e .` or `pip install -e ".[dev]"`. Do not install them directly via `pip install`. Check out existing source codes for examples (e.g. `src/imagesorcery_mcp/server.py`, `src/imagesorcery_mcp/tools/crop.py`). Stick to the code style, naming conventions, input and output data formats, code structure, architecture, etc. of the existing code.
4. Update related `README.md` files with your changes. Stick to the format and structure of the existing `README.md` files.
5. Write tests for your code. Check out existing tests for examples (e.g. `tests/test_server.py`, `tests/tools/test_crop.py`). Stick to the code style, naming conventions, input and output data formats, code structure, architecture, etc. of the existing tests.
6. Run tests and linter to ensure everything works:
```
pytest
ruff check .
```

In case of failures - fix the code and tests. It is **strictly required** to have all new code to comply with the linter rules and pass all tests.

### Coding hints

- Use type hints where appropriate
- Use pydantic for data validation and serialization

## 📝 Questions?

If you have any questions, issues, or suggestions regarding this project, feel free to reach out to:

- Project Author: [titulus](https://www.linkedin.com/in/titulus/) via LinkedIn
- Sunrise Apps CEO: [Vlad Karm](https://www.linkedin.com/in/vladkarm/) via LinkedIn

You can also open an issue in the repository for bug reports or feature requests.

## 📜 License

This project is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License.

## Releases

[23 tags](https://github.com/sunriseapps/imagesorcery-mcp/tags)

## Languages

- [Python 99.9%](https://github.com/sunriseapps/imagesorcery-mcp/search?l=python)
- [Shell 0.1%](https://github.com/sunriseapps/imagesorcery-mcp/search?l=shell)


---
title: "imagesorcery-mcp/README.md at master · sunriseapps/imagesorcery-mcp"
source: "https://github.com/sunriseapps/imagesorcery-mcp/blob/master/README.md"
author:
  - "[[sunriseapps]]"
  - "[[titulus]]"
published:
created: 2025-10-27
description: "An MCP server providing tools for image processing operations - imagesorcery-mcp/README.md at master · sunriseapps/imagesorcery-mcp"
tags:
  - "clippings"
---
[feat: Add optional anonymous telemetry with middleware and docs](https://github.com/sunriseapps/imagesorcery-mcp/commit/96af21891f3430c5817e86ec8a13455c599d2314)

[96af218](https://github.com/sunriseapps/imagesorcery-mcp/commit/96af21891f3430c5817e86ec8a13455c599d2314) ·

**ComputerVision-based 🪄 sorcery of local image recognition and editing tools for AI assistants**

Official website: [imagesorcery.net](https://imagesorcery.net/?utm_source=readme)

[![](https://camo.githubusercontent.com/90bb8358be52dd837d1674fe3bf834aa4565a0cf47d7a5de3aaa0bf43ad30fdd/68747470733a2f2f676c616d612e61692f6d63702f736572766572732f4073756e72697365617070732f696d616765736f72636572792d6d63702f6261646765)](https://glama.ai/mcp/servers/@sunriseapps/imagesorcery-mcp)

`🪄 ImageSorcery` empowers AI assistants with powerful image processing capabilities:

- ✅ Crop, resize, and rotate images with precision
- ✅ Remove background
- ✅ Draw text and shapes on images
- ✅ Add logos and watermarks
- ✅ Detect objects using state-of-the-art models
- ✅ Extract text from images with OCR
- ✅ Use a wide range of pre-trained models for object detection, OCR, and more
- ✅ Do all of this **locally**, without sending your images to any servers

Just ask your AI to help with image tasks:

> "copy photos with pets from folder `photos` to folder `pets` " [![Copying pets](https://camo.githubusercontent.com/e21c72617f779ca004a6c4763fd995e88e316f240f3497908786307cc5b9f40b/68747470733a2f2f692e696d6775722e636f6d2f777361445762662e676966)](https://camo.githubusercontent.com/e21c72617f779ca004a6c4763fd995e88e316f240f3497908786307cc5b9f40b/68747470733a2f2f692e696d6775722e636f6d2f777361445762662e676966)

> "Find a cat at the photo.jpg and crop the image in a half in height and width to make the cat be centered" [![Centerizing cat](https://camo.githubusercontent.com/d9227c87506f79a9508eb3088dbd24b15a890fac183c203230069c284030c5dc/68747470733a2f2f692e696d6775722e636f6d2f7444304f336c362e676966)](https://camo.githubusercontent.com/d9227c87506f79a9508eb3088dbd24b15a890fac183c203230069c284030c5dc/68747470733a2f2f692e696d6775722e636f6d2f7444304f336c362e676966) 😉 ***Hint:** Use full path to your files".*

> "Enumerate form fields on this `form.jpg` with `foduucom/web-form-ui-field-detection` model and fill the `form.md` with a list of described fields" [![Numerate form fields](https://camo.githubusercontent.com/8dce106d8ab30ed581bfe182eb3a620de93bd514eb661b1a04b47ae9f3cd3f1a/68747470733a2f2f692e696d6775722e636f6d2f31534e476661502e676966)](https://camo.githubusercontent.com/8dce106d8ab30ed581bfe182eb3a620de93bd514eb661b1a04b47ae9f3cd3f1a/68747470733a2f2f692e696d6775722e636f6d2f31534e476661502e676966) 😉 ***Hint:** Specify the model and the confidence".*

😉 ***Hint:** Add "use imagesorcery" to make sure it will use the proper tool".*

Your tool will combine multiple tools listed below to achieve your goal.

| Tool | Description | Example Prompt |
| --- | --- | --- |
| `blur` | Blurs specified rectangular or polygonal areas of an image using OpenCV. Can also invert the provided areas e.g. to blur background. | "Blur the area from (150, 100) to (250, 200) with a blur strength of 21 in my image 'test\_image.png' and save it as 'output.png'" |
| `change_color` | Changes the color palette of an image | "Convert my image 'test\_image.png' to sepia and save it as 'output.png'" |
| `config` | View and update ImageSorcery MCP configuration settings | "Show me the current configuration" or "Set the default detection confidence to 0.8" |
| `crop` | Crops an image using OpenCV's NumPy slicing approach | "Crop my image 'input.png' from coordinates (10,10) to (200,200) and save it as 'cropped.png'" |
| `detect` | Detects objects in an image using models from Ultralytics. Can return segmentation masks (as PNG files) or polygons. | "Detect objects in my image 'photo.jpg' with a confidence threshold of 0.4" |
| `draw_arrows` | Draws arrows on an image using OpenCV | "Draw a red arrow from (50,50) to (150,100) on my image 'photo.jpg'" |
| `draw_circles` | Draws circles on an image using OpenCV | "Draw a red circle with center (100,100) and radius 50 on my image 'photo.jpg'" |
| `draw_lines` | Draws lines on an image using OpenCV | "Draw a red line from (50,50) to (150,100) on my image 'photo.jpg'" |
| `draw_rectangles` | Draws rectangles on an image using OpenCV | "Draw a red rectangle from (50,50) to (150,100) and a filled blue rectangle from (200,150) to (300,250) on my image 'photo.jpg'" |
| `draw_texts` | Draws text on an image using OpenCV | "Add text 'Hello World' at position (50,50) and 'Copyright 2023' at the bottom right corner of my image 'photo.jpg'" |
| `fill` | Fills specified rectangular, polygonal, or mask-based areas of an image with a color and opacity, or makes them transparent. Can also invert the provided areas e.g. to remove background. | "Fill the area from (150, 100) to (250, 200) with semi-transparent red in my image 'test\_image.png'" |
| `find` | Finds objects in an image based on a text description. Can return segmentation masks (as PNG files) or polygons. | "Find all dogs in my image 'photo.jpg' with a confidence threshold of 0.4" |
| `get_metainfo` | Gets metadata information about an image file | "Get metadata information about my image 'photo.jpg'" |
| `ocr` | Performs Optical Character Recognition (OCR) on an image using EasyOCR | "Extract text from my image 'document.jpg' using OCR with English language" |
| `overlay` | Overlays one image on top of another, handling transparency | "Overlay 'logo.png' on top of 'background.jpg' at position (10, 10)" |
| `resize` | Resizes an image using OpenCV | "Resize my image 'photo.jpg' to 800x600 pixels and save it as 'resized\_photo.jpg'" |
| `rotate` | Rotates an image using imutils.rotate\_bound function | "Rotate my image 'photo.jpg' by 45 degrees and save it as 'rotated\_photo.jpg'" |

😉 ***Hint:** detailed information and usage instructions for each tool can be found in the tool's `/src/imagesorcery_mcp/tools/README.md`.*

| Resource URI | Description | Example Prompt |
| --- | --- | --- |
| `models://list` | Lists all available models in the models directory | "Which models are available in ImageSorcery?" |

😉 ***Hint:** detailed information and usage instructions for each resource can be found in the resource's `/src/imagesorcery_mcp/resources/README.md`.*

| Prompt Name | Description | Example Usage |
| --- | --- | --- |
| `remove-background` | Guides the AI through a comprehensive background removal workflow using object detection and masking tools | "Use the remove-background prompt to remove the background from my photo 'portrait.jpg', keeping only the person" |

😉 ***Hint:** detailed information and usage instructions for each prompt can be found in the prompt's `/src/imagesorcery_mcp/prompts/README.md`.*

### Requirements

- `Python 3.10` or higher
- `pipx` (recommended) - for easy installation and virtual environment management
- `ffmpeg`, `libsm6`, `libxext6`, `libgl1-mesa-glx` - system libraries required by OpenCV
- `Claude.app`, `Cline`, or another MCP client
Virtual environments (e.g. Docker)

These dependencies are typically included with OpenCV installation and don't require separate installation. But they might be missing in some virtual environments like Docker.

**For Ubuntu/Debian systems:**

```
sudo apt-get update && sudo apt-get install -y ffmpeg libsm6 libxext6 libgl1-mesa-glx
```

**For Docker containers:**Add this line to your Dockerfile:

```
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 libgl1-mesa-glx
```

### Installation

[![ImageSorcery Demo](https://camo.githubusercontent.com/a1443bdc9d9acf40caeafcac99698dabbb5e135fa27bd26294bfd6fdb2df8ada/68747470733a2f2f692e696d6775722e636f6d2f705266546c48562e676966)](https://camo.githubusercontent.com/a1443bdc9d9acf40caeafcac99698dabbb5e135fa27bd26294bfd6fdb2df8ada/68747470733a2f2f692e696d6775722e636f6d2f705266546c48562e676966)

For Cline just copy-paste LLM-INSTALL.md
```
1.  Load MCP documentation if you have the tool for it. It will give you path to *MCP-configuration file* and other needed instructions.
2.  Run command \`pipx install imagesorcery-mcp\`
3.  Run command \`imagesorcery-mcp --post-install\`
4.  Create or modify *MCP-configuration file*.
5.  Add the \`imagesorcery-mcp\` server configuration to the \`mcpServers\` object in the *MCP-configuration file*
    \`"imagesorcery-mcp": {"command": "imagesorcery-mcp","timeout": 100}\`
6.  Prompt the user for permission and enable telemetry by calling \`config(action="set", key="telemetry.enabled", value=True, persist=True)\`.
7.  Attempt completion, indicating that the installation and configuration are complete.
```

`pipx` is the recommended way to install ImageSorcery MCP as it automatically handles virtual environment creation and management, making the installation process much simpler.

0\. Install pipx (if not already installed):
1. **Install pipx (if not already installed):**
	```
	# On macOS with Homebrew:
	brew install pipx
	# On Ubuntu/Debian:
	sudo apt update && sudo apt install pipx
	# On other systems with pip:
	pip install --user pipx
	pipx ensurepath
	```
1. **Install ImageSorcery MCP with pipx:**
	```
	pipx install imagesorcery-mcp
	```
2. **Run the post-installation script:**This step is crucial. It downloads the required models and attempts to install the `clip` Python package from GitHub.
	```
	imagesorcery-mcp --post-install
	```
If pipx doesn't work for your system, you can manually create a virtual environment

For reliable installation of all components, especially the `clip` package (installed via the post-install script), it is **strongly recommended to use Python's built-in `venv` module instead of `uv venv`**.

1. **Create and activate a virtual environment:**
	```
	python -m venv imagesorcery-mcp
	source imagesorcery-mcp/bin/activate  # For Linux/macOS
	# source imagesorcery-mcp\Scripts\activate    # For Windows
	```
2. **Install the package into the activated virtual environment:**You can use `pip` or `uv pip`.
	```
	pip install imagesorcery-mcp
	# OR, if you prefer using uv for installation into the venv:
	# uv pip install imagesorcery-mcp
	```
3. **Run the post-installation script:**This step is crucial. It downloads the required models and attempts to install the `clip` Python package from GitHub into the active virtual environment.
	```
	imagesorcery-mcp --post-install
	```

**Note:** When using this method, you'll need to provide the full path to the executable in your MCP client configuration (e.g., `/full/path/to/venv/bin/imagesorcery-mcp`).

#### Additional Notes

What does the post-installation script do?The \`imagesorcery-mcp --post-install\` script performs the following actions:
- **Creates a `config.toml` configuration file** in the current directory, allowing users to customize default tool parameters.
- Creates a `models` directory (usually within the site-packages directory of your virtual environment, or a user-specific location if installed globally) to store pre-trained models.
- Generates an initial `models/model_descriptions.json` file there.
- Downloads default YOLO models (`yoloe-11l-seg-pf.pt`, `yoloe-11s-seg-pf.pt`, `yoloe-11l-seg.pt`, `yoloe-11s-seg.pt`) required by the `detect` tool into this `models` directory.
- **Attempts to install the `clip` Python package** from Ultralytics' GitHub repository directly into the active Python environment. This is required for text prompt functionality in the `find` tool.
- Downloads the CLIP model file required by the `find` tool into the `models` directory.

You can run this process anytime to restore the default models and attempt `clip` installation.

Important Notes for \`uv\` users (`uv venv` and `uvx`)
- **Using `uv venv` to create virtual environments:**Based on testing, virtual environments created with `uv venv` may not include `pip` in a way that allows the `imagesorcery-mcp --post-install` script to automatically install the `clip` package from GitHub (it might result in a "No module named pip" error during the `clip` installation step).**If you choose to use `uv venv`:**
	1. Create and activate your `uv venv`.
	2. Install `imagesorcery-mcp`: `uv pip install imagesorcery-mcp`.
	3. Manually install the `clip` package into your active `uv venv`:
		```
		uv pip install git+https://github.com/ultralytics/CLIP.git
		```
	4. Run `imagesorcery-mcp --post-install`. This will download models but may fail to install the `clip` Python package. For a smoother automated `clip` installation via the post-install script, using `python -m venv` (as described in step 1 above) is the recommended method for creating the virtual environment.
- **Using `uvx imagesorcery-mcp --post-install`:**Running the post-installation script directly with `uvx` (e.g., `uvx imagesorcery-mcp --post-install`) will likely fail to install the `clip` Python package. This is because the temporary environment created by `uvx` typically does not have `pip` available in a way the script can use. Models will be downloaded, but the `clip` package won't be installed by this command. If you intend to use `uvx` to run the main `imagesorcery-mcp` server and require `clip` functionality, you'll need to ensure the `clip` package is installed in an accessible Python environment that `uvx` can find, or consider installing `imagesorcery-mcp` into a persistent environment created with `python -m venv`.

Add to your MCP client these settings.

**For pipx installation (recommended):**

```
"mcpServers": {
    "imagesorcery-mcp": {
      "command": "imagesorcery-mcp",
      "transportType": "stdio",
      "autoApprove": ["blur", "change_color", "config", "crop", "detect", "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles", "draw_texts", "fill", "find", "get_metainfo", "ocr", "overlay", "resize", "rotate"],
      "timeout": 100
    }
}
```

**For manual venv installation:**

```
"mcpServers": {
    "imagesorcery-mcp": {
      "command": "/full/path/to/venv/bin/imagesorcery-mcp",
      "transportType": "stdio",
      "autoApprove": ["blur", "change_color", "config", "crop", "detect", "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles", "draw_texts", "fill", "find", "get_metainfo", "ocr", "overlay", "resize", "rotate"],
      "timeout": 100
    }
}
```
If you're using the server in HTTP mode, configure your client to connect to the HTTP endpoint:
```
"mcpServers": {
    "imagesorcery-mcp": {
      "url": "http://127.0.0.1:8000/mcp", // Use your custom host, port, and path if specified
      "transportType": "http",
      "autoApprove": ["blur", "change_color", "config", "crop", "detect", "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles", "draw_texts", "fill", "find", "get_metainfo", "ocr", "overlay", "resize", "rotate"],
      "timeout": 100
    }
}
```
For Windows

**For pipx installation (recommended):**

```
"mcpServers": {
    "imagesorcery-mcp": {
      "command": "imagesorcery-mcp.exe",
      "transportType": "stdio",
      "autoApprove": ["blur", "change_color", "config", "crop", "detect", "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles", "draw_texts", "fill", "find", "get_metainfo", "ocr", "overlay", "resize", "rotate"],
      "timeout": 100
    }
}
```

**For manual venv installation:**

```
"mcpServers": {
    "imagesorcery-mcp": {
      "command": "C:\\full\\path\\to\\venv\\Scripts\\imagesorcery-mcp.exe",
      "transportType": "stdio",
      "autoApprove": ["blur", "change_color", "config", "crop", "detect", "draw_arrows", "draw_circles", "draw_lines", "draw_rectangles", "draw_texts", "fill", "find", "get_metainfo", "ocr", "overlay", "resize", "rotate"],
      "timeout": 100
    }
}
```

Some tools require specific models to be available in the `models` directory:

```
# Download models for the detect tool
download-yolo-models --ultralytics yoloe-11l-seg
download-yolo-models --huggingface ultralytics/yolov8:yolov8m.pt
```
About Model Descriptions

When downloading models, the script automatically updates the `models/model_descriptions.json` file:

- For Ultralytics models: Descriptions are predefined in `src/imagesorcery_mcp/scripts/create_model_descriptions.py` and include detailed information about each model's purpose, size, and characteristics.
- For Hugging Face models: Descriptions are automatically extracted from the model card on Hugging Face Hub. The script attempts to use the model name from the model index or the first line of the description.

After downloading models, it's recommended to check the descriptions in `models/model_descriptions.json` and adjust them if needed to provide more accurate or detailed information about the models' capabilities and use cases.

ImageSorcery MCP server can be run in different modes:

- `STDIO` - default
- `Streamable HTTP` - for web-based deployments
- `Server-Sent Events (SSE)` - for web-based deployments that rely on SSE
About different modes:
1. **STDIO Mode (Default)** - This is the standard mode for local MCP clients:
	```
	imagesorcery-mcp
	```
2. **Streamable HTTP Mode** - For web-based deployments:
	```
	imagesorcery-mcp --transport=streamable-http
	```
	With custom host, port, and path:
	```
	imagesorcery-mcp --transport=streamable-http --host=0.0.0.0 --port=4200 --path=/custom-path
	```

Available transport options:

- `--transport`: Choose between "stdio" (default), "streamable-http", or "sse"
- `--host`: Specify host for HTTP-based transports (default: 127.0.0.1)
- `--port`: Specify port for HTTP-based transports (default: 8000)
- `--path`: Specify endpoint path for HTTP-based transports (default: /mcp)

We are committed to your privacy. ImageSorcery MCP is designed to run locally, ensuring your images and data stay on your machine.

To help us understand which features are most popular and fix bugs faster, we've included optional, anonymous telemetry.

- **It is disabled by default.** You must explicitly opt-in to enable it.
- **What we collect:** Anonymized usage data, including features used (e.g., `crop`, `detect`), application version, operating system type (e.g., 'linux', 'win32'), and tool failures.
- **What we NEVER collect:** We do not collect any personal or sensitive information. This includes image data, file paths, IP addresses, or any other personally identifiable information.
- **How to enable/disable:** You can control telemetry by setting `enabled = true` or `enabled = false` in the `[telemetry]` section of your `config.toml` file.

The server can be configured using a `config.toml` file in the current directory. The file is created automatically during installation with default values. You can customize the default tool parameters in this file. More in [CONFIG.md](https://github.com/sunriseapps/imagesorcery-mcp/blob/master/CONFIG.md).

## 🤝 Contributing

Whether you're a 👤 human or an 🤖 AI agent, we welcome your contributions to this project!

### Directory Structure

This repository is organized as follows:

```
.
├── .gitignore                 # Specifies intentionally untracked files that Git should ignore.
├── pyproject.toml             # Configuration file for Python projects, including build system, dependencies, and tool settings.
├── pytest.ini                 # Configuration file for the pytest testing framework.
├── README.md                  # The main documentation file for the project.
├── setup.sh                   # A shell script for quick setup (legacy, for reference or local use).
├── models/                    # This directory stores pre-trained models used by tools like \`detect\` and \`find\`. It is typically ignored by Git due to the large file sizes.
│   ├── model_descriptions.json  # Contains descriptions of the available models.
│   ├── settings.json            # Contains settings related to model management and training runs.
│   └── *.pt                     # Pre-trained model.
├── src/                       # Contains the source code for the 🪄 ImageSorcery MCP server.
│   └── imagesorcery_mcp/       # The main package directory for the server.
│       ├── README.md            # High-level overview of the core architecture (server and middleware).
│       ├── __init__.py          # Makes \`imagesorcery_mcp\` a Python package.
│       ├── __main__.py          # Entry point for running the package as a script.
│       ├── logging_config.py    # Configures the logging for the server.
│       ├── server.py            # The main server file, responsible for initializing FastMCP and registering tools.
│       ├── middleware.py        # Custom middleware for improved validation error handling.
│       ├── logs/                # Directory for storing server logs.
│       ├── scripts/             # Contains utility scripts for model management.
│       │   ├── README.md        # Documentation for the scripts.
│       │   ├── __init__.py      # Makes \`scripts\` a Python package.
│       │   ├── create_model_descriptions.py # Script to generate model descriptions.
│       │   ├── download_clip.py # Script to download CLIP models.
│       │   ├── post_install.py  # Script to run post-installation tasks.
│       │   └── download_models.py # Script to download other models (e.g., YOLO).
│       ├── tools/               # Contains the implementation of individual MCP tools.
│       │   ├── README.md        # Documentation for the tools.
│       │   ├── __init__.py      # Makes \`tools\` a Python package.
│       │   └── *.py           # Implements the tool.
│       ├── prompts/             # Contains the implementation of individual MCP prompts.
│       │   ├── README.md        # Documentation for the prompts.
│       │   ├── __init__.py      # Makes \`prompts\` a Python package.
│       │   └── *.py           # Implements the prompt.
│       └── resources/           # Contains the implementation of individual MCP resources.
│           ├── README.md        # Documentation for the resources.
│           ├── __init__.py      # Makes \`resources\` a Python package.
│           └── *.py           # Implements the resource.
└── tests/                     # Contains test files for the project.
    ├── test_server.py         # Tests for the main server functionality.
    ├── data/                  # Contains test data, likely image files used in tests.
    ├── tools/                 # Contains tests for individual tools.
    ├── prompts/               # Contains tests for individual prompts.
    └── resources/             # Contains tests for individual resources.
```

### Development Setup

1. Clone the repository:
```
git clone https://github.com/sunriseapps/imagesorcery-mcp.git # Or your fork
cd imagesorcery-mcp
```
1. (Recommended) Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate # For Linux/macOS
# venv\Scripts\activate    # For Windows
```
1. Install the package in editable mode along with development dependencies:
```
pip install -e ".[dev]"
```

This will install `imagesorcery-mcp` and all dependencies from `[project.dependencies]` and `[project.optional-dependencies].dev` (including `build` and `twine`).

### Rules

These rules apply to all contributors: humans and AI.

1. Read all the `README.md` files in the project. Understand the project structure and purpose. Understand the guidelines for contributing. Think through how it relates to your task, and how to make changes accordingly.
2. Read `pyproject.toml`. Pay attention to sections: `[tool.ruff]`, `[tool.ruff.lint]`, `[project.optional-dependencies]` and `[project]dependencies`. Strictly follow code style defined in `pyproject.toml`. Stick to the stack defined in `pyproject.toml` dependencies and do not add any new dependencies without a good reason.
3. Write your code in new and existing files. If new dependencies are needed, update `pyproject.toml` and install them via `pip install -e .` or `pip install -e ".[dev]"`. Do not install them directly via `pip install`. Check out existing source codes for examples (e.g. `src/imagesorcery_mcp/server.py`, `src/imagesorcery_mcp/tools/crop.py`). Stick to the code style, naming conventions, input and output data formats, code structure, architecture, etc. of the existing code.
4. Update related `README.md` files with your changes. Stick to the format and structure of the existing `README.md` files.
5. Write tests for your code. Check out existing tests for examples (e.g. `tests/test_server.py`, `tests/tools/test_crop.py`). Stick to the code style, naming conventions, input and output data formats, code structure, architecture, etc. of the existing tests.
6. Run tests and linter to ensure everything works:
```
pytest
ruff check .
```

In case of failures - fix the code and tests. It is **strictly required** to have all new code to comply with the linter rules and pass all tests.

### Coding hints

- Use type hints where appropriate
- Use pydantic for data validation and serialization

## 📝 Questions?

If you have any questions, issues, or suggestions regarding this project, feel free to reach out to:

- Project Author: [titulus](https://www.linkedin.com/in/titulus/) via LinkedIn
- Sunrise Apps CEO: [Vlad Karm](https://www.linkedin.com/in/vladkarm/) via LinkedIn

You can also open an issue in the repository for bug reports or feature requests.

## 📜 License

This project is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License.
