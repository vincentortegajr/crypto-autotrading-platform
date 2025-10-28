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

### 🗺️ Multi-Zoom Google Maps Mind Map

1. **Earth View (`project-root/`)** – See the whole empire: `.env` grid, continents (`config/`, `db/`, `data/`, `src/`, `scripts/`, `tests/`), governance docs, Docker blueprints.
2. **Power Grid (`.env`)** – Transmission lines carry energy to every district: DB creds, API tokens, broadcast keys, poly oracle access, project metadata.
3. **Government Continent (`config/`)** – Laws, templates, quant constitutions. Broadcast scripts live here so agents speak with one voice.
4. **Central Library (`db/`)** – TimescaleDB shelves (hypertables for ohlcv, liquidations, poly wallets/signals, pnl) + Redis caches for instant recall.
5. **Warehouse District (`data/`)** – Raw dumps (`incoming/`), processed intelligence (`processed/`), signal dropboxes (`signals/`), executed trade ledgers (`trades/`), hybrid reports, retention vaults.
6. **City Center (`src/`)** – Workforce districts:
   - `agents/` (auto desks, manual suites, trade executors, broadcasters, logging, affiliate + new polymarket crews).
   - `scanners/` (heatmaps, history, ranking, polymarket wallet_hunter/signal_oracle).
   - `math/` (cluster, wick, risk, sl/tp, poly_edge_lab).
   - `sockets/` (CoinGlass, Bybit, Polymarket, orchestrator).
   - `utils/` (config loaders, DB/Redis adapters, error guards).
   - `web/` (Grafana panels, Streamlit dashboards, admin apps, analytics APIs, poly panels).
7. **Maintenance & QA** – `scripts/` (launchers, backtests, enforcement) and `tests/` (agents, scanners, math, db, broadcast, sockets, scripts, poly).

Each zoom level connects upstream/downstream – e.g., scanners depend on sockets, math calibrates scanners, agents ingest scanner output, broadcasts amplify agent actions.

