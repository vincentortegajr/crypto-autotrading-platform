"""
Data Utilities for Vince Quant Whale Stack + Polymarket Oracle Helix.

Provides data I/O utilities for saving/loading CSV, JSON, and DataFrames.
Handles polymarket wallet analytics, CLOB snapshots, and signal exports.

Flow: DataFrame/JSON → CSV/JSON files → Load for analysis/CLOB.
"""

import json
import csv
import logging
from typing import Any, Dict, List, Optional, Union
from pathlib import Path
import pandas as pd

from .config_utils import Config

logger = logging.getLogger(__name__)


class DataUtils:
    """Data I/O utilities for CSV, JSON, and DataFrame operations."""

    def __init__(self, config: Config):
        self.config = config
        self.data_dir = Path("data")
        self.ensure_directories()

    def ensure_directories(self) -> None:
        """Ensure all data directories exist."""
        directories = [
            self.data_dir / "incoming" / "coinglass_json",
            self.data_dir / "incoming" / "bybit_json",
            self.data_dir / "incoming" / "binance_json",
            self.data_dir / "incoming" / "ws_raw",
            self.data_dir / "incoming" / "polymarket_json",
            self.data_dir / "processed" / "liquidation_csv",
            self.data_dir / "processed" / "oi_csv",
            self.data_dir / "processed" / "trades_csv",
            self.data_dir / "processed" / "wicks_csv",
            self.data_dir / "processed" / "agent_logs_csv",
            self.data_dir / "processed" / "poly_wallets_csv",
            self.data_dir / "processed" / "clob_snapshots",
            self.data_dir / "signals" / "grid_bot",
            self.data_dir / "signals" / "momentum_bot",
            self.data_dir / "signals" / "scanner_oi",
            self.data_dir / "signals" / "manual",
            self.data_dir / "signals" / "poly_perfect_bets",
            self.data_dir / "trades" / "autotrader",
            self.data_dir / "trades" / "manual",
            self.data_dir / "trades" / "agent_pnl",
            self.data_dir / "trades" / "poly_copy",
            self.data_dir / "logs" / "agents",
            self.data_dir / "logs" / "scanners",
            self.data_dir / "logs" / "broadcast",
            self.data_dir / "logs" / "db",
            self.data_dir / "logs" / "poly",
            self.data_dir / "images" / "agent_screenshots",
            self.data_dir / "images" / "heatmaps",
            self.data_dir / "images" / "dashboards",
            self.data_dir / "images" / "tg_broadcasts",
            self.data_dir / "images" / "x_broadcasts",
            self.data_dir / "images" / "strategy_visuals",
            self.data_dir / "images" / "tutorials",
            self.data_dir / "images" / "poly_charts",
            self.data_dir / "videos" / "tutorials",
            self.data_dir / "videos" / "agent_guides",
            self.data_dir / "videos" / "output_for_social",
            self.data_dir / "reports" / "daily",
            self.data_dir / "reports" / "weekly",
            self.data_dir / "reports" / "monthly",
            self.data_dir / "reports" / "pnl",
            self.data_dir / "reports" / "audit_exports",
            self.data_dir / "reports" / "hybrid_arbs",
            self.data_dir / "retention" / "delete_queue",
            self.data_dir / "retention" / "cold_archive"
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)

        logger.info("Data directories ensured")

    def save_json(self, data: Union[Dict[str, Any], List[Dict[str, Any]]], filename: str, directory: str) -> Path:
        """Save data as JSON file."""
        file_path = self.data_dir / directory / f"{filename}.json"
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str)
            logger.debug(f"Saved JSON to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Failed to save JSON {filename}: {e}")
            raise

    def load_json(self, filename: str, directory: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """Load data from JSON file."""
        file_path = self.data_dir / directory / f"{filename}.json"
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.debug(f"Loaded JSON from {file_path}")
            return data
        except FileNotFoundError:
            logger.warning(f"JSON file not found: {file_path}")
            return {}
        except Exception as e:
            logger.error(f"Failed to load JSON {filename}: {e}")
            raise

    def save_csv(self, data: List[Dict[str, Any]], filename: str, directory: str) -> Path:
        """Save list of dicts as CSV file."""
        if not data:
            logger.warning(f"No data to save for {filename}")
            return Path()

        file_path = self.data_dir / directory / f"{filename}.csv"
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            logger.debug(f"Saved CSV to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Failed to save CSV {filename}: {e}")
            raise

    def load_csv(self, filename: str, directory: str) -> List[Dict[str, Any]]:
        """Load data from CSV file."""
        file_path = self.data_dir / directory / f"{filename}.csv"
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = list(reader)
            logger.debug(f"Loaded CSV from {file_path}")
            return data
        except FileNotFoundError:
            logger.warning(f"CSV file not found: {file_path}")
            return []
        except Exception as e:
            logger.error(f"Failed to load CSV {filename}: {e}")
            raise

    def save_dataframe(self, df: pd.DataFrame, filename: str, directory: str, index: bool = False) -> Path:
        """Save pandas DataFrame as CSV."""
        file_path = self.data_dir / directory / f"{filename}.csv"
        try:
            df.to_csv(file_path, index=index)
            logger.debug(f"Saved DataFrame to {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Failed to save DataFrame {filename}: {e}")
            raise

    def load_dataframe(self, filename: str, directory: str, index_col: Optional[str] = None) -> pd.DataFrame:
        """Load pandas DataFrame from CSV."""
        file_path = self.data_dir / directory / f"{filename}.csv"
        try:
            df = pd.read_csv(file_path, index_col=index_col)
            logger.debug(f"Loaded DataFrame from {file_path}")
            return df
        except FileNotFoundError:
            logger.warning(f"DataFrame CSV not found: {file_path}")
            return pd.DataFrame()
        except Exception as e:
            logger.error(f"Failed to load DataFrame {filename}: {e}")
            raise

    # Polymarket-specific utilities

    def save_poly_wallet_csv(self, wallets: List[Dict[str, Any]], filename: str = "poly_wallets") -> Path:
        """Save polymarket wallet data as CSV."""
        return self.save_csv(wallets, filename, "processed/poly_wallets_csv")

    def load_poly_wallet_csv(self, filename: str = "poly_wallets") -> List[Dict[str, Any]]:
        """Load polymarket wallet data from CSV."""
        return self.load_csv(filename, "processed/poly_wallets_csv")

    def save_clob_snapshot(self, snapshot: Dict[str, Any], market_id: str, timestamp: str) -> Path:
        """Save CLOB market snapshot as JSON."""
        filename = f"clob_{market_id}_{timestamp.replace(':', '').replace('-', '').replace(' ', '_')}"
        return self.save_json(snapshot, filename, "processed/clob_snapshots")

    def load_clob_snapshot(self, market_id: str, timestamp: str) -> Dict[str, Any]:
        """Load CLOB market snapshot from JSON."""
        filename = f"clob_{market_id}_{timestamp.replace(':', '').replace('-', '').replace(' ', '_')}"
        return self.load_json(filename, "processed/clob_snapshots")

    def save_poly_signal_csv(self, signals: List[Dict[str, Any]], filename: str = "poly_signals") -> Path:
        """Save polymarket signals as CSV."""
        return self.save_csv(signals, filename, "signals/poly_perfect_bets")

    def load_poly_signal_csv(self, filename: str = "poly_signals") -> List[Dict[str, Any]]:
        """Load polymarket signals from CSV."""
        return self.load_csv(filename, "signals/poly_perfect_bets")

    # General utilities

    def list_files(self, directory: str, extension: Optional[str] = None) -> List[Path]:
        """List files in a data directory."""
        dir_path = self.data_dir / directory
        try:
            if extension:
                return list(dir_path.glob(f"*.{extension}"))
            else:
                return list(dir_path.glob("*"))
        except Exception as e:
            logger.error(f"Failed to list files in {directory}: {e}")
            return []

    def cleanup_old_files(self, directory: str, days_old: int = 30) -> int:
        """Remove files older than specified days."""
        import time
        dir_path = self.data_dir / directory
        try:
            removed = 0
            cutoff = time.time() - (days_old * 24 * 60 * 60)
            for file_path in dir_path.glob("*"):
                if file_path.is_file() and file_path.stat().st_mtime < cutoff:
                    file_path.unlink()
                    removed += 1
            logger.info(f"Cleaned up {removed} old files from {directory}")
            return removed
        except Exception as e:
            logger.error(f"Failed to cleanup {directory}: {e}")
            return 0


# Global instance
_data_utils_instance: Optional[DataUtils] = None


def get_data_utils(config: Config) -> DataUtils:
    """Get singleton data utilities instance."""
    global _data_utils_instance
    if _data_utils_instance is None:
        _data_utils_instance = DataUtils(config)
    return _data_utils_instance


def test_data_utils():
    """Test function for data utilities."""
    config = Config()
    data_utils = DataUtils(config)

    try:
        logger.info("Testing data utilities...")

        # Test JSON save/load
        test_data = {"message": "hello world", "number": 42, "list": [1, 2, 3]}
        json_path = data_utils.save_json(test_data, "test_json", "incoming/ws_raw")
        loaded_json = data_utils.load_json("test_json", "incoming/ws_raw")
        assert loaded_json == test_data, "JSON save/load failed"
        logger.info("JSON test passed")

        # Test CSV save/load
        test_csv_data = [
            {"name": "Alice", "age": "30.0", "city": "NYC"},
            {"name": "Bob", "age": "25.0", "city": "LA"},
            {"name": "Charlie", "age": "35.0", "city": "Chicago"}
        ]
        csv_path = data_utils.save_csv(test_csv_data, "test_csv", "processed/agent_logs_csv")
        loaded_csv = data_utils.load_csv("test_csv", "processed/agent_logs_csv")
        assert loaded_csv == test_csv_data, "CSV save/load failed"
        logger.info("CSV test passed")

        # Test DataFrame save/load
        df_data = [
            {"name": "Alice", "age": 30.0, "city": "NYC"},
            {"name": "Bob", "age": 25.0, "city": "LA"},
            {"name": "Charlie", "age": 35.0, "city": "Chicago"}
        ]
        df = pd.DataFrame(df_data)
        df_path = data_utils.save_dataframe(df, "test_df", "processed/trades_csv")
        loaded_df = data_utils.load_dataframe("test_df", "processed/trades_csv")
        pd.testing.assert_frame_equal(df, loaded_df)
        logger.info("DataFrame test passed")

        # Test poly wallet functions
        poly_wallets = [
            {"wallet_address": "0x123", "balance_usd": "50000.0", "pnl_24h": "2500.0", "market_count": "15.0"},
            {"wallet_address": "0x456", "balance_usd": "75000.0", "pnl_24h": "-1000.0", "market_count": "22.0"}
        ]
        poly_path = data_utils.save_poly_wallet_csv(poly_wallets, "test_poly_wallets")
        loaded_poly = data_utils.load_poly_wallet_csv("test_poly_wallets")
        assert loaded_poly == poly_wallets, "Poly wallet CSV failed"
        logger.info("Poly wallet CSV test passed")

        # Test CLOB snapshot
        clob_snapshot = {
            "market_id": "0x789",
            "bids": [{"price": "0.6", "size": "100"}],
            "asks": [{"price": "0.65", "size": "150"}],
            "timestamp": "2024-01-01T12:00:00Z"
        }
        clob_path = data_utils.save_clob_snapshot(clob_snapshot, "0x789", "2024-01-01_12-00-00")
        loaded_clob = data_utils.load_clob_snapshot("0x789", "2024-01-01_12-00-00")
        assert loaded_clob == clob_snapshot, "CLOB snapshot failed"
        logger.info("CLOB snapshot test passed")

        logger.info("All data utilities tests passed successfully!")

    except Exception as e:
        logger.error(f"Data utils test failed: {e}")
        raise


if __name__ == "__main__":
    # Run test when executed directly
    logging.basicConfig(level=logging.INFO)
    test_data_utils()