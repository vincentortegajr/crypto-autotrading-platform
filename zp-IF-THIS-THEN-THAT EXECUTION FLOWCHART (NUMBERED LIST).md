# 🎯 THE COMPLETE IF-THIS-THEN-THAT EXECUTION FLOWCHART (NUMBERED LIST)

**VINCE QUANT WHALE STACK - DECISION TREE VERSION**  
**Every decision point, every branch, every action—numbered sequentially**

***

## 📋 SYSTEM STARTUP SEQUENCE

### **1. System Initialization**
1. Check: Is Docker running?
   - **IF YES** → Go to step 2
   - **IF NO** → Start Docker Desktop → Wait for services to start → Go to step 2

2. Check: Are TimescaleDB, Redis, and Grafana containers running?
   - **IF YES** → Go to step 3
   - **IF NO** → Run `docker-compose up -d` → Wait 30 seconds → Verify containers are up → Go to step 3

3. Check: Does `.env` file exist with all API keys?
   - **IF YES** → Load config from `.env` → Go to step 4
   - **IF NO** → ERROR: Create `.env` file first → STOP

4. Check: Can we connect to TimescaleDB?
   - **IF YES** → Go to step 5
   - **IF NO** → ERROR: Check TimescaleDB credentials in `.env` → STOP

5. Check: Can we connect to Redis?
   - **IF YES** → Go to step 6
   - **IF NO** → ERROR: Check Redis connection settings → STOP

6. Check: Do all required database tables exist?
   - **IF YES** → Go to step 7
   - **IF NO** → Run database schema creation script → Verify tables created → Go to step 7

7. Check: Can we reach CoinGlass API?
   - **IF YES** → Go to step 8
   - **IF NO** → ERROR: Check CoinGlass API key in `.env` → STOP

8. Check: Can we reach Bybit API?
   - **IF YES** → Go to step 9
   - **IF NO** → ERROR: Check Bybit API credentials in `.env` → STOP

9. System is ready → Start background processes → Go to step 10

***

## 🔄 BACKGROUND PROCESS 1: LIQUIDATION DATA COLLECTOR

### **10. Liquidation Data Collection Loop**
10. Start Liquidation Data Collector process
11. Get list of all perpetual coins from Bybit (call API: `/v5/market/instruments-info`, category=linear)
12. Store coin list in memory (e.g., 500+ coins: BTCUSDT, ETHUSDT, SOLUSDT, etc.)
13. For each coin in list → Go to step 14

14. Set timeframes to pull: 12h, 1d, 3d, 7d, 14d, 30d, 90d, 180d, 365d
15. For each timeframe → Go to step 16

16. Call CoinGlass API: `/public/v2/liquidation_heatmap`
    - Parameters: symbol={coin}, timeframe={timeframe}
17. Check: Did API call succeed?
    - **IF YES** → Parse response → Go to step 18
    - **IF NO** → Log error → Skip this timeframe → Go back to step 15 (next timeframe)

18. Extract liquidation levels from response:
    - Each level has: price, leverage, side (long or short)
19. Store each level in TimescaleDB table `liquidation_data_raw`:
    - Columns: symbol, timeframe, price, leverage, side, fetched_at (timestamp)
20. Check: Are there more timeframes to pull for this coin?
    - **IF YES** → Go back to step 15 (next timeframe)
    - **IF NO** → Go to step 21

21. Check: Are there more coins to process?
    - **IF YES** → Go back to step 14 (next coin)
    - **IF NO** → Go to step 22

22. All coins processed → Wait 5 minutes → Go back to step 11 (start next collection cycle)

***

## 🔄 BACKGROUND PROCESS 2: OI/VOLUME/PRICE MONITOR

### **23. OI/Volume/Price Monitoring Loop**
23. Start OI/Volume/Price Monitor process
24. Get list of all perpetual coins from memory (from step 12)
25. For each coin → Go to step 26

26. Call CoinGlass API: `/public/v2/open_interest`
    - Parameters: symbol={coin}
27. Store current OI in memory as `oi_current`
28. Query TimescaleDB: Get OI from 15 minutes ago for this coin
29. Calculate: `oi_change_pct = ((oi_current - oi_15min_ago) / oi_15min_ago) × 100`

30. Call Bybit API: `/v5/market/tickers`
    - Parameters: symbol={coin}, category=linear
31. Extract: current price, 24h volume
32. Store current volume in memory as `volume_current`
33. Query TimescaleDB: Get average 5-min volume over last 1 hour for this coin
34. Calculate: `volume_spike_ratio = volume_current / volume_avg_1h`