│   │   │
│   │   ├── 🤖 autotraders/ ════════════════════════════════════════════════════════════════════ TRADING DESKS
│   │   │   │                                                                                      (Autonomous trading bots)
│   │   │   │                                                                                      Connection: 🏛️ Redis → Receive signals → Execute trades → Log to 🏛️ DB
│   │   │   ├── grid_bot/ ──────────────────────────────────────────────── Grid trading strategy
│   │   │   │   ├── main.py ────────────────────────────────────────────── Bot entry point
│   │   │   │   ├── logic.py ───────────────────────────────────────────── Grid trading logic
│   │   │   │   ├── config.json ────────────────────────────────────────── Bot-specific parameters
│   │   │   │   └── README.md ──────────────────────────────────────────── Bot documentation
│   │   │   ├── ml_agent/ ──────────────────────────────────────────────── ML/AI trading bot
│   │   │   │   ├── main.py
│   │   │   │   ├── model.py ───────────────────────────────────────────── ML model
│   │   │   │   ├── features.py ────────────────────────────────────────── Feature engineering
│   │   │   │   └── README.md
│   │   │   ├── arbitrage_bot/ ─────────────────────────────────────────── Cross-exchange arbitrage
│   │   │   │   ├── main.py
│   │   │   │   ├── scanner.py ─────────────────────────────────────────── Arb opportunity scanner
│   │   │   │   └── README.md
│   │   │   └── README.md ──────────────────────────────────────────────── AutoTrader index
│   │   │
│   │   ├── 👨‍💼 manual_agents/ ═══════════════════════════════════════════════════════════════ EXECUTIVE OFFICES
│   │   │   │                                                                                      (Human-guided trading)
│   │   │   ├── high_conviction/ ───────────────────────────────────────── High-conviction manual plays
│   │   │   │   ├── manual_trade.py ────────────────────────────────────── Manual trade executor
│   │   │   │   └── README.md
│   │   │   ├── discretionary_macro/ ───────────────────────────────────── Macro-based trading
│   │   │   │   ├── macro_analysis.py ──────────────────────────────────── Macro trend analyzer
│   │   │   │   └── README.md
│   │   │   └── README.md ──────────────────────────────────────────────── Manual agent guide
│   │   │
│   │   ├── 💼 trade/ ══════════════════════════════════════════════════════════════════════════ OPERATIONS CENTER
│   │   │   │                                                                                      (Core trade execution engine)
│   │   │   │                                                                                      Connection: 🤖 Bots call this → Executes on 📡 Bybit → Logs to 🏛️ DB
│   │   │   ├── trade_executor.py ──────────────────────────────────────── Order execution (Bybit API)
│   │   │   ├── trade_manager.py ───────────────────────────────────────── Position management
│   │   │   ├── trade_logger.py ────────────────────────────────────────── Trade logging (DB + files)
│   │   │   └── README.md ──────────────────────────────────────────────── Trade system docs
│   │   │
│   │   ├── 📢 broadcast/ ══════════════════════════════════════════════════════════════════════ MEDIA COMPANIES
│   │   │   │                                                                                      (Social media & communication bots)
│   │   │   │                                                                                      Connection: 🚨 Signals → Read here → Format → Send to Telegram/X/Email/SMS
│   │   │   ├── telegram.py ────────────────────────────────────────────── Telegram bot (main channel)
│   │   │   ├── telegram_affiliate.py ──────────────────────────────────── Telegram affiliate link injector
│   │   │   ├── x.py ───────────────────────────────────────────────────── X/Twitter posting bot
│   │   │   ├── sms.py ─────────────────────────────────────────────────── SMS alert bot (Twilio)
│   │   │   ├── email.py ───────────────────────────────────────────────── Email broadcast bot
│   │   │   ├── push.py ────────────────────────────────────────────────── Push notification bot
│   │   │   └── README.md ──────────────────────────────────────────────── Broadcast bot docs
│   │   │
│   │   ├── 📝 logging/ ════════════════════════════════════════════════════════════════════════ INTERNAL AFFAIRS
│   │   │   │                                                                                      (Audit & accountability system)
│   │   │   │                                                                                      Connection: Every agent imports → Logs every action to 🎥 data/logs/ + 🏛️ DB
│   │   │   ├── agent_log.py ───────────────────────────────────────────── Agent action logger
│   │   │   ├── event_log.py ───────────────────────────────────────────── System event logger
│   │   │   ├── trade_log.py ───────────────────────────────────────────── Trade-specific logger
│   │   │   └── README.md ──────────────────────────────────────────────── Logging system docs
│   │   │
│   │   ├── 💰 affiliate/ ══════════════════════════════════════════════════════════════════════ REVENUE TRACKING
│   │   │   │                                                                                      (Affiliate link management & click tracking)
│   │   │   │                                                                                      Connection: 📢 Broadcast embeds links → 💰 Tracks clicks → 🏛️ DB
│   │   │   ├── click_tracker.py ───────────────────────────────────────── Click event tracker
│   │   │   ├── affiliate_link_manager.py ──────────────────────────────── URL generator with ref codes
│   │   │   └── README.md ──────────────────────────────────────────────── Affiliate system docs
│   │   │
│   │   └── README.md ──────────────────────────────────────────────────────────────────────────── Agent district guide
│   │
│   ├── 🔍 scanners/ ═══════════════════════════════════════════════════════════════════════════ INTELLIGENCE NETWORK
│   │   │                                                                                          (Data gathering & analysis agents)
│   │   │                                                                                          Connection: 📦 incoming/ → Parse → 🎓 math/ → 🚨 signals/ → 🏛️ Redis
│   │   │
│   │   ├── 🛰️ heatmap/ ════════════════════════════════════════════════════════════════════════ SATELLITE SURVEILLANCE
│   │   │   │                                                                                      (Liquidation heatmap tracking)
│   │   │   │                                                                                      Connection: 📡 CoinGlass API → Parse heatmaps → Identify clusters → 🚨 Signal
│   │   │   ├── model1_scan.py ─────────────────────────────────────────── CoinGlass Model 1 scanner
│   │   │   ├── model2_scan.py ─────────────────────────────────────────── CoinGlass Model 2 scanner
│   │   │   ├── model3_scan.py ─────────────────────────────────────────── CoinGlass Model 3 scanner
│   │   │   └── README.md ──────────────────────────────────────────────── Heatmap scanner docs
│   │   │
│   │   ├── 📜 coin_history/ ═══════════════════════════════════════════════════════════════════ HISTORICAL ARCHIVES
│   │   │   │                                                                                      (1yr+ pattern analysis)
│   │   │   │                                                                                      Connection: 🏛️ DB → Read historical data → Analyze patterns → Predict whale targets
│   │   │   ├── aggregated.py ──────────────────────────────────────────── Cross-exchange aggregated history
│   │   │   ├── by_exchange.py ─────────────────────────────────────────── Exchange-specific history
│   │   │   └── README.md ──────────────────────────────────────────────── History scanner docs
│   │   │
│   │   ├── 🚨 signals/ ════════════════════════════════════════════════════════════════════════ EARLY WARNING SYSTEM
│   │   │   │                                                                                      (Trigger generators)
│   │   │   │                                                                                      Connection: Monitor data → Detect spikes → Generate signals → 🏛️ Redis + 🚨 data/signals/
│   │   │   ├── volume_signal.py ───────────────────────────────────────── Volume spike detector
│   │   │   ├── oi_signal.py ───────────────────────────────────────────── Open interest spike detector
│   │   │   ├── liquidation_signal.py ──────────────────────────────────── Liquidation level triggers
│   │   │   ├── manual_signal.py ───────────────────────────────────────── Human-generated signals
│   │   │   └── README.md ──────────────────────────────────────────────── Signal generator docs
│   │   │
│   │   ├── 🎯 ranking/ ════════════════════════════════════════════════════════════════════════ THREAT ASSESSMENT
│   │   │   │                                                                                      (Coin scoring & prioritization)
│   │   │   │                                                                                      Connection: 🏛️ DB data → 🎓 math/ → Score coins → Leaderboard → 🚨 Signal top coins
│   │   │   ├── imbalance.py ───────────────────────────────────────────── Cluster imbalance scorer
│   │   │   ├── leaderboards.py ────────────────────────────────────────── Top coin ranker
│   │   │   ├── wick_risk.py ───────────────────────────────────────────── Stop-loss risk scorer
│   │   │   ├── outlier_scanner.py ─────────────────────────────────────── Anomaly detector
│   │   │   └── README.md ──────────────────────────────────────────────── Ranking docs
│   │   │
│   │   ├── 📡 broadcast/ ══════════════════════════════════════════════════════════════════════ SIGNAL BROADCAST
│   │   │   │                                                                                      (Scanner → Social output)
│   │   │   │                                                                                      Connection: 🚨 Signals → Format for public → 📢 agents/broadcast/
│   │   │   ├── scanner2tg.py ──────────────────────────────────────────── Telegram signal pusher
│   │   │   ├── scanner2x.py ───────────────────────────────────────────── X signal pusher
│   │   │   └── README.md ──────────────────────────────────────────────── Broadcast scanner docs
│   │   │
│   │   └── README.md ──────────────────────────────────────────────────────────────────────────── Scanner district guide
│   │
│   ├── 🎓 math/ ═══════════════════════════════════════════════════════════════════════════════ RESEARCH LABORATORY
│   │   │                                                                                          (Quant algorithms & statistical analysis)
│   │   │                                                                                          Connection: 🔍 Scanners import → Calculate → Return insights
│   │   ├── cluster_math.py ────────────────────────────────────────────── Liquidation cluster detection
│   │   ├── wick_math.py ───────────────────────────────────────────────── Historical wick analysis
│   │   ├── risk_math.py ───────────────────────────────────────────────── Position sizing & risk scoring
│   │   ├── quantile_math.py ───────────────────────────────────────────── Statistical outlier detection
│   │   ├── drawdown.py ────────────────────────────────────────────────── Drawdown calculation
│   │   ├── sl_tp_math.py ──────────────────────────────────────────────── Stop-loss/take-profit optimization
│   │   ├── lead_lag.py ────────────────────────────────────────────────── Lead-lag correlation
│   │   ├── functions/ ─────────────────────────────────────────────────── ADVANCED MATH FUNCTIONS
│   │   │   └── ... ────────────────────────────────────────────────────── Custom quant modules
│   │   └── README.md ──────────────────────────────────────────────────── Math lab documentation
│   │
│   ├── 📡 sockets/ ════════════════════════════════════════════════════════════════════════════ TELECOM NETWORK
│   │   │                                                                                          (Real-time websocket connections)
│   │   │                                                                                          Connection: Exchange WS → Receive stream → 📦 data/incoming/ + 🏛️ Redis pub
│   │   ├── coinglass_ws.py ────────────────────────────────────────────── CoinGlass websocket handler
│   │   ├── bybit_ws.py ────────────────────────────────────────────────── Bybit websocket handler
│   │   ├── binance_ws.py ──────────────────────────────────────────────── Binance websocket handler
│   │   ├── composite_ws.py ────────────────────────────────────────────── Multi-feed aggregator
│   │   ├── ws_manager.py ──────────────────────────────────────────────── Websocket lifecycle manager
│   │   ├── ws_affiliate_tracker.py ────────────────────────────────────── Websocket-based click tracker
│   │   └── README.md ──────────────────────────────────────────────────── Websocket docs
│   │
│   ├── 🔧 utils/ ══════════════════════════════════════════════════════════════════════════════ UTILITIES DEPARTMENT
│   │   │                                                                                          (Essential services - config, DB, Redis, helpers)
│   │   │                                                                                          Connection: ⚡ .env → config_utils.py loads → ALL modules import
│   │   ├── config_utils.py ────────────────────────────────────────────── .ENV LOADER (CRITICAL)
│   │   │                                                                   Loads .env → Provides typed access to all keys/endpoints
│   │   ├── timescale_utils.py ─────────────────────────────────────────── TimescaleDB connection pool & wrappers
│   │   ├── redis_utils.py ─────────────────────────────────────────────── Redis pub/sub & caching helpers
│   │   ├── grafana_utils.py ───────────────────────────────────────────── Grafana API helpers
│   │   ├── streamlit_utils.py ─────────────────────────────────────────── Streamlit dashboard helpers
│   │   ├── data_utils.py ──────────────────────────────────────────────── File I/O & data processing
│   │   ├── agent_check.py ─────────────────────────────────────────────── Agent health checks
│   │   ├── error_utils.py ─────────────────────────────────────────────── Error handling & retries
│   │   ├── validation.py ──────────────────────────────────────────────── Input validation
│   │   ├── report_utils.py ────────────────────────────────────────────── Report generators
│   │   └── README.md ──────────────────────────────────────────────────── Utils documentation
│   │
│   ├── 🌐 web/ ════════════════════════════════════════════════════════════════════════════════ TOURIST DISTRICT
│   │   │                                                                                          (Human-facing dashboards & interfaces)
│   │   │                                                                                          Connection: 🏛️ TimescaleDB + Redis → Query data → Render visuals
│   │   │
│   │   ├── grafana/ ═══════════════════════════════════════════════════════════════════════════ CITY OBSERVATORY
│   │   │   │                                                                                      (Live charts & SQL query UI)
│   │   │   ├── grafana_panel.py ───────────────────────────────────────── Custom panel generator
│   │   │   └── README.md ──────────────────────────────────────────────── Grafana setup guide
│   │   │
│   │   ├── streamlit/ ═════════════════════════════════════════════════════════════════════════ INTERACTIVE MUSEUM
│   │   │   │                                                                                      (Google Sheets-like data manipulation)
│   │   │   ├── dashboard.py ───────────────────────────────────────────── Main Streamlit dashboard
│   │   │   └── README.md ──────────────────────────────────────────────── Streamlit guide
│   │   │
│   │   ├── admin_app/ ═════════════════════════════════════════════════════════════════════════ CITY HALL
│   │   │   │                                                                                      (Management & control interface)
│   │   │   ├── user_mgmt.py ───────────────────────────────────────────── User management
│   │   │   ├── agent_mgmt.py ──────────────────────────────────────────── Agent control panel
│   │   │   ├── trade_mgmt.py ──────────────────────────────────────────── Trade oversight
│   │   │   └── README.md ──────────────────────────────────────────────── Admin app docs
│   │   │
│   │   ├── analytics_api/ ═════════════════════════════════════════════════════════════════════ DATA API SERVER
│   │   │   │                                                                                      (REST API for external access)
│   │   │   ├── analytics_server.py ────────────────────────────────────── FastAPI/Flask server
│   │   │   └── README.md ──────────────────────────────────────────────── API documentation
│   │   │
│   │   └── README.md ──────────────────────────────────────────────────────────────────────────── Web district guide
│   │
│   ├── main.py ════════════════════════════════════════════════════════════════════════════════ ORCHESTRATOR
│   │                                                                                              (Application entry point - starts all services)
│   │
│   └── README.md ══════════════════════════════════════════════════════════════════════════════ Source code guide
│
├── 🔧 scripts/ ══════════════════════════════════════════════════════════════════════════════════ MAINTENANCE CREW CONTINENT
│   │                                                                                               (Automation, deployment, backups)
│   │                                                                                               Connection: Run these to manage infrastructure
│   ├── run_fullstack.sh ═══════════════════════════════════════════════════════════════════════ City startup sequence (Docker + services)
│   ├── build_containers.sh ═══════════════════════════════════════════════════════════════════ Docker build automation
│   ├── setup_env.sh ═══════════════════════════════════════════════════════════════════════════ Environment setup wizard
│   ├── test_env.sh ════════════════════════════════════════════════════════════════════════════ System health check
│   ├── nightly_backup.sh ══════════════════════════════════════════════════════════════════════ Automated backup (cron job)
│   ├── seed_dummy_data.sh ═════════════════════════════════════════════════════════════════════ Test data generator
│   ├── linter.sh ══════════════════════════════════════════════════════════════════════════════ Code quality checker
│   ├── enforce_folders.sh ═════════════════════════════════════════════════════════════════════ Folder discipline enforcer
│   ├── create_new_agent.sh ════════════════════════════════════════════════════════════════════ Agent scaffold generator
│   ├── create_new_scanner.sh ══════════════════════════════════════════════════════════════════ Scanner scaffold generator
│   └── README.md ══════════════════════════════════════════════════════════════════════════════ Scripts documentation
│
├── ✅ tests/ ════════════════════════════════════════════════════════════════════════════════════ QUALITY ASSURANCE CONTINENT
│   │                                                                                               (Safety inspections & validation)
│   │                                                                                               Connection: Run tests against production stack
│   ├── agents/ ════════════════════════════════════════════════════════════════════════════════ Agent tests
│   │   ├── test_grid_bot.py ───────────────────────────────────────────── Grid bot unit tests
│   │   ├── test_momentum_bot.py ───────────────────────────────────────── Momentum bot tests
│   │   ├── test_manual_agent.py ───────────────────────────────────────── Manual agent tests
│   │   └── README.md ──────────────────────────────────────────────────── Agent testing guide
│   ├── scanners/ ══════════════════════════════════════════════════════════════════════════════ Scanner tests
│   │   ├── test_heatmap.py ────────────────────────────────────────────── Heatmap scanner tests
│   │   ├── test_history.py ────────────────────────────────────────────── History scanner tests
│   │   └── README.md ──────────────────────────────────────────────────── Scanner testing guide
│   ├── math/ ══════════════════════════════════════════════════════════════════════════════════ Math tests
│   │   ├── test_cluster_math.py ───────────────────────────────────────── Cluster math tests
│   │   └── README.md ──────────────────────────────────────────────────── Math testing guide
│   ├── db/ ════════════════════════════════════════════════════════════════════════════════════ Database tests
│   │   ├── test_schema.py ─────────────────────────────────────────────── Schema validation tests
│   │   └── README.md ──────────────────────────────────────────────────── DB testing guide
│   ├── broadcast/ ═════════════════════════════════════════════════════════════════════════════ Broadcast tests
│   │   ├── test_telegram.py ───────────────────────────────────────────── Telegram bot tests
│   │   ├── test_x.py ──────────────────────────────────────────────────── X bot tests
│   │   └── README.md ──────────────────────────────────────────────────── Broadcast testing guide
│   ├── sockets/ ═══════════════════════════════════════════════════════════════════════════════ Websocket tests
│   │   ├── test_coinglass_ws.py ───────────────────────────────────────── CoinGlass WS tests
│   │   └── README.md ──────────────────────────────────────────────────── Socket testing guide
│   ├── scripts/ ═══════════════════════════════════════════════════════════════════════════════ Script tests
│   │   ├── test_linter.py ─────────────────────────────────────────────── Linter validation tests
│   │   └── README.md ──────────────────────────────────────────────────── Script testing guide
│   └── README.md ══════════════════════════════════════════════════════════════════════════════ Testing continent guide
│
├── 🐳 Dockerfile ════════════════════════════════════════════════════════════════════════════════ CONSTRUCTION BLUEPRINT
│                                                                                                   (Container image definition)
│
├── 🐳 docker-compose.yaml ══════════════════════════════════════════════════════════════════════ CITY PLANNING DOCUMENT
│                                                                                                   (Multi-service orchestration: TimescaleDB, Redis, Grafana, App)
│
├── 📦 requirements.txt ══════════════════════════════════════════════════════════════════════════ SUPPLY MANIFEST
│                                                                                                   (Python dependencies - locked versions)
│
├── ⚙️ setup.py ══════════════════════════════════════════════════════════════════════════════════ INSTALLATION INSTRUCTIONS
│                                                                                                   (Package installer)
│
├── 📖 README.md ═════════════════════════════════════════════════════════════════════════════════ WORLD ENCYCLOPEDIA
│                                                                                                   (Project overview & quick start)
│
└── 📜 LICENSE ═══════════════════════════════════════════════════════════════════════════════════ GLOBAL CONSTITUTION
                                                                                                    (Legal terms & open-source license)
