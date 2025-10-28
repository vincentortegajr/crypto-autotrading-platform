# AI Coding Assistant Instructions for Vince Quant Whale Stack + Polymarket Oracle Helix

## Project Overview

This is a hybrid quant trading platform fusing whale liquidation hunting in perpetual markets (yang) with prediction market oracles (yin) for trillion-dollar market domination. The system tracks liquidation heatmaps across all timeframes, predicts whale targets via historical patterns and OI/volume spikes, and executes trades across perps (Bybit) and predictions (Polymarket CLOB), arbing event-driven correlations like election odds to crypto volatility.

## Architecture

- **Trading Bot**: Python 3.11 application in `src/` with dual-vertical execution (perps + poly)
- **Automation**: MCP servers (Terminator for desktop/browser control, ImageSorcery for image processing)
- **Data Sources**: CoinGlass (liquidation heatmaps), Bybit (perps trading), Polymarket CLOB/Gamma (prediction markets), Polysights/Nevua/HashDive/PolyTale (wallet analytics), Polygon RPC (on-chain)
- **Output**: Annotated heatmap images in `screenshots/`, trading logs in `logs/`, poly wallet CSVs and CLOB snapshots
- **Fusion**: Redis pub/sub bridges perps OI spikes with poly wallet clusters for hybrid signals

## Key Conventions

- **MCP Integration**: Use Terminator MCP for browser automation (navigate, click, screenshot) and ImageSorcery for image annotation (draw rectangles, arrows, text labels)
- **Error Handling**: Always include try/catch with specific error messages; use MCP tools for visual verification
- **File Paths**: Use absolute paths for all file operations, especially with image processing
- **API Authentication**: Store tokens in `.env` file; never commit credentials
- **Vertical Tagging**: All DB writes include `vertical` field ('perps' or 'poly'); fusion modules hook both
- **Documentation**: Update docs in `docs/` for any workflow changes; maintain API reference in `docs/reference/API-TOKENS-ENDPOINTS.md`

## Critical Workflows

- **MCP Connection**: If Terminator MCP fails, restart Claude completely (`claude` command) - this reinitializes MCP servers
- **CoinGlass Automation**: Use workflow in `docs/COINGLASS-AUTOMATION/WORKFLOWS/COINGLASS_HEATMAP_AUTOMATION_WORKFLOW.md` for heatmap capture
- **Polymarket Fusion**: Wallet hunters pull Polysights/HashDive, build NetworkX graphs, fuse with perps OI for hybrid signals
- **Testing**: Run automation end-to-end before committing; verify MCP connections with "Show me all running applications"
- **Build/Run**: Use `npm run trade:advice` for Phase 1 (advice only), `npm run trade:auto` for Phase 2 (full execution); poly copy trades via CLOB

## Specific Patterns

- **Browser Automation**: Wrap JavaScript in IIFE `(function() { ... })()` for `execute_browser_script`
- **Image Annotation**: Use BGR color format `[0, 0, 255]` for red rectangles around liquidation zones
- **Data Extraction**: Hover over yellow heatmap zones to get tooltip data (price + leverage); for poly, pull wallet clusters via Polysights API
- **Social Media Prep**: Annotate images with red rectangles, green arrows, white text labels, and CoinGlass watermark; poly alerts include affiliate links
- **API Calls**: Include CG-API-KEY for CoinGlass; use X-BAPI-\* for Bybit; Polymarket CLOB requires proxy wallet signatures
- **Fusion Logic**: Poly modules check Redis for perps OI spikes; hybrid signals amplify strength if both verticals align
- **Math Formulas**: Use sympy for poly edge formulas (signal _ (1-vol) _ alloc _ emot); Kelly hybrids combine perps_prob _ poly_edge

## Examples

- **Capture Heatmap**: `navigate_browser` to CoinGlass, select timeframe, `capture_element_screenshot` of heatmap area
- **Annotate Zones**: Use `draw_rectangles` with coordinates around yellow areas, add text "$116,932 - 25.31M"
- **Extract Data**: Run browser script to query `[data-liquidation]` elements; for poly, Polysights API → NetworkX graph density >0.5
- **Send Alert**: Use Telegram API to send annotated image with caption including affiliate links; poly alerts like "Insider Copy: +33% Trump odds"
- **Hybrid Trade**: Grid bot subscribes to "poly_signals", executes if OI >0.7; poly copy gradual exits (0.1 steps) with 10% cap

## Dependencies

- Python 3.11.14 (locked for compatibility)
- TimescaleDB 2.22.1 (Postgres 16) with poly tables (polymarket_wallets, polymarket_signals)
- Redis 7.4 for pub/sub fusion
- Docker Desktop for containers
- MCP servers: Terminator MCP Agent v0.19.1, ImageSorcery MCP
- Additional: networkx, torch, sympy, ecdsa for poly math/wallets

