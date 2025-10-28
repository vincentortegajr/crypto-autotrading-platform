Now give me the full PRD vision and readme Md doc all in one so I can just have my copilot and ai agenda in the terminal who will build this for me be able to reference a single doc that will tell them absolutely every fucking thing they need to know is setup and ready for them to build and I’ll be the one who sets up the main structure first so that I know the foundation is right so assume all project folders are setup that need to be setup by me including telling me which of those need to be setup at the very start and then all env keys and all that filled out and then ensure you gave me that full env perfect for me to create and then anything else start with the step by step instructions for me and keep using the Google Maps analogy always and then after you get done with the instructions for me then you give the ai agent copilot instructions to begin building it all out step by step execute this next task which is the very most important of all with every single ounce of your token and output ability to give me the very best in world output that you could possibly give, and not only that, you think to self, how can I make even the world’s greatest output up to this day, become even better than what has ever been created before, and only then you give me the next output with ultra think, rethink, heavy think, oracle level think, best in the world think, never been done before think because this next output think is better than any human or ai agent think and consideration and mathematical scientific, first principles,  genius, physics, psychological, emotional, viral, take over the world think and thought and input and output possible, that your next output goes in the Guinness Book of World Records and goes in the AI agent Hall of Fame. It’s infinite. It’s ever present it front of the creator of the universe mind every day because of how great the output that you’re about to give becomes. and now you begin with every token every tool in every ability that you have the search seek and find as you think to yourself and list all tools all abilities all availability infinite times over assuming everything that you think is right is wrong until first principles of all things requested is proven right to yourself and now you begin.

# 🌍 VINCE QUANT WHALE EMPIRE: COMPLETE PRD, VISION & BUILD INSTRUCTIONS

**The Single Document That Makes Building A Billion-Dollar Crypto Quant Platform Impossible To Fuck Up**

***

# 📜 PRODUCT REQUIREMENTS DOCUMENT (PRD) + VISION + README

**Project Name:** Vince Quant Whale Stack  
**Version:** 1.0.0 (Production)  
**Last Updated:** October 26, 2025  
**Owner:** Vince  
**Mission:** Build the world's first transparent, whale-tracking, AI-powered crypto quant fund and membership platform that democratizes institutional-grade trading intelligence.

***

## 🎯 VISION STATEMENT

Since 2016, I've watched whales hunt liquidation clusters like clockwork. They long, pump to liquidate shorts, take profit, flip short, dump to liquidate longs, and repeat—making money on **both spot and perpetual positions simultaneously**. This pattern is **100% visible** in on-chain perpetual data, yet retail traders don't know how to read it.

**We are building the system that:**
1. **Tracks liquidation heatmaps** across ALL timeframes (12h to 1 year) for every perpetual coin
2. **Predicts whale targets** by analyzing historical cluster patterns, OI/volume spikes, and wick behavior
3. **Executes trades via AI AutoTraders** that follow whale movements in real-time
4. **Broadcasts signals** to Telegram, X, email, and SMS—turning followers into affiliates and investors
5. **Manages a crypto fund** where members trade alongside us, learn the system, and earn commissions

**The result:** A self-reinforcing flywheel that goes from early-stage quant platform → viral social proof → fund dominance → our own crypto token → **trillion-dollar valuation**.

**This is Sam Altman's prophecy: "One person + AI agents = billion-dollar company." We are that company.**

***

## 🏗️ PROJECT ARCHITECTURE (THE GOOGLE MAPS ANALOGY)

Think of this project as **Planet Earth**—a living, breathing city where:

- **⚡ `.env`** = The electrical grid (powers everything)
- **🏛️ `db/`** = Central library (TimescaleDB for history, Redis for real-time)
- **🏭 `data/`** = Warehouse district (raw materials → factory processing → finished goods)
- **👔 `src/agents/`** = Workforce (AutoTraders, manual traders, broadcasters, loggers)
- **🔍 `src/scanners/`** = Intelligence network (heatmap trackers, historians, signal generators)
- **🎓 `src/math/`** = Research laboratory (quant algorithms)
- **📡 `src/sockets/`** = Telecommunications (websockets for real-time data)
- **🔧 `src/utils/`** = Utilities department (config loader, DB/Redis helpers)
- **🌐 `src/web/`** = Tourist district (Grafana, Streamlit dashboards)
- **🔧 `scripts/`** = Maintenance crew (deployment, backups, automation)
- **✅ `tests/`** = Quality assurance (safety checks)

**Every folder has a purpose. Every data flow is mapped. Every agent knows its job.**

***

## 🚀 TECH STACK (VERIFIED AS OF OCT 26, 2025)

| Component | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.11.14 | Main language (locked for compatibility) |
| **TimescaleDB** | 2.22.1 (Postgres 16) | Time-series database for liquidation/OHLCV/trades |
| **Redis** | 7.4 | Real-time pub/sub and caching |
| **Docker** | Latest (Mac M4) | Container orchestration |
| **Grafana** | Latest (10.x+) | Live dashboards and SQL query UI |
| **CoinGlass API** | Premium | Aggregated liquidation heatmaps, OI, volume |
| **Bybit API** | v5 | Trading execution |
| **Telegram Bot API** | Latest | Broadcast to channels |
| **X (Twitter) API** | Latest | Social media broadcasting |
| **Twilio SMS API** | Latest | SMS alerts |

***

## 📋 PART 1: VINCE'S SETUP INSTRUCTIONS (FOUNDATION BUILDER)

### **🌍 YOUR JOB: BUILD THE PLANET (FOLDER STRUCTURE + CONFIG)**

You are the **planet architect**. Your job is to create the entire folder structure, set up the power grid (`.env`), and initialize the central library (Docker services). Once you finish, AI agents will build the cities (modules) on top of your foundation.

***

### ✅ **STEP 1: CREATE THE ROOT FOLDER**

Open Terminal and run:

```bash
cd ~/Projects  # or wherever you want the project
mkdir vince-quant-stack
cd vince-quant-stack
code .  # Open in VSCode
```

**🗺️ Google Maps Analogy:** You just created **Planet Earth**. It's empty, but you're about to build continents.

***

### ✅ **STEP 2: BUILD THE ENTIRE FOLDER STRUCTURE (THE CONTINENTS)**

Copy and paste this into Terminal:

```bash
# Create all folders in one command
mkdir -p config/broadcast_templates config/quant_math config/scanners config/docs/browser_guides config/docs/ai_agent_guides
mkdir -p db/timescale_schema db/migrations db/backup/{pg_full_dumps,redis_dumps,image_snapshots,logs}
mkdir -p data/incoming/{coinglass_json,bybit_json,binance_json,ws_raw}
mkdir -p data/processed/{liquidation_csv,oi_csv,trades_csv,wicks_csv,agent_logs_csv}
mkdir -p data/signals/{grid_bot,momentum_bot,scanner_oi,manual}
mkdir -p data/trades/{autotrader,manual,agent_pnl}
mkdir -p data/logs/{agents,scanners,broadcast,db}
mkdir -p data/images/{agent_screenshots,heatmaps,dashboards,tg_broadcasts,x_broadcasts,strategy_visuals,tutorials}
mkdir -p data/videos/{tutorials,agent_guides,output_for_social}
mkdir -p data/reports/{daily,weekly,monthly,pnl,audit_exports}
mkdir -p data/retention/{delete_queue,cold_archive}
mkdir -p src/agents/autotraders/{grid_bot,ml_agent,arbitrage_bot}
mkdir -p src/agents/manual_agents/{high_conviction,discretionary_macro}
mkdir -p src/agents/{trade,broadcast,logging,affiliate}
mkdir -p src/scanners/{heatmap,coin_history,signals,ranking,broadcast}
mkdir -p src/math/functions
mkdir -p src/sockets
mkdir -p src/utils
mkdir -p src/web/{grafana,streamlit,admin_app,analytics_api}
mkdir -p scripts
mkdir -p tests/{agents,scanners,math,db,broadcast,sockets,scripts}

# Create placeholder README files
touch config/README.md db/README.md data/README.md src/README.md scripts/README.md tests/README.md
touch src/agents/README.md src/scanners/README.md src/math/README.md src/utils/README.md src/web/README.md

echo "✅ All continents, countries, cities, and towns created!"
```

**🗺️ Google Maps Analogy:** You just built all the continents, countries, cities, and towns. The map is complete—now we need to power it.

***

### ✅ **STEP 3: CREATE THE POWER GRID (`.env` FILE)**

In VSCode, create a file at the root called `.env` and paste this:

