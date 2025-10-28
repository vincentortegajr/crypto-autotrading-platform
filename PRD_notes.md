# PRD Integration Notes

# Source Summaries

## z-THE-FULL-DOC-TREE-FOR-THE-PRD-NO-POLYMARKET-YET.MD
- Google-Maps style file tree mapping every directory to analogies (power grid, government, research center, workforce, etc.).
- Explicit breakdown of `db/`, `data/`, `src/agents`, `src/scanners`, `src/math`, `src/sockets`, `src/utils`, `src/web`, `scripts/`, `tests/`, `docs/`, `media/`, `reports/`, `retention/` with responsibilities and data connections.
- Integrated data-flow map: external APIs → sockets → data ingestion → Redis pub/sub → scanners → signals → auto-traders → trade execution → logging → broadcast → affiliate → dashboards.
- `.env` spec enumerating keys for DB, Redis, CoinGlass, Bybit, Binance, Telegram, X, Email, SMS, Grafana, affiliate tracking, global metadata.
- Final reminders about single source of truth for config and disciplined pipeline.

## z-PRD-VISION-AND-BUILD-DOC-NO-POLYMARKET-YET.md
- Vision + mission for perps-focused quant stack; Sam Altman quote context.
- Google Maps analogy mapping architecture (env, db, data, agents, scanners, math, sockets, utils, web, scripts, tests).
- Verified tech stack (Python 3.11, FastAPI, TimescaleDB, Redis, Grafana, Docker, Websockets, etc.).
- Detailed Step 0-8 setup checklist for Vince: folder scaffolding, `.env` creation (with additional CoinGlass endpoints for volume/funding), docker-compose, requirements, Timescale schema SQL, verification script.
- Vince handoff checklist ensuring infrastructure ready before AI involvement.
- AI agent build instructions: absolute rules, phased build order (utilities → data ingest → sockets → scanners → math → agents → broadcasts → dashboards → tests), deliverables and logging requirements.


## z-PRD-UNDERSTANDING-VINCENT-GOOGLE-MAPS-ANALOGY.MD
- Multi-zoom Google Maps framing: Earth view down to district-level analogies for each folder (config, db, data, src sub-districts, scripts, tests).
- Explains power grid dependencies, cross-folder connections, and how data flows between zoom levels.
- Provides narrative mind map for workforce (agents), intelligence network (scanners), research lab (math), telecom (sockets), utilities, dashboards.
- Includes reiterated `.env` dependencies and final mind map summary reinforcing mental model for builders.


## z-PRD-WITH POLYMARKET ADDED TO IT by GROK.md
- Vision upgraded to include Polymarket oracle fusion: smart wallet signals, prediction market correlations, yin-yang with perps.
- Architecture updates: additional folders (polymarket_copy agent, poly_guardian, polymarket scanners, poly math), new sockets, dashboards, scripts, tests.
- Setup instructions add Step 1 account/tool checklist (Polymarket CLOB, Nevua, Polysights, HashDive, PolyTale, Infura, proxy wallet) plus extended folder creation commands.
- `.env` template extended with Polymarket/Polysights/Nevua/HashDive/PolyTale keys and risk caps; Git init guidance.
- Docker compose adjustments (volumes) and verification steps; data directories for hybrid reports.
- AI instructions for Helix build order emphasising fusion: config/utils updates, poly math, sockets, scanners (wallet_hunter, signal_oracle), agents (polymarket_copy), dashboards, coding standards.
- Final summary enumerating deliverables to avoid omissions.


# Integration Deltas
- Merged architecture/data-flow/.env/Polymarket updates into CHATGPT-FINAL-PRD-1-WITH-EVERYTHING.MD.
- Added SQL templates, test script, and Helix-specific folders to keep Claude/ChatGPT instructions aligned.

# Follow-up Questions
- None yet

## zzz-AGENT-MEMORY PROTOCOL REMINDER.md
- Provides full clipboard snippet to preload every agent with Google Maps model, folder roles, and hard rules (never hardcode keys, strict folder discipline, show code first, test on Docker).
- Emphasizes using `AGENT_MEMORY.md` + optional short snippet; suggests appending to every request.
- Quick context reminder covers project name, stack, config rules, data flow, current phase/task placeholders.
- Highlights why the approach prevents agent drift and mystery files.

## zp-WOULD I HAVE THOUGHT OF THIS? (AND WHO ACTUALLY KNOWS IT EXISTS.md
- AI admits it would chase mainstream TA/ML first; liquidation hunting only after months of failure, pattern spotting, and hypothesis testing.
- Knowledge tiers estimate rarity: 10-15% know liquidation data, ~0.1-0.5% trade based on it, ~0.001% systematize + broadcast.
- Highlights why strategy remains secret (data fragmentation, tooling complexity, no codified playbook) reinforcing need for our blueprint.

