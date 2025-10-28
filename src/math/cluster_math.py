"""
Cluster Math Module

Provides mathematical functions for identifying and analyzing liquidation clusters in perpetual markets.

Flow: Take liquidation data → calculate cluster centers, sizes, densities → output cluster metrics.
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Tuple, Optional
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Global constants
AGENT_NAME = "cluster_math"
VERTICAL = "perps"

def calculate_liquidation_clusters(
    liquidations: List[Dict],
    eps: float = 0.01,  # Price distance threshold (1% for crypto)
    min_samples: int = 5  # Minimum liquidations per cluster
) -> List[Dict]:
    """
    Identify liquidation clusters using DBSCAN clustering.

    Args:
        liquidations: List of liquidation dicts with 'price' and 'quantity' keys.
        eps: Maximum distance between points in a cluster (normalized price difference).
        min_samples: Minimum number of liquidations to form a cluster.

    Returns:
        List of cluster dictionaries with center_price, total_quantity, liquidation_count, density.
    """
    if not liquidations:
        return []

    # Extract prices and quantities
    prices = np.array([liq['price'] for liq in liquidations])
    quantities = np.array([liq['quantity'] for liq in liquidations])

    # Normalize prices for clustering
    scaler = StandardScaler()
    prices_normalized = scaler.fit_transform(prices.reshape(-1, 1)).flatten()

    # Perform DBSCAN clustering
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(prices_normalized.reshape(-1, 1))
    labels = clustering.labels_

    clusters = []
    unique_labels = set(labels)
    for label in unique_labels:
        if label == -1:  # Noise points
            continue

        # Get points in this cluster
        mask = labels == label
        cluster_prices = prices[mask]
        cluster_quantities = quantities[mask]

        # Calculate cluster metrics
        center_price = np.mean(cluster_prices)
        total_quantity = np.sum(cluster_quantities)
        liquidation_count = len(cluster_prices)
        price_std = np.std(cluster_prices)
        density = total_quantity / (price_std + 1e-8)  # Avoid division by zero

        clusters.append({
            'center_price': center_price,
            'total_quantity': total_quantity,
            'liquidation_count': liquidation_count,
            'price_std': price_std,
            'density': density,
            'price_range': (np.min(cluster_prices), np.max(cluster_prices))
        })

    # Sort clusters by density (most concentrated first)
    clusters.sort(key=lambda x: x['density'], reverse=True)
    return clusters

def find_whale_liquidation_zones(
    clusters: List[Dict],
    min_quantity_threshold: float = 1000000  # $1M minimum
) -> List[Dict]:
    """
    Identify whale liquidation zones from clusters.

    Args:
        clusters: List of cluster dictionaries from calculate_liquidation_clusters.
        min_quantity_threshold: Minimum total quantity to consider a whale zone.

    Returns:
        List of whale zones with enhanced metrics.
    """
    whale_zones = []
    for cluster in clusters:
        if cluster['total_quantity'] >= min_quantity_threshold:
            # Calculate whale-specific metrics
            whale_score = cluster['density'] * np.log(cluster['total_quantity'])
            cluster['whale_score'] = whale_score
            cluster['is_whale_zone'] = True
            whale_zones.append(cluster)
        else:
            cluster['whale_score'] = 0
            cluster['is_whale_zone'] = False

    return whale_zones

def predict_cluster_impact(
    cluster: Dict,
    current_price: float,
    leverage_avg: float = 10.0
) -> Dict:
    """
    Predict the market impact of a liquidation cluster.

    Args:
        cluster: Cluster dictionary.
        current_price: Current market price.
        leverage_avg: Average leverage of liquidated positions.

    Returns:
        Dictionary with impact predictions.
    """
    price_distance = abs(cluster['center_price'] - current_price) / current_price
    potential_impact = cluster['total_quantity'] * leverage_avg * price_distance

    return {
        'price_distance_pct': price_distance * 100,
        'potential_impact_usd': potential_impact,
        'impact_probability': min(1.0, cluster['density'] / 1000),  # Arbitrary scaling
        'cluster': cluster
    }

# Test function
if __name__ == "__main__":
    # Test data: simulated liquidations
    test_liquidations = [
        {'price': 100.0, 'quantity': 10000},
        {'price': 101.0, 'quantity': 15000},
        {'price': 102.0, 'quantity': 20000},  # Cluster 1
        {'price': 102.5, 'quantity': 25000},
        {'price': 103.0, 'quantity': 30000},
        {'price': 200.0, 'quantity': 5000},   # Isolated
        {'price': 300.0, 'quantity': 100000}, # Cluster 2
        {'price': 301.0, 'quantity': 120000},
        {'price': 302.0, 'quantity': 150000},
    ]

    clusters = calculate_liquidation_clusters(test_liquidations, eps=0.05, min_samples=3)
    print(f"✅ {AGENT_NAME}: Found {len(clusters)} clusters")

    whale_zones = find_whale_liquidation_zones(clusters, min_quantity_threshold=100000)
    print(f"✅ {AGENT_NAME}: Found {len(whale_zones)} whale zones")

    if clusters:
        impact = predict_cluster_impact(clusters[0], current_price=105.0)
        print(f"✅ {AGENT_NAME}: Cluster impact prediction: {impact['potential_impact_usd']:.2f} USD")

    print(f"✅ {AGENT_NAME}: All tests passed!")