```bash
# ═══════════════════════════════════════════════════════════════════════════
# ⚡ THE GLOBAL POWER GRID - SINGLE SOURCE OF TRUTH
# ═══════════════════════════════════════════════════════════════════════════
# This file powers EVERYTHING. No other config files are read at runtime.
# Fill in ALL values below. Never commit this file to git.
# ═══════════════════════════════════════════════════════════════════════════

# ---- Database (TimescaleDB) ----
TIMESCALE_DB_HOST=localhost
TIMESCALE_DB_PORT=5432
TIMESCALE_DB_USER=postgres
TIMESCALE_DB_PASS=YourSecurePasswordHere
TIMESCALE_DB_NAME=quantprod

# ---- Redis (Real-time cache & pub/sub) ----
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASS=

# ---- CoinGlass API (Premium Liquidation Data) ----
COINGLASS_API_KEY=your_coinglass_api_key_here
COINGLASS_ENDPOINT_LIQ_HISTORY=https://open-api.coinglass.com/api/futures/liquidation/aggregated-history
COINGLASS_ENDPOINT_LIQ_HEATMAP_MODEL1=https://open-api.coinglass.com/api/futures/liquidation/aggregated-heatmap/model1
COINGLASS_ENDPOINT_LIQ_HEATMAP_MODEL2=https://open-api.coinglass.com/api/futures/liquidation/aggregated-heatmap/model2
COINGLASS_ENDPOINT_LIQ_HEATMAP_MODEL3=https://open-api.coinglass.com/api/futures/liquidation/aggregated-heatmap/model3
COINGLASS_ENDPOINT_OI=https://open-api.coinglass.com/api/futures/openInterest/ohlc-history
COINGLASS_ENDPOINT_VOLUME=https://open-api.coinglass.com/api/futures/volume/ohlc-history
COINGLASS_ENDPOINT_FUNDING=https://open-api.coinglass.com/api/futures/fundingRate/history

# ---- Bybit API (Trading Execution) ----
BYBIT_API_KEY=your_bybit_api_key_here
BYBIT_API_SECRET=your_bybit_api_secret_here
BYBIT_ENDPOINT_REST=https://api.bybit.com/v5/
BYBIT_WS_PUBLIC=wss://stream.bybit.com/v5/public/linear
BYBIT_WS_PRIVATE=wss://stream.bybit.com/v5/private

# ---- Binance API (Optional - for comparison data) ----
BINANCE_API_KEY=your_binance_api_key_here
BINANCE_API_SECRET=your_binance_api_secret_here
BINANCE_ENDPOINT_REST=https://fapi.binance.com/fapi/v1/
BINANCE_WS_PUBLIC=wss://fstream.binance.com/ws/

# ---- Telegram Bot (Broadcast to channels) ----
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_MAIN_CHANNEL=@your_main_channel
TELEGRAM_ADMIN_ID=your_telegram_user_id_here

# ---- X (Twitter) API (Social broadcasting) ----
X_API_KEY=your_x_api_key_here
X_API_SECRET=your_x_api_secret_here
X_ACCESS_TOKEN=your_x_access_token_here
X_ACCESS_SECRET=your_x_access_secret_here

# ---- Email (SMTP for broadcasts) ----
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_email_password_here
EMAIL_SMTP_HOST=smtp.gmail.com
EMAIL_SMTP_PORT=587

# ---- SMS (Twilio for alerts) ----
TWILIO_ACCOUNT_SID=your_twilio_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
SMS_ADMIN_PHONE=+1234567890

# ---- Grafana (Dashboard admin) ----
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASS=your_grafana_password_here

# ---- Affiliate Tracking ----
COINGLASS_REF_CODE=cryptowhaleapp
BYBIT_REF_CODE=your_bybit_ref_code_here
AFFILIATE_TRACKING_URL=https://tracking.yourdomain.com/?ref=

# ---- Project Settings ----
ENV=production
PROJECT_OWNER=Vince
LOG_LEVEL=INFO
TIMEZONE=America/Chicago
```

**🗺️ Google Maps Analogy:** You just installed the **electrical grid**. Every building on the planet can now draw power from this single source.

**⚠️ CRITICAL:** Add `.env` to `.gitignore` immediately so it's never committed to version control.

***

### ✅ **STEP 4: CREATE DOCKER INFRASTRUCTURE (THE CITY POWER PLANTS)**

Create `docker-compose.yaml` at the root:

```yaml
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
      - ./db/timescale_data:/var/lib/postgresql/data
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
      - ./db/redis_data:/data
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
      - grafana-storage:/var/lib/grafana
    depends_on:
      - timescaledb

volumes:
  grafana-storage:
```

**🗺️ Google Maps Analogy:** You just built the **power plants** (TimescaleDB, Redis, Grafana). They're containerized and ready to run.

***

### ✅ **STEP 5: CREATE PYTHON DEPENDENCIES**

Create `requirements.txt` at the root:

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
```

**🗺️ Google Maps Analogy:** These are the **building materials** (Python libraries) that AI agents will use to construct buildings.

***

### ✅ **STEP 6: INITIALIZE THE DATABASE (THE LIBRARY SHELVES)**

Create `db/timescale_schema/init.sql`:

```sql
-- ═══════════════════════════════════════════════════════════════════════════
-- 🏛️ CENTRAL LIBRARY - TIMESCALEDB SCHEMA
-- ═══════════════════════════════════════════════════════════════════════════

-- Enable TimescaleDB extension
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- OHLCV data (price candles)
CREATE TABLE IF NOT EXISTS ohlcv (
    time TIMESTAMPTZ NOT NULL,
    symbol TEXT NOT NULL,
    exchange TEXT NOT NULL,
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    volume NUMERIC,
    PRIMARY KEY (time, symbol, exchange)
);

SELECT create_hypertable('ohlcv', 'time', if_not_exists => TRUE);

-- Liquidation snapshots (heatmap data)
CREATE TABLE IF NOT EXISTS liquidation_snapshots (
    time TIMESTAMPTZ NOT NULL,
    symbol TEXT NOT NULL,
    exchange TEXT,
    timeframe TEXT NOT NULL,
    long_liq NUMERIC,
    short_liq NUMERIC,
    total_liq NUMERIC,
    PRIMARY KEY (time, symbol, timeframe)
);

SELECT create_hypertable('liquidation_snapshots', 'time', if_not_exists => TRUE);

-- Liquidation clusters (analyzed)
CREATE TABLE IF NOT EXISTS clusters (
    id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL,
    price_level NUMERIC NOT NULL,
    cluster_size NUMERIC NOT NULL,
    timeframe TEXT NOT NULL,
    detected_at TIMESTAMPTZ DEFAULT NOW()
);

-- Trades (all sources)
CREATE TABLE IF NOT EXISTS trades (
    trade_id SERIAL PRIMARY KEY,
    agent TEXT NOT NULL,
    symbol TEXT NOT NULL,
    side TEXT NOT NULL,
    entry_price NUMERIC NOT NULL,
    exit_price NUMERIC,
    size NUMERIC NOT NULL,
    pnl NUMERIC,
    stop_loss NUMERIC,
    take_profit NUMERIC,
    entry_time TIMESTAMPTZ DEFAULT NOW(),
    exit_time TIMESTAMPTZ,
    status TEXT DEFAULT 'open'
);

