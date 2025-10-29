-- Core TimescaleDB schema for Vince Quant Whale Stack (perps foundation)
-- Creates base tables with composite primary keys so hypertables can be created cleanly.

CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE TABLE IF NOT EXISTS ohlcv (
    symbol TEXT NOT NULL,
    timeframe TEXT NOT NULL,
    time TIMESTAMPTZ NOT NULL,
    open NUMERIC NOT NULL,
    high NUMERIC NOT NULL,
    low NUMERIC NOT NULL,
    close NUMERIC NOT NULL,
    volume NUMERIC NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (symbol, timeframe, time)
);
SELECT create_hypertable('ohlcv', 'time', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS liquidation_snapshots (
    symbol TEXT NOT NULL,
    timeframe TEXT NOT NULL,
    price NUMERIC NOT NULL,
    long_liq NUMERIC NOT NULL,
    short_liq NUMERIC NOT NULL,
    cluster_score NUMERIC,
    heatmap_model TEXT,
    time TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (symbol, timeframe, time)
);
SELECT create_hypertable('liquidation_snapshots', 'time', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS liquidation_data_raw (
    symbol TEXT NOT NULL,
    timeframe TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    y_axis JSONB NOT NULL,
    liquidation_data JSONB NOT NULL,
    candles JSONB NOT NULL,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (symbol, timeframe, timestamp)
);
SELECT create_hypertable('liquidation_data_raw', 'timestamp', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS open_interest (
    symbol TEXT NOT NULL,
    timeframe TEXT NOT NULL,
    oi NUMERIC NOT NULL,
    volume NUMERIC,
    funding_rate NUMERIC,
    time TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (symbol, timeframe, time)
);
SELECT create_hypertable('open_interest', 'time', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS trades (
    trade_id BIGSERIAL,
    agent TEXT NOT NULL,
    symbol TEXT NOT NULL,
    direction TEXT NOT NULL,
    size NUMERIC NOT NULL,
    entry_price NUMERIC NOT NULL,
    exit_price NUMERIC,
    pnl NUMERIC,
    status TEXT DEFAULT 'open',
    entry_time TIMESTAMPTZ NOT NULL,
    exit_time TIMESTAMPTZ,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (trade_id, entry_time)
);
SELECT create_hypertable('trades', 'entry_time', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS signals (
    signal_id BIGSERIAL,
    agent TEXT NOT NULL,
    symbol TEXT,
    signal_type TEXT NOT NULL,
    confidence NUMERIC,
    payload JSONB,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (signal_id, created_at)
);
SELECT create_hypertable('signals', 'created_at', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS agent_logs (
    log_id BIGSERIAL,
    agent TEXT NOT NULL,
    event_type TEXT NOT NULL,
    detail TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (log_id, created_at)
);
SELECT create_hypertable('agent_logs', 'created_at', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS affiliate_clicks (
    click_id BIGSERIAL PRIMARY KEY,
    ref_code TEXT NOT NULL,
    source TEXT,
    ip_address TEXT,
    user_agent TEXT,
    clicked_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS wicks (
    symbol TEXT NOT NULL,
    analyzed_period TEXT NOT NULL,
    max_wick_up NUMERIC NOT NULL,
    max_wick_down NUMERIC NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (symbol, analyzed_period, updated_at)
);
SELECT create_hypertable('wicks', 'updated_at', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS pnl (
    pnl_id BIGSERIAL,
    agent TEXT NOT NULL,
    period TEXT NOT NULL,
    total_pnl NUMERIC NOT NULL,
    win_rate NUMERIC,
    trades_count INT,
    calculated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (pnl_id, calculated_at)
);
SELECT create_hypertable('pnl', 'calculated_at', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS auto_traders (
    trader_id BIGSERIAL PRIMARY KEY,
    trader_name TEXT UNIQUE NOT NULL,
    strategy TEXT NOT NULL,
    status TEXT DEFAULT 'active',
    current_positions JSONB,
    last_trade_time TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_ohlcv_symbol_time ON ohlcv (symbol, timeframe, time DESC);
CREATE INDEX IF NOT EXISTS idx_liq_symbol_time ON liquidation_snapshots (symbol, timeframe, time DESC);
CREATE INDEX IF NOT EXISTS idx_liq_raw_symbol_time ON liquidation_data_raw (symbol, timeframe, timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_oi_symbol_time ON open_interest (symbol, timeframe, time DESC);
CREATE INDEX IF NOT EXISTS idx_trades_agent_time ON trades (agent, entry_time DESC);
CREATE INDEX IF NOT EXISTS idx_signals_agent_time ON signals (agent, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_agent_logs_agent_time ON agent_logs (agent, created_at DESC);