## Security

- Never expose API keys in code or logs
- Use environment variables for all credentials
- Validate MCP permissions for desktop automation
- Poly proxy wallet privkey secure; generate via MetaMask export
- Test automation in isolated environment first

## Common Pitfalls

- MCP servers disconnect on Claude restart - always verify connection before automation
- Image paths must be absolute for ImageSorcery tools
- CoinGlass requires Pro subscription for full heatmap access
- Polymarket CLOB needs proxy wallet setup; Nevua/HashDive require sign-ups
- Fusion requires both verticals aligned; test hybrids on paper first
- DB writes must tag vertical; poly tables extend perps schema

## Extended File Structure

- `src/scanners/polymarket/`: wallet_hunter.py (Polysights → NetworkX graphs), signal_oracle.py (edge scoring → pub "poly_signals")
- `src/agents/autotraders/polymarket_copy/`: Subscribes to poly signals, executes CLOB trades with guardian caps
- `src/math/poly_edge_math.py`: Bet formulas, checklist_score (>=5), poly_kelly hybrids
- `src/sockets/polymarket_ws.py`: Nevua/PolyTale websockets for real-time alerts
- `data/processed/poly_wallets_csv/`: Wallet analytics exports
- `data/signals/poly_perfect_bets/`: High-conviction poly signals
- `scripts/launch_poly_swarm.sh`: Swarm deployment for poly agents
- `tests/poly/`: Backtest stubs for poly strategies

## Build Order & Phases

### Phase 1: Infrastructure (Utils & Config)

1. `src/utils/config_utils.py` – .env loader + getters (add poly: polymarket_clob_key, polysights_key, etc.)
2. `src/utils/timescale_utils.py` – Pooling/queries (add insert_poly_wallet, insert_poly_signal)
3. `src/utils/redis_utils.py` – Pub/sub (add "poly_signals" channel)
4. `src/utils/data_utils.py` – I/O (add poly JSON/CSV for CLOB)
5. `src/utils/error_utils.py` – Decorators/retry (universal)

### Phase 2: Math & Sockets

6. `src/math/poly_edge_math.py` – Bet formulas, checklist_score (>=5), poly_kelly hybrids
7. `src/sockets/polymarket_ws.py` – Nevua/PolyTale websockets for real-time alerts

### Phase 3: Scanners

8. `src/scanners/polymarket/wallet_hunter.py` – Polysights/HashDive pull, networkx graph (density>0.5=sync), insert_poly_wallet. Pub "poly_smart_wallets"
9. `src/scanners/polymarket/signal_oracle.py` – Score via poly_edge_math, checklist>=5 → pub "poly_signals" (hybrid if oi>0.7). 10s loop

### Phase 4: Agents

10. `src/agents/trade/trade_executor.py` – Base (add poly_clob_exec)
11. `src/agents/logging/agent_log.py` – Base (tag vertical)
12. `src/agents/autotraders/polymarket_copy/` – Subscribes to poly signals, executes CLOB trades with guardian caps
13. `src/agents/poly_guardian/` – Risk management for poly trades

### Phase 5: Web & Scripts

14. `src/web/poly_panels/` – Grafana/Streamlit dashboards fusing perps PnL with poly ROI
15. `scripts/launch_poly_swarm.sh` – Swarm deployment for poly agents

## .env Variables (Extended)

```
# ---- Polymarket Oracle Helix (Yin to Perps Yang) ----
POLYMARKET_CLOB_KEY=your_polymarket_clob_key_here
POLYMARKET_GAMMA_URL=https://gamma.api.polymarket.com
POLYMARKET_RPC_URL=https://polygon-mainnet.infura.io/v3/YOUR_INFURA_KEY
POLYSIGHTS_API_URL=https://app.polysights.xyz/api/v1
POLYSIGHTS_KEY=your_polysights_api_key_here
NEVUA_WS_URL=wss://nevua.markets/ws
NEVUA_TOKEN=your_nevua_token_here
HASHDIVE_API_URL=https://www.hashdive.com/api
HASHDIVE_KEY=your_hashdive_key_here
POLYTALE_API_URL=https://www.polytale.live/api
POLYTALE_KEY=your_polytale_key_here
PROXY_WALLET_PRIVKEY=your_polygon_proxy_hex_here
POLY_RISK_CAP=0.10
```

## Vision Alignment

This is Sam Altman's prophecy: One person + AI agents + oracle hybrids = trillion-dollar empire. Perps (liquidation yang) + Polymarket (prediction yin) = ultimate market domination. Whale hunts fuse with event-driven edges for infinite alpha.
