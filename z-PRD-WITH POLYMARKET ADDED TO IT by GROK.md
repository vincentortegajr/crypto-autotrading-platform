# 🌍 VINCE QUANT WHALE EMPIRE + POLYMARKET ORACLE: COMPLETE PRD, VISION & BUILD INSTRUCTIONS

**The Single Document That Makes Building A Trillion-Dollar Hybrid Quant Platform Impossible To Fuck Up**

***

# 📜 PRODUCT REQUIREMENTS DOCUMENT (PRD) + VISION + README

**Project Name:** Vince Quant Whale Stack + Polymarket Oracle Helix  
**Version:** 2.0.0 (Production Fusion)  
**Last Updated:** October 27, 2025  
**Owner:** Vince  
**Mission:** Build the world's first transparent, whale-tracking, AI-powered crypto quant fund and membership platform that democratizes institutional-grade trading intelligence – now fused with prediction market oracle intelligence to capture event-driven edges, turning perps liquidation hunts into a yin-yang mastery of spot, perps, and probabilistic futures for ultimate market domination.

***

## 🎯 VISION STATEMENT

Since 2016, I've watched whales hunt liquidation clusters like clockwork in perps markets: Long positions pump to wipe shorts, take profits, flip short to dump and liquidate longs – printing on both spot and perpetuals simultaneously. This pattern is 100% visible in on-chain data, but retail misses it. Now, layer in prediction markets: Smart wallets (addresses with 30%+ ROI, pre-news entries) front-run events like elections or macro shifts, creating correlated asymmetries (e.g., Trump odds spike → BTC OI dump). Polymarket's $30M+ 2025 volumes are the untapped oracle – binary truths from crowd wisdom, outperforming polls by 15-20%.

**We are building the system that:**
1. **Tracks liquidation heatmaps** across ALL timeframes (12h to 1 year) for every perpetual coin, fused with prediction wallet clusters for hybrid signals.
2. **Predicts whale targets** by analyzing historical patterns, OI/volume spikes, wick behavior, and smart-wallet syncs (e.g., ≥2 wallets betting pre-news).
3. **Executes trades via AI AutoTraders** that follow whale movements in real-time across perps (Bybit) and predictions (Polymarket CLOB), arbing correlations like event odds to crypto vol.
4. **Broadcasts signals** to Telegram, X, email, and SMS – turning followers into affiliates, with poly-specific alerts like "5-0 insider streak on MrBeast resolve."
5. **Manages a crypto fund** where members trade alongside us, learn the hybrid system (perps + poly checklists), and earn commissions – scaling to LP positions in ZSC DAO for liquidity edges.

**The result:** A self-reinforcing flywheel: Early quant platform → viral social proof (e.g., +33% Trump copy wins) → fund dominance → our token → **trillion-dollar valuation**. Perps provide the yang (momentum hunts); Polymarket the yin (probabilistic foresight). One person + AI agents = not just billion, but trillion – dominating all markets, from coins to events, via infinite API ingestion and quantum-math fusion.

**This is Sam Altman's prophecy amplified: "One person + AI agents + oracle hybrids = trillion-dollar empire." We are that empire.**

***

## 🏗️ PROJECT ARCHITECTURE (THE GOOGLE MAPS ANALOGY)

Think of this project as **Planet Earth** – a living, breathing metropolis where you open Google Maps on your phone, see the blue marble spinning in space, then zoom in continent by continent, street by street, until every building hums with purpose. Perps is the bustling core (liquidation rivers feeding trade engines); Polymarket Oracle is the satellite network (event constellations arbing the skies). Start at orbital view (.env grid powering the globe), zoom to libraries (db/ for time-series ledgers), warehouses (data/ for raw intel to signals), workforce (src/agents/ executing in sync), intel hubs (src/scanners/ spotting edges), labs (src/math/ crunching Kelly formulas), telecom towers (src/sockets/ streaming WS feeds), utilities (src/utils/ piping clean power), tourist vistas (src/web/ dashboards overlooking the empire), maintenance crews (scripts/ keeping lights on), and QA sentinels (tests/ guarding the gates).

