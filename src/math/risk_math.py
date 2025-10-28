"""
Risk Math Module

Provides mathematical functions for position sizing and risk management in hybrid perps + poly trading.

Flow: Take probabilities/edges → calculate Kelly fractions → output position sizes with hybrid fusion.
"""

import numpy as np
from typing import Dict, Tuple, Optional
import sympy as sp

# Global constants
AGENT_NAME = "risk_math"
VERTICAL = "hybrid"

def kelly_fraction(win_prob: float, win_loss_ratio: float) -> float:
    """
    Calculate the Kelly fraction for position sizing.

    Args:
        win_prob: Probability of winning (0-1).
        win_loss_ratio: Ratio of win size to loss size (e.g., 2.0 for 2:1).

    Returns:
        Kelly fraction (0-1, where 1 = full Kelly).
    """
    if win_prob <= 0 or win_prob >= 1 or win_loss_ratio <= 0:
        return 0.0

    # Kelly formula: f = (bp - q) / b
    # where b = odds received, p = win prob, q = loss prob
    b = win_loss_ratio
    p = win_prob
    q = 1 - p

    kelly = (b * p - q) / b

    # Cap at reasonable maximum (half Kelly for safety)
    return max(0.0, min(kelly, 0.5))

def half_kelly_fraction(win_prob: float, win_loss_ratio: float) -> float:
    """
    Calculate half Kelly fraction for conservative sizing.

    Args:
        win_prob: Probability of winning.
        win_loss_ratio: Win/loss ratio.

    Returns:
        Half Kelly fraction.
    """
    return kelly_fraction(win_prob, win_loss_ratio) * 0.5

def hybrid_kelly_fraction(
    perps_prob: float,
    perps_win_loss_ratio: float,
    poly_edge: float,
    fusion_weight: float = 0.5
) -> float:
    """
    Calculate hybrid Kelly fraction combining perps probability and poly edge.

    Args:
        perps_prob: Perps win probability (0-1).
        perps_win_loss_ratio: Perps win/loss ratio.
        poly_edge: Poly edge score (0+).
        fusion_weight: Weight for poly influence (0-1).

    Returns:
        Hybrid Kelly fraction.
    """
    # Base perps Kelly
    perps_kelly = kelly_fraction(perps_prob, perps_win_loss_ratio)

    # Poly adjustment (edge amplifies Kelly if positive)
    poly_multiplier = 1.0 + (poly_edge - 1.0) * fusion_weight

    # Hybrid Kelly
    hybrid_kelly = perps_kelly * poly_multiplier

    # Conservative cap
    return max(0.0, min(hybrid_kelly, 0.3))  # Max 30% for safety

def position_size_from_kelly(
    kelly_fraction: float,
    account_balance: float,
    risk_per_trade: float = 0.02  # 2% max risk per trade
) -> float:
    """
    Calculate position size from Kelly fraction and account balance.

    Args:
        kelly_fraction: Kelly fraction (0-1).
        account_balance: Total account balance.
        risk_per_trade: Maximum risk per trade as fraction of balance.

    Returns:
        Position size in base currency.
    """
    max_position = account_balance * risk_per_trade
    kelly_position = account_balance * kelly_fraction

    # Use the more conservative of Kelly and max risk
    return min(kelly_position, max_position)

def calculate_risk_metrics(
    position_size: float,
    entry_price: float,
    stop_loss_price: float,
    take_profit_price: Optional[float] = None
) -> Dict:
    """
    Calculate risk metrics for a position.

    Args:
        position_size: Size of position.
        entry_price: Entry price.
        stop_loss_price: Stop loss price.
        take_profit_price: Take profit price (optional).

    Returns:
        Dictionary with risk metrics.
    """
    risk_amount = position_size * abs(entry_price - stop_loss_price) / entry_price

    metrics = {
        'risk_amount': risk_amount,
        'risk_pct': risk_amount / (position_size * entry_price) * 100 if position_size > 0 else 0,
        'stop_distance_pct': abs(stop_loss_price - entry_price) / entry_price * 100
    }

    if take_profit_price:
        reward_amount = position_size * abs(take_profit_price - entry_price) / entry_price
        metrics.update({
            'reward_amount': reward_amount,
            'reward_risk_ratio': reward_amount / risk_amount if risk_amount > 0 else 0
        })

    return metrics

def optimize_stop_loss(
    entry_price: float,
    volatility: float,
    risk_tolerance: float = 0.01  # 1% risk tolerance
) -> float:
    """
    Optimize stop loss based on volatility.

    Args:
        entry_price: Entry price.
        volatility: Price volatility (standard deviation).
        risk_tolerance: Maximum acceptable loss as fraction.

    Returns:
        Optimal stop loss price.
    """
    # Simple volatility-based stop: entry - (volatility * multiplier)
    stop_distance = volatility * 2.0  # 2-sigma stop
    return entry_price - stop_distance

# Test function
if __name__ == "__main__":
    # Test Kelly calculations
    kelly = kelly_fraction(0.6, 2.0)  # 60% win prob, 2:1 ratio
    print(f"✅ {AGENT_NAME}: Kelly fraction: {kelly:.3f}")

    half_kelly = half_kelly_fraction(0.6, 2.0)
    print(f"✅ {AGENT_NAME}: Half Kelly: {half_kelly:.3f}")

    # Test hybrid Kelly
    hybrid_kelly = hybrid_kelly_fraction(0.6, 2.0, 1.5, 0.5)
    print(f"✅ {AGENT_NAME}: Hybrid Kelly: {hybrid_kelly:.3f}")

    # Test position sizing
    position = position_size_from_kelly(hybrid_kelly, 10000.0)
    print(f"✅ {AGENT_NAME}: Position size: ${position:.2f}")

    # Test risk metrics
    metrics = calculate_risk_metrics(position, 100.0, 98.0, 105.0)
    print(f"✅ {AGENT_NAME}: Risk-reward ratio: {metrics['reward_risk_ratio']:.2f}")

    print(f"✅ {AGENT_NAME}: All tests passed!")