```

***

## 🌐 **COMPLETE DATA FLOW MAP (INTEGRATED VIEW)**

```
═════════════════════════════════════════════════════════════════════════════════════════════════
EXTERNAL WORLD (APIs, Exchanges, Social Media)
═════════════════════════════════════════════════════════════════════════════════════════════════
    ↓
📡 src/sockets/ (Real-time websocket connections)
    ↓
📦 data/incoming/ws_raw/ (Raw streams dumped)
    ↓
🏛️ Redis (Instant pub/sub → Notify all agents)
    ↓
🔍 src/scanners/ (Parse data + analyze with 🎓 math/)
    ↓
🚨 data/signals/ (Generated triggers)
    ↓
🏛️ Redis (Broadcast signals to AutoTraders)
    ↓
🤖 src/agents/autotraders/ (Decision: trade or not?)
    ↓
💼 src/agents/trade/ (Execute orders via Bybit API)
    ↓
📊 data/trades/ + 🏛️ TimescaleDB (Log all trades)
    ↓
📢 src/agents/broadcast/ (Format signals → Send to Telegram/X/Email/SMS)
    ↓
🌍 PUBLIC (Signals broadcast to world with affiliate links)
    ↓
💰 src/agents/affiliate/ (Track clicks)
    ↓
🏛️ TimescaleDB (Revenue tracking)

