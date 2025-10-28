"""
Stop Loss / Take Profit Math Module

Provides mathematical functions for optimizing stop loss and take profit levels in perpetual trading.

Flow: Take market data → calculate optimal SL/TP → output levels with risk-reward analysis.
"""

import numpy as np
from typing import Dict, Tuple, Optional, List
from enum import Enum

# Global constants
AGENT_NAME = "sl_tp_math"
VERTICAL = "perps"

class SLTPMethod(Enum):
    FIXED_PCT = "fixed_pct"
    VOLATILITY_BASED = "volatility_based"
    SUPPORT_RESISTANCE = "support_resistance"
    FIBONACCI = "fibonacci"
    ATR_BASED = "atr_based"

def calculate_atr(highs: List[float], lows: List[float], closes: List[float], period: int = 14) -> float:
    """
    Calculate Average True Range for volatility measurement.

    Args:
        highs: List of high prices.
        lows: List of low prices.
        closes: List of close prices.
        period: ATR period.

    Returns:
        Current ATR value.
    """
    if len(highs) < period + 1:
        return 0.0

    tr_values = []
    for i in range(1, len(highs)):
        tr = max(
            highs[i] - lows[i],
            abs(highs[i] - closes[i-1]),
            abs(lows[i] - closes[i-1])
        )
        tr_values.append(tr)

    # Simple moving average of TR
    return np.mean(tr_values[-period:]) if tr_values else 0.0

def optimize_sl_tp_fixed_pct(
    entry_price: float,
    direction: str,  # 'long' or 'short'
    risk_pct: float = 0.01,  # 1% risk
    reward_risk_ratio: float = 2.0
) -> Dict:
    """
    Optimize SL/TP using fixed percentage method.

    Args:
        entry_price: Entry price.
        direction: 'long' or 'short'.
        risk_pct: Risk per trade as percentage.
        reward_risk_ratio: Target reward to risk ratio.

    Returns:
        Dictionary with stop_loss and take_profit prices.
    """
    if direction == 'long':
        stop_loss = entry_price * (1 - risk_pct)
        take_profit = entry_price * (1 + risk_pct * reward_risk_ratio)
    else:  # short
        stop_loss = entry_price * (1 + risk_pct)
        take_profit = entry_price * (1 - risk_pct * reward_risk_ratio)

    return {
        'stop_loss': stop_loss,
        'take_profit': take_profit,
        'risk_pct': risk_pct,
        'reward_risk_ratio': reward_risk_ratio,
        'method': SLTPMethod.FIXED_PCT.value
    }

def optimize_sl_tp_volatility_based(
    entry_price: float,
    direction: str,
    volatility: float,  # Standard deviation of price
    risk_multiplier: float = 2.0,
    reward_multiplier: float = 3.0
) -> Dict:
    """
    Optimize SL/TP based on price volatility.

    Args:
        entry_price: Entry price.
        direction: 'long' or 'short'.
        volatility: Price volatility (std dev).
        risk_multiplier: Multiplier for stop loss distance.
        reward_multiplier: Multiplier for take profit distance.

    Returns:
        Dictionary with stop_loss and take_profit prices.
    """
    risk_distance = volatility * risk_multiplier
    reward_distance = volatility * reward_multiplier

    if direction == 'long':
        stop_loss = entry_price - risk_distance
        take_profit = entry_price + reward_distance
    else:  # short
        stop_loss = entry_price + risk_distance
        take_profit = entry_price - reward_distance

    return {
        'stop_loss': stop_loss,
        'take_profit': take_profit,
        'volatility': volatility,
        'risk_multiplier': risk_multiplier,
        'reward_multiplier': reward_multiplier,
        'method': SLTPMethod.VOLATILITY_BASED.value
    }

def optimize_sl_tp_atr_based(
    entry_price: float,
    direction: str,
    highs: List[float],
    lows: List[float],
    closes: List[float],
    atr_period: int = 14,
    risk_multiplier: float = 1.5,
    reward_multiplier: float = 2.5
) -> Dict:
    """
    Optimize SL/TP using ATR for dynamic levels.

    Args:
        entry_price: Entry price.
        direction: 'long' or 'short'.
        highs: Recent high prices.
        lows: Recent low prices.
        closes: Recent close prices.
        atr_period: ATR calculation period.
        risk_multiplier: ATR multiplier for stop loss.
        reward_multiplier: ATR multiplier for take profit.

    Returns:
        Dictionary with stop_loss and take_profit prices.
    """
    atr = calculate_atr(highs, lows, closes, atr_period)

    if direction == 'long':
        stop_loss = entry_price - (atr * risk_multiplier)
        take_profit = entry_price + (atr * reward_multiplier)
    else:  # short
        stop_loss = entry_price + (atr * risk_multiplier)
        take_profit = entry_price - (atr * reward_multiplier)

    return {
        'stop_loss': stop_loss,
        'take_profit': take_profit,
        'atr': atr,
        'risk_multiplier': risk_multiplier,
        'reward_multiplier': reward_multiplier,
        'method': SLTPMethod.ATR_BASED.value
    }

