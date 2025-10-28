# Vince Quant Whale Helix - Build Todo List

## Phase 1: Utilities (Basement Pipes) - 5 Modules

- [x] 1. `src/utils/config_utils.py` – .env loader + getters (add poly keys). Test: `python3 -c "from src.utils.config_utils import get_config; print(get_config().coinglass_api_key)"`.
- [x] 2. `src/utils/timescale_utils.py` – Pooling/queries (add insert_poly_wallet, insert_poly_signal). Test: Insert dummy trade/poly signal.
- [x] 3. `src/utils/redis_utils.py` – Pub/sub (add "poly_signals" channel). Test: Publish/subscribe echo.
- [ ] 4. `src/utils/data_utils.py` – I/O (add poly JSON/CSV for CLOB). Test: Save/load wallet DF.
- [ ] 5. `src/utils/error_utils.py` – Decorators/retry (universal). Test: `@retry_on_failure def flaky(): raise`.

## Phase 2: Math (Lab Benches) - 5 Modules

- [ ] 6. `src/math/cluster_math.py` – Perps clusters (base).
- [ ] 7. `src/math/wick_math.py` – Wicks (base).
- [ ] 8. `src/math/risk_math.py` – Sizing (add hybrid_kelly: perps_prob * poly_edge).
- [ ] 9. `src/math/sl_tp_math.py` – Optimization (base).
- [ ] 10. `src/math/poly_edge_math.py` – Bet formula (sympy: signal * (1-vol) * alloc * emot), checklist_score(>=5), poly_kelly. Hook risk_math. Test: `score_edge(0.8, 0.1) >0.5`.

## Phase 3: Sockets (Tower Antennas) - 3 Modules

- [ ] 11. `src/sockets/coinglass_ws.py` – Base.
- [ ] 12. `src/sockets/bybit_ws.py` – Base.
- [ ] 13. `src/sockets/polymarket_ws.py` – Nevua/PolyTale WS (on_message pub "poly_bet_alert"). Test: Mock sub.

## Phase 4: Scanners (Intel Outposts) - 6 Modules

- [ ] 14. `src/sockets/ws_manager.py` – Manager (add poly restart). Test: `docker logs`.
- [ ] 15. `src/scanners/heatmap/model1_scan.py` – Base.
- [ ] 16. `src/scanners/coin_history/aggregated.py` – Base.
- [ ] 17. `src/scanners/signals/oi_signal.py` – Base (add if poly_boost: amp strength).
- [ ] 18. `src/scanners/ranking/imbalance.py` – Base (rank hybrids).
- [ ] 19. `src/scanners/polymarket/wallet_hunter.py` – Polysights/HashDive pull, networkx graph (density>0.5=sync), insert_poly_wallet. Pub "poly_smart_wallets".
- [ ] 20. `src/scanners/polymarket/signal_oracle.py` – Score via poly_edge_math, checklist>=5 → pub "poly_signals" (hybrid if oi>0.7). 10s loop.

## Phase 5: Agents (Work Crews) - 5 Modules

- [ ] 21. `src/agents/trade/trade_executor.py` – Base (add poly_clob_exec).
- [ ] 22. `src/agents/logging/agent_log.py` – Base (tag vertical).
- [ ] 23. `src/agents/broadcast/telegram.py` – Base (add poly templates: "🚀 Insider Copy: +33% [market]!").
- [ ] 24. `src/agents/autotraders/grid_bot/main.py` – Base (sub poly for arbs).
- [ ] 25. `src/agents/autotraders/polymarket_copy/main.py` – Sub "poly_signals", ecdsa-sign CLOB, gradual exits (0.1 steps), guardian (10% cap).

## Phase 6: Dashboards (Observation Decks) - 2 Modules

- [ ] 26. `src/web/grafana/grafana_panel.py` – Base (add "Hybrid ROI: perps + poly").
- [ ] 27. `src/web/streamlit/dashboard.py` – Base (add poly tab: wallet graphs).

**Total: 27 Modules. Build one at a time. Test each on live Docker stack. Fusion: Poly modules hook perps for hybrids.**