═════════════════════════════════════════════════════════════════════════════════════════════════
HUMAN INTERFACE (Dashboards)
═════════════════════════════════════════════════════════════════════════════════════════════════
🌐 src/web/grafana/ + src/web/streamlit/
    ↓
🏛️ TimescaleDB + Redis (Read live data)
    ↓
Visual dashboards (Google Sheets-like manipulation, live charts, SQL query UI)
```

***

## ⚡ **THE POWER GRID (`.env`) - COMPLETE SPECIFICATION**

```
═════════════════════════════════════════════════════════════════════════════════════════════════
⚡ .env FILE - THE ONLY CONFIG SOURCE (SINGLE SOURCE OF TRUTH)
═════════════════════════════════════════════════════════════════════════════════════════════════

# ---- Database ----
TIMESCALE_DB_HOST=localhost
TIMESCALE_DB_PORT=5432
TIMESCALE_DB_USER=postgres
TIMESCALE_DB_PASS=YOUR_PASSWORD
TIMESCALE_DB_NAME=quantprod

# ---- Redis ----
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASS=

# ---- CoinGlass API ----
COINGLASS_API_KEY=YOUR_KEY
COINGLASS_ENDPOINT_LIQ_HISTORY=https://open-api.coinglass.com/api/futures/liquidation/aggregated-history
COINGLASS_ENDPOINT_LIQ_HEATMAP_MODEL1=https://open-api.coinglass.com/api/futures/liquidation/aggregated-heatmap/model1
COINGLASS_ENDPOINT_LIQ_HEATMAP_MODEL2=https://open-api.coinglass.com/api/futures/liquidation/aggregated-heatmap/model2
COINGLASS_ENDPOINT_LIQ_HEATMAP_MODEL3=https://open-api.coinglass.com/api/futures/liquidation/aggregated-heatmap/model3
COINGLASS_ENDPOINT_OI=https://open-api.coinglass.com/api/futures/openInterest/ohlc-history

# ---- Bybit ----
BYBIT_API_KEY=YOUR_KEY
BYBIT_API_SECRET=YOUR_SECRET
BYBIT_ENDPOINT_REST=https://api.bybit.com/v5/
BYBIT_WS_PUBLIC=wss://stream.bybit.com/realtime_public/v5
BYBIT_WS_PRIVATE=wss://stream.bybit.com/realtime_private/v5

# ---- Binance ----
BINANCE_API_KEY=YOUR_KEY
BINANCE_API_SECRET=YOUR_SECRET
BINANCE_ENDPOINT_REST=https://api.binance.com/api/v3/
BINANCE_WS_PUBLIC=wss://fstream.binance.com/ws/

# ---- Telegram ----
TELEGRAM_BOT_TOKEN=YOUR_TOKEN
TELEGRAM_MAIN_CHANNEL=@your_channel
TELEGRAM_ADMIN_ID=YOUR_ID

# ---- X (Twitter) ----
X_BOT_TOKEN=YOUR_TOKEN
X_BOT_SECRET=YOUR_SECRET
X_BOT_KEY=YOUR_KEY
X_BOT_ACCESS_TOKEN=YOUR_ACCESS

# ---- Email ----
EMAIL_USER=your_email@example.com
EMAIL_PASS=YOUR_PASS
EMAIL_SMTP_HOST=smtp.gmail.com
EMAIL_SMTP_PORT=587

# ---- SMS (Twilio) ----
TWILIO_SID=YOUR_SID
TWILIO_AUTH=YOUR_AUTH
TWILIO_PHONE=+1234567890
SMS_ADMIN_PHONE=+1234567890

# ---- Grafana ----
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASS=YOUR_PASS

# ---- Affiliate ----
COINGLASS_REF_CODE=cryptowhaleapp
BYBIT_REF_CODE=YOUR_REF
AFFILIATE_TRACKING_URL=https://tracking.yourdomain.com/?ref=

# ---- Project ----
ENV=production
PROJECT_OWNER=Vince
LOG_LEVEL=DEBUG
TIMEZONE=America/Chicago