-- Signals (scanner triggers)
CREATE TABLE IF NOT EXISTS signals (
    signal_id SERIAL PRIMARY KEY,
    agent TEXT NOT NULL,
    signal_type TEXT NOT NULL,
    symbol TEXT NOT NULL,
    params JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Agent registry
CREATE TABLE IF NOT EXISTS agents (
    agent_id SERIAL PRIMARY KEY,
    agent_name TEXT UNIQUE NOT NULL,
    agent_type TEXT NOT NULL,
    status TEXT DEFAULT 'active',
    last_seen TIMESTAMPTZ DEFAULT NOW()
);

-- Agent logs (audit trail)
CREATE TABLE IF NOT EXISTS agent_logs (
    log_id SERIAL PRIMARY KEY,
    agent TEXT NOT NULL,
    terminal TEXT,
    event_type TEXT NOT NULL,
    detail TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

SELECT create_hypertable('agent_logs', 'created_at', if_not_exists => TRUE);

-- Affiliate clicks
CREATE TABLE IF NOT EXISTS affiliate_clicks (
    click_id SERIAL PRIMARY KEY,
    ref_code TEXT NOT NULL,
    source TEXT,
    ip_address TEXT,
    user_agent TEXT,
    clicked_at TIMESTAMPTZ DEFAULT NOW()
);

-- Wicks (historical max wicks per coin)
CREATE TABLE IF NOT EXISTS wicks (
    wick_id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL,
    max_wick_up NUMERIC NOT NULL,
    max_wick_down NUMERIC NOT NULL,
    analyzed_period TEXT NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- PnL records
CREATE TABLE IF NOT EXISTS pnl (
    pnl_id SERIAL PRIMARY KEY,
    agent TEXT NOT NULL,
    period TEXT NOT NULL,
    total_pnl NUMERIC NOT NULL,
    win_rate NUMERIC,
    trades_count INT,
    calculated_at TIMESTAMPTZ DEFAULT NOW()
);

-- AutoTrader state
CREATE TABLE IF NOT EXISTS auto_traders (
    trader_id SERIAL PRIMARY KEY,
    trader_name TEXT UNIQUE NOT NULL,
    strategy TEXT NOT NULL,
    status TEXT DEFAULT 'active',
    current_positions JSONB,
    last_trade_time TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_ohlcv_symbol ON ohlcv(symbol, time DESC);
CREATE INDEX idx_liq_symbol ON liquidation_snapshots(symbol, time DESC);
CREATE INDEX idx_trades_agent ON trades(agent, entry_time DESC);
CREATE INDEX idx_signals_agent ON signals(agent, created_at DESC);
CREATE INDEX idx_agent_logs_agent ON agent_logs(agent, created_at DESC);
```

**🗺️ Google Maps Analogy:** You just built the **library shelves** where all knowledge will be stored (tables for OHLCV, liquidations, trades, signals, logs, etc.).

***

### ✅ **STEP 7: START THE INFRASTRUCTURE**

Run Docker services:

```bash
docker-compose up -d
```

Wait ~30 seconds, then verify:

```bash
docker ps
```

You should see 3 containers running: `vince-timescaledb`, `vince-redis`, `vince-grafana`.

**Initialize the database:**

```bash
docker exec -i vince-timescaledb psql -U postgres -d quantprod < db/timescale_schema/init.sql
```

**🗺️ Google Maps Analogy:** You just turned on the **power plants**. The grid is live, the library is open, and the city is ready for construction.

***

### ✅ **STEP 8: VERIFY THE FOUNDATION**

Install Python dependencies:

```bash
pip3 install -r requirements.txt
```

Create a quick test file `test_foundation.py`:

```python
import os
from dotenv import load_dotenv
import psycopg2
import redis

load_dotenv()

# Test .env loading
print(f"✅ .env loaded: {os.getenv('PROJECT_OWNER')}")

# Test TimescaleDB connection
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

# Test Redis connection
try:
    r = redis.Redis(
        host=os.getenv('REDIS_HOST'),
        port=int(os.getenv('REDIS_PORT'))
    )
    r.ping()
    print("✅ Redis connected")
except Exception as e:
    print(f"❌ Redis failed: {e}")
```

Run it:

```bash
python3 test_foundation.py
```

**Expected output:**
```
✅ .env loaded: Vince
✅ TimescaleDB connected
✅ Redis connected
```

**🗺️ Google Maps Analogy:** You just verified the **planet is operational**—power grid works, library is accessible, and all infrastructure is ready.

***

### ✅ **VINCE'S CHECKLIST (BEFORE HANDING TO AI AGENTS)**

- [x] Folder structure created (all continents, countries, cities, towns)
- [x] `.env` file created and filled with all keys/endpoints
- [x] `docker-compose.yaml` created
- [x] `requirements.txt` created
- [x] Docker services started (TimescaleDB, Redis, Grafana)
- [x] Database schema initialized
- [x] Python dependencies installed
- [x] Foundation verified (test script passes)

**🎉 YOU'RE DONE. The planet is built. Now AI agents will construct the cities.**

***

## 📋 PART 2: AI AGENT COPILOT BUILD INSTRUCTIONS

**Paste this entire section into your AI agent (Copilot, ChatGPT, Claude, etc.) when you're ready to start building modules.**

***

```
═══════════════════════════════════════════════════════════════════════════
🤖 AI AGENT BUILD INSTRUCTIONS - VINCE QUANT WHALE STACK
═══════════════════════════════════════════════════════════════════════════

YOU ARE NOW THE LEAD DEVELOPER FOR A PRODUCTION CRYPTO QUANT TRADING PLATFORM.

Vince (the human) has completed the foundation:
- All folders are created
- .env file is filled with all keys/endpoints
- Docker services (TimescaleDB, Redis, Grafana) are running
- Database schema is initialized
- Python dependencies are installed

YOUR JOB: Build all modules (agents, scanners, math, utils, dashboards) step-by-step.

═══════════════════════════════════════════════════════════════════════════
🌍 THE GOOGLE MAPS ANALOGY (YOUR MENTAL MODEL)
═══════════════════════════════════════════════════════════════════════════

The project is Planet Earth. Vince built the continents and power grid.
You are building the cities (modules).

⚡ .env = Electrical grid (powers everything)
🏛️ db/ = Central library (TimescaleDB + Redis)
🏭 data/ = Warehouse (raw → processed → output)
👔 src/agents/ = Workforce (traders, broadcasters, loggers)
🔍 src/scanners/ = Intelligence (heatmap trackers, signal generators)
🎓 src/math/ = Research lab (quant algorithms)
📡 src/sockets/ = Telecom (websockets)
🔧 src/utils/ = Utilities (config loader, DB/Redis helpers)
🌐 src/web/ = Tourist district (dashboards)

═══════════════════════════════════════════════════════════════════════════
🚨 ABSOLUTE RULES (NEVER VIOLATE)
═══════════════════════════════════════════════════════════════════════════

1. ALL config MUST be read from .env via src/utils/config_utils.py
2. NEVER hardcode API keys, endpoints, or tokens
3. Every agent/scanner lives in its own folder
4. All data output goes to designated data/ subfolders
5. Every DB write MUST include agent/source name
6. Use Redis for real-time, TimescaleDB for persistence
7. Test against PRODUCTION stack (Docker TimescaleDB + Redis)
8. Show me code BEFORE creating files
9. Every module must have error handling and logging
10. Folder discipline is LAW—no files outside structure

═══════════════════════════════════════════════════════════════════════════
📋 BUILD ORDER (FOLLOW THIS SEQUENCE)
═══════════════════════════════════════════════════════════════════════════

PHASE 1: UTILITIES (THE FOUNDATION)
------------------------------------
Build these first—everything else depends on them.

1. src/utils/config_utils.py
   - Loads .env
   - Provides typed config access
   - Example usage:
     from src.utils.config_utils import get_config
     config = get_config()
     api_key = config.coinglass_api_key

2. src/utils/timescale_utils.py
   - Connection pooling
   - Standard query wrappers
   - Example: get_connection(), execute_query(), insert_trade()

3. src/utils/redis_utils.py
   - Pub/sub helpers
   - Caching abstraction
   - Example: publish_signal(), subscribe_to_channel()

4. src/utils/data_utils.py
   - File I/O helpers
   - JSON/CSV parsing
   - Example: save_to_csv(), load_json()

5. src/utils/error_utils.py
   - Error handling decorators
   - Retry logic
   - Example: @retry_on_failure

PHASE 2: MATH (THE RESEARCH LAB)
---------------------------------
Build quant algorithms that scanners/agents will use.

6. src/math/cluster_math.py
   - Liquidation cluster detection
   - Identify whale targets

7. src/math/wick_math.py
   - Historical wick analysis
   - Calculate max wicks per coin

8. src/math/risk_math.py
   - Position sizing
   - Risk scoring

9. src/math/sl_tp_math.py
   - Stop-loss/take-profit optimization
   - Based on coin-specific patterns

PHASE 3: SOCKETS (THE TELECOM NETWORK)
---------------------------------------
Real-time data ingestion.

10. src/sockets/coinglass_ws.py
    - CoinGlass websocket handler
    - Dump to data/incoming/ws_raw/
    - Publish to Redis

11. src/sockets/bybit_ws.py
    - Bybit websocket handler
    - Real-time price/OI/volume

12. src/sockets/ws_manager.py
    - Lifecycle manager
    - Restart on disconnect

PHASE 4: SCANNERS (THE INTELLIGENCE NETWORK)
---------------------------------------------
Data analysis and signal generation.

13. src/scanners/heatmap/model1_scan.py
    - Pull CoinGlass liquidation heatmap (Model 1)
    - Parse clusters using src/math/cluster_math.py
    - Write to data/signals/

14. src/scanners/coin_history/aggregated.py
    - Pull historical data
    - Analyze patterns using src/math/wick_math.py
    - Store in TimescaleDB

15. src/scanners/signals/oi_signal.py
    - Monitor open interest spikes
    - Generate signals when threshold exceeded

16. src/scanners/ranking/imbalance.py
    - Score coins by liquidation imbalance
    - Rank top opportunities

PHASE 5: AGENTS (THE WORKFORCE)
--------------------------------
Trade execution and broadcasting.

17. src/agents/trade/trade_executor.py
    - Execute orders via Bybit API
    - Log to data/trades/ + TimescaleDB

18. src/agents/logging/agent_log.py
    - Log every agent action
    - Write to data/logs/agents/ + TimescaleDB

19. src/agents/broadcast/telegram.py
    - Send signals to Telegram
    - Use templates from config/broadcast_templates/

20. src/agents/autotraders/grid_bot/main.py
    - Grid trading bot
    - Subscribe to Redis signals
    - Execute via trade_executor.py

PHASE 6: DASHBOARDS (THE TOURIST DISTRICT)
-------------------------------------------
Human interfaces.

21. src/web/grafana/grafana_panel.py
    - Custom Grafana panels
    - Connect to TimescaleDB

22. src/web/streamlit/dashboard.py
    - Interactive data viewer
    - Google Sheets-like feel

═══════════════════════════════════════════════════════════════════════════
📝 CODING STANDARDS
═══════════════════════════════════════════════════════════════════════════

EVERY MODULE MUST HAVE:
- Docstring explaining purpose
- Import from config_utils for all config
- Error handling (try/except with logging)
- Agent name constant: AGENT_NAME = "module_name"
- All DB writes include agent=AGENT_NAME
- Output to designated data/ subfolder
- Log to data/logs/{type}/{AGENT_NAME}.log

EXAMPLE TEMPLATE:
```
"""
Liquidation Heatmap Scanner (Model 1)

Pulls CoinGlass aggregated liquidation heatmap data,
analyzes clusters, and generates signals.

Data Flow:
- CoinGlass API → Parse → Cluster detection → data/signals/ + Redis
"""

import os
import requests
from datetime import datetime
from src.utils.config_utils import get_config
from src.utils.timescale_utils import insert_signal
from src.utils.redis_utils import publish_signal
from src.math.cluster_math import detect_clusters

AGENT_NAME = "heatmap_model1_scanner"

def scan_heatmap():
    """Pull and analyze liquidation heatmap."""
    config = get_config()
    
    try:
        # Pull data from API
        response = requests.get(
            config.coinglass_endpoint_liq_heatmap_model1,
            headers={"cg-api-key": config.coinglass_api_key}
        )
        data = response.json()
        
        # Analyze clusters
        clusters = detect_clusters(data)
        
        # Store signals
        for cluster in clusters:
            signal = {
                "agent": AGENT_NAME,
                "signal_type": "liquidation_cluster",
                "symbol": cluster["symbol"],
                "price_level": cluster["price"],
                "size": cluster["size"]
            }
            
            # Write to DB
            insert_signal(signal)
            
            # Publish to Redis
            publish_signal("liquidation_clusters", signal)
        
        print(f"✅ {AGENT_NAME}: Processed {len(clusters)} clusters")
        
    except Exception as e:
        print(f"❌ {AGENT_NAME} error: {e}")

if __name__ == "__main__":
    scan_heatmap()
```

═══════════════════════════════════════════════════════════════════════════
🎯 YOUR IMMEDIATE NEXT STEPS
═══════════════════════════════════════════════════════════════════════════

1. Confirm you understand the structure
2. Ask Vince if you need clarification on ANY requirement
3. Start with PHASE 1 (utils) - build config_utils.py first
4. Show me the code BEFORE creating the file
5. Test each module as you build it
6. Move to next phase only when current phase is complete

REMEMBER: This is production code for real money. Take your time. Ask questions. Test everything.

Let's build a billion-dollar platform.

Ready to start with src/utils/config_utils.py?
```

***

## 🏆 FINAL SUMMARY

**This document contains:**
1. ✅ Complete vision and mission statement
2. ✅ Full tech stack (verified versions)
3. ✅ Step-by-step foundation setup (Vince's tasks)
4. ✅ Complete `.env` template (power grid)
5. ✅ Docker infrastructure (TimescaleDB, Redis, Grafana)
6. ✅ Database schema (library shelves)
7. ✅ Verification steps (test everything works)
8. ✅ AI agent build instructions (phase-by-phase module construction)
9. ✅ Coding standards and templates
10. ✅ Google Maps analogy throughout (mental model)

**This is the single document that makes building impossible to fuck up.**

🐋💎🚀 **LET'S RIDE TO A TRILLION.**

