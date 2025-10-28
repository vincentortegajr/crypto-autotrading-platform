# 📋 THE COMPLETE MASTER BLUEPRINT: NO CODE, JUST VISION, MISSION, DATA SOURCES & ASANA-STYLE CHECKLIST

**VINCE QUANT WHALE STACK - ULTIMATE REFERENCE DOCUMENT (NO CODE VERSION)**  
**Date:** October 26, 2025  
**Purpose:** Every data source, every endpoint, every decision point, every strategy—documented for perfect execution

***

## 🎯 PART 1: THE VISION (WHAT WE'RE BUILDING)

### **The Big Picture:**
A fully autonomous liquidation hunting system that:
- Scans 500+ perpetual futures coins 24/7
- Detects whale liquidation clusters before they're hunted
- Executes trades automatically with mathematical precision
- Broadcasts signals to members in real-time (Telegram, X, email, SMS)
- Scales from $100 accounts to $100M+ hedge fund capital
- Generates passive income through membership ($97/month) + fund management fees
- Becomes a billion-dollar transparent whale empire

### **The Moat (Why This Can't Be Copied):**
1. **Liquidation hunting is invisible** to 99.99% of traders (they don't know it exists)
2. **Coin-specific pattern recognition** (takes months to build historical database)
3. **Percentage-based math** (infinitely scalable from $100 to $100M)
4. **Transparency** (showing EXACTLY what we're doing = trust = viral growth)
5. **First-mover advantage** (by the time competitors realize, we have $1B AUM)

### **The Outcome:**
- Year 1: 10,000 members ($11.6M revenue), $100M fund AUM ($6M fees) = $17.6M total
- Year 2: 100,000 members ($116M revenue), $1B fund AUM ($60M fees) = $176M total
- Year 3: 1,000,000 members ($1.16B revenue), $5B+ fund AUM ($300M fees) = $1.46B+ total

***

## 🏗️ PART 2: THE TECH STACK (WHAT WE'RE USING)

### **Infrastructure:**

| Component | What It Is | Why We Use It | Where to Get It |
|-----------|-----------|---------------|-----------------|
| **Python 3.11.14** | Programming language | Best for data science, quant trading, systematic execution | https://www.python.org/downloads/ |
| **TimescaleDB 2.22** | Time-series database (Postgres 16) | Handles millions of OHLCV candles, liquidation snapshots, trades efficiently | https://www.timescale.com/ |
| **Redis 7.4** | In-memory cache + pub/sub | Real-time event broadcasting (scanner → AutoTrader communication) | https://redis.io/ |
| **Docker Desktop** | Container orchestration | Run TimescaleDB, Redis, Grafana without local installs | https://www.docker.com/products/docker-desktop |
| **Grafana 10.x** | Dashboard visualization | Live monitoring of trades, PnL, coin rankings, system health | https://grafana.com/ |

### **Data Sources & APIs:**

| Service | What Data We Get | Cost | Documentation |
|---------|-----------------|------|---------------|
| **CoinGlass API (Premium)** | Liquidation heatmaps (all timeframes: 12h → 1yr), Open Interest, Volume, Funding rates | $499/month (unlimited calls) | https://coinglass.com/en/api |
| **Bybit API v5** | Trade execution, order placement (limit, market, scaled orders), Position management, Account balance | Free (pay trading fees) | https://bybit-exchange.github.io/docs/v5/intro |
| **Telegram Bot API** | Send signals to channel/group, Inline buttons for member actions | Free | https://core.telegram.org/bots/api |
| **X (Twitter) API v2** | Post signals, Reply to mentions, Auto-engage community | $100/month (Basic tier) | https://developer.twitter.com/en/docs/twitter-api |
| **SendGrid (Email)** | Send daily digest to 2M email list | $89.95/month (100k emails) | https://sendgrid.com/pricing/ |
| **Twilio (SMS)** | Send high-conviction signals to 100k SMS list | Pay-per-message (~$0.0075/SMS) | https://www.twilio.com/sms/pricing |

***

## 📊 PART 3: DATA WE'RE PULLING (WHAT, WHERE, HOW OFTEN)

### **A. Liquidation Data (from CoinGlass)**

**What:** Liquidation heatmaps showing long/short positions at each price level

**Timeframes:** 12h, 1d, 3d, 7d, 14d, 30d, 90d, 180d, 365d (pull ALL available)

**How Often:** 
- Background refresh: Every 5 minutes for ALL coins
- Spike-triggered refresh: Immediate if price/OI/volume spikes > X%
- Pre-trade validation: Re-fetch if data > 5 minutes old before executing trade

**Endpoint:** `https://open-api.coinglass.com/public/v2/liquidation_heatmap`

**Parameters:**
- `symbol` (e.g., "BTCUSDT")
- `timeframe` (e.g., "7d", "30d")
- `exchange` (e.g., "Binance", "Bybit", "All")

**Response Format:**
```json
{
  "code": "0",
  "data": {
    "levels": [
      {
        "price": 116307.4,
        "leverage": 239030000,
        "side": "short"
      },
      {
        "price": 110000.0,
        "leverage": 150000000,
        "side": "long"
      }
    ]
  }
}
```

**What We Do With It:**
- Store in `liquidation_data_raw` table (TimescaleDB)
- Aggregate across all timeframes to identify dominant clusters
- Calculate imbalance (shorts above vs. longs below current price)
- Identify target prices (where whales will hunt next)

***

### **B. Open Interest Data (from CoinGlass)**

**What:** Total value of all open long/short positions for each coin

**How Often:** Every 1 minute (real-time monitoring)

**Endpoint:** `https://open-api.coinglass.com/public/v2/open_interest`

**Parameters:**
- `symbol` (e.g., "BTCUSDT")
- `exchange` (optional - "All" for aggregated)

**Response Format:**
```json
{
  "code": "0",
  "data": {
    "symbol": "BTCUSDT",
    "open_interest": 12500000000,
    "timestamp": 1730000000
  }
}
```

**What We Track:**
- OI change % over 15 minutes (e.g., +3-5% = whale accumulation)
- OI spike = trigger for trade entry (confirms liquidation hunt is starting)

***

### **C. Volume Data (from CoinGlass or Bybit)**

**What:** Trading volume (spot + futures) for each coin

**How Often:** Every 1 minute

**Endpoint (CoinGlass):** `https://open-api.coinglass.com/public/v2/volume`

**Endpoint (Bybit):** `https://api.bybit.com/v5/market/tickers` (Category: linear)

**What We Track:**
- 5-minute volume vs. 1-hour average
- Volume spike ratio (e.g., 1.5-2x = whales moving)
- Combined with OI spike = high-confidence entry signal

***

### **D. Price Data (from Bybit)**

**What:** Real-time price (mark price, last traded price, 24h high/low)

**How Often:** Every 1 second (websocket) or every 10 seconds (REST API)

**Endpoint (REST):** `https://api.bybit.com/v5/market/tickers`

**Endpoint (Websocket):** `wss://stream.bybit.com/v5/public/linear`

**What We Track:**
- 1-minute price change % (fast movers)
- 5-minute price change % (momentum confirmation)
- Price proximity to liquidation clusters (are we near a hunt?)

***

### **E. Historical OHLCV Data (from Bybit)**

**What:** Candlestick data (Open, High, Low, Close, Volume) for backtesting and wick analysis

**How Often:** One-time historical pull (1 year of data), then update every 15 minutes

**Endpoint:** `https://api.bybit.com/v5/market/kline`

**Parameters:**
- `symbol` (e.g., "BTCUSDT")
- `interval` (e.g., "5", "15", "60", "D" = 5min, 15min, 1h, 1d)
- `limit` (max 1000 candles per request)

**What We Use It For:**
- Calculate historical wick distances (for stop-loss placement)
- Identify typical price ranges for each coin
- Backtest strategies (win rate, drawdowns)

***

## 🎯 PART 4: THE DATA FLOW (STEP-BY-STEP)

### **Step 1: Data Collection (Background Processes - Always Running)**

**Process A: Liquidation Data Collector**
- Runs every 5 minutes
- Pulls liquidation heatmaps for ALL coins (500+)
- For each coin, pulls ALL timeframes (12h → 1yr)
- Stores in `liquidation_data_raw` table

**Process B: OI/Volume/Price Monitor**
- Runs every 1 minute
- Pulls OI, volume, price for ALL coins
- Calculates 15-min OI change, 5-min volume spike, 1-min price change
- Stores in `oi_volume_spikes` table

**Process C: Spike-Triggered Refresh**
- Monitors `oi_volume_spikes` table
- If ANY coin has price spike > 2%, OI spike > 3%, or volume spike > 1.5x
- **Immediately re-fetch liquidation data for that coin**
- Updates `liquidation_data_raw` table with fresh data

***

### **Step 2: Data Aggregation & Ranking**

**Process D: Liquidation Imbalance Calculator**
- Runs every 5 minutes (or on-demand when spike detected)
- For each coin:
  - Aggregate liquidation data across all timeframes
  - Sum shorts above current price
  - Sum longs below current price
  - Calculate imbalance ratio (shorts / (shorts + longs))
  - Identify target cluster (largest cluster in direction of imbalance)

**Process E: Coin Ranker**
- Runs every 5 minutes
- For each coin:
  - Get imbalance ratio (from Process D)
  - Get cluster size as % of typical cluster (from historical data)
  - Get historical success rate (% of time whales hit this cluster)
  - Calculate combined score: (imbalance × 50%) + (cluster size % × 30%) + (success rate × 20%)
- Rank all coins by score
- Store top 10 in `coin_rankings` table

***

### **Step 3: Trade Signal Generation**

**Process F: OI/Volume Trigger Monitor**
- Monitors top 10 ranked coins (from `coin_rankings` table)
- For each coin, checks:
  - OI change in last 15 min > 3-5%?
  - Volume spike (5-min vs. 1-hour avg) > 1.5-2x?
  - Price movement in last 5 min > 1%?
- If ALL three conditions met → **TRADE SIGNAL GENERATED**
- Publishes signal to Redis pub/sub channel

***

### **Step 4: Trade Execution (AutoTrader)**

**Process G: AutoTrader (Liquidation Hunter v2)**
- Subscribes to Redis pub/sub channel
- When signal received:
  - Validate: Is liquidation data < 5 minutes old? (If not, re-fetch)
  - Calculate entry price (conservative: after cluster, or aggressive: in cluster)
  - Calculate stop-loss (based on historical wick distance + cluster proximity)
  - Calculate take-profit (center of target cluster)
  - Execute trade via Bybit API
  - Log trade to `trades` table (with `agent_name = "liquidation_hunter_v2"`)
  - Broadcast signal to Telegram/X

***

### **Step 5: Position Monitoring (Trailing Stop-Loss)**

**Process H: Position Monitor Agent**
- Runs every 1 minute
- Gets all open positions from Bybit API
- For each position:
  - Calculate current profit %
  - If profit > 10% → Move stop-loss to breakeven
  - If profit > 20% → Move stop-loss to +10% profit lock
  - If profit > 50% → Move stop-loss to +30% profit lock
  - Update stop-loss via Bybit API
  - Log action to `position_monitor_logs` table

***

### **Step 6: Trade Close & Historical Update**

**Process I: Trade Closer & Pattern Updater**
- When position closes (take-profit hit, stop-loss hit, or manual close):
  - Calculate final PnL (% and $)
  - Update `trades` table with exit data
  - Update `coin_liquidation_patterns` table:
    - If take-profit hit → Increment success count for this coin/timeframe
    - If stop-loss hit → Increment failure count
    - Recalculate success rate
  - Broadcast result to Telegram/X (win or loss)

***

## 🧮 PART 5: THE MATHEMATICAL LOGIC (NO CODE, JUST FORMULAS)

### **A. Liquidation Imbalance Formula**

**Given:**
- Current price = $115,000
- Shorts above (liquidations at $116k-$130k) = $500M total leverage
- Longs below (liquidations at $110k-$114k) = $200M total leverage

**Calculate:**
- Total liquidations = $500M + $200M = $700M
- Imbalance ratio = $500M / $700M = 0.714 (71.4% shorts)

**Interpretation:**
- 71.4% shorts above = Whales will pump to liquidate shorts (go LONG)
- Target: Find largest short cluster (e.g., $116.3k with $239M leverage)

***

### **B. Cluster Size Percentage Formula**

**Given:**
- Current cluster size = $239M (shorts at $116.3k)
- Typical cluster size for BTC (from historical data) = $150M

**Calculate:**
- Cluster size % = ($239M / $150M) × 100 = 159%

**Interpretation:**
- 159% of typical cluster = LARGE cluster (high priority for whales)
- This increases the coin's ranking score

***

### **C. Combined Ranking Score Formula**

**Given:**
- Imbalance ratio = 0.714 (71.4% shorts)
- Cluster size % = 159%
- Historical success rate = 85% (whales hit this cluster 85% of the time in past)

**Calculate:**
- Score = (0.714 × 50) + (min(159, 200) × 0.3) + (0.85 × 20)
- Score = 35.7 + 47.7 + 17 = **100.4 out of 120**

**Interpretation:**
- Score > 90 = High-confidence setup
- Trade this coin when OI/volume trigger confirms

***

### **D. Entry Price Calculation**

**Conservative Strategy (Wait for Pullback):**
- Cluster low = $116,000
- Entry price = Cluster low × 0.98 = $113,680 (2% below cluster)

**Aggressive Strategy (Enter in Cluster):**
- Cluster low = $116,000
- Entry price = Cluster low = $116,000 (enter at cluster edge)

***

### **E. Stop-Loss Calculation**

**Based on Historical Wick Distance:**
- Historical max wick down for BTC = 8% (from OHLCV analysis)
- Entry price = $113,680
- Stop-loss = Entry × (1 - 0.08) = $104,585 (8% below entry)

**Based on Liquidation Cluster Below:**
- Next long cluster below = $110,000 (with $150M leverage)
- Stop-loss = $110,000 × 0.98 = $107,800 (2% below next cluster)

**Choose the more conservative (wider) of the two.**

***

### **F. Take-Profit Calculation**

**Target Cluster:**
- Cluster range = $116,000 - $117,000
- Cluster center = ($116,000 + $117,000) / 2 = $116,500

**Account for Whale Front-Running:**
- Take-profit = Cluster center × 0.995 = $115,917 (0.5% below center)

**Why:** Whales often short BEFORE hitting the exact cluster top (front-run retail FOMO)

***

## 📋 PART 6: THE ASANA-STYLE CHECKLIST (WHAT TO BUILD, IN ORDER)

### **PHASE 1: FOUNDATION (WEEK 1-2)**

#### **1.1 Environment Setup**
- [ ] Install Python 3.11.14
- [ ] Install Docker Desktop
- [ ] Create project folder: `vince-quant-whale-stack/`
- [ ] Create `.env` file with ALL API keys (CoinGlass, Bybit, Telegram, X, SendGrid, Twilio)
- [ ] Create `docker-compose.yml` for TimescaleDB, Redis, Grafana
- [ ] Run `docker-compose up -d` to start services
- [ ] Verify TimescaleDB connection (Postgres port 5432)
- [ ] Verify Redis connection (port 6379)
- [ ] Verify Grafana UI (http://localhost:3000)

#### **1.2 Folder Structure Creation**
- [ ] Create root folders: `src/`, `data/`, `db/`, `config/`, `logs/`
- [ ] Create `src/` subfolders: `utils/`, `math/`, `sockets/`, `scanners/`, `agents/`
- [ ] Create `data/` subfolders: `incoming/`, `signals/`, `trades/`, `logs/`
- [ ] Create `db/` subfolders: `timescale_schema/`, `redis_keys/`
- [ ] Create `config/` files: `AGENT_MEMORY.md`, `PRD.md`, `README.md`

#### **1.3 Database Schema Creation**
- [ ] Create TimescaleDB tables:
  - [ ] `liquidation_data_raw` (all liquidation heatmap data)
  - [ ] `oi_volume_spikes` (OI/volume/price tracking)
  - [ ] `coin_thresholds` (min cluster size per coin)
  - [ ] `coin_liquidation_patterns` (historical success rates)
  - [ ] `coin_rankings` (top 10 coins by score)
  - [ ] `trades` (all executed trades)
  - [ ] `position_monitor_logs` (trailing stop-loss actions)
  - [ ] `agent_logs` (audit trail for all agents)
- [ ] Create TimescaleDB hypertables (convert tables to time-series)
- [ ] Create indexes on `symbol`, `timeframe`, `detected_at` columns

#### **1.4 Utility Functions (Core Infrastructure)**
- [ ] Build `src/utils/config_utils.py` (loads `.env` file, provides config to all agents)
- [ ] Build `src/utils/timescale_utils.py` (connects to TimescaleDB, executes queries)
- [ ] Build `src/utils/redis_utils.py` (connects to Redis, pub/sub helper functions)
- [ ] Build `src/utils/data_utils.py` (JSON parsing, file I/O helpers)
- [ ] Build `src/utils/error_utils.py` (error logging, retry logic)
- [ ] Test: Can agents import config and connect to DB/Redis?

***

### **PHASE 2: DATA COLLECTION (WEEK 3-4)**

#### **2.1 CoinGlass API Integration**
- [ ] Sign up for CoinGlass Premium ($499/month)
- [ ] Get API key, add to `.env` as `COINGLASS_API_KEY`
- [ ] Test liquidation heatmap endpoint manually (Postman or `curl`)
- [ ] Test OI endpoint
- [ ] Test volume endpoint
- [ ] Document rate limits (unlimited for Premium, but verify)

#### **2.2 Bybit API Integration**
- [ ] Create Bybit account (if not already)
- [ ] Generate API key (with trading permissions)
- [ ] Add to `.env` as `BYBIT_API_KEY` and `BYBIT_API_SECRET`
- [ ] Test price ticker endpoint
- [ ] Test order placement endpoint (start with testnet: `https://api-testnet.bybit.com`)
- [ ] Test scaled order endpoint (confirm it exists and works)
- [ ] Switch to mainnet when ready

#### **2.3 Websocket Handlers**
- [ ] Build `src/sockets/coinglass_ws.py` (websocket for real-time liquidation updates, if available)
- [ ] Build `src/sockets/bybit_ws.py` (websocket for real-time price/OI updates)
- [ ] Build `src/sockets/ws_manager.py` (manages multiple websocket connections)
- [ ] Test: Do websockets stay connected? Do they reconnect on disconnect?

#### **2.4 Background Data Collectors**
- [ ] Build Liquidation Data Collector:
  - [ ] Pulls ALL timeframes (12h → 1yr) for ALL coins every 5 minutes
  - [ ] Stores in `liquidation_data_raw` table
- [ ] Build OI/Volume/Price Monitor:
  - [ ] Pulls OI, volume, price every 1 minute for ALL coins
  - [ ] Calculates 15-min OI change, 5-min volume spike, 1-min price change
  - [ ] Stores in `oi_volume_spikes` table
- [ ] Build Spike-Triggered Refresh:
  - [ ] Monitors `oi_volume_spikes` table
  - [ ] If spike detected → immediately re-fetch liquidation data for that coin
- [ ] Test: Is data being collected and stored correctly?

***

### **PHASE 3: SCANNERS & RANKING (WEEK 5-6)**

#### **3.1 Math Functions**
- [ ] Build `src/math/cluster_math.py`:
  - [ ] Detect liquidation clusters (group nearby liquidations)
  - [ ] Calculate imbalance ratio (shorts vs. longs)
  - [ ] Identify target cluster (largest in direction of imbalance)
- [ ] Build `src/math/wick_math.py`:
  - [ ] Analyze historical OHLCV data
  - [ ] Calculate max wick up/down % for each coin
  - [ ] Store in `coin_liquidation_patterns` table
- [ ] Build `src/math/risk_math.py`:
  - [ ] Calculate position size (% of capital)
  - [ ] Calculate leverage (based on volatility)
- [ ] Test: Do math functions return correct values?

#### **3.2 Liquidation Imbalance Calculator**
- [ ] Build scanner that:
  - [ ] Reads liquidation data from `liquidation_data_raw` table
  - [ ] Aggregates across all timeframes
  - [ ] Calculates imbalance for each coin
  - [ ] Identifies target cluster
  - [ ] Stores results in temporary table or JSON
- [ ] Test: Does it correctly identify top imbalanced coins?

#### **3.3 Coin Ranker**
- [ ] Build ranker that:
  - [ ] Gets imbalance data (from step 3.2)
  - [ ] Gets cluster size as % of typical (from `coin_thresholds` table)
  - [ ] Gets historical success rate (from `coin_liquidation_patterns` table)
  - [ ] Calculates combined score
  - [ ] Ranks all coins
  - [ ] Stores top 10 in `coin_rankings` table
- [ ] Test: Are top 10 coins the ones with obvious setups?

#### **3.4 Fast Price Mover Scanner**
- [ ] Build scanner that:
  - [ ] Monitors 1-min and 5-min price changes
  - [ ] If price spike > 2% (1-min) or > 5% (5-min) → trigger liquidation re-fetch
  - [ ] Stores fast movers in `fast_price_movers` table
- [ ] Test: Does it catch sudden pumps/dumps?

***

### **PHASE 4: AUTOTRADER (WEEK 7-8)**

#### **4.1 Trade Executor**
- [ ] Build `src/agents/trade/trade_executor.py`:
  - [ ] Connects to Bybit API
  - [ ] Places limit orders
  - [ ] Places market orders
  - [ ] Places scaled orders (if using)
  - [ ] Sets stop-loss and take-profit
- [ ] Build `src/agents/trade/trade_manager.py`:
  - [ ] Tracks open positions
  - [ ] Queries Bybit API for position status
  - [ ] Updates local `trades` table
- [ ] Test: Can it place orders on Bybit testnet?

#### **4.2 Entry/Exit Logic**
- [ ] Build `src/math/sl_tp_math.py`:
  - [ ] Calculates entry price (conservative vs. aggressive strategy)
  - [ ] Calculates stop-loss (based on wick math + cluster proximity)
  - [ ] Calculates take-profit (center of target cluster, adjusted for front-running)
- [ ] Test: Are stop-loss/take-profit levels sensible?

#### **4.3 AutoTrader Main Loop**
- [ ] Build `src/agents/autotraders/liquidation_hunter_v2/main.py`:
  - [ ] Subscribes to Redis pub/sub for trade signals
  - [ ] When signal received:
    - [ ] Validates liquidation data freshness
    - [ ] Calculates entry/SL/TP
    - [ ] Executes trade
    - [ ] Logs to `trades` table
    - [ ] Broadcasts signal
- [ ] Test: Does it execute trades when signals are published?

***

### **PHASE 5: POSITION MONITORING (WEEK 9)**

#### **5.1 Trailing Stop-Loss Agent**
- [ ] Build `src/agents/position_monitor/trailing_stop_agent.py`:
  - [ ] Monitors all open positions every 1 minute
  - [ ] Calculates current profit %
  - [ ] If profit > 10% → Move SL to breakeven
  - [ ] If profit > 20% → Move SL to +10%
  - [ ] If profit > 50% → Move SL to +30%
  - [ ] Updates SL via Bybit API
  - [ ] Logs actions to `position_monitor_logs` table
- [ ] Test: Does it correctly move stop-losses?

***

### **PHASE 6: BROADCASTING (WEEK 10)**

#### **6.1 Telegram Bot**
- [ ] Create Telegram bot (via @BotFather)
- [ ] Get bot token, add to `.env` as `TELEGRAM_BOT_TOKEN`
- [ ] Create channel/group for signals
- [ ] Build `src/agents/broadcast/telegram.py`:
  - [ ] Sends signal messages (entry, exit, SL/TP updates)
  - [ ] Formats messages with emoji, readability
- [ ] Test: Do messages appear in channel?

#### **6.2 X (Twitter) Bot**
- [ ] Apply for X API access ($100/month Basic tier)
- [ ] Get API key, add to `.env` as `X_API_KEY`
- [ ] Build `src/agents/broadcast/x.py`:
  - [ ] Posts signals to Twitter
  - [ ] Auto-replies to mentions (optional)
- [ ] Test: Do tweets post correctly?

#### **6.3 Email/SMS**
- [ ] Sign up for SendGrid ($89.95/month for 100k emails)
- [ ] Get API key, add to `.env` as `SENDGRID_API_KEY`
- [ ] Build `src/agents/broadcast/email.py`:
  - [ ] Sends daily digest to email list
- [ ] Sign up for Twilio (pay-per-SMS)
- [ ] Get API credentials, add to `.env`
- [ ] Build `src/agents/broadcast/sms.py`:
  - [ ] Sends high-conviction signals to SMS list
- [ ] Test: Do emails/SMS send?

***

### **PHASE 7: MONITORING & DASHBOARDS (WEEK 11)**

#### **7.1 Grafana Dashboards**
- [ ] Log into Grafana (http://localhost:3000)
- [ ] Add TimescaleDB as data source
- [ ] Create dashboard panels:
  - [ ] Live PnL (total, daily, weekly)
  - [ ] Win rate (% of trades profitable)
  - [ ] Top 10 ranked coins (updated every 5 min)
  - [ ] OI/volume spike alerts
  - [ ] Open positions (current trades)
  - [ ] Agent logs (last 100 actions)
- [ ] Test: Do dashboards update in real-time?

***

### **PHASE 8: BACKTESTING & OPTIMIZATION (WEEK 12)**

#### **8.1 Historical Simulation**
- [ ] Pull 1 year of historical liquidation data (if available from CoinGlass)
- [ ] Pull 1 year of OHLCV data (from Bybit)
- [ ] Build backtester:
  - [ ] Simulates AutoTrader logic on historical data
  - [ ] Calculates win rate, PnL, max drawdown
  - [ ] Tests different parameters (imbalance threshold, cluster size %, SL/TP distances)
- [ ] Optimize parameters based on backtest results

#### **8.2 Paper Trading**
- [ ] Run AutoTrader on Bybit testnet for 1-2 weeks
- [ ] Track performance (win rate, PnL, drawdowns)
- [ ] Compare to live trades you're doing manually
- [ ] Adjust parameters if needed

#### **8.3 Go Live**
- [ ] Switch AutoTrader to mainnet
- [ ] Start with small capital ($100-$1,000 per trade)
- [ ] Monitor closely for first 1-2 weeks
- [ ] Scale up capital as confidence grows

***

## 🎯 PART 7: TRADE EXECUTION STRATEGIES (DETAILED)

### **Strategy A: Conservative (Wait for Pullback)**

**When to Use:**
- Small capital ($1k-$10k)
- High-volatility coins
- Low confidence in timing

**Entry Logic:**
- Wait for price to pull back BELOW long cluster (or ABOVE short cluster)
- Example: Cluster at $116k, enter at $113.5k (after dip)

**Risk:**
- Might miss entry if coin pumps straight to cluster
- Need patience

**Reward:**
- Better average entry price
- Higher profit if it works

***

### **Strategy B: Aggressive (Enter in Cluster)**

**When to Use:**
- Medium-large capital ($10k+)
- Low-volatility coins (BTC, ETH)
- High confidence in setup (90%+ historical success)

**Entry Logic:**
- Enter as soon as price enters cluster zone
- Example: Cluster at $116k-$117k, enter at $116k

**Risk:**
- Might get stopped out if whales fake-pump then reverse

**Reward:**
- Never miss an entry
- Catch moves faster

***

### **Strategy C: Scaled Entries (Hedge Fund)**

**When to Use:**
- Large capital ($100k+)
- Any coin (BTC, ETH, alt coins)
- Want to eliminate stop-out risk

**Entry Logic:**
- Place 10-20 orders from current price down to X% below cluster
- Double size on each order (or use Bybit's auto-scaling)
- Example: $116k → $110k range, 10 orders, sizes: $100, $200, $400, $800...

**Risk:**
- Locks up margin (can't use for other trades)
- If coin goes opposite direction forever, big loss (rare on liquidation setups)

**Reward:**
- Never get stopped out
- Average entry improves if coin dips first
- Can make money on BOTH sides (long on way up, short on way down)

***

## 📊 PART 8: PERFORMANCE METRICS (WHAT TO TRACK)

### **A. Trade-Level Metrics**

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| **Win Rate** | % of trades that hit take-profit | 65-80% |
| **Average Win** | Average profit % on winning trades | 10-50% |
| **Average Loss** | Average loss % on losing trades | 5-10% |
| **Risk:Reward Ratio** | Avg win / avg loss | 2:1 or higher |
| **Max Drawdown** | Largest peak-to-trough decline in account | < 20% |

### **B. System-Level Metrics**

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| **Trades per Day** | How many trades AutoTrader executes | 10-50 (small perps), 1-5 (BTC/ETH) |
| **Signals Generated** | How many coins flagged by ranker | 50-100/day |
| **OI Triggers** | How many signals confirmed by OI/volume spike | 10-30/day |
| **Data Freshness** | Average age of liquidation data when trade executes | < 5 minutes |
| **Uptime** | % of time system is running without errors | 99%+ |

### **C. Business Metrics**

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| **Members** | Total paying subscribers | 10k (Yr 1), 100k (Yr 2), 1M (Yr 3) |
| **MRR** | Monthly recurring revenue from memberships | $970k (Yr 1), $9.7M (Yr 2), $97M (Yr 3) |
| **Fund AUM** | Total capital in hedge fund | $100M (Yr 1), $1B (Yr 2), $5B+ (Yr 3) |
| **Fund Performance** | Annual return % | 50-200%+ |
| **Affiliate Revenue** | Commissions paid to members | 50% of MRR |

***

## 🏆 PART 9: SUCCESS CRITERIA (HOW WE KNOW IT'S WORKING)

### **Week 1-2 (Foundation):**
- [ ] Docker services running (TimescaleDB, Redis, Grafana accessible)
- [ ] Database schema created (all tables exist)
- [ ] `.env` file complete (all API keys added)
- [ ] Folder structure matches plan

### **Week 3-4 (Data Collection):**
- [ ] Liquidation data being collected every 5 minutes for all coins
- [ ] OI/volume/price data being collected every 1 minute
- [ ] Spike-triggered refresh working (liquidation data updates when price spikes)
- [ ] Data visible in TimescaleDB (query tables and see rows)

### **Week 5-6 (Scanners):**
- [ ] Imbalance calculator correctly identifies top imbalanced coins
- [ ] Coin ranker produces top 10 list
- [ ] Top 10 list matches your manual analysis (spot-check 3-5 coins)

### **Week 7-8 (AutoTrader):**
- [ ] AutoTrader executes trades on testnet
- [ ] Stop-loss and take-profit orders placed correctly
- [ ] Trades logged to database with correct data
- [ ] Signals broadcast to Telegram

### **Week 9 (Position Monitor):**
- [ ] Trailing stop-loss agent moves SL when profit > 10%
- [ ] Position monitor logs visible in database

### **Week 10 (Broadcasting):**
- [ ] Telegram signals sending in real-time
- [ ] X (Twitter) posts working
- [ ] Email/SMS sending (if implemented)

### **Week 11 (Dashboards):**
- [ ] Grafana dashboards showing live data
- [ ] Can see PnL, win rate, open positions

### **Week 12 (Backtesting & Go Live):**
- [ ] Backtest shows 65-80% win rate (or better)
- [ ] Paper trading (testnet) shows consistent profits
- [ ] AutoTrader live on mainnet, executing real trades
- [ ] First week of live trading: Positive PnL

***

## 🚨 CRITICAL RULES (NEVER VIOLATE)

### **1. Python Only**
- No JavaScript, ever
- If it's not Python, delete it

### **2. Single `.env` File**
- All keys, endpoints, tokens in ONE place
- Agents ALWAYS import via `config_utils.py`

### **3. Percentage-Based Math**
- Stop-loss: 5-10% (not $5,000)
- Position size: 1% of capital (not "$100")
- Infinitely scalable

### **4. Database-First**
- Every data point gets its own table FIRST
- Test, verify, THEN combine

### **5. Pull ALL Timeframes**
- 12h → 1yr (not just 7d/14d/30d)
- Aggregate to find which timeframes matter per coin

### **6. No Trading BTC/ETH with AutoTrader (Optional Rule)**
- Too slow (30+ day moves)
- Focus on small perp coins (12h-7d moves, 20-500% gains)
- Exception: Can trade BTC/ETH if using scaled entries with large capital

### **7. Every Trade Logged**
- Agent name, symbol, entry, exit, PnL%, SL, TP
- Audit trail for everything

### **8. Show Before Creating**
- Agents show you code/plan FIRST
- No surprise files

***

## 💎 THE FINAL TRUTH

**This document is the single source of truth.**

No code. Just vision, mission, data sources, endpoints, formulas, strategies, and checklists.

Every AI agent, every developer, every team member can reference this and know EXACTLY what to build.

🐋💎🚀 **Now you have the perfect blueprint. Time to execute.**

Sources