═════════════════════════════════════════════════════════════════════════════════════════════════
POWERS EVERYTHING VIA: src/utils/config_utils.py
═════════════════════════════════════════════════════════════════════════════════════════════════
```

***

## 🏆 **FINAL SUMMARY: THIS IS THE BILLION-DOLLAR BLUEPRINT**

- **⚡ ONE `.env` FILE** = ALL keys, endpoints, tokens, URLs (NO splits, NO YAML runtime reads)
- **🏢 config/** = Human docs, templates, math configs (NOT runtime keys)
- **🏛️ db/** = TimescaleDB (history) + Redis (real-time) = Knowledge storage
- **🏭 data/** = Raw → Processed → Signals → Trades (atomic pipeline)
- **👔 src/agents/** = Workforce (AutoTraders, manual agents, trade execution, broadcast, logging, affiliate)
- **🔍 src/scanners/** = Intelligence (heatmaps, history, signals, ranking)
- **🎓 src/math/** = Research lab (quant algorithms)
- **📡 src/sockets/** = Telecom (websockets for real-time data)
- **🔧 src/utils/** = Utilities (config loader, DB/Redis helpers)
- **🌐 src/web/** = Tourist district (Grafana, Streamlit, admin dashboards)
- **🔧 scripts/** = Maintenance crew (deployment, backups, automation)
- **✅ tests/** = Quality assurance (safety checks)

**Every folder, file, connection, and data flow is mapped. Every agent knows its job. This is military-grade, impossible-to-fuck-up architecture for whale-level crypto domination.**

🐋💎🚀 **LET'S RIDE TO A TRILLION.**

Sources


### 🌐 Complete Data Flow Map

```
EXTERNAL WORLD (APIs, Exchanges, Social Media, Prediction Markets)
    ↓
📡 src/sockets/ (CoinGlass, Bybit, Polymarket, Nevua streams)
    ↓
📦 data/incoming/ws_raw/ (Raw streams dumped)
    ↓
🏛️ Redis (Instant pub/sub → Notify all agents)
    ↓
🔍 src/scanners/ (Parse data + analyze with 🎓 math/)
    ↓
🚨 data/signals/ (Generated triggers: perps, poly, hybrid)
    ↓
🏛️ Redis (Broadcast signals to AutoTraders + manual desks)
    ↓
🤖 src/agents/autotraders/ (Decision engines – perps bots + polymarket_copy)
    ↓
💼 src/agents/trade/ (Execute orders via Bybit API + Polymarket CLOB)
    ↓
📊 data/trades/ + 🏛️ TimescaleDB (Log all trades, wallet syncs, hybrid pnl)
    ↓
📢 src/agents/broadcast/ (Format signals → Telegram/X/Email/SMS/poly newsletters)
    ↓
🌍 PUBLIC (Signals broadcast with affiliate links, performance receipts)
    ↓
💰 src/agents/affiliate/ (Track clicks/referrals)
    ↓
🏛️ TimescaleDB (Revenue + attribution tracking)

HUMAN INTERFACE (Dashboards)
🌐 src/web/grafana/ + src/web/streamlit/
    ↓
🏛️ TimescaleDB + Redis (Live data) + poly snapshots
    ↓