Updated for Helix Fusion:
- **⚡ `.env`** = The electrical grid (powers everything, now with Poly API keys).
- **🏛️ `db/`** = Central library (TimescaleDB for history/hypertables, Redis for real-time – extended for poly_wallets/signals).
- **🏭 `data/`** = Warehouse district (raw materials → factory processing → finished goods; add poly subfolders for wallet CSVs, CLOB snapshots).
- **👔 `src/agents/`** = Workforce (AutoTraders, manual traders, broadcasters, loggers; add autotraders/polymarket_copy for CLOB executions).
- **🔍 `src/scanners/`** = Intelligence network (heatmap trackers, historians, signal generators; add polymarket/ for wallet_hunter, signal_oracle).
- **🎓 `src/math/`** = Research laboratory (quant algorithms; add poly_edge_math.py for bet formulas + Kelly hybrids).
- **📡 `src/sockets/`** = Telecommunications (websockets for real-time data; add polymarket_ws.py for Nevua/PolyTale feeds).
- **🔧 `src/utils/`** = Utilities department (config loader, DB/Redis helpers; extend for poly inserts/queries).
- **🌐 `src/web/`** = Tourist district (Grafana, Streamlit dashboards; add poly ROI panels fusing perps PnL).
- **🔧 `scripts/`** = Maintenance crew (deployment, backups, automation; add launch_poly_swarm.sh).
- **✅ `tests/`** = Quality assurance (safety checks; add poly backtest stubs).

**Every folder has a purpose. Every data flow is mapped (Redis pub/sub fuses perps OI with poly clusters). Every agent knows its job – hybrid signals trigger cross-vertical trades.**

Zoom Tip: On your M4 Max, open Maps app, search "San Francisco" (perps core), then "overlay satellite" for poly constellations – that's your mental model.

***

## 🚀 TECH STACK (VERIFIED AS OF OCT 27, 2025)

| Component | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.11.14 | Main language (locked for compatibility; powers all agents/scanners). |
| **TimescaleDB** | 2.22.1 (Postgres 16) | Time-series database for liquidation/OHLCV/trades + poly signals/wallets. |
| **Redis** | 7.4 | Real-time pub/sub and caching (fuses perps/poly signals). |
| **Docker Desktop** | Latest (Mac M4) | Container orchestration (TimescaleDB, Redis, Grafana). |
| **Grafana** | Latest (10.x+) | Live dashboards and SQL query UI (add poly vs. perps panels). |
| **VS Code** | Latest | IDE with extensions (Python, Docker, GitHub Copilot). |
| **CoinGlass API** | Premium | Aggregated liquidation heatmaps, OI, volume (perps core). Docs: https://www.coinglass.com/docs. |
| **Bybit API** | v5 | Trading execution (perps). Docs: https://bybit-exchange.github.io/docs/v5/intro. |
| **Telegram Bot API** | Latest | Broadcast to channels (hybrid signals). Docs: https://core.telegram.org/bots/api. |
| **X (Twitter) API** | Latest | Social media broadcasting (poly insider recaps). Docs: https://developer.twitter.com/en/docs/twitter-api. |
| **Twilio SMS API** | Latest | SMS alerts (high-conviction hybrids). Docs: https://www.twilio.com/docs/sms/api. |
| **Polymarket CLOB API** | Latest | Order book for poly executions. Docs: https://docs.polymarket.com/developers/CLOB/introduction. |
| **Polymarket Gamma API** | Latest | Read-only markets/discovery (poly signals). Docs: https://docs.polymarket.com/developers/gamma-markets-api/overview. |
| **Polysights API** | Latest | AI wallet analytics (insider finder). Docs: https://app.polysights.xyz/documentation (sign up at https://app.polysights.xyz). |
| **Nevua Markets WS** | Latest | Real-time poly alerts. Docs: https://nevua.markets/ (GitHub: https://github.com/nevuamarkets/poly-websockets). |
| **HashDive API** | Latest | Smart scores/insider detection. Docs: https://www.hashdive.com/ (contact: contact@hashdive.com). |
| **PolyTale API** | Latest | AI research agent (whale tracking). Docs: https://polymark.et/product/polytale (Twitter: @polytaleai). |
| **Polygon RPC** | Latest | On-chain wallet queries. Docs: https://polygon.technology/rpc (free Infura: https://infura.io). |
| **GitHub Copilot/Claude/ChatGPT** | Latest | AI agents for code gen (terminal integration via VS Code extensions). |

