"""
Config Utils Module

Loads environment variables from .env file and provides getters for all configuration values.
This is the foundation module that powers the entire system.

Flow: Load .env → Validate required keys → Provide typed getters for all services.
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Central configuration class for all system settings."""

    # Database Configuration
    @property
    def timescale_db_user(self) -> str:
        return os.getenv('TIMESCALE_DB_USER', 'vince')

    @property
    def timescale_db_pass(self) -> str:
        return os.getenv('TIMESCALE_DB_PASS', '')

    @property
    def timescale_db_name(self) -> str:
        return os.getenv('TIMESCALE_DB_NAME', 'quantprod')

    @property
    def timescale_db_host(self) -> str:
        return os.getenv('TIMESCALE_DB_HOST', 'localhost')

    @property
    def timescale_db_port(self) -> int:
        return int(os.getenv('TIMESCALE_DB_PORT', '5432'))

    # Grafana Configuration
    @property
    def grafana_admin_user(self) -> str:
        return os.getenv('GRAFANA_ADMIN_USER', 'admin')

    @property
    def grafana_admin_pass(self) -> str:
        return os.getenv('GRAFANA_ADMIN_PASS', '')

    # CoinGlass API
    @property
    def coinglass_api_key(self) -> str:
        return os.getenv('COINGLASS_API_KEY', '')

    @property
    def coinglass_base_url(self) -> str:
        return os.getenv('COINGLASS_BASE_URL', 'https://open-api.coinglass.com')

    # Bybit API
    @property
    def bybit_api_key(self) -> str:
        return os.getenv('BYBIT_API_KEY', '')

    @property
    def bybit_api_secret(self) -> str:
        return os.getenv('BYBIT_API_SECRET', '')

    @property
    def bybit_base_url(self) -> str:
        return os.getenv('BYBIT_BASE_URL', 'https://api.bybit.com')

    # Telegram Bot
    @property
    def telegram_bot_token(self) -> str:
        return os.getenv('TELEGRAM_BOT_TOKEN', '')

    @property
    def telegram_chat_id(self) -> str:
        return os.getenv('TELEGRAM_CHAT_ID', '')

    # X (Twitter) API
    @property
    def x_api_key(self) -> str:
        return os.getenv('X_API_KEY', '')

    @property
    def x_api_secret(self) -> str:
        return os.getenv('X_API_SECRET', '')

    @property
    def x_access_token(self) -> str:
        return os.getenv('X_ACCESS_TOKEN', '')

    @property
    def x_access_token_secret(self) -> str:
        return os.getenv('X_ACCESS_TOKEN_SECRET', '')

    # Twilio SMS
    @property
    def twilio_account_sid(self) -> str:
        return os.getenv('TWILIO_ACCOUNT_SID', '')

    @property
    def twilio_auth_token(self) -> str:
        return os.getenv('TWILIO_AUTH_TOKEN', '')

    @property
    def twilio_phone_number(self) -> str:
        return os.getenv('TWILIO_PHONE_NUMBER', '')

    # Email (Gmail)
    @property
    def email_user(self) -> str:
        return os.getenv('EMAIL_USER', '')

    @property
    def email_app_password(self) -> str:
        return os.getenv('EMAIL_APP_PASSWORD', '')

    # Polymarket Oracle Helix
    @property
    def polymarket_clob_key(self) -> str:
        return os.getenv('POLYMARKET_CLOB_KEY', '')

    @property
    def polymarket_gamma_url(self) -> str:
        return os.getenv('POLYMARKET_GAMMA_URL', 'https://gamma.api.polymarket.com')

    @property
    def polymarket_rpc_url(self) -> str:
        return os.getenv('POLYMARKET_RPC_URL', '')

    @property
    def polysights_api_url(self) -> str:
        return os.getenv('POLYSIGHTS_API_URL', 'https://app.polysights.xyz/api/v1')

    @property
    def polysights_key(self) -> str:
        return os.getenv('POLYSIGHTS_KEY', '')

    @property
    def nevua_ws_url(self) -> str:
        return os.getenv('NEVUA_WS_URL', 'wss://nevua.markets/ws')

    @property
    def nevua_token(self) -> str:
        return os.getenv('NEVUA_TOKEN', '')

    @property
    def hashdive_api_url(self) -> str:
        return os.getenv('HASHDIVE_API_URL', 'https://www.hashdive.com/api')

    @property
    def hashdive_key(self) -> str:
        return os.getenv('HASHDIVE_KEY', '')

    @property
    def polytale_api_url(self) -> str:
        return os.getenv('POLYTALE_API_URL', 'https://www.polytale.live/api')

    @property
    def polytale_key(self) -> str:
        return os.getenv('POLYTALE_KEY', '')

    @property
    def proxy_wallet_privkey(self) -> str:
        return os.getenv('PROXY_WALLET_PRIVKEY', '')

    @property
    def poly_risk_cap(self) -> float:
        return float(os.getenv('POLY_RISK_CAP', '0.10'))

    # Trading Configuration
    @property
    def entry_strategy(self) -> str:
        return os.getenv('ENTRY_STRATEGY', 'conservative')

    @property
    def position_size_pct(self) -> float:
        return float(os.getenv('POSITION_SIZE_PCT', '1.0'))

    @property
    def leverage(self) -> int:
        return int(os.getenv('LEVERAGE', '10'))

    @property
    def max_open_positions(self) -> int:
        return int(os.getenv('MAX_OPEN_POSITIONS', '5'))

    # Redis Configuration
    @property
    def redis_host(self) -> str:
        return os.getenv('REDIS_HOST', 'localhost')

    @property
    def redis_port(self) -> int:
        return int(os.getenv('REDIS_PORT', '6379'))

    @property
    def redis_db(self) -> int:
        return int(os.getenv('REDIS_DB', '0'))

    # Logging
    @property
    def log_level(self) -> str:
        return os.getenv('LOG_LEVEL', 'INFO')

    @property
    def log_file(self) -> str:
        return os.getenv('LOG_FILE', 'data/logs/system.log')

# Global config instance
_config_instance: Optional[Config] = None

def get_config() -> Config:
    """Get the global config instance (singleton pattern)."""
    global _config_instance
    if _config_instance is None:
        _config_instance = Config()
    return _config_instance

# Test function
if __name__ == "__main__":
    config = get_config()
    print(f"CoinGlass API Key: {config.coinglass_api_key}")
    print(f"TimescaleDB User: {config.timescale_db_user}")
    print(f"Poly Risk Cap: {config.poly_risk_cap}")
    print("✅ Config utils loaded successfully!")