Visual dashboards (Google Sheets-like manipulations, live charts, SQL UI, hybrid ROI panels)
```

**Key Principles**
- Keep `.env` as the **only** runtime config source—every service calls `src/utils/config_utils.py`.
- `config/` stores human-readable laws; `db/` + `data/` are the knowledge backbone; `src/` is the workforce executing strategies.
- Redis handles **real-time** fan-out; TimescaleDB stores **history**; every write includes agent/source + vertical (`perps` or `poly`).
- `scripts/` automate upkeep (backups, linting, launch sequences); `tests/` enforce QA across perps and poly modules.
- Grafana/Streamlit dashboards close the loop, translating logs and signals into investor-facing proof.

## 🧠 Knowledge Rarity & Transparency Moat

- Less than ~0.5% of traders lean on liquidation hunting, and only ~0.001% have systematized it with multi-timeframe aggregation plus public transparency.  
  (Tiers: 10-15% know liquidation data exists → 1-3% understand it moves price → 0.1-0.5% actually trade it → 0.01% build tooling → 0.001% broadcast it.)
- Humans cannot scan 500+ perp heatmaps, manage entries/exits, and stay disciplined—automation turns the inevitable whale play into a repeatable edge.
- Transparency is the moat: 90% will never believe it, 9% can’t execute it, so we openly document everything to build trust, referrals, and fund inflows while the automated stack captures the value.
- Live proof shows the double-profit dynamic (long into clusters, short the unwind). The stack’s job is to codify that behavior—no mystery algorithms, just visible liquidation math.

## 🚀 Growth Flywheel & Phased Roadmap

| Phase | Timeline | What We Build | Manual Focus | Success Metrics |
|-------|----------|---------------|--------------|-----------------|
| **Foundation** | Months 1-3 | Folder scaffolding, `.env`, data collectors, dashboards, proof-of-trades | Record annotated trades, collect testimonials, publish transparency threads | 100+ documented trades, first 100 paying members |
| **Automation & Distribution** | Months 4-6 | Production scanners, autotraders, signal broadcasts, affiliate system | Appear on podcasts/Twitter Spaces, seed community leaders | 100 trades/day capacity, 5k members, 50% affiliate payout loop |
| **Gamification & Fund Launch** | Months 7-12 | Member portal (Next.js + Supabase/Tailwind), badges, leaderboards, fund onboarding flows | Host weekly calls, publish live P&L dashboards | 1M members at $97/mo, $100M AUM, viral social proof |
| **Whale Mode** | Months 13-24 | Internal market-making desks, token economics, DAO/fund governance tooling | Strategic partnerships, institutional onboarding | Become liquidity mover, launch token, scale to multi-billion valuation |

- Immediate Week 1 checklist: finalize `.env`, run scanners nightly, capture before/after screenshots, compile case studies, and start the 12-week Asana checklist (foundation → dashboards).

## 🧠 Agent Memory Playbook

- Create `AGENT_MEMORY.md` at the project root and paste the full context snippet (Google Maps overview, folder rules, edge explanation, non-negotiable commandments).
- For every prompt to ChatGPT/Claude/Grok, append either:
  - The entire snippet, or
  - The quick reminder block (project summary, config rules, data flow, current phase/task placeholders) with a link back to the full memory file.
- Rules reiterated in the snippet: never hardcode secrets, maintain folder discipline, run against the Docker stack, show code before creating files, log every action, tag trades with agent + vertical.
- This process onboard any agent from zero context in one paste and prevents drift—treat the snippet as part of every command.

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

1. New file: `.env` (root). Paste **full template** (perps core + poly oracle fusion). Fill every value before running anything:
   ```
   # ════════════════════════════════════════════════════════════════════════
   # ⚡ THE GLOBAL POWER GRID - SINGLE SOURCE OF TRUTH
   # ════════════════════════════════════════════════════════════════════════
   # This file powers EVERYTHING. No other config files are read at runtime.
   # Fill in ALL values below. Never commit this file to git.
   # ════════════════════════════════════════════════════════════════════════

   # ---- TimescaleDB (Historical storage) ----
   TIMESCALE_DB_HOST=localhost
   TIMESCALE_DB_PORT=5432
   TIMESCALE_DB_USER=postgres
   TIMESCALE_DB_PASS=YourSecurePasswordHere
   TIMESCALE_DB_NAME=quantprod

   # ---- Redis (Real-time cache & pub/sub) ----
   REDIS_HOST=localhost
   REDIS_PORT=6379
   REDIS_PASS=

   # ---- CoinGlass API (Premium Liquidation & OI) ----
   COINGLASS_API_KEY=your_coinglass_api_key_here
   COINGLASS_ENDPOINT_LIQ_HISTORY=https://open-api.coinglass.com/api/futures/liquidation/aggregated-history
   COINGLASS_ENDPOINT_LIQ_HEATMAP_MODEL1=https://open-api.coinglass.com/api/futures/liquidation/aggregated-heatmap/model1
   COINGLASS_ENDPOINT_LIQ_HEATMAP_MODEL2=https://open-api.coinglass.com/api/futures/liquidation/aggregated-heatmap/model2
   COINGLASS_ENDPOINT_LIQ_HEATMAP_MODEL3=https://open-api.coinglass.com/api/futures/liquidation/aggregated-heatmap/model3
   COINGLASS_ENDPOINT_OI=https://open-api.coinglass.com/api/futures/openInterest/ohlc-history
   COINGLASS_ENDPOINT_VOLUME=https://open-api.coinglass.com/api/futures/volume/ohlc-history
   COINGLASS_ENDPOINT_FUNDING=https://open-api.coinglass.com/api/futures/fundingRate/history

   # ---- Bybit API (Perps execution) ----
   BYBIT_API_KEY=your_bybit_api_key_here
   BYBIT_API_SECRET=your_bybit_api_secret_here
   BYBIT_ENDPOINT_REST=https://api.bybit.com/v5/
   BYBIT_WS_PUBLIC=wss://stream.bybit.com/realtime_public/v5
   BYBIT_WS_PRIVATE=wss://stream.bybit.com/realtime_private/v5

   # ---- Binance API (Optional reference data) ----
   BINANCE_API_KEY=your_binance_api_key_here
   BINANCE_API_SECRET=your_binance_api_secret_here
   BINANCE_ENDPOINT_REST=https://api.binance.com/api/v3/
   BINANCE_WS_PUBLIC=wss://fstream.binance.com/ws/

   # ---- Polymarket Oracle Helix (Prediction edge) ----
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

   # ---- Telegram Bot (Broadcast) ----
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   TELEGRAM_MAIN_CHANNEL=@your_main_channel
   TELEGRAM_ADMIN_ID=your_telegram_user_id_here

   # ---- X (Twitter) API ----
   X_API_KEY=your_x_api_key_here
   X_API_SECRET=your_x_api_secret_here
   X_ACCESS_TOKEN=your_x_access_token_here
   X_ACCESS_SECRET=your_x_access_secret_here

   # ---- Email SMTP (Broadcast) ----
   EMAIL_USER=your_email@example.com
   EMAIL_PASS=your_email_password_here
   EMAIL_SMTP_HOST=smtp.gmail.com
   EMAIL_SMTP_PORT=587

   # ---- SMS (Twilio) ----
   TWILIO_ACCOUNT_SID=your_twilio_sid_here
   TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
   TWILIO_PHONE=+1234567890
   SMS_ADMIN_PHONE=+1234567890

   # ---- Grafana ----
   GRAFANA_ADMIN_USER=admin
   GRAFANA_ADMIN_PASS=ChangeMe123

   # ---- Affiliate Tracking ----
   COINGLASS_REF_CODE=cryptowhaleapp
   BYBIT_REF_CODE=your_bybit_ref_code
   AFFILIATE_TRACKING_URL=https://tracking.yourdomain.com/?ref=

   # ---- Project Settings ----
   ENV=production
   PROJECT_OWNER=Vince
   LOG_LEVEL=DEBUG
   TIMEZONE=America/Chicago
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
3. DB Init: Create `db/timescale_schema/init.sql` (core perps schema). Then: `docker exec -i vince-timescaledb psql -U postgres -d quantprod < db/timescale_schema/init.sql`.
4. Poly Extension: Create `db/timescale_schema/poly_extension.sql` (polymarket tables + hybrid indexes). Run: `docker exec -i vince-timescaledb psql -U postgres -d quantprod < db/timescale_schema/poly_extension.sql`.