35. Query TimescaleDB: Get price from 1 minute ago and 5 minutes ago for this coin
36. Calculate: `price_1min_change_pct = ((price_current - price_1min_ago) / price_1min_ago) × 100`
37. Calculate: `price_5min_change_pct = ((price_current - price_5min_ago) / price_5min_ago) × 100`

38. Store all data in TimescaleDB table `oi_volume_spikes`:
    - Columns: symbol, oi_change_pct, volume_spike_ratio, price_1min_change_pct, price_5min_change_pct, detected_at (timestamp)

39. Check: Is there a spike? (oi_change_pct > 3% OR volume_spike_ratio > 1.5 OR abs(price_5min_change_pct) > 2%)
    - **IF YES** → Publish spike alert to Redis channel `spike_alerts` → Trigger immediate liquidation re-fetch for this coin → Go to step 40
    - **IF NO** → Go to step 41

40. Call Liquidation Data Collector (steps 16-20) IMMEDIATELY for this coin → Go to step 41

41. Check: Are there more coins to process?
    - **IF YES** → Go back to step 26 (next coin)
    - **IF NO** → Go to step 42

42. All coins processed → Wait 1 minute → Go back to step 25 (start next monitoring cycle)

***

## 🔍 SCANNER 1: LIQUIDATION IMBALANCE CALCULATOR

### **43. Imbalance Calculation Loop**
43. Start Liquidation Imbalance Calculator process
44. Get list of all perpetual coins from memory
45. For each coin → Go to step 46

46. Get current price from TimescaleDB (latest entry in `oi_volume_spikes` table)
47. Query TimescaleDB: Get ALL liquidation data for this coin (all timeframes) from `liquidation_data_raw` where `fetched_at` is within last 5 minutes
48. Check: Is data fresh (< 5 minutes old)?
    - **IF YES** → Go to step 49
    - **IF NO** → Trigger immediate liquidation re-fetch for this coin (call steps 16-20) → Go to step 49

49. Aggregate liquidation levels:
    - Separate into two groups:
      - Group A: Shorts (liquidations ABOVE current price)
      - Group B: Longs (liquidations BELOW current price)
50. Sum total leverage for Group A → Store as `total_shorts`
51. Sum total leverage for Group B → Store as `total_longs`
52. Calculate: `total_liquidations = total_shorts + total_longs`

53. Check: Is total_liquidations > 0?
    - **IF YES** → Go to step 54
    - **IF NO** → Skip this coin (no significant liquidations) → Go to step 60

54. Calculate: `imbalance_ratio = total_shorts / total_liquidations`
55. Check: Is imbalance_ratio > 0.50?
    - **IF YES** → Set `direction = "LONG"` (whales will pump to liquidate shorts) → Go to step 56
    - **IF NO** → Check: Is imbalance_ratio < 0.50?
      - **IF YES** → Set `direction = "SHORT"` (whales will dump to liquidate longs) → Go to step 56
      - **IF NO** → Set `direction = "NEUTRAL"` (50/50 split, no clear direction) → Skip this coin → Go to step 60

56. Identify target cluster:
    - **IF direction = "LONG"** → Find largest short cluster ABOVE current price → Store as `target_price`
    - **IF direction = "SHORT"** → Find largest long cluster BELOW current price → Store as `target_price`

57. Query TimescaleDB: Get typical cluster size for this coin from `coin_thresholds` table
58. Calculate: `cluster_size_pct = (target_cluster_leverage / typical_cluster_size) × 100`

59. Store imbalance data in memory:
    - symbol, imbalance_ratio, direction, target_price, cluster_size_pct, total_shorts, total_longs

60. Check: Are there more coins to process?
    - **IF YES** → Go back to step 46 (next coin)
    - **IF NO** → Go to step 61

61. All coins processed → Proceed to Coin Ranker → Go to step 62

***

## 📊 SCANNER 2: COIN RANKER

### **62. Coin Ranking Loop**
62. Start Coin Ranker process
63. Get all coins with imbalance data from step 59
64. For each coin → Go to step 65

65. Get imbalance_ratio, cluster_size_pct from memory (step 59)
66. Query TimescaleDB: Get historical success rate for this coin from `coin_liquidation_patterns` table
    - Success rate = % of times whales hit the target cluster in past (e.g., 0.85 = 85%)
67. Check: Does historical data exist for this coin?
    - **IF YES** → Use success_rate from database → Go to step 68
    - **IF NO** → Set success_rate = 0.50 (default 50% if no history) → Go to step 68

