# 🤖 AGENT PLAYBOOK — VINCE QUANT WHALE HELIX

This is the street-level guide for every ChatGPT / Claude / Grok session that jumps into the repo. Treat it like mission control: run the pre-flight checks, follow the build phases, and leave breadcrumbs for the next agent.

---



- **Heatmap ground truth checkpoint (memorize this stack):**
  - `FINAL_AGENT_COMMUNICATION_GROUND_TRUTH.md`
  - `ROUND2_VERIFICATION_ALL_AGENTS_CONFIRMED.md`
  - `docs/AGENT-SYNC-COINGLASS-MODEL-DISCOVERY.md`
  - `AI_AGENT_HANDOFF_COINGLASS_MODEL_ANALYSIS.md` and all agent response files
  - Raw API captures: `zzzzzz*/zzzzzzz*/zzzzzzzz*` (each model × timeframe)
  - Summary table: `docs/heatmap-verification/BTC-12h-model-comparison.md`
  - Liquidation map primer: `docs/liquidation-reference/LIQUIDATION_MAPS.md`
  - Strategy anchor: `ZZZZzzzzzLiquidation-is-all-that-matters.md`
  - Canonical behavior snapshot:
    * Model 1 — standard schema all ranges, intraday band
    * Model 2 — alternate keys (`y/liq/prices`) on 180d & 1y, 58 420 rows (180d), 53 115 rows (1y)
    * Model 3 — macro band, heaviest payload; archive in Parquet/Arrow
## 1. Pre-Flight Ritual (Do This First)
- **Sync with the map:** skim `CHATGPT-FINAL-PRD-1-WITH-EVERYTHING.MD` ➟ this is the canonical PRD + Google Maps analogy.  
- **Check workspace health:** `git status -sb`. If other automation is modifying files, pause and align before touching anything.  
- **Verify services:** `docker ps` must show `vince-timescaledb`, `vince-redis`, `vince-grafana` as healthy. We now ship a clean schema: if hypertables are missing, re-run `docker-compose down && rm -rf db/timescaledb_data && docker-compose up -d`.  
- **Config sanity:** `.env` already exists with placeholders. Never hard-code secrets; always consume via `src/utils/config_utils.py`.  Use `config/.env.example` as the template when sharing with other agents.
- **Focus reminder:** Per Vince, nail Bybit/perps execution first; Polymarket features are second phase once the perps auto-trader is rock solid.

---

## 2. Mission Brief
- **Goal:** build the hybrid perps + Polymarket platform, exactly as laid out in the PRD. Perps deliver liquidation edge (yang), Polymarket adds event oracle foresight (yin).  
- **Fusion rule:** every Polymarket feature must link back to perps intelligence (e.g., redis channels, shared risk math).  
- **Documentation orbit:**  
  - `TASKS.md` ➟ phase checklist (27 modules).  
  - `VINCE-QUANT-WHALE-EMPIRE-INTEGRATION.md` + `z-FILE TREE-UNDERSTANDING-VINCENT-GOOGLE-MAPS-ANALOGY.MD` ➟ structural references.  
  - `docs/API-TOKENS-ENDPOINTS.md` ➟ data sources.  
  - `docs/mcp/` ➟ tool configuration breakdown (ChatGPT vs Claude folders).  

---


- **Liquidation reference hub:** see `docs/liquidation-reference/` for consensus docs, raw API dumps, and schema behavior.
- **Heatmap ingestion:** background `full_heatmap_scan.py` loop (nohup) is populating `liquidation_data_raw`; monitor via `logs/heatmap_scanner_*.log` and Timescale queries.
## 2.5 ROUND 10 COORDINATION (Oct 29, 2025 @ 5:52 AM)

**SCANNER DEPLOYMENT STATUS:**
- ✅ Full universe scanner LIVE (PID 2174)
- ✅ 289+ snapshots stored, 20.5/minute rate
- ✅ ALL 4 agents synchronized (Agent 1 lead, Agent 2 support, Agent 3 fix deployed, Agent 4 monitoring)
- ✅ Agent 3's PYTHONPATH fix critical for background stability
- ✅ Partial storage working (0G, CHEEMS proof)
- ✅ Time-series snapshots capturing liquidation shifts

**Agent Responsibilities:**
- Agent 1 (Claude Code): Monitor scanner health, verify normalizer when M2 180d/1y data appears
- Agent 2 (Copilot): Data quality review after first full cycle, Phase 2 consensus view prep
- Agent 3 (ChatGPT): Scanner fix successful, documentation updates post-cycle
- Agent 4 (Docker Terminal): Infrastructure monitoring, performance metrics after 24h

---