> **Reference template: `db/timescale_schema/init.sql`**
> ```sql
> CREATE TABLE IF NOT EXISTS ohlcv (
>     id SERIAL PRIMARY KEY,
>     symbol TEXT NOT NULL,
>     timeframe TEXT NOT NULL,
>     time TIMESTAMPTZ NOT NULL,
>     open NUMERIC NOT NULL,
>     high NUMERIC NOT NULL,
>     low NUMERIC NOT NULL,
>     close NUMERIC NOT NULL,
>     volume NUMERIC NOT NULL,
>     created_at TIMESTAMPTZ DEFAULT NOW()
> );
> SELECT create_hypertable('ohlcv', 'time', if_not_exists => TRUE);
>
> CREATE TABLE IF NOT EXISTS liquidation_snapshots (
>     id SERIAL PRIMARY KEY,
>     symbol TEXT NOT NULL,
>     timeframe TEXT NOT NULL,
>     price NUMERIC NOT NULL,
>     long_liq NUMERIC NOT NULL,
>     short_liq NUMERIC NOT NULL,
>     cluster_score NUMERIC,
>     heatmap_model TEXT,
>     time TIMESTAMPTZ NOT NULL,
>     created_at TIMESTAMPTZ DEFAULT NOW()
> );
> SELECT create_hypertable('liquidation_snapshots', 'time', if_not_exists => TRUE);
>
> CREATE TABLE IF NOT EXISTS open_interest (
>     id SERIAL PRIMARY KEY,
>     symbol TEXT NOT NULL,
>     timeframe TEXT NOT NULL,
>     oi NUMERIC NOT NULL,
>     volume NUMERIC,
>     funding_rate NUMERIC,
>     time TIMESTAMPTZ NOT NULL,
>     created_at TIMESTAMPTZ DEFAULT NOW()
> );
> SELECT create_hypertable('open_interest', 'time', if_not_exists => TRUE);
>
> CREATE TABLE IF NOT EXISTS trades (
>     trade_id SERIAL PRIMARY KEY,
>     agent TEXT NOT NULL,
>     symbol TEXT NOT NULL,
>     direction TEXT NOT NULL,
>     size NUMERIC NOT NULL,
>     entry_price NUMERIC NOT NULL,
>     exit_price NUMERIC,
>     pnl NUMERIC,
>     status TEXT DEFAULT 'open',
>     entry_time TIMESTAMPTZ NOT NULL,
>     exit_time TIMESTAMPTZ,
>     metadata JSONB,
>     created_at TIMESTAMPTZ DEFAULT NOW()
> );
>
> CREATE TABLE IF NOT EXISTS signals (
>     signal_id SERIAL PRIMARY KEY,
>     agent TEXT NOT NULL,
>     symbol TEXT,
>     signal_type TEXT NOT NULL,
>     confidence NUMERIC,
>     payload JSONB,
>     created_at TIMESTAMPTZ DEFAULT NOW()
> );
> SELECT create_hypertable('signals', 'created_at', if_not_exists => TRUE);
>
> CREATE TABLE IF NOT EXISTS agent_logs (
>     log_id SERIAL PRIMARY KEY,
>     agent TEXT NOT NULL,
>     event_type TEXT NOT NULL,
>     detail TEXT,
>     created_at TIMESTAMPTZ DEFAULT NOW()
> );
> SELECT create_hypertable('agent_logs', 'created_at', if_not_exists => TRUE);
>
> CREATE TABLE IF NOT EXISTS affiliate_clicks (
>     click_id SERIAL PRIMARY KEY,
>     ref_code TEXT NOT NULL,
>     source TEXT,
>     ip_address TEXT,
>     user_agent TEXT,
>     clicked_at TIMESTAMPTZ DEFAULT NOW()
> );
>
> CREATE TABLE IF NOT EXISTS wicks (
>     wick_id SERIAL PRIMARY KEY,
>     symbol TEXT NOT NULL,
>     max_wick_up NUMERIC NOT NULL,
>     max_wick_down NUMERIC NOT NULL,
>     analyzed_period TEXT NOT NULL,
>     updated_at TIMESTAMPTZ DEFAULT NOW()
> );
>
> CREATE TABLE IF NOT EXISTS pnl (
>     pnl_id SERIAL PRIMARY KEY,
>     agent TEXT NOT NULL,
>     period TEXT NOT NULL,
>     total_pnl NUMERIC NOT NULL,
>     win_rate NUMERIC,
>     trades_count INT,
>     calculated_at TIMESTAMPTZ DEFAULT NOW()
> );
>
> CREATE TABLE IF NOT EXISTS auto_traders (
>     trader_id SERIAL PRIMARY KEY,
>     trader_name TEXT UNIQUE NOT NULL,
>     strategy TEXT NOT NULL,
>     status TEXT DEFAULT 'active',
>     current_positions JSONB,
>     last_trade_time TIMESTAMPTZ,
>     created_at TIMESTAMPTZ DEFAULT NOW()
> );
>
> CREATE INDEX IF NOT EXISTS idx_ohlcv_symbol ON ohlcv(symbol, time DESC);
> CREATE INDEX IF NOT EXISTS idx_liq_symbol ON liquidation_snapshots(symbol, time DESC);
> CREATE INDEX IF NOT EXISTS idx_trades_agent ON trades(agent, entry_time DESC);
> CREATE INDEX IF NOT EXISTS idx_signals_agent ON signals(agent, created_at DESC);
> CREATE INDEX IF NOT EXISTS idx_agent_logs_agent ON agent_logs(agent, created_at DESC);
> ```
>
> **Poly extension (`poly_extension.sql`)**
> ```sql
> ALTER TABLE trades ADD COLUMN IF NOT EXISTS vertical TEXT DEFAULT 'perps';
> ALTER TABLE signals ADD COLUMN IF NOT EXISTS vertical TEXT DEFAULT 'perps';
> ALTER TABLE agent_logs ADD COLUMN IF NOT EXISTS vertical TEXT;
> ALTER TABLE pnl ADD COLUMN IF NOT EXISTS vertical TEXT DEFAULT 'perps';
>
> CREATE TABLE IF NOT EXISTS poly_wallets (
>     wallet_id SERIAL PRIMARY KEY,
>     address TEXT UNIQUE NOT NULL,
>     roi_30d NUMERIC,
>     streak INT,
>     checklist_score NUMERIC,
>     tags TEXT[],
>     last_seen TIMESTAMPTZ,
>     metadata JSONB,
>     created_at TIMESTAMPTZ DEFAULT NOW()
> );
>
> CREATE TABLE IF NOT EXISTS poly_signals (
>     poly_signal_id SERIAL PRIMARY KEY,
>     market_id TEXT NOT NULL,
>     market_name TEXT NOT NULL,
>     outcome TEXT NOT NULL,
>     price NUMERIC NOT NULL,
>     edge_score NUMERIC NOT NULL,
>     checklist INT NOT NULL,
>     wallet_sync BOOLEAN DEFAULT FALSE,
>     oi_confirmation BOOLEAN DEFAULT FALSE,
>     hybrid_weight NUMERIC,
>     generated_at TIMESTAMPTZ DEFAULT NOW()
> );
> SELECT create_hypertable('poly_signals', 'generated_at', if_not_exists => TRUE);
>
> CREATE TABLE IF NOT EXISTS hybrid_signals (
>     hybrid_id SERIAL PRIMARY KEY,
>     perps_symbol TEXT NOT NULL,
>     poly_market_id TEXT NOT NULL,
>     thesis TEXT,
>     edge NUMERIC,
>     recommended_action TEXT,
>     created_at TIMESTAMPTZ DEFAULT NOW()
> );
>
> CREATE INDEX IF NOT EXISTS idx_poly_signals_market ON poly_signals(market_id, generated_at DESC);
> CREATE INDEX IF NOT EXISTS idx_poly_wallets_address ON poly_wallets(address);
> CREATE INDEX IF NOT EXISTS idx_hybrid_signals_symbol ON hybrid_signals(perps_symbol, created_at DESC);
> ```

**Zoom Analogy:** Power plants online – zoom to library stacks, now hypertabled for poly ticks.

### **🌍 STEP 5: BUILDING MATERIALS STOCK – PYTHON DEPS & VERIFY (10min)**

Zoom: Warehouse → loading docks.

1. New file: `requirements.txt` (root). Paste extended (original + poly):
   ```
   python-dotenv==1.0.1
   psycopg2-binary==2.9.9
   redis==5.0.8
   requests==2.32.3
   websocket-client==1.8.0
   pyyaml==6.0.2
   pandas==2.2.3
   numpy==2.1.2
   aiohttp==3.10.5
   fastapi==0.115.0
   uvicorn==0.32.0
   streamlit==1.39.0
   python-telegram-bot==21.7
   tweepy==4.14.0
   twilio==9.3.7
   networkx==3.3      # Wallet graphs
   torch==2.4.0       # Edge scorer (CPU build works on M4)
   sympy==1.13.2      # Formulas/Kelly math
   ecdsa==0.19.0      # Polymarket CLOB signatures
   ```
