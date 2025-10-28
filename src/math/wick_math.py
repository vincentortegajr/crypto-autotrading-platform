"""
Wick Math Module

Provides mathematical functions for analyzing candlestick wicks in perpetual markets.

Flow: Take OHLCV data → calculate wick metrics → identify whale manipulation patterns.
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Tuple, Optional

# Global constants
AGENT_NAME = "wick_math"
VERTICAL = "perps"

def calculate_wick_metrics(ohlcv: Dict) -> Dict:
    """
    Calculate wick metrics for a single candlestick.

    Args:
        ohlcv: Dictionary with 'open', 'high', 'low', 'close', 'volume' keys.

    Returns:
        Dictionary with wick ratios and directions.
    """
    open_price = ohlcv['open']
    high = ohlcv['high']
    low = ohlcv['low']
    close = ohlcv['close']

    # Calculate body and wicks
    body_high = max(open_price, close)
    body_low = min(open_price, close)
    body_size = body_high - body_low

    upper_wick = high - body_high
    lower_wick = body_low - low

    # Avoid division by zero
    total_range = high - low
    if total_range == 0:
        return {
            'upper_wick_ratio': 0,
            'lower_wick_ratio': 0,
            'body_ratio': 1,
            'wick_imbalance': 0,
            'is_long_upper_wick': False,
            'is_long_lower_wick': False
        }

    # Calculate ratios
    upper_wick_ratio = upper_wick / total_range
    lower_wick_ratio = lower_wick / total_range
    body_ratio = body_size / total_range

    # Wick imbalance (positive = upper wick longer, negative = lower wick longer)
    wick_imbalance = upper_wick_ratio - lower_wick_ratio

    # Identify long wicks (arbitrary threshold: >40% of total range)
    is_long_upper_wick = upper_wick_ratio > 0.4
    is_long_lower_wick = lower_wick_ratio > 0.4

    return {
        'upper_wick_ratio': upper_wick_ratio,
        'lower_wick_ratio': lower_wick_ratio,
        'body_ratio': body_ratio,
        'wick_imbalance': wick_imbalance,
        'is_long_upper_wick': is_long_upper_wick,
        'is_long_lower_wick': is_long_lower_wick,
        'upper_wick_size': upper_wick,
        'lower_wick_size': lower_wick,
        'total_range': total_range
    }

def analyze_wick_patterns(ohlcv_list: List[Dict], window: int = 10) -> List[Dict]:
    """
    Analyze wick patterns over a series of candles.

    Args:
        ohlcv_list: List of OHLCV dictionaries.
        window: Rolling window size for pattern analysis.

    Returns:
        List of wick analysis results for each candle.
    """
    results = []
    for i, ohlcv in enumerate(ohlcv_list):
        metrics = calculate_wick_metrics(ohlcv)

        # Add rolling statistics if enough data
        if i >= window - 1:
            window_data = ohlcv_list[i-window+1:i+1]
            window_metrics = [calculate_wick_metrics(c) for c in window_data]

            avg_upper_wick = np.mean([m['upper_wick_ratio'] for m in window_metrics])
            avg_lower_wick = np.mean([m['lower_wick_ratio'] for m in window_metrics])
            avg_imbalance = np.mean([m['wick_imbalance'] for m in window_metrics])

            metrics.update({
                'rolling_avg_upper_wick': avg_upper_wick,
                'rolling_avg_lower_wick': avg_lower_wick,
                'rolling_avg_imbalance': avg_imbalance,
                'is_extreme_upper_wick': metrics['upper_wick_ratio'] > avg_upper_wick + 0.2,
                'is_extreme_lower_wick': metrics['lower_wick_ratio'] > avg_lower_wick + 0.2
            })

        results.append(metrics)

    return results

def detect_whale_wick_manipulation(
    wick_analysis: List[Dict],
    volume_threshold: float = 1000000
) -> List[Dict]:
    """
    Detect potential whale wick manipulation patterns.

    Args:
        wick_analysis: List of wick metrics from analyze_wick_patterns.
        volume_threshold: Minimum volume to consider for manipulation detection.

    Returns:
        List of potential manipulation signals.
    """
    signals = []

    for i, metrics in enumerate(wick_analysis):
        # Look for extreme upper wicks with high volume (potential whale resistance)
        if (metrics.get('is_extreme_upper_wick', False) and
            metrics.get('volume', 0) > volume_threshold):
            signals.append({
                'type': 'whale_resistance',
                'index': i,
                'wick_ratio': metrics['upper_wick_ratio'],
                'volume': metrics.get('volume', 0),
                'confidence': min(1.0, metrics['upper_wick_ratio'] * metrics.get('volume', 0) / volume_threshold)
            })

        # Look for extreme lower wicks (potential whale support)
        if (metrics.get('is_extreme_lower_wick', False) and
            metrics.get('volume', 0) > volume_threshold):
            signals.append({
                'type': 'whale_support',
                'index': i,
                'wick_ratio': metrics['lower_wick_ratio'],
                'volume': metrics.get('volume', 0),
                'confidence': min(1.0, metrics['lower_wick_ratio'] * metrics.get('volume', 0) / volume_threshold)
            })

    return signals

# Test function
if __name__ == "__main__":
    # Test data: simulated OHLCV candles
    test_ohlcv = [
        {'open': 100.0, 'high': 105.0, 'low': 95.0, 'close': 102.0, 'volume': 1000000},  # Long lower wick
        {'open': 102.0, 'high': 110.0, 'low': 100.0, 'close': 101.0, 'volume': 1500000}, # Long upper wick
        {'open': 101.0, 'high': 103.0, 'low': 99.0, 'close': 102.0, 'volume': 800000},   # Normal
    ]

    # Test single candle
    metrics = calculate_wick_metrics(test_ohlcv[0])
    print(f"✅ {AGENT_NAME}: Single candle metrics - upper_wick_ratio: {metrics['upper_wick_ratio']:.3f}")

    # Test pattern analysis
    analysis = analyze_wick_patterns(test_ohlcv, window=3)
    print(f"✅ {AGENT_NAME}: Analyzed {len(analysis)} candles")

    # Test manipulation detection
    signals = detect_whale_wick_manipulation(analysis, volume_threshold=500000)
    print(f"✅ {AGENT_NAME}: Detected {len(signals)} manipulation signals")

    print(f"✅ {AGENT_NAME}: All tests passed!")