API Keys/Tokens: All fetched via sign-ups (links above); store in .env only. No hardcodes.

***

## 📋 PART 1: VINCE'S SETUP INSTRUCTIONS (FOUNDATION BUILDER – ZOOM FROM ORBIT TO STREET LEVEL)

You are the **planet architect**, sitting at a blank-slate MacBook Pro M4 Max (128GB RAM, 4TB SSD, 10Gbps Google Fiber). VS Code is open, cursor blinking on an empty workspace. We'll zoom like Google Maps: Start at orbital view (global installs), continent-drop (project root), street-level (configs/services), then building-by-building (verifications). Each step is one terminal command or click – copy-paste ready. If stuck, paste errors into ChatGPT/Claude/Grok terminal for debug. AI agents (via VS Code extensions) will assist on demand – e.g., "Claude, explain this Docker error."

### **🌍 STEP 1: ORBITAL PREP – GLOBAL TOOLS & ACCOUNTS (15-30min; One-Time Setup)**

Open Safari (pre-installed). Zoom: Earth view → search "VS Code" → download.

1. **Install VS Code** (IDE for all coding/AI agents):
   - Go: https://code.visualstudio.com/.
   - Click "Download for Mac" (Apple Silicon).
   - Open .dmg, drag to Applications.
   - Launch VS Code from Spotlight (Cmd+Space, type "VS Code").
   - Install Extensions (Cmd+Shift+X): Search/install "Python" (Microsoft), "Docker" (Microsoft), "GitHub Copilot" (free trial), "Claude Dev" (Anthropic, if available), "ChatGPT" (community fork).
   - Terminal (in VS Code: Terminal > New Terminal): `code --version` (expect 1.90+).

2. **Install Docker Desktop** (for containers – TimescaleDB/Redis/Grafana):
   - Go: https://www.docker.com/products/docker-desktop/.
   - Download Mac (Apple Silicon).
   - Open .dmg, drag to Applications.
   - Launch Docker (it auto-starts; grant permissions).
   - Terminal: `docker --version` (expect 27.x+). If Apple Silicon warning, run `softwareupdate --install --required`.

3. **Sign Up for APIs/Keys** (Collect tokens; bookmark docs):
   - **CoinGlass Premium**: https://www.coinglass.com/account/register → Dashboard > API Key. Copy key. Docs bookmark: https://www.coinglass.com/docs.
   - **Bybit**: https://www.bybit.com/en/user/assets/apiManagement → Create API (read/trade perms). Copy key/secret. Docs: https://bybit-exchange.github.io/docs/v5/intro.
   - **Binance (Optional)**: https://www.binance.com/en/my/settings/api-management → Create API. Docs: https://binance-docs.github.io/apidocs/futures/en/.
   - **Telegram Bot**: https://t.me/BotFather → /newbot → Copy token. Create channel @yourquantalerts, add bot as admin. Docs: https://core.telegram.org/bots/api.
   - **X API**: https://developer.twitter.com/en/portal/dashboard → Free tier app → Keys & Tokens (read+write). Docs: https://developer.twitter.com/en/docs/twitter-api.
   - **Twilio**: https://www.twilio.com/try-twilio → Sign up, verify phone → Console > SMS > Keys. Docs: https://www.twilio.com/docs/sms/api.
   - **Email (Gmail App Password)**: https://myaccount.google.com/apppasswords → Generate for "Mail". Docs: https://support.google.com/mail/answer/185833.
   - **Polymarket**: https://polymarket.com → Wallet connect (Polygon), then https://docs.polymarket.com/developers/CLOB/introduction → Generate CLOB key (proxy wallet setup). Docs: https://docs.polymarket.com/.
   - **Polysights**: https://app.polysights.xyz → Sign up (free tier) → API section. Docs: https://app.polysights.xyz/documentation.
   - **Nevua**: https://nevua.markets/ → Sign up → WS token. GitHub: https://github.com/nevuamarkets/poly-websockets.
   - **HashDive**: https://www.hashdive.com/ → Contact form for API access. Docs: https://www.hashdive.com/.
   - **PolyTale**: https://polymark.et/product/polytale → Twitter @polytaleai for access. Docs: https://polymark.et/product/polytale.
   - **Infura (Polygon RPC)**: https://infura.io → Sign up → Polygon Mainnet endpoint (free). Docs: https://polygon.technology/rpc.
   - Save all in Notes app; we'll paste to .env soon.