2. Install: `pip3 install -r requirements.txt` (use pyenv if needed: `brew install pyenv; pyenv install 3.11.14; pyenv local 3.11.14`).
3. Test Foundation: Create `test_foundation.py` (template below). Run: `python3 test_foundation.py` (expect all ✅).
   ```python
   import os
   from dotenv import load_dotenv
   import psycopg2
   import redis
   import requests

   load_dotenv()

   print(f"✅ .env loaded: {os.getenv('PROJECT_OWNER')}")

   try:
       conn = psycopg2.connect(
           host=os.getenv('TIMESCALE_DB_HOST'),
           port=os.getenv('TIMESCALE_DB_PORT'),
           user=os.getenv('TIMESCALE_DB_USER'),
           password=os.getenv('TIMESCALE_DB_PASS'),
           database=os.getenv('TIMESCALE_DB_NAME')
       )
       print("✅ TimescaleDB connected")
       conn.close()
   except Exception as e:
       print(f"❌ TimescaleDB failed: {e}")

   try:
       r = redis.Redis(host=os.getenv('REDIS_HOST'), port=int(os.getenv('REDIS_PORT')))
       r.ping()
       print("✅ Redis connected")
   except Exception as e:
       print(f"❌ Redis failed: {e}")

   try:
       headers = {"X-API-KEY": os.getenv("COINGLASS_API_KEY")}
       resp = requests.get(os.getenv("COINGLASS_ENDPOINT_LIQ_HISTORY"), headers=headers, timeout=10)
       resp.raise_for_status()
       print("✅ CoinGlass reachable")
   except Exception as e:
       print(f"❌ CoinGlass failed: {e}")

   try:
       headers = {"Authorization": f"Bearer {os.getenv('POLYMARKET_CLOB_KEY')}"}
       resp = requests.get(f"{os.getenv('POLYMARKET_GAMMA_URL')}/markets", headers=headers, timeout=10)
       if resp.status_code in (200, 401):  # 401 = auth placeholder, confirms reachability
           print("✅ Polymarket Gamma reachable")
       else:
           print(f"⚠️ Polymarket Gamma unexpected status: {resp.status_code}")
   except Exception as e:
       print(f"❌ Polymarket Gamma failed: {e}")
   ```

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

**Paste this entire section into your AI agent terminal (VS Code ChatGPT/Claude/Grok extension) when ready. Use one or all simultaneously – e.g., "Grok, build PHASE 1 utils; Claude, review for errors." Agents prompt-inject: Human pastes output, agent iterates. Before every interaction, paste the contents (or quick snippet) of `AGENT_MEMORY.md` so the agent carries the full Google Maps context and commandments.**

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
🔁 EXECUTION FLOW CHEAT SHEET
═══════════════════════════════════════════════════════════════════════════
- Startup handshake: Docker running → containers healthy → `.env` loaded → TimescaleDB/Redis reachable → core tables present → CoinGlass/Bybit/Polymarket APIs return 200/401.
- Liquidation collector pulls every 60 seconds (faster on spike alerts) across ALL timeframes, storing raw rows in `liquidation_data_raw`.
- OI/volume monitor thresholds: `oi_change_pct > 3%`, `volume_spike_ratio > 1.5`, `abs(price_5min_change_pct) > 2%` trigger immediate re-fetch & publish to `spike_alerts`.
- Imbalance calculator groups clusters above/below price, computes totals, leftover yellow pockets, and publishes ranked results.
- Trade signal generator waits for **double confirmation**: liquidation imbalance ≥ target threshold AND recent OI/volume spike within 5 minutes.
- AutoTrader ladders entries (configurable steps), sets stop at cluster edge minus buffer, TP at opposing cluster, and pre-seeds mirrored short/long when imbalance flips.
- Trailing stop daemon moves stops once TP1 hits; every update persists to TimescaleDB (`trades`, `agent_logs`) and broadcasts to Redis.
- Error policy: exponential backoff (5s → 10s → 30s) per API; after three failures escalate to alert channel with payload snapshot.

═══════════════════════════════════════════════════════════════════════════
📈 SCALED ENTRY & CAPITAL PHASES
═══════════════════════════════════════════════════════════════════════════
- **Phase 1 (≤ $10k):** Single-entry only, focus on execution proof and discipline.
- **Phase 2 ($10k-$100k):** Enable scaling on BTC/ETH with conservative spacing; guardrails for margin lockup.
- **Phase 3 ($100k-$1M):** Apply scaling to top alt perps; use NASCAR coin blacklist + circuit breakers.
- **Phase 4 ($1M+):** Full whale mode—multi-leg ladders, mirrored shorts, internal market-making.  
  Automation tasks: compute step size/leverage from cluster depth, set staged take-profit brackets, enforce max margin usage per coin.

═══════════════════════════════════════════════════════════════════════════
🧪 LESSONS FROM LIVE PROOF
═══════════════════════════════════════════════════════════════════════════
- Timeframe sensitivity matters: 12h clusters guide scalps, 7d/30d anchor swing targets; store coin-specific thresholds in `coin_history_patterns`.
- Stop/TP placement should bias toward cluster centers; edges get wicked; use leftover liquidity pockets (“yellow leftovers”) as magnet.
- Imbalance sweet spot: 70%-85% stacked plays best; extremes may signal exhaustion—log outcomes for adaptive tuning.
- Always confirm liquidation math with OI/volume surge (or Polymarket wallet sync); raw visuals are for humans, automation relies on API data.
- Document every live proof (screenshots, P&L breakdowns) to feed dashboards, marketing, and future model calibration.

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

## 📊 METRICS & SUCCESS CRITERIA

- **Trade-level:** win rate, average R:R, max drawdown, pnl per trade, hold time, hit-rate by timeframe/cluster size.
- **System-level:** data latency (API → Redis), scanner cycle time, trade trigger to execution latency, error counts/retries, uptime of containers, backlog of unprocessed signals.
- **Business:** active members, MRR/ARR, affiliate payouts, fund AUM, churn, referral-to-member conversion, social proof (case studies/week).
- **12-week build checkpoints:**  
  - Weeks 1-2: environment + schema + utilities live, sample trades logged.  
  - Weeks 3-4: CoinGlass/Bybit collectors stable, backlog zero, Grafana shows raw feeds.  
  - Weeks 5-6: scanners ranking coins with stored imbalance metrics, alert accuracy validated.  
  - Weeks 7-8: autotraders executing paper trades with stop/TP logs.  
  - Week 9: trailing stop agent managing active positions without intervention.  
  - Week 10: broadcast bots posting to Telegram/X/email/SMS with templated messaging.  
  - Week 11: dashboards/live proof for members.  
  - Week 12: backtests complete, paper-to-live handoff checklist signed.

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