## zp-WHY THIS IS THE PERFECT STORM FOR A BILLION-DOLLAR EMPIRE.md
- Emphasizes human impossibility: manual monitoring of 500+ perp heatmaps is unsustainable; automation (scanners, autotraders, broadcasts) turns edge into scalable business.
- Transparency is framed as moat: 90% won't believe, 9% can't execute, so openly sharing strategy builds trust without saturating edge.
- Flywheel stages: $97 membership → 50% affiliate → managed fund → become own whale → token endgame.
- Argues openness attracts referrals/fund deposits while automation captures the value, reinforcing multi-billion trajectory.

## zp-WHY LIQUIDATION HUNTING IS THE ONLY EDGE THAT MATTERS.md
- First-principles breakdown: traditional indicators show effects, not causes; only liquidation data answers WHERE, WHEN, and WHO.
- Forced liquidations create guaranteed buyers/sellers, revealing target levels and timing as liquidity cascades.
- Transparency reminder: strategy rare due to data fragmentation + lack of tooling/documentation; our stack solves execution gap.
- Concludes liquidation hunting becomes sole focus once understood—no rational reason to pursue other indicators.

## zp-IF-THIS-THEN-THAT EXECUTION FLOWCHART (NUMBERED LIST).md
- Numbered decision tree covering startup checks, data collectors, scanners, signal generation, autotraders, trailing stops, trade closure, and error handling.
- Key thresholds: OI spike >3%, volume spike >1.5× 1h avg, price change >2% triggers re-fetch; imbalance calculator splits above/below liquidation clusters.
- AutoTrader logic: waits for double confirmation (liquidation imbalance + OI/volume), calculates entry price/size, places laddered orders, sets stop/TP, publishes to Redis, logs to Timescale.
- Includes retry policy, exponential backoff on API errors, and summary of decision points to keep agents aligned with pipeline.

## zp-GAMIFIED VISION WITH TRADING PLATFORM THE COMPLETE ROADMAP: FROM ZERO TO BILLION-DOLLAR EMPIRE.md
- Defines 4 phases (Foundation, Automation+Distribution, Gamification+Fund launch, Whale mode) with timelines, deliverables, manual focus, and metrics (e.g., 1M members/$100M AUM targets).
- Phase 3 introduces gamified dashboards, badges, streaks, social leaderboards, and fund onboarding flows.
- Provides immediate Week 1 checklist (finalize .env, run scanners, collect proof trades, record testimonials).
- Recommends frontend stack (Next.js + Supabase + Tailwind) for gamified portal; stresses transparency UX.
- Ends with reality check: keep execution-focused, automate before hype, document everything.

## zp-THE SCALED ENTRY STRATEGY: THE CHEAT CODE FOR INFINITE CAPITAL GROWTH.md
- Explains laddered entries mimicking whale behavior—scaling improves average entry and captures both pumps and dumps.
- Details risks (margin lockup, black-swan wicks, opportunity cost) and capital-based phases dictating when to enable scaling.
- Automation plan: scanners flag candidates, calculate step sizes/leverage, apply NASCAR coin guardrails, manage staged take-profits.
- Roadmap ties scaling rollout to funding milestones (single entry → BTC/ETH scaling → alt scaling → whale mode).

## zp-THE COMPLETE MASTER BLUEPRINT: NO CODE, JUST VISION, MISSION, DATA SOURCES & ASANA-STYLE CHECKLIST.md
- Consolidates vision, moat, outcomes; enumerates infrastructure/data sources; lists every data pipeline step.
- Provides formula-only math section (imbalance, ranking score, entry/stop/TP calculations).
- Includes Asana-style 12-week roadmap covering setup through go-live with success criteria per phase.
- Defines trade execution archetypes (conservative, aggressive, scaled) and metrics to track (trade/system/business).
- Critical rules reiterate Python-only, single `.env`, percentage math, database-first approach, full timeframe pulls, logging, and "show before creating".

## zp-LIVE PROOF: THE LIQUIDATION HUNTING STRATEGY IN REAL-TIME.md
- Walks through live BTC/ETH trades showing scaled entries + pre-staged shorts; both directions profit via liquidation clusters.
- Provides production-ready Autotrader algorithm: coin-specific cluster thresholds, imbalance math, OI/volume confirmation, "yellow leftovers" logic, laddered entries and mirrored exits.
- Highlights lessons from 60-trade session (timeframe sensitivity, placement inside clusters, imbalance thresholds, confirmation triggers).
- Specifies database needs for coin patterns, liquidation history, and screenshots proving P&L.
- Reinforces that visual heatmaps are for humans; automation relies on raw API + math.