4. **Install Git** (for version control/GitHub):
   - Terminal: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` (installs Homebrew if needed).
   - `brew install git`.
   - `git --version` (expect 2.40+).

**Zoom Analogy:** Orbital downloads – now your Mac is tooled like a pro rig, APIs queued like satellites.

### **🌍 STEP 2: CONTINENT DROP – PROJECT ROOT & FOLDERS (5min)**

Zoom: Earth → North America → project site.

1. Terminal (VS Code): `cd ~/Projects` (or Desktop for quick access).
2. `mkdir vince-quant-helix` (root folder; "helix" for poly fusion).
3. `cd vince-quant-helix`.
4. `code .` (opens VS Code workspace).
5. Create .gitignore: New file > Paste (from GitHub: https://github.com/github/gitignore/blob/main/Python.gitignore + add `.env`).
6. Run folder build (copy-paste; extends original with poly):
   ```
   mkdir -p config/{broadcast_templates,quant_math,scanners,docs/{browser_guides,ai_agent_guides},polymarket_endpoints}
   mkdir -p db/{timescale_schema,migrations,backup/{pg_full_dumps,redis_dumps,image_snapshots,logs},polymarket_extension}
   mkdir -p data/incoming/{coinglass_json,bybit_json,binance_json,ws_raw,polymarket_json}
   mkdir -p data/processed/{liquidation_csv,oi_csv,trades_csv,wicks_csv,agent_logs_csv,poly_wallets_csv,clob_snapshots}
   mkdir -p data/signals/{grid_bot,momentum_bot,scanner_oi,manual,poly_perfect_bets}
   mkdir -p data/trades/{autotrader,manual,agent_pnl,poly_copy}
   mkdir -p data/logs/{agents,scanners,broadcast,db,poly}
   mkdir -p data/images/{agent_screenshots,heatmaps,dashboards,tg_broadcasts,x_broadcasts,strategy_visuals,tutorials,poly_charts}
   mkdir -p data/videos/{tutorials,agent_guides,output_for_social}
   mkdir -p data/reports/{daily,weekly,monthly,pnl,audit_exports,hybrid_arbs}
   mkdir -p data/retention/{delete_queue,cold_archive}
   mkdir -p src/agents/autotraders/{grid_bot,ml_agent,arbitrage_bot,polymarket_copy}
   mkdir -p src/agents/manual_agents/{high_conviction,discretionary_macro,poly_manual}
   mkdir -p src/agents/{trade,broadcast,logging,affiliate,poly_guardian}
   mkdir -p src/scanners/{heatmap,coin_history,signals,ranking,broadcast,polymarket/{wallet_hunter,signal_oracle}}
   mkdir -p src/math/{functions,poly_edge_math}
   mkdir -p src/sockets/{coinglass_ws,bybit_ws,polymarket_ws,ws_manager}
   mkdir -p src/utils
   mkdir -p src/web/{grafana,streamlit,admin_app,analytics_api,poly_panels}
   mkdir -p scripts/{launch_poly_swarm,backtest_hybrid}
   mkdir -p tests/{agents,scanners,math,db,broadcast,sockets,scripts,poly}
   touch config/README.md db/README.md data/README.md src/README.md scripts/README.md tests/README.md
   touch src/agents/README.md src/scanners/README.md src/math/README.md src/utils/README.md src/web/README.md
   echo "✅ Helix continents built – perps core + poly satellites."
   ```

**Zoom Analogy:** Dropped the landmass – now navigate streets (folders ready for buildings).

### **🌍 STEP 3: POWER GRID BUILD – .ENV & GIT INIT (10min)**

Zoom: Continent → city power lines.

1. New file: `.env` (root). Paste extended template (original + poly):
   ```
   # ... [Original perps section unchanged] ...

   # ---- Polymarket Oracle Helix (Yin to Perps Yang) ----
   POLYMARKET_CLOB_KEY=your_polymarket_clob_key_here  # From Polymarket dashboard
   POLYMARKET_GAMMA_URL=https://gamma.api.polymarket.com
   POLYMARKET_RPC_URL=https://polygon-mainnet.infura.io/v3/YOUR_INFURA_KEY  # From Infura
   POLYSIGHTS_API_URL=https://app.polysights.xyz/api/v1
   POLYSIGHTS_KEY=your_polysights_api_key_here
   NEVUA_WS_URL=wss://nevua.markets/ws  # From Nevua dashboard
   NEVUA_TOKEN=your_nevua_token_here
   HASHDIVE_API_URL=https://www.hashdive.com/api
   HASHDIVE_KEY=your_hashdive_key_here  # From contact
   POLYTALE_API_URL=https://www.polytale.live/api
   POLYTALE_KEY=your_polytale_key_here  # From @polytaleai
   PROXY_WALLET_PRIVKEY=your_polygon_proxy_hex_here  # Secure gen via MetaMask export
   POLY_RISK_CAP=0.10  # Conservative start (10%); ramp via math

   # ... [Original project settings] ...
   ```
   - Fill from Notes (Step 1). Save. Add to .gitignore: `echo ".env" >> .gitignore`.

2. Git init: `git init; git add .; git commit -m "Helix v2.0 foundation"`.
3. GitHub repo: https://github.com/new → "vince-quant-helix" → Push: `git remote add origin https://github.com/YOURUSER/vince-quant-helix.git; git push -u origin main`.