68. Calculate combined score:
    - `score = (imbalance_ratio × 50) + (min(cluster_size_pct, 200) × 0.3) + (success_rate × 20)`
69. Store score in memory along with coin data

70. Check: Are there more coins to rank?
    - **IF YES** → Go back to step 65 (next coin)
    - **IF NO** → Go to step 71

71. Sort all coins by score (highest to lowest)
72. Take top 10 coins
73. Store top 10 in TimescaleDB table `coin_rankings`:
    - Columns: symbol, imbalance_ratio, direction, score, target_price, created_at (timestamp)
74. Publish top 10 list to Redis channel `top_coins` → Go to step 75

75. Wait 5 minutes → Go back to step 44 (start next ranking cycle)

***

## 🚨 TRIGGER MONITOR: OI/VOLUME CONFIRMATION

### **76. Trade Signal Generation Loop**
76. Start OI/Volume Trigger Monitor process
77. Subscribe to Redis channel `top_coins` (receives top 10 list from step 74)
78. When new top 10 list received → Store in memory → Go to step 79

79. For each coin in top 10 list → Go to step 80

80. Query TimescaleDB: Get latest OI/volume/price data from `oi_volume_spikes` table for this coin
81. Check OI trigger: Is oi_change_pct > 3%?
    - **IF YES** → Set `oi_triggered = TRUE` → Go to step 82
    - **IF NO** → Set `oi_triggered = FALSE` → Go to step 82

82. Check volume trigger: Is volume_spike_ratio > 1.5?
    - **IF YES** → Set `volume_triggered = TRUE` → Go to step 83
    - **IF NO** → Set `volume_triggered = FALSE` → Go to step 83

83. Check price trigger: Is abs(price_5min_change_pct) > 1%?
    - **IF YES** → Set `price_triggered = TRUE` → Go to step 84
    - **IF NO** → Set `price_triggered = FALSE` → Go to step 84

84. Check: Are ALL three triggers TRUE (oi_triggered AND volume_triggered AND price_triggered)?
    - **IF YES** → TRADE SIGNAL CONFIRMED → Go to step 85
    - **IF NO** → Skip this coin (wait for next cycle) → Go to step 87

85. Publish trade signal to Redis channel `trade_signals`:
    - Message includes: symbol, direction, target_price, imbalance_ratio, score
86. Log signal to TimescaleDB table `agent_logs`:
    - agent_name = "trigger_monitor", action = "trade_signal_generated", details = {symbol, direction, etc.}

87. Check: Are there more coins in top 10 to check?
    - **IF YES** → Go back to step 80 (next coin)
    - **IF NO** → Wait 1 minute → Go back to step 79 (monitor top 10 again)

***

## 🤖 AUTOTRADER: LIQUIDATION HUNTER V2

### **88. AutoTrader Main Loop**
88. Start AutoTrader process
89. Subscribe to Redis channel `trade_signals` (receives signals from step 85)
90. When trade signal received → Store signal data in memory → Go to step 91

91. Extract from signal: symbol, direction, target_price
92. Get current price from Bybit API: `/v5/market/tickers`
93. Query TimescaleDB: Get liquidation data for this coin from `liquidation_data_raw` table
94. Check: Is liquidation data < 5 minutes old?
    - **IF YES** → Use existing data → Go to step 96
    - **IF NO** → Trigger immediate liquidation re-fetch (call steps 16-20) → Wait for completion → Go to step 96

95. (Reserved for future use)

96. Identify target cluster:
    - **IF direction = "LONG"** → Find largest short cluster ABOVE current price
    - **IF direction = "SHORT"** → Find largest long cluster BELOW current price
97. Extract cluster data: cluster_low_price, cluster_high_price, cluster_leverage

98. Query config: What is ENTRY_STRATEGY? (conservative or aggressive)
99. Calculate entry price:
    - **IF ENTRY_STRATEGY = "conservative"**:
      - **IF direction = "LONG"** → `entry_price = cluster_low_price × 0.98` (2% below cluster)
      - **IF direction = "SHORT"** → `entry_price = cluster_high_price × 1.02` (2% above cluster)
    - **IF ENTRY_STRATEGY = "aggressive"**:
      - **IF direction = "LONG"** → `entry_price = cluster_low_price` (at cluster edge)
      - **IF direction = "SHORT"** → `entry_price = cluster_high_price` (at cluster edge)

100. Check: Is current price within entry range (±2% of calculated entry_price)?
    - **IF YES** → Proceed to trade execution → Go to step 101
    - **IF NO** → Wait for price to reach entry zone → Re-check every 30 seconds → Loop back to step 100

