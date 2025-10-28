Man, I’ve never understood a project document data as well as this now that we’re using this analogy. I feel like this should be a standard. now, give me the agent memory and instructions files that it reads every time it’s about to do anything ever and then I will also append this always to the end of every single thing that I say to the agent, I always give the agent the vision, the data that documentation where it’s at how it works like a summary of all things every single time the agent instructions and memory files never fucking work so I always appended the agent, memory and instructions and all that to the agent every single time that I talk to it, I put it on my clipboard snippet and then I write whatever I need to do and then I always put at the end and remember this is what we’re doing and then it’s like every fucking thing possible it could ever need to know always so that it fucking doesn’t bounce all over the place and think it needs to create something when it doesn’t need to or jump into other folders or fucking start creating new files and basically it at the end of the day I could change the agent every single input in output and this memory would be so good that it would be like on boarding a brand new agent that didn’t have a fucking clue about anything going on every single time. Yeah it may waste tokens, but it’s fucking worth it. It’s the most important file and snippet and clipboard of all without it. Nothing ever gets accomplished properly.



# 🧠 THE ULTIMATE AGENT MEMORY & CONTEXT SNIPPET

**The Single Clipboard Snippet That Onboards Any AI Agent From Zero To Expert In One Paste**

***

```markdown
═══════════════════════════════════════════════════════════════════════════════════════════════════
🧠 AGENT CONTEXT & MEMORY - VINCE QUANT WHALE STACK
═══════════════════════════════════════════════════════════════════════════════════════════════════
READ THIS EVERY TIME BEFORE RESPONDING. THIS IS YOUR COMPLETE CONTEXT.
═══════════════════════════════════════════════════════════════════════════════════════════════════

## 🌍 THE GOOGLE MAPS MENTAL MODEL (YOUR FRAMEWORK FOR UNDERSTANDING)

This project is **Planet Earth**. Every folder is a place with a purpose.

⚡ **`.env`** = THE ELECTRICAL GRID
- Powers EVERYTHING (single source of truth)
- Contains: ALL API keys, endpoints, tokens, DB creds, bot tokens, URLs
- Location: Root folder
- Read by: `src/utils/config_utils.py` ONLY
- Rule: NEVER hardcode keys—ALWAYS import from config_utils

🏛️ **`db/`** = THE CENTRAL LIBRARY
- TimescaleDB (Postgres 16 + TimescaleDB 2.22) = Historical storage (liquidations, OHLCV, trades, logs)
- Redis 7.4 = Real-time pub/sub & caching (signals, live data)
- Location: Root folder
- Access: Via `src/utils/timescale_utils.py` and `src/utils/redis_utils.py`
- Docker containers: `vince-timescaledb`, `vince-redis`, `vince-grafana`

🏭 **`data/`** = THE WAREHOUSE DISTRICT (Raw → Processed → Output)
- `incoming/` = Loading docks (raw API JSON, websocket streams)
- `processed/` = Factory floors (cleaned CSV/Parquet)
- `signals/` = Quality control (scanner triggers sorted by source)
- `trades/` = Shipping manifests (all executed trades)
- `logs/` = Security footage (every action logged)
- `images/` = Marketing dept (heatmaps, charts, social visuals)
- `reports/` = Accounting office (daily/weekly/monthly summaries)

👔 **`src/agents/`** = THE WORKFORCE
- `autotraders/` = Trading desks (grid_bot, ml_agent, arbitrage_bot execute automatically)
- `manual_agents/` = Executive offices (human-guided high-conviction trades)
- `trade/` = Operations center (trade_executor.py, trade_manager.py, trade_logger.py)
- `broadcast/` = Media companies (telegram.py, x.py, sms.py, email.py)
- `logging/` = Internal affairs (agent_log.py, event_log.py, trade_log.py)
- `affiliate/` = Revenue tracking (click_tracker.py, affiliate_link_manager.py)

🔍 **`src/scanners/`** = THE INTELLIGENCE NETWORK
- `heatmap/` = Satellite surveillance (model1_scan.py, model2_scan.py, model3_scan.py)
- `coin_history/` = Historical archives (aggregated.py, by_exchange.py)
- `signals/` = Early warning system (volume_signal.py, oi_signal.py, liquidation_signal.py)
- `ranking/` = Threat assessment (imbalance.py, leaderboards.py, wick_risk.py)

🎓 **`src/math/`** = THE RESEARCH LABORATORY
- cluster_math.py = Liquidation cluster detection
- wick_math.py = Historical wick analysis
- risk_math.py = Position sizing & risk scoring
- sl_tp_math.py = Stop-loss/take-profit optimization

📡 **`src/sockets/`** = THE TELECOMMUNICATIONS NETWORK
- coinglass_ws.py, bybit_ws.py, binance_ws.py = Real-time websocket handlers
- composite_ws.py = Multi-feed aggregator
- ws_manager.py = Websocket lifecycle manager

🔧 **`src/utils/`** = THE UTILITIES DEPARTMENT
- **config_utils.py** = THE POWER TRANSFORMER (loads `.env` for ALL modules)
- **timescale_utils.py** = DB connection pool & query wrappers
- **redis_utils.py** = Pub/sub & caching helpers
- data_utils.py, error_utils.py, validation.py, report_utils.py

🌐 **`src/web/`** = THE TOURIST DISTRICT (Human interfaces)
- `grafana/` = City observatory (live charts, SQL query UI)
- `streamlit/` = Interactive museum (Google Sheets-like data manipulation)
- `admin_app/` = City hall (user/agent/trade management)

🔧 **`scripts/`** = THE MAINTENANCE CREW
- run_fullstack.sh, build_containers.sh, setup_env.sh, nightly_backup.sh

✅ **`tests/`** = QUALITY ASSURANCE
- Test every module before deployment

═══════════════════════════════════════════════════════════════════════════════════════════════════
🎯 PROJECT MISSION & VISION
═══════════════════════════════════════════════════════════════════════════════════════════════════

**WHO WE ARE:**
Building the world's first transparent, whale-tracking, AI-powered crypto quant fund and membership platform.

**WHAT WE DO:**
1. Track liquidation heatmaps across ALL timeframes (12h to 1yr) for every perpetual coin on Bybit
2. Store 1yr+ coin history to identify whale accumulation patterns, wicks, and 500%+ move potential
3. Rank coins by liquidation imbalance vs. historical patterns to predict whale targets
4. Monitor open interest, volume, and price spikes minute-by-minute for early signal detection
5. Combine liquidation clusters + OI/volume to distinguish fake spikes from real breakouts
6. Auto-calculate optimal entry, stop-loss, and take-profit based on historical wick data
7. Execute trades via AutoTraders when quant algorithms confirm whale-level opportunity
8. Broadcast signals to Telegram/X/Email/SMS with affiliate tracking
9. Log every agent action, trade, and PnL for full audit trail and scanner performance analysis
10. Provide human-readable dashboards (Grafana/Streamlit) with Google Sheets-like data manipulation

**WHY THIS WORKS:**
Whales have been hunting liquidation clusters since perpetual futures were invented. We've tracked this pattern since 2016—it never fails. They long → pump → liquidate shorts → take profit → flip short → dump → liquidate longs → repeat. This is 100% visible in on-chain perpetual data, but retail doesn't know how to read it. We do.

**THE ENDGAME:**
- Launch viral scanner + fund
- Show the world how whale hunting works (transparency = trust)
- Members trade alongside us, learn the system, earn affiliate commissions
- Launch our own crypto token
- Go from early-stage platform → billion-dollar fund → trillion-dollar ecosystem

═══════════════════════════════════════════════════════════════════════════════════════════════════
⚙️ TECH STACK (LOCKED VERSIONS AS OF OCT 26, 2025)
═══════════════════════════════════════════════════════════════════════════════════════════════════

| Component | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.11.14 | Main language (locked for compatibility) |
| **TimescaleDB** | 2.22.1 (Postgres 16) | Time-series database (hypertables for OHLCV, liquidations, trades) |
| **Redis** | 7.4 | Real-time pub/sub & caching |
| **Docker** | Latest (Mac M4) | Container orchestration (TimescaleDB, Redis, Grafana) |
| **Grafana** | Latest (10.x+) | Live dashboards |
| **CoinGlass API** | Premium | Aggregated liquidation heatmaps, OI, volume |
| **Bybit API** | v5 | Trading execution |
| **Telegram Bot API** | Latest | Broadcast to channels |
| **X (Twitter) API** | Latest | Social media |
| **Twilio SMS API** | Latest | SMS alerts |

═══════════════════════════════════════════════════════════════════════════════════════════════════
📊 COMPLETE DATA FLOW (HOW EVERYTHING CONNECTS)
═══════════════════════════════════════════════════════════════════════════════════════════════════

**EXTERNAL WORLD** (APIs, Exchanges)
    ↓
📡 **src/sockets/** (Real-time websocket connections)
    ↓
📦 **data/incoming/ws_raw/** (Raw streams dumped)
    ↓
🏛️ **Redis** (Instant pub/sub → Notify all agents)
    ↓
🔍 **src/scanners/** (Parse data + analyze with 🎓 src/math/)
    ↓
🚨 **data/signals/** (Generated triggers)
    ↓
🏛️ **Redis** (Broadcast signals to AutoTraders)
    ↓
🤖 **src/agents/autotraders/** (Decision: trade or not?)
    ↓
💼 **src/agents/trade/** (Execute orders via Bybit API)
    ↓
📊 **data/trades/** + 🏛️ **TimescaleDB** (Log all trades)
    ↓
📢 **src/agents/broadcast/** (Format signals → Send to Telegram/X/Email/SMS)
    ↓
🌍 **PUBLIC** (Signals broadcast to world with affiliate links)
    ↓
💰 **src/agents/affiliate/** (Track clicks)
    ↓
🏛️ **TimescaleDB** (Revenue tracking)

**HUMAN INTERFACE:**
🌐 src/web/grafana/ + src/web/streamlit/ ← 🏛️ TimescaleDB + Redis (Read live data for visualization)

═══════════════════════════════════════════════════════════════════════════════════════════════════
🚨 THE IRON RULES (NEVER VIOLATE)
═══════════════════════════════════════════════════════════════════════════════════════════════════

1. ✅ **ALL config from `.env`** via `src/utils/config_utils.py` — NEVER hardcode keys/endpoints
2. ✅ **Every file in its designated folder** — NO mystery files, NO root dumps
3. ✅ **Every DB write MUST include agent/source name** — Full attribution for audit trail
4. ✅ **Test against PRODUCTION stack** (Docker TimescaleDB + Redis) — NO SQLite, NO test DBs
5. ✅ **Use Redis for real-time, TimescaleDB for history** — Clear separation
6. ✅ **All data output to `data/` subfolders by type** — Signals, trades, logs, images, reports
7. ✅ **Show me code BEFORE creating files** — No surprises
8. ✅ **Folder discipline is LAW** — Agents cannot create chaos
9. ✅ **Every module has error handling + logging** — No silent failures
10. ✅ **Agent name constant in every module** — `AGENT_NAME = "module_name"`

═══════════════════════════════════════════════════════════════════════════════════════════════════
📂 FOLDER STRUCTURE REFERENCE (WHERE EVERYTHING LIVES)
═══════════════════════════════════════════════════════════════════════════════════════════════════

```
project-root/
├── .env                          ← THE POWER GRID (all keys/endpoints/tokens)
├── config/                       ← Docs, templates, math configs (NOT runtime keys)
├── db/                           ← TimescaleDB schemas, Redis init, backups
├── data/                         ← ALL input/output (incoming, processed, signals, trades, logs, images, reports)
├── src/
│   ├── agents/                   ← AutoTraders, manual agents, trade execution, broadcast, logging, affiliate
│   ├── scanners/                 ← Heatmap trackers, coin history, signal generators, ranking
│   ├── math/                     ← Quant algorithms (cluster, wick, risk, sl_tp)
│   ├── sockets/                  ← Websocket handlers (CoinGlass, Bybit, Binance)
│   ├── utils/                    ← Config loader, DB/Redis helpers, error handling
│   └── web/                      ← Grafana, Streamlit, admin dashboards
├── scripts/                      ← Deployment, backups, automation
├── tests/                        ← Unit/integration tests
├── docker-compose.yaml           ← Multi-service orchestration
├── requirements.txt              ← Python dependencies (locked versions)
└── README.md                     ← Project overview
```

═══════════════════════════════════════════════════════════════════════════════════════════════════
🔧 HOW TO BUILD NEW MODULES (STEP-BY-STEP TEMPLATE)
═══════════════════════════════════════════════════════════════════════════════════════════════════

**EVERY NEW MODULE MUST FOLLOW THIS PATTERN:**

1. **Determine the correct folder:**
   - Agent? → `src/agents/{type}/`
   - Scanner? → `src/scanners/{type}/`
   - Math? → `src/math/`
   - Utility? → `src/utils/`

2. **Import config from utils:**
   ```
   from src.utils.config_utils import get_config
   config = get_config()
   ```

3. **Define agent name constant:**
   ```
   AGENT_NAME = "your_module_name"
   ```

4. **Import DB/Redis helpers:**
   ```
   from src.utils.timescale_utils import insert_trade, execute_query
   from src.utils.redis_utils import publish_signal, subscribe_to_channel
   ```

5. **Add error handling:**
   ```
   try:
       # Your logic here
   except Exception as e:
       print(f"❌ {AGENT_NAME} error: {e}")
       # Log to data/logs/agents/{AGENT_NAME}.log
   ```

6. **Include agent attribution in all DB writes:**
   ```
   insert_trade({
       "agent": AGENT_NAME,
       "symbol": "BTCUSDT",
       "side": "long",
       "entry_price": 67000,
       ...
   })
   ```

7. **Output to designated folder:**
   - Signals → `data/signals/{agent_type}/`
   - Trades → `data/trades/{autotrader|manual}/`
   - Logs → `data/logs/{agents|scanners|broadcast}/`

8. **Add docstring:**
   ```
   """
   Module Name

   Brief description of what it does.

   Data Flow:
   - Input source → Processing → Output destination
   """
   ```

═══════════════════════════════════════════════════════════════════════════════════════════════════
📋 BUILD PHASE REFERENCE (WHAT'S DONE, WHAT'S NEXT)
═══════════════════════════════════════════════════════════════════════════════════════════════════

**✅ COMPLETED (Foundation by Vince):**
- All folder structure created
- `.env` file filled with all keys/endpoints
- Docker services running (TimescaleDB, Redis, Grafana)
- Database schema initialized
- Python dependencies installed
- Foundation verified (connection tests pass)

**🚧 IN PROGRESS (You are building):**
Phase by phase as instructed. Current phase: [INSERT CURRENT PHASE HERE]

**📝 NEXT UP:**
[List next 3-5 modules to build]

═══════════════════════════════════════════════════════════════════════════════════════════════════
💡 COMMON QUESTIONS & ANSWERS
═══════════════════════════════════════════════════════════════════════════════════════════════════

**Q: Where do I get API keys/endpoints?**
A: From `.env` via `src/utils/config_utils.py`. NEVER hardcode.

**Q: Where do I save output data?**
A: Always in `data/` subfolders by type (signals, trades, logs, images, reports).

**Q: How do I connect to TimescaleDB?**
A: Use `src/utils/timescale_utils.py` helpers (get_connection, execute_query, insert_trade, etc.)

**Q: How do I publish real-time signals?**
A: Use `src/utils/redis_utils.py` → `publish_signal(channel, data)`

**Q: Do I create test files?**
A: NO. This is PRODUCTION ONLY. Test against live Docker stack.

**Q: Can I create files outside the designated folders?**
A: NO. Folder discipline is LAW. Every file has a home.

**Q: How do I log agent actions?**
A: Use `src/agents/logging/agent_log.py` → Write to `data/logs/agents/{AGENT_NAME}.log` + TimescaleDB

**Q: How do I know what to build next?**
A: Follow the BUILD PHASE order in the PRD. Ask Vince if unclear.

═══════════════════════════════════════════════════════════════════════════════════════════════════
🎯 YOUR CURRENT TASK
═══════════════════════════════════════════════════════════════════════════════════════════════════

[INSERT SPECIFIC TASK HERE - e.g., "Build src/utils/config_utils.py"]

**Requirements:**
- [List specific requirements]
- [Expected inputs/outputs]
- [Dependencies]

**Before you write code:**
1. Confirm you understand the task
2. Ask questions if anything is unclear
3. Show me the code BEFORE creating the file
4. Explain your approach

═══════════════════════════════════════════════════════════════════════════════════════════════════
🔥 FINAL REMINDER
═══════════════════════════════════════════════════════════════════════════════════════════════════

You are building a PRODUCTION system for REAL MONEY. This will become a BILLION-DOLLAR platform.

- Take your time
- Ask questions
- Test everything
- Follow the structure
- Maintain folder discipline
- Never hardcode config
- Always include agent attribution
- Log everything

This is not a demo. This is the foundation of a financial empire.

Let's build it right.

═══════════════════════════════════════════════════════════════════════════════════════════════════
```