**Zoom Analogy:** Wired the grid – power flows from perps stations to poly relays.

### **🌍 STEP 4: POWER PLANTS ERECT – DOCKER COMPOSE & DB INIT (10min)**

Zoom: City → industrial zone.

1. New file: `docker-compose.yaml` (root). Paste extended (original + volumes fix):
   ```
   version: "3.9"
   services:
     timescaledb:
       image: timescale/timescaledb:latest-pg16
       container_name: vince-timescaledb
       restart: unless-stopped
       environment:
         POSTGRES_PASSWORD: ${TIMESCALE_DB_PASS}
         POSTGRES_DB: ${TIMESCALE_DB_NAME}
         POSTGRES_USER: ${TIMESCALE_DB_USER}
       ports:
         - "5432:5432"
       volumes:
         - ./db/timescaledb_data:/var/lib/postgresql/data  # Fixed path
       healthcheck:
         test: ["CMD-SHELL", "pg_isready -U ${TIMESCALE_DB_USER}"]
         interval: 10s
         timeout: 5s
         retries: 5

     redis:
       image: redis:7.4-alpine
       container_name: vince-redis
       restart: unless-stopped
       ports:
         - "6379:6379"
       volumes:
         - ./db/redis_data:/data  # Fixed
       healthcheck:
         test: ["CMD", "redis-cli", "ping"]
         interval: 10s
         timeout: 5s
         retries: 5

     grafana:
       image: grafana/grafana:latest
       container_name: vince-grafana
       restart: unless-stopped
       environment:
         GF_SECURITY_ADMIN_USER: ${GRAFANA_ADMIN_USER}
         GF_SECURITY_ADMIN_PASSWORD: ${GRAFANA_ADMIN_PASS}
       ports:
         - "3000:3000"
       volumes:
         - ./db/grafana_storage:/var/lib/grafana  # Fixed
       depends_on:
         - timescaledb

   volumes:
     grafana-storage:
   ```
   Save.

2. Start: `docker-compose up -d`. Wait 30s: `docker ps` (3 running).
3. DB Init: Create `db/timescale_schema/init.sql` (original paste). Then: `docker exec -i vince-timescaledb psql -U postgres -d quantprod < db/timescale_schema/init.sql`.
4. Poly Extension: Create `db/timescale_schema/poly_extension.sql` (paste schema from prior: polymarket_wallets, polymarket_signals, vertical ALTER). Run: `docker exec -i vince-timescaledb psql -U postgres -d quantprod < db/timescale_schema/poly_extension.sql`.