101. Calculate take-profit price:
    - `cluster_center = (cluster_low_price + cluster_high_price) / 2`
    - `take_profit = cluster_center × 0.995` (0.5% below center to account for whale front-running)

102. Calculate stop-loss price:
    - Query TimescaleDB: Get max historical wick distance for this coin from `coin_liquidation_patterns` table
    - **IF direction = "LONG"**:
      - `stop_loss = entry_price × (1 - max_wick_down_pct)`
      - Example: If max wick down = 8%, stop_loss = entry_price × 0.92
    - **IF direction = "SHORT"**:
      - `stop_loss = entry_price × (1 + max_wick_up_pct)`
      - Example: If max wick up = 10%, stop_loss = entry_price × 1.10

103. Calculate position size:
    - Query config: What is POSITION_SIZE_PCT? (e.g., 1% of capital per trade)
    - Get account balance from Bybit API: `/v5/account/wallet-balance`
    - `position_size_usd = account_balance × (POSITION_SIZE_PCT / 100)`
    - `qty = position_size_usd / entry_price` (quantity of coin to buy/sell)

104. Query config: What is LEVERAGE? (e.g., 10x)
105. Set leverage on Bybit: Call API `/v5/position/set-leverage` with leverage value

106. Place order on Bybit:
    - Call API: `/v5/order/create`
    - Parameters:
      - symbol = {coin}
      - side = "Buy" (if LONG) or "Sell" (if SHORT)
      - orderType = "Limit"
      - price = {entry_price}
      - qty = {qty}
      - stopLoss = {stop_loss}
      - takeProfit = {take_profit}
107. Check: Did order placement succeed?
    - **IF YES** → Store order_id from response → Go to step 108
    - **IF NO** → Log error to `agent_logs` table → Retry up to 3 times → If still fails, ABORT trade → Go back to step 90 (wait for next signal)

108. Log trade to TimescaleDB table `trades`:
    - Columns: agent_name = "liquidation_hunter_v2", symbol, side, entry_price, stop_loss, take_profit, qty, leverage, entry_time (timestamp), status = "open"
109. Broadcast signal to Telegram (call Telegram Bot API: `/sendMessage`)
    - Message format: "🚀 LONG {symbol} @ ${entry_price} | Target: ${take_profit} | SL: ${stop_loss}"
110. Broadcast signal to X/Twitter (call X API: `/2/tweets`, POST request)
    - Tweet format: "🚀 New signal: LONG {symbol} @ ${entry_price} | Target: ${take_profit}"

111. Wait for next trade signal → Go back to step 90

***

## 📡 POSITION MONITOR: TRAILING STOP-LOSS AGENT

### **112. Position Monitoring Loop**
112. Start Position Monitor Agent process
113. Query Bybit API: `/v5/position/list` → Get all open positions
114. Check: Are there any open positions?
    - **IF YES** → Store positions in memory → Go to step 115
    - **IF NO** → Wait 1 minute → Go back to step 113

115. For each open position → Go to step 116

116. Extract from position: symbol, side (Buy or Sell), entry_price, current_mark_price
117. Calculate current profit %:
    - **IF side = "Buy" (LONG)**:
      - `profit_pct = ((current_mark_price - entry_price) / entry_price) × 100`
    - **IF side = "Sell" (SHORT)**:
      - `profit_pct = ((entry_price - current_mark_price) / entry_price) × 100`

118. Check: Is profit_pct ≥ 50%?
    - **IF YES** → Move stop-loss to +30% profit lock → Go to step 119
    - **IF NO** → Go to step 120

119. Calculate new stop-loss:
    - **IF side = "Buy"** → `new_stop_loss = entry_price × 1.30` (30% above entry)
    - **IF side = "Sell"** → `new_stop_loss = entry_price × 0.70` (30% below entry)
    - Update stop-loss on Bybit: Call API `/v5/position/trading-stop`
    - Log action to `position_monitor_logs` table
    - Go to step 124

120. Check: Is profit_pct ≥ 20%?
    - **IF YES** → Move stop-loss to +10% profit lock → Go to step 121
    - **IF NO** → Go to step 122

121. Calculate new stop-loss:
    - **IF side = "Buy"** → `new_stop_loss = entry_price × 1.10` (10% above entry)
    - **IF side = "Sell"** → `new_stop_loss = entry_price × 0.90` (10% below entry)
    - Update stop-loss on Bybit: Call API `/v5/position/trading-stop`
    - Log action to `position_monitor_logs` table
    - Go to step 124

122. Check: Is profit_pct ≥ 10%?
    - **IF YES** → Move stop-loss to breakeven (0% profit lock) → Go to step 123
    - **IF NO** → No action needed → Go to step 124