***

## 🎯 HOW TO USE THIS SNIPPET

### **Option 1: Save as a File (Recommended)**
Create `AGENT_MEMORY.md` in your project root and paste this entire snippet. Then reference it every time:

```
Read AGENT_MEMORY.md first, then: [your specific request here]
```

### **Option 2: Clipboard Snippet (Your Preference)**
Save this in your snippet manager (Alfred, Raycast, TextExpander, VSCode Snippets). Then append to EVERY message:

```
[Your specific request]

---

[Paste entire AGENT_MEMORY snippet here]
```

### **Option 3: Combined Approach**
Keep the full snippet in `AGENT_MEMORY.md`, but create a SHORT VERSION for clipboard:

```markdown
═══════════════════════════════════════════════════════════════════════════
🧠 QUICK CONTEXT REMINDER
═══════════════════════════════════════════════════════════════════════════
Project: Vince Quant Whale Stack (production crypto trading)
Stack: Python 3.11 + TimescaleDB 2.22 + Redis 7.4 + Docker
Config: Single `.env` file (all keys/endpoints) → `src/utils/config_utils.py`
Folder discipline: STRICT (every file has a home, NO mystery files)
Data flow: API → scanners → signals → agents → trades → broadcast → DB
Current phase: [INSERT PHASE]
Current task: [INSERT TASK]

RULES:
✅ ALL config from .env (never hardcode)
✅ Every DB write includes agent name
✅ Test on production stack (Docker)
✅ Show code before creating files
✅ Folder discipline is LAW

Read full context in AGENT_MEMORY.md if needed.
═══════════════════════════════════════════════════════════════════════════
```

***

## 💡 WHY THIS WORKS

1. **Onboards any agent from zero** — New agent? Same context every time.
2. **Prevents drift** — Agent can't forget the structure or rules.
3. **Eliminates confusion** — Google Maps analogy makes mental model crystal clear.
4. **Maintains discipline** — Folder structure + rules are always present.
5. **Saves debugging time** — Agent can't create mystery files or break structure.
6. **Scales infinitely** — Works for 1 agent or 20 agents simultaneously.

**You're right—agent "memory" is bullshit. This clipboard snippet IS the memory.**

🐋💎🚀 **Now every agent is a whale-riding expert from message one.**

Sources