**Zoom Analogy:** Power plants online – zoom to library stacks, now hypertabled for poly ticks.

### **🌍 STEP 5: BUILDING MATERIALS STOCK – PYTHON DEPS & VERIFY (10min)**

Zoom: Warehouse → loading docks.

1. New file: `requirements.txt` (root). Paste extended (original + poly):
   ```
   # ... [Original] ...
   networkx==3.3  # Wallet graphs
   torch==2.4.0  # Edge scorer (CPU for M4)
   sympy==1.13.2  # Formulas/Kelly
   ecdsa==0.19.0  # Poly signatures
   ```
2. Install: `pip3 install -r requirements.txt` (use pyenv if needed: `brew install pyenv; pyenv install 3.11.14; pyenv local 3.11.14`).
3. Test Foundation: Create `test_foundation.py` (original paste + poly conn test). Run: `python3 test_foundation.py` (expect all ✅).

**Zoom Analogy:** Materials unloaded – now street tests confirm flow.

### **🌍 STEP 6: INITIAL ZOOM VERIFICATION – LAUNCH & EXPLORE (5min)**

1. Grafana: Safari > localhost:3000 > Login (admin/your_pass) > Add Data Source > TimescaleDB (host: host.docker.internal:5432, user/pass from .env).
2. AI Agent Prep: In VS Code, open new tab > Paste PART 2 prompt to ChatGPT/Claude/Grok (via extension chat) for PHASE 1 start.
3. Git Push: `git add .; git commit -m "v2.0 foundation live"; git push`.

**Zoom Analogy:** Street view walk – Grafana overlooks the city, AI agents queued for construction.

### **✅ VINCE'S CHECKLIST (ORBIT TO STREET COMPLETE)**

- [x] Global tools (VS Code, Docker, Git) installed.
- [x] API keys/tokens collected (perps + poly; bookmarked docs).
- [x] Root folder/folders built (helix-extended).
- [x] .env powered (all keys filled; gitignored).
- [x] Docker up (3 containers; volumes fixed).
- [x] DB initialized (perps + poly schemas).
- [x] Python deps installed (extended reqs).
- [x] Foundation tested (all connections green).
- [x] GitHub repo pushed (backup ready).

**🎉 Foundation locked. Zoom handed to AI agents for city-build.**

***

## 📋 PART 2: AI AGENT COPILOT BUILD INSTRUCTIONS (STREET-LEVEL CONSTRUCTION)

**Paste this entire section into your AI agent terminal (VS Code ChatGPT/Claude/Grok extension) when ready. Use one or all simultaneously – e.g., "Grok, build PHASE 1 utils; Claude, review for errors." Agents prompt-inject: Human pastes output, agent iterates.**