123. Calculate new stop-loss:
    - `new_stop_loss = entry_price` (breakeven)
    - Update stop-loss on Bybit: Call API `/v5/position/trading-stop`
    - Log action to `position_monitor_logs` table
    - Go to step 124

124. Check: Are there more open positions to monitor?
    - **IF YES** → Go back to step 116 (next position)
    - **IF NO** → Wait 1 minute → Go back to step 113 (check for new positions)

***

## 🏁 TRADE CLOSE & PATTERN UPDATE

### **125. Trade Close Detection Loop**
125. Start Trade Close Monitor process
126. Query Bybit API: `/v5/position/list` → Get all positions
127. Query TimescaleDB: Get all trades with status = "open" from `trades` table
128. For each open trade in database → Go to step 129

129. Check: Does this trade still have an open position on Bybit?
    - **IF YES** → Trade is still open → Skip this trade → Go to step 137
    - **IF NO** → Position closed → Go to step 130

130. Query Bybit API: `/v5/execution/list` → Get execution history for this trade (to find exit price)
131. Extract exit_price from execution history
132. Calculate final PnL:
    - `pnl_pct = ((exit_price - entry_price) / entry_price) × 100` (for LONG)
    - OR `pnl_pct = ((entry_price - exit_price) / entry_price) × 100` (for SHORT)
    - `pnl_usd = (pnl_pct / 100) × position_value × leverage`

133. Update TimescaleDB `trades` table:
    - Set exit_price = {exit_price}
    - Set pnl_pct = {pnl_pct}
    - Set pnl_usd = {pnl_usd}
    - Set exit_time = NOW()
    - Set status = "closed"

134. Check: Was take-profit hit (profitable trade)?
    - **IF YES** → Increment success count for this coin/timeframe in `coin_liquidation_patterns` table → Go to step 135
    - **IF NO** → Increment failure count → Go to step 135

135. Recalculate success_rate for this coin:
    - `success_rate = success_count / (success_count + failure_count)`
    - Update `coin_liquidation_patterns` table

136. Broadcast result to Telegram and X:
    - **IF profitable** → Message: "✅ WIN: {symbol} | Entry: ${entry_price} | Exit: ${exit_price} | Profit: {pnl_pct}%"
    - **IF loss** → Message: "❌ LOSS: {symbol} | Entry: ${entry_price} | Exit: ${exit_price} | Loss: {pnl_pct}%"

137. Check: Are there more open trades to check?
    - **IF YES** → Go back to step 129 (next trade)
    - **IF NO** → Wait 1 minute → Go back to step 126 (check for newly closed trades)

***

## 🔄 ERROR HANDLING & RETRY LOGIC

### **138. API Call Error Handling**
138. **WHENEVER any API call fails** → Go to step 139

139. Check: Is this a rate limit error (HTTP 429)?
    - **IF YES** → Wait 60 seconds → Retry API call → Go to step 140
    - **IF NO** → Go to step 141

140. Check: Did retry succeed?
    - **IF YES** → Continue normal flow → Go back to wherever the API call was made
    - **IF NO** → Go to step 141

141. Check: Is this a connection timeout error?
    - **IF YES** → Wait 10 seconds → Retry API call (max 3 retries) → Go to step 142
    - **IF NO** → Go to step 143

142. Check: Did retry succeed after timeout?
    - **IF YES** → Continue normal flow
    - **IF NO** → Log error to `agent_logs` table → Skip this action → Continue

143. Check: Is this an authentication error (HTTP 401/403)?
    - **IF YES** → ERROR: Check API keys in `.env` file → Alert admin → STOP this process
    - **IF NO** → Log unknown error → Skip this action → Continue

***

## 🎯 DECISION POINTS SUMMARY

**Total numbered steps:** 143

**Key decision branches:**
- System startup: 9 checks
- Liquidation data collection: 500+ coins × 9 timeframes = 4,500+ iterations per cycle
- OI/Volume monitoring: 500+ coins × 1-minute intervals = 43,200+ checks per day
- Imbalance calculation: 500+ coins per cycle
- Coin ranking: Top 10 selected every 5 minutes
- Trade signal generation: 10 coins monitored every minute
- AutoTrader execution: Triggered by confirmed signals only
- Position monitoring: All open positions checked every minute
- Trade close detection: All open trades checked every minute

**This is your IF-THIS-THEN-THAT flowchart. Every step numbered. Every decision explicit. Impossible to misunderstand.**

🐋💎🚀 **This is the execution plan. Now build it.**

Sources