## 3. Infrastructure Status (✅ PRODUCTION DEPLOYED - Round 9/10)
- **TimescaleDB:** ✅ LIVE with 289 snapshots stored (14 min runtime, 20.5 rows/min). Hypertables healthy, schema correct (`liquidation_data_raw`). Database: `quantprod`.  
- **Redis:** ✅ Running, pub/sub channels active for scanner updates.  
- **Grafana:** Running on `http://localhost:3000` (credentials in `.env`). Dashboards pending Phase 6.  
- **Scanner:** ✅ PID 2174 (`full_heatmap_scan.py`) stable, launched via `scripts/launch_heatmap_scanner.sh` (Agent 3's PYTHONPATH fix).  
- **Team Status:** ALL 4 AGENTS ALIGNED (Claude/Copilot/ChatGPT/Docker), ZERO CONFLICTS.

---

## 4. Build Phases Checklist
Keep the phases in order; mark progress in `TASKS.md` and commit after each module.

| Phase | Scope | Status | Notes |
| --- | --- | --- | --- |
| 1. Utilities | `config_utils`, `timescale_utils`, `redis_utils`, `data_utils`, `error_utils` | ✅ done | Verify new helpers before math layer uses them. |
| 2. Math | `cluster_math`, `wick_math`, `risk_math`, `sl_tp_math`, `poly_edge_math` | ✅ done | Follow-up: add unit tests for edge cases (empty datasets, Kelly sizing). |
| 3. Sockets | `coinglass_ws`, `bybit_ws`, `polymarket_ws`, `ws_manager` | 🚧 not started | Plan for Nevua/PolyTale auth via config. |
| 4. Scanners | **HEATMAP ✅ DEPLOYED (Round 9/10)**, history, signals, ranking, polymarket hunters/oracle | � heatmap live | **PID 2174 stable, 289 snapshots, 20.5/min, ALL 4 agents aligned.** Remaining scanners: design redis payload schemas before coding. |
| 5. Agents | Trade execution, logging, broadcast, grid bot, poly copy bot | 🚧 | `trade_executor` must respect `POLY_RISK_CAP`. |
| 6. Dashboards | Grafana panels, Streamlit UI | 🚧 | After DB populated, wire Grafana queries + Streamlit tabs. |

Whenever you finish a module, rerun targeted tests (e.g., `python3 -m src.utils.data_utils`) and commit with clear messages (`Phase X Module Y done`). Push to `origin/master` unless coordination dictates otherwise.

---

## 5. Operational Guardrails
- **No hard resets:** never `git reset --hard` or wipe files without explicit user request.  
- **Env-first:** all secrets and configurable values live in `.env`, surfaced through `config_utils`.  
- **Logging:** log to `data/logs/<vertical>/<agent>.log`. Create subfolders as needed.  
- **Data paths:** respect the directory contract from the PRD (`data/incoming/…`, `data/signals/…`, etc.).  
- **Retry policy:** wrap external calls with `error_utils.retry_on_failure`.  
- **Schema alignment:** before writing DB code, confirm the table structure in the SQL files. Keep polymarket and perps tables fused via shared keys (e.g., `vertical` column).

---

## 6. Daily Cadence for Agents
1. **Morning sweep:** pull latest (`git pull`), review `CHATGPT-FINAL-PRD-1-WITH-EVERYTHING.MD` diff, check Docker health.  
2. **Task selection:** pick next unchecked item in `TASKS.md`. Update the list as you work.  
3. **Implementation:** write code with small commits; run module self-tests.  
4. **Validation:** if the module touches Timescale or Redis, use the docker containers to smoke test (psql, redis-cli).  
5. **Documentation:** add any findings to `docs/heatmap-verification/FINDINGS.md` or equivalent folder so Claude/ChatGPT stay synchronized.  
6. **Handoff:** summarize changes in chat (logs, git status) before ending the session.

---

## 7. Known Open Items
- ✅ **ROUND 9/10 COMPLETE:** Heatmap scanner deployed and stable (PID 2174, 14+ min, 289 snapshots).  
- ✅ **Agent 3's Fix:** PYTHONPATH launcher script (`scripts/launch_heatmap_scanner.sh`) prevents nohup crash.  
- ✅ **All 4 Agents Aligned:** Claude (lead), Copilot (support), ChatGPT (infra fix), Docker (monitoring) - ZERO CONFLICTS.  
- ⏳ **Next Milestone:** First full cycle completion (~73 min remaining), then Agent 2 data quality review.  
- 🚧 Phase 3 sockets: Build `coinglass_ws` after scanner proves stable for 24h.  
- 🚧 Redis / Grafana dashboards: Build in Phase 6 after 24h+ uptime proven.

---

## 8. Point People & Communication
- **Vince (human owner):** final authority on structure, analogies, and priorities.  
- **Agent collaboration:** if running multiple models (ChatGPT + Claude), note progress in chat + update shared docs so cross-agent memory stays aligned.  
- **Escalation:** when blocked on infra (e.g., DB migrations), pause and notify Vince rather than guessing.

---

### TL;DR
Start with the map, respect the grid, build one street at a time, and leave the city cleaner than you found it. The trillion-dollar helix depends on every agent following this playbook. Go build.