def optimize_sl_tp_fibonacci(
    entry_price: float,
    direction: str,
    swing_low: float,
    swing_high: float,
    risk_pct: float = 0.015  # 1.5% risk
) -> Dict:
    """
    Optimize SL/TP using Fibonacci retracement levels.

    Args:
        entry_price: Entry price.
        direction: 'long' or 'short'.
        swing_low: Recent swing low.
        swing_high: Recent swing high.
        risk_pct: Risk per trade as percentage.

    Returns:
        Dictionary with stop_loss and take_profit prices.
    """
    fib_levels = {
        0.236: 0.236,
        0.382: 0.382,
        0.5: 0.5,
        0.618: 0.618,
        0.786: 0.786
    }

    swing_range = swing_high - swing_low

    if direction == 'long':
        # Stop at swing low or calculated risk level
        stop_loss = max(swing_low, entry_price * (1 - risk_pct))
        # Take profit at Fibonacci levels above entry
        take_profit_levels = {k: entry_price + (swing_range * v) for k, v in fib_levels.items()}
        take_profit = take_profit_levels[0.618]  # 61.8% level
    else:  # short
        stop_loss = min(swing_high, entry_price * (1 + risk_pct))
        take_profit_levels = {k: entry_price - (swing_range * v) for k, v in fib_levels.items()}
        take_profit = take_profit_levels[0.618]

    return {
        'stop_loss': stop_loss,
        'take_profit': take_profit,
        'fib_levels': take_profit_levels,
        'swing_low': swing_low,
        'swing_high': swing_high,
        'method': SLTPMethod.FIBONACCI.value
    }

def validate_sl_tp_levels(
    entry_price: float,
    stop_loss: float,
    take_profit: float,
    direction: str,
    min_reward_risk_ratio: float = 1.5
) -> Dict:
    """
    Validate SL/TP levels for reasonableness.

    Args:
        entry_price: Entry price.
        stop_loss: Stop loss price.
        take_profit: Take profit price.
        direction: 'long' or 'short'.
        min_reward_risk_ratio: Minimum acceptable reward/risk ratio.

    Returns:
        Validation results.
    """
    risk = abs(entry_price - stop_loss)
    reward = abs(take_profit - entry_price)
    reward_risk_ratio = reward / risk if risk > 0 else 0

    is_valid = True
    issues = []

    if direction == 'long':
        if stop_loss >= entry_price:
            is_valid = False
            issues.append("Stop loss should be below entry for long position")
        if take_profit <= entry_price:
            is_valid = False
            issues.append("Take profit should be above entry for long position")
    else:  # short
        if stop_loss <= entry_price:
            is_valid = False
            issues.append("Stop loss should be above entry for short position")
        if take_profit >= entry_price:
            is_valid = False
            issues.append("Take profit should be below entry for short position")

    if reward_risk_ratio < min_reward_risk_ratio:
        issues.append(f"Reward/risk ratio {reward_risk_ratio:.2f} below minimum {min_reward_risk_ratio}")

    return {
        'is_valid': is_valid,
        'reward_risk_ratio': reward_risk_ratio,
        'risk_amount': risk,
        'reward_amount': reward,
        'issues': issues
    }

# Test function
if __name__ == "__main__":
    # Test fixed percentage
    fixed = optimize_sl_tp_fixed_pct(100.0, 'long', 0.01, 2.0)
    print(f"✅ {AGENT_NAME}: Fixed SL: {fixed['stop_loss']:.2f}, TP: {fixed['take_profit']:.2f}")

    # Test volatility based
    vol = optimize_sl_tp_volatility_based(100.0, 'long', 2.0)
    print(f"✅ {AGENT_NAME}: Vol SL: {vol['stop_loss']:.2f}, TP: {vol['take_profit']:.2f}")

    # Test ATR based
    highs = [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
    lows = [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
    closes = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]
    atr_result = optimize_sl_tp_atr_based(110.0, 'long', highs, lows, closes)
    print(f"✅ {AGENT_NAME}: ATR SL: {atr_result['stop_loss']:.2f}, TP: {atr_result['take_profit']:.2f}")

    # Test validation
    validation = validate_sl_tp_levels(100.0, 98.0, 105.0, 'long')
    print(f"✅ {AGENT_NAME}: Validation - Valid: {validation['is_valid']}, R:R: {validation['reward_risk_ratio']:.2f}")

    print(f"✅ {AGENT_NAME}: All tests passed!")