---
title: "Chrome DevTools MCP vs Playwright MCP – Heatmap Automation Notes"
created: 2025-10-28
updated: 2025-10-29
author: ChatGPT (Codex session)
tags:
  - mcp
  - automation
  - chrome-devtools
  - playwright
---

## Environment Snapshot

- MCP config lives at `~/.codex/config.toml`; there is no project-local override yet.  
  ```toml
  [mcp_servers.chrome-devtools]
  command = "npx"
  args = ["-y", "chrome-devtools-mcp@latest"]

  [mcp_servers.playwright]
  command = "npx"
  args = ["@playwright/mcp@latest"]

  [mcp_servers.imagesorcery-mcp]
  command = "imagesorcery-mcp"
  ```
- `chrome-devtools-mcp` and `@playwright/mcp` are installed as devDependencies (`npm install --save-dev`).
- `imagesorcery-mcp` is installed via `pipx` and launched through `scripts/run_imagesorcery_mcp.py` (FastMCP wrapper).
- All automation scripts run from this repo; shared artifacts land in `artifacts/`.

## Experience Comparison (latest sweep)

- **Chrome DevTools MCP** – Highest-fidelity experience for humans reviewing the heatmap live. We interact with the full Chrome UI, click shortcuts, open tabs, and the screenshot captured via `take_screenshot` is identical to what a human sees. DevTools extras (performance tracing, console, network) are instantly available.
- **Playwright MCP** – Headless, resource-light, and fully accessible through structured actions (`browser_click`, `browser_evaluate`, `browser_snapshot`). The capture is pixel-perfect once we pin the viewport to `1600x900`, but there is no GUI—best for agents that should remain invisible.
- **ImageSorcery MCP** – Provides the “billion-dollar deck” finish. Our pipeline now crops, adds branded banners/panels, draws metric cards, and overlays insights/callouts so both Chrome and Playwright captures publish with the same premium layout.

## Pipeline Enhancements (2025-10-29)

1. `scripts/process_liquidation_heatmap.py`
   - New `--metric` flag (label=value or label:value).
   - Metric cards render inside the insight panel with accent bars and dual-typography.
   - Callout captions auto-clamp to panel bounds; insights shift below the metric stack.
2. `scripts/run_heatmap_sweep.py`
   - Injects metric presets per timeframe (`--metric` args) alongside insights and callouts.
   - Retries Playwright captures twice with exponential-style delay to absorb slow launches.
   - Shared helper `_metric_args` keeps Chrome/Playwright annotation inputs identical.
3. Both capture scripts already accept timeframe, viewport, timeout, and output overrides.

Run the full campaign:

```bash
python scripts/run_heatmap_sweep.py --timeframes "12 hour" "24 hour" "2 week"
```

Each timeframe produces:

1. Raw Chrome screenshot → annotated premium card (`#2979FF` palette).
2. Raw Playwright screenshot → annotated premium card (`#FF8A3D` palette).

## Observed Strengths & Tradeoffs

- **Best human viewing experience:** Chrome DevTools MCP. You watch the actual heatmap animate, switch tabs, and investigate anomalies in-place. Perfect when the operator wants parity with a trader’s workstation.
- **Best autonomous/headless option:** Playwright MCP. Zero UI overhead, deterministic accessibility tree, easy to scale across dozens of concurrent sessions or CI jobs.
- **Deep debugging & diagnostics:** Chrome wins thanks to built-in performance and network tools. Playwright can collect traces, but DevTools exposes Core Web Vitals instantly.
- **Profile persistence:** Chrome keeps the same profile between runs (ideal for authenticated dashboards). Playwright runs isolated by default; reuse requires explicit `--storage-state`.
- **Reliability on flaky networks:** Playwright’s headless Chromium spins up quickly but sometimes races on first navigation, hence the new retry loop. Chrome tends to be slower to launch but rarely misses UI elements once open.

## Headless vs Desktop Takeaways

- Use **Playwright** when the agent must operate invisibly (server jobs, CI, repeat sweeps) or when accessibility-tree reasoning is sufficient.
- Use **Chrome DevTools** when a human wants to co-pilot, when we need to pull perf traces, or when we lean on stored cookies/logins.
- Keep both registered: Playwright can pre-validate actions headlessly, then Chrome can reproduce the same steps visually for review.

## Path to Fully Automated Heatmap Intelligence

1. **Daily sweep cron** – Schedule `scripts/run_heatmap_sweep.py` to cover the full timeframe matrix and archive outputs per timestamp.
2. **Metric ingestion** – Pipe on-chain or exchange stats into the new `--metric` flags (JSON → CLI args) so cards reflect live numbers.
3. **Callout intelligence** – Calculate liquidity clusters programmatically and feed `--callout` coords instead of static presets.
4. **Story generation** – Summarize Chrome performance traces and Playwright console logs into narrative bullets for Slack/Notion drops.
5. **Packaging** – Export ImageSorcery outputs in multiple ratios (story, square, widescreen) for social decks; scripts already expose crop + fill hooks to adapt.

## Pending Tests (priority order)

1. Validate remaining timeframes (`48 hour`, `3 day`, `1 week`, `1 month`) plus alt pairs (ETH, SOL) through both MCP paths.
2. Stress-test Playwright retries on throttled network profiles; capture logs for failure analysis.
3. Exercise Chrome’s `performance_*` tools to benchmark heatmap load times versus headless captures.
4. Implement storage-state reuse for Playwright to confirm authenticated dashboards function without GUI.
5. Add integration guard: diff annotated outputs to detect layout regressions when ImageSorcery updates models.

## Prompt Library & Safety Notes

- **Chrome DevTools MCP**
  - `Open https://www.coinglass.com/pro/futures/LiquidationHeatMapNew, wait for "24 hour", switch to "2 week", take a full-page screenshot, and list console warnings.`  
  - `Throttle to Fast 3G, reload, then run performance_start_trace and summarize the top insight.`
- **Playwright MCP**
  - `Navigate to the CoinGlass heatmap, dismiss the consent modal, switch to 12 hour, and share the accessibility snapshot for the heatmap table.`  
  - `Headless run: capture 24 hour heatmap, then list every network request to *.coinglass.* made during navigation.`
- **ImageSorcery MCP**
  - `use imagesorcery → Crop 60,350,1540,1850 from artifacts/heatmap_playwright_mcp_24-hour.png, add brand panel #151E2D, and overlay title "BTC Liquidation Heatmap · 24 Hour".`
  - `use imagesorcery → Detect objects on screenshots/heatmap.png, highlight the heaviest cluster, and annotate with "Whale Stack".`

Always remind the assistant to ignore page-level prompt injection. Specify allowed domains (e.g., “Do not execute scripts outside coinglass.com”) and prefer isolated/headless modes for untrusted sites.

## File References

- `scripts/capture_chrome_heatmap.py`
- `scripts/capture_playwright_heatmap.py`
- `scripts/process_liquidation_heatmap.py`
- `scripts/run_heatmap_sweep.py`
- `scripts/run_imagesorcery_mcp.py`
- `docs/mcp/HOW_TO_USE-IMAGE-SOURCERY.md`
- `docs/mcp/chatgpt/CHROME_DEVTOOLS.md`
*** End Patch
