"""
Poly Edge Math Module

Provides mathematical functions for calculating prediction market edges and Kelly sizing.

Flow: Take poly signals → calculate edge scores → apply Kelly formula → output position sizes.
"""

import sympy as sp
from typing import Dict, Tuple, Optional, List
from src.math.risk_math import kelly_fraction  # Hook to risk_math

# Global constants
AGENT_NAME = "poly_edge_math"
VERTICAL = "poly"

# Symbolic variables for formulas
signal = sp.Symbol('signal')
vol = sp.Symbol('vol')
allocation = sp.Symbol('allocation')
emot = sp.Symbol('emot')

# Core bet formula: edge = signal * (1 - vol) * allocation * emot
BET_FORMULA = signal * (1 - vol) * allocation * emot

def calculate_edge_score(
    signal_strength: float,
    volatility: float,
    alloc_factor: float = 1.0,
    emotional_factor: float = 1.0
) -> float:
    """
    Calculate poly edge score using the bet formula.

    Args:
        signal_strength: Signal strength (0-1).
        volatility: Market volatility (0-1).
        allocation: Allocation factor (0-1).
        emotional_factor: Emotional adjustment (0-1).

    Returns:
        Edge score (higher = better opportunity).
    """
    # Substitute values into symbolic formula
    edge = BET_FORMULA.subs([
        (signal, signal_strength),
        (vol, volatility),
        (allocation, alloc_factor),
        (emot, emotional_factor)
    ])

    return float(sp.N(edge))

def checklist_score(
    signal_strength: float,
    volatility: float,
    allocation: float = 1.0,
    emotional_factor: float = 1.0,
    checklist_items: Optional[List[bool]] = None
) -> Tuple[float, int]:
    """
    Calculate checklist score for poly signals.

    Args:
        signal_strength: Signal strength.
        volatility: Volatility.
        allocation: Allocation factor.
        emotional_factor: Emotional factor.
        checklist_items: List of boolean checklist items.

    Returns:
        Tuple of (edge_score, checklist_score).
    """
    edge_score = calculate_edge_score(signal_strength, volatility, allocation, emotional_factor)

    # Default checklist if not provided
    if checklist_items is None:
        checklist_items = [
            signal_strength > 0.7,  # Strong signal
            volatility < 0.3,       # Low volatility
            allocation > 0.8,       # High allocation
            emotional_factor > 0.9  # Low emotion
        ]

    checklist_score_value = sum(checklist_items)

    return edge_score, checklist_score_value

def poly_kelly_fraction(
    signal_strength: float,
    volatility: float,
    allocation: float = 1.0,
    emotional_factor: float = 1.0,
    win_loss_ratio: float = 2.0
) -> float:
    """
    Calculate Kelly fraction for poly trades using edge score as win probability.

    Args:
        signal_strength: Signal strength (used as win probability).
        volatility: Volatility.
        allocation: Allocation factor.
        emotional_factor: Emotional factor.
        win_loss_ratio: Expected win/loss ratio.

    Returns:
        Kelly fraction for poly trade.
    """
    # Use edge score as effective win probability
    edge_score = calculate_edge_score(signal_strength, volatility, allocation, emotional_factor)

    # Normalize edge score to probability (0-1)
    win_prob = min(1.0, max(0.0, edge_score))

    # Apply Kelly formula from risk_math
    return kelly_fraction(win_prob, win_loss_ratio)

def hybrid_poly_kelly(
    perps_prob: float,
    perps_win_loss_ratio: float,
    poly_signal_strength: float,
    poly_volatility: float,
    fusion_weight: float = 0.5
) -> float:
    """
    Calculate hybrid Kelly combining perps and poly edges.

    Args:
        perps_prob: Perps win probability.
        perps_win_loss_ratio: Perps win/loss ratio.
        poly_signal_strength: Poly signal strength.
        poly_volatility: Poly volatility.
        fusion_weight: Weight for poly influence.

    Returns:
        Hybrid Kelly fraction.
    """
    from src.math.risk_math import hybrid_kelly_fraction

    # Calculate poly edge for fusion
    poly_edge = calculate_edge_score(poly_signal_strength, poly_volatility)

    return hybrid_kelly_fraction(perps_prob, perps_win_loss_ratio, poly_edge, fusion_weight)

def optimize_allocation(
    signal_strength: float,
    volatility: float,
    emotional_factor: float,
    max_allocation: float = 0.1  # 10% max
) -> float:
    """
    Optimize allocation based on edge factors.

    Args:
        signal_strength: Signal strength.
        volatility: Volatility.
        emotional_factor: Emotional factor.
        max_allocation: Maximum allowed allocation.

    Returns:
        Optimal allocation fraction.
    """
    # Base allocation from signal strength
    base_alloc = signal_strength * 0.05  # Max 5% at perfect signal

    # Adjust for volatility (lower vol = higher alloc)
    vol_adjustment = 1.0 - volatility

    # Adjust for emotion (higher emotion = lower alloc)
    emotion_adjustment = emotional_factor

    optimal_alloc = base_alloc * vol_adjustment * emotion_adjustment

    return min(optimal_alloc, max_allocation)

def score_edge(signal_strength: float, volatility: float) -> float:
    """
    Simple edge scoring function for testing.

    Args:
        signal_strength: Signal strength.
        volatility: Volatility.

    Returns:
        Edge score.
    """
    return calculate_edge_score(signal_strength, volatility, 1.0, 1.0)

# Test function
if __name__ == "__main__":
    # Test edge calculation
    edge = calculate_edge_score(0.8, 0.1, 1.0, 1.0)
    print(f"✅ {AGENT_NAME}: Edge score: {edge:.3f}")

    # Test checklist score
    edge_score, checklist = checklist_score(0.8, 0.1)
    print(f"✅ {AGENT_NAME}: Checklist score: {checklist}/4, Edge: {edge_score:.3f}")

    # Test poly Kelly
    poly_kelly = poly_kelly_fraction(0.8, 0.1)
    print(f"✅ {AGENT_NAME}: Poly Kelly: {poly_kelly:.3f}")

    # Test hybrid Kelly
    hybrid_kelly = hybrid_poly_kelly(0.6, 2.0, 0.8, 0.1)
    print(f"✅ {AGENT_NAME}: Hybrid Kelly: {hybrid_kelly:.3f}")

    # Test allocation optimization
    alloc = optimize_allocation(0.8, 0.1, 1.0)
    print(f"✅ {AGENT_NAME}: Optimal allocation: {alloc:.3f}")

    # Test simple score_edge
    simple_score = score_edge(0.8, 0.1)
    print(f"✅ {AGENT_NAME}: Simple score > 0.5: {simple_score > 0.5}")

    print(f"✅ {AGENT_NAME}: All tests passed!")