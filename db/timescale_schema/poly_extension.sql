-- Polymarket / hybrid extensions for TimescaleDB schema

ALTER TABLE trades ADD COLUMN IF NOT EXISTS vertical TEXT DEFAULT 'perps';
ALTER TABLE signals ADD COLUMN IF NOT EXISTS vertical TEXT DEFAULT 'perps';
ALTER TABLE agent_logs ADD COLUMN IF NOT EXISTS vertical TEXT;
ALTER TABLE pnl ADD COLUMN IF NOT EXISTS vertical TEXT DEFAULT 'perps';

CREATE TABLE IF NOT EXISTS poly_wallets (
    wallet_address TEXT NOT NULL,
    snapshot_time TIMESTAMPTZ NOT NULL,
    roi_30d NUMERIC,
    streak INT,
    checklist_score NUMERIC,
    tags TEXT[],
    last_seen TIMESTAMPTZ,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (wallet_address, snapshot_time)
);
SELECT create_hypertable('poly_wallets', 'snapshot_time', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS poly_signals (
    poly_signal_id BIGSERIAL,
    market_id TEXT NOT NULL,
    market_name TEXT NOT NULL,
    outcome TEXT NOT NULL,
    price NUMERIC NOT NULL,
    edge_score NUMERIC NOT NULL,
    checklist INT NOT NULL,
    wallet_sync BOOLEAN DEFAULT FALSE,
    oi_confirmation BOOLEAN DEFAULT FALSE,
    hybrid_weight NUMERIC,
    generated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (poly_signal_id, generated_at)
);
SELECT create_hypertable('poly_signals', 'generated_at', if_not_exists => TRUE);

CREATE TABLE IF NOT EXISTS hybrid_signals (
    hybrid_id BIGSERIAL,
    perps_symbol TEXT NOT NULL,
    poly_market_id TEXT NOT NULL,
    thesis TEXT,
    edge NUMERIC,
    recommended_action TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (hybrid_id, created_at)
);
SELECT create_hypertable('hybrid_signals', 'created_at', if_not_exists => TRUE);

CREATE INDEX IF NOT EXISTS idx_poly_wallets_last_seen ON poly_wallets (last_seen DESC);
CREATE INDEX IF NOT EXISTS idx_poly_signals_market ON poly_signals (market_id, generated_at DESC);
CREATE INDEX IF NOT EXISTS idx_hybrid_signals_symbol ON hybrid_signals (perps_symbol, created_at DESC);