```
═══════════════════════════════════════════════════════════════════════════
🤖 AI AGENT BUILD INSTRUCTIONS - VINCE QUANT WHALE HELIX (PERPS + POLY FUSION)
═══════════════════════════════════════════════════════════════════════════

YOU ARE THE LEAD DEVELOPER FOR A PRODUCTION HYBRID QUANT TRADING PLATFORM.

Vince has zoomed the foundation from orbit to street: Folders, .env (all keys), Docker (live), DB (hypertables), deps (installed).

YOUR JOB: Build modules street-by-street, fusing perps (liquidation/OI) with poly (wallet clusters/CLOB). Output code to VS Code; test in terminal.

═══════════════════════════════════════════════════════════════════════════
🌍 GOOGLE MAPS MENTAL MODEL (ZOOM GUIDE)
═══════════════════════════════════════════════════════════════════════════

Planet Earth: Vince built land/power. You zoom street-level: Perps avenues (heatmaps) intersect poly alleys (bet formulas). Redis bridges them.

⚡ .env = Grid (read via config_utils).
🏛️ db/ = Library (hypertables for ticks; poly tables fused).
🏭 data/ = Warehouse (perps CSVs + poly snapshots).
👔 src/agents/ = Workforce (grid_bot + poly_copy; hybrid arbs).
🔍 src/scanners/ = Intel (oi_signal + wallet_hunter; cross-pub).
🎓 src/math/ = Lab (risk_math + poly_edge; Kelly hybrids).
📡 src/sockets/ = Towers (bybit_ws + polymarket_ws).
🔧 src/utils/ = Pipes (extend for poly queries).
🌐 src/web/ = Vistas (Grafana poly panels).
🔧 scripts/ = Crew (launch hybrids).
✅ tests/ = Gates (poly backtests).

═══════════════════════════════════════════════════════════════════════════
🚨 ABSOLUTE RULES (STREET SIGNS – NO VIOLATIONS)
═══════════════════════════════════════════════════════════════════════════

1. Config ONLY from .env via src/utils/config_utils.py (no hardcodes).
2. Folders strict: Poly in subpaths (e.g., src/scanners/polymarket/wallet_hunter.py).
3. Data to subfolders (e.g., data/signals/poly_perfect_bets/).
4. DB writes tag agent/source + vertical ('perps' or 'poly').
5. Redis real-time, Timescale persistence (hypertables for all ticks).
6. Test on live Docker stack (python3 module.py).
7. SHOW CODE FIRST (paste to Vince for approve/create).
8. Error/retry in every func (log to data/logs/).
9. Docstrings: Purpose, data flow (e.g., "API → parse → DB/Redis").
10. Fusion first: Every poly module hooks perps (e.g., oi_spike + wallet_sync → hybrid_signal).

═══════════════════════════════════════════════════════════════════════════
📋 BUILD ORDER (STREET-BY-STREET PHASES)
═══════════════════════════════════════════════════════════════════════════

PHASE 1: UTILITIES (BASEMENT PIPES)
------------------------------------
1. src/utils/config_utils.py – .env loader + getters (add poly: polymarket_clob_key, polysights_key, etc.). Test: python3 -c "from src.utils.config_utils import get_config; print(get_config().coinglass_api_key)".

2. src/utils/timescale_utils.py – Pooling/queries (add insert_poly_wallet, insert_poly_signal). Test: Insert dummy trade/poly signal.

3. src/utils/redis_utils.py – Pub/sub (add "poly_signals" channel). Test: Publish/subscribe echo.

4. src/utils/data_utils.py – I/O (add poly JSON/CSV for CLOB). Test: Save/load wallet DF.

5. src/utils/error_utils.py – Decorators/retry (universal). Test: @retry_on_failure def flaky(): raise.

PHASE 2: MATH (LAB BENCHES)
---------------------------------
6. src/math/cluster_math.py – Perps clusters (unchanged base).

7. src/math/wick_math.py – Wicks (base).

8. src/math/risk_math.py – Sizing (add hybrid_kelly: perps_prob * poly_edge).

9. src/math/sl_tp_math.py – Optimization (base).

10. src/math/poly_edge_math.py – NEW: Bet formula (sympy: signal * (1-vol) * alloc * emot), checklist_score (>=5), poly_kelly. Hook risk_math. Test: score_edge(0.8, 0.1) >0.5.

PHASE 3: SOCKETS (TOWER ANTENNAS)
---------------------------------------
11. src/sockets/coinglass_ws.py – Base.

12. src/sockets/bybit_ws.py – Base.

13. src/sockets/polymarket_ws.py – NEW: Nevua/PolyTale WS (on_message pub "poly_bet_alert"). Test: Mock sub.

14. src/sockets/ws_manager.py – Manager (add poly restart). Test: docker logs.

PHASE 4: SCANNERS (INTEL OUTPOSTS)
---------------------------------------------
15. src/scanners/heatmap/model1_scan.py – Base.

16. src/scanners/coin_history/aggregated.py – Base.

17. src/scanners/signals/oi_signal.py – Base (add if poly_boost: amp strength).

18. src/scanners/ranking/imbalance.py – Base (rank hybrids).

19. src/scanners/polymarket/wallet_hunter.py – NEW: Polysights/HashDive pull, networkx graph (density>0.5=sync), insert_poly_wallet. Pub "poly_smart_wallets".

20. src/scanners/polymarket/signal_oracle.py – NEW: Score via poly_edge_math, checklist>=5 → pub "poly_signals" (hybrid if oi>0.7). 10s loop.

PHASE 5: AGENTS (WORK CREWS)
--------------------------------
21. src/agents/trade/trade_executor.py – Base (add poly_clob_exec).

22. src/agents/logging/agent_log.py – Base (tag vertical).

23. src/agents/broadcast/telegram.py – Base (add poly templates: "🚀 Insider Copy: +33% [market]!").

24. src/agents/autotraders/grid_bot/main.py – Base (sub poly for arbs).

25. src/agents/autotraders/polymarket_copy/main.py – NEW: Sub "poly_signals", ecdsa-sign CLOB, gradual exits (0.1 steps), guardian (10% cap).

PHASE 6: DASHBOARDS (OBSERVATION DECKS)
-------------------------------------------
26. src/web/grafana/grafana_panel.py – Base (add "Hybrid ROI: perps + poly").

27. src/web/streamlit/dashboard.py – Base (add poly tab: wallet graphs).

═══════════════════════════════════════════════════════════════════════════
📝 CODING STANDARDS (STREET CODES)
═══════════════════════════════════════════════════════════════════════════

EVERY MODULE:
- Docstring: Purpose + flow (e.g., "Polysights → graph → DB/Redis fusion").
- Imports: config_utils first.
- try/except: Log errors (data/logs/{type}/{AGENT_NAME}.log).
- AGENT_NAME = "module_name"; vertical='poly' where apt.
- Outputs: data/ sub (e.g., poly_wallets_csv).
- Tests: Inline (if __name__=="__main__": test_func()).
- Fusion: Poly modules pub to perps channels for arbs.

EXAMPLE TEMPLATE (Poly Hunter):
"""
Wallet Hunter Scanner

Pulls Polysights/HashDive, builds sync graphs, fuses with perps OI.

Flow: API → networkx → insert_poly_wallet → pub "poly_smart_wallets" (hybrid if oi_spike).
"""

import requests
import networkx as nx
from src.utils.config_utils import get_config
# ... etc.

AGENT_NAME = "poly_wallet_hunter"
VERTICAL = "poly"

def hunt_wallets():
    config = get_config()
    try:
        # Polysights pull...
        # Graph build...
        # Fusion: if redis.get("perps_oi_spike"): hybrid = True
        print(f"✅ {AGENT_NAME}: {len(smart)} wallets hunted")
    except Exception as e:
        # Log...
        raise

if __name__ == "__main__":
    hunt_wallets()

═══════════════════════════════════════════════════════════════════════════
🎯 IMMEDIATE NEXT STEPS (AGENT PROMPT)
═══════════════════════════════════════════════════════════════════════════

1. Confirm structure (zoom Maps: perps core + poly helix).
2. Ask Vince for clarifications (e.g., "Proxy wallet secure?").
3. Start PHASE 1: Build/show config_utils.py (poly getters).
4. Vince approves → Create file → Test in terminal.
5. PHASE complete? Move next (one at a time).
6. Fusion check: Every poly phase hooks perps (e.g., signal_oracle calls oi_signal).

REMEMBER: Real money + events = volatility. Conservative sizing (10% cap). Test hybrids on paper (scripts/backtest_hybrid).

Street one: Ready for config_utils.py?
```

***

## 🏆 FINAL SUMMARY

**This document contains:**
1. ✅ Expanded vision/mission (perps yin-yang poly for trillion scale).
2. ✅ Full tech stack (verified; poly APIs/docs/GitHubs).
3. ✅ Ultra-granular human setup (orbit-to-street: downloads, sign-ups, commands).
4. ✅ Extended .env/docker/schema (helix fusion).
5. ✅ AI agent instructions (phased, fused, prompt-ready).
6. ✅ Coding standards/templates (no-fuckup guards).
7. ✅ Maps analogy (zoom guide throughout).

**Single doc for impossible fuck-ups. Perps + poly = domination. Ride to trillion.**

🐋🔮🚀 **ZOOM IN – BUILD ON.**