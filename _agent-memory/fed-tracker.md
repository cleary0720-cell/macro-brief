# Fed Tracker Agent Memory
Last updated: August 12, 2026

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.

## Reliable data sources
- Fed Funds Rate & FOMC decisions: federalreserve.gov press release pages (e.g. monetary20260617a.htm); CNBC, NPR, Fox Business cover decisions same day
- Effective rate: EFFR via NY Fed / FRED — search "effective federal funds rate EFFR [date]"; search snippets from federalreserve.gov H.15 / newyorkfed.org; sofrrate.com/policy-rates
- Market probabilities: CME FedWatch (search for snippets via WebSearch); Polymarket for binary year-end/meeting odds; blockchain.news for Polymarket summary articles
- Vote breakdown: federalreserve.gov FOMC statement pages; search "FOMC [date] vote statement"
- Dot plot / SEP: Seeking Alpha, TradingKey, CNBC post-decision summaries carry dot plot details
- Post-decision analysis: sherwood.news, coinpedia.org, forexfactory.com, interactivecrypto.com
- FOMC minutes content: goldsilver.com, tradingview.com/news, thestreet.com, cnbc.com, interactivecrypto.com, ig.com/uk — all covered July 8 release well
- ISM PMI: prnewswire.com carries official ISM press releases; babypips.com, investinglive.com, forexfactory.com, neilsethi.substack.com good sources
- Jobs Report: qz.com, foxbusiness.com, nbcnews.com all covered July 2026 jobs release well
- Jobless Claims: verifiedinvesting.com, bloomberg.com, fastcompany.com, academic-capital.com all cover weekly releases
- CME post-data repricing: Yahoo Finance (search "US rate futures [meeting] probability"), Convera ("weak jobs print resets Fed bets"), cryptobriefing.com all covered post-jobs CME repricing clearly with specific percentage figures
- CPI release: foxbusiness.com, nbcnews.com, cnbc.com, washingtonexaminer.com all covered July 2026 CPI well with specific figures
- Cleveland Fed Nowcast: clevelandfed.org/indicators-and-data/inflation-nowcasting — search snippets via WebSearch; good for pre-release CPI forecasts

## Known issues
- Most aggregator sites that display CME FedWatch data (centralbank.watch, rateprobability.com, atlantafed.org, growbeansprout.com, morningstar.com, interactivecrypto.com, sofrrate.com) return HTTP 403 on WebFetch. Use WebSearch and read snippets.
- Yahoo Finance, CBS News, CNBC article pages also return 403 on WebFetch — use WebSearch to pull snippets.
- tradingeconomics.com also returns 403 on WebFetch.
- fxstreet.com analysis pages return 403 (including AMP versions).
- kucoin.com also returns 403 on WebFetch.
- EFFR data: NY Fed releases prior business day's data at approximately 9:00am ET. Weekends and federal holidays = no publication.
- Polymarket and CME FedWatch can diverge significantly — note both when available.
- Warsh withheld his dot at June meeting; 18 dots submitted going forward (not 19). May change at future meetings.
- sofrrate.com page title may show weekly average EFFR rather than daily EFFR — prefer ycharts/NY Fed for daily figure.
- WebSearch snippets about Polymarket may mix current odds with older quotes; cross-check against CME FedWatch for consistency.
- IMPORTANT: CME FedWatch direction matters — always confirm if a % refers to a hike, hold, or cut.
- HALLUCINATION WARNING: WebSearch CME results sometimes synthesize probability figures that contradict all other evidence. Cross-check against Polymarket, Kalshi, and prior-day baselines before using.
- Post-CPI repricing: CPI July 2026 (Aug 12) caused CME to reprice from ~40% hike to ~50% hike — even a "dovish" (in-line) CPI reading can shift markets toward hike if the headline remains elevated (3.4% >> 2% target).
- Polymarket September odds sometimes lag intraday CME moves by hours; when CME reprices on data day, cite Polymarket as "repricing" with a range rather than a precise figure.
- KuCoin article titled "Polymarket Prices 53% Odds of Fed Rate Hike in September 2026 vs. 32% in Futures" — dates in this article are UNRELIABLE; CME September hike was never at 32% in our tracking period. Treat as anecdote only.
- growbeansprout.com consistently returns cached pre-FOMC-decision data — completely stale. Ignore for directional analysis.
- defirate.com Polymarket/Kalshi data appears significantly lagged — don't use for real-time odds.

## Run log

### August 12, 2026 — CPI DAY
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (stable; Aug 11 data for Aug 10; Aug 12 data for Aug 11 expected same)
- Next meeting: September 15–16, 2026 (decision Sep 16 at 2pm ET)
- **CPI July 2026 ACTUAL (released 8:30am ET Aug 12):**
  - Headline: +0.1% MoM, +3.4% YoY (down from 3.5% June — modest disinflation; in line with consensus)
  - Core: +0.2% MoM, +2.5% YoY (down from 2.6% June; very close to Cleveland Nowcast of 2.52%)
  - Components: Shelter +0.1%; food +0.1%; new vehicles +0.1%; used cars +0.4%; medical care +0.4%; airline fares +2.2%
  - Sources: Fox Business, NBC News, CNBC, Washington Examiner all confirmed 3.4%/2.5%
- CME September post-CPI (Aug 12): ~50% hold / ~50% hike (repriced from ~60%/40% Aug 11)
- Polymarket September hike: ~38%–53% (repricing in progress on Aug 12; prior day Aug 11: ~38%; CME now at ~50%; Polymarket lagging toward convergence)
- Polymarket "rate hike in 2026?": ~56% (Aug 12; stable from Aug 11)
- Polymarket "zero cuts in 2026?": ~84% (stable; baseline from Aug 5–6)
- New FOMC row added: NO (next is September 16, 2026)
- MEANS-FOR-YOU: not updated (rate unchanged since Dec 2025)
- JS countdown: 2026-09-16T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → August 12, 2026
  - Card 1: CME odds updated to ~50% post-CPI; CPI July actual results added; Cleveland Nowcast noted as pre-release (matched actual)
  - Card 2: CME updated to ~50% hike; Polymarket range noted as repricing; "CPI releases Aug 12" → "CPI released Aug 12" with actual results; catalysts updated to Jackson Hole + August CPI Sep 10
  - Card 3: CPI July inline with actual results; CME updated to ~50% hike; Polymarket range noted
  - Rate path table: Sep row updated with actual CPI + new CME odds; Oct row cleaned up
- Notes: Big data day — July CPI met expectations exactly. Headline 3.4% (Cleveland Nowcast had called 3.42%; actual 3.4%). Core 2.5% (Nowcast: 2.52%; actual 2.5%). Still well above 2% target. CME repriced hawkishly to 50/50 despite "dovish" print — suggests markets interpreted in-line reading as not enough to warrant hold. Essentially, the job report shock (Aug 7: -23k NFP) has now been partially reversed by CPI not being softer. The Sep 16 FOMC decision is now genuinely a coin flip. Jackson Hole (Aug 27–29) is the next key event.

### CRITICAL NOTE for NEXT RUN (Aug 13):
- CME baselines as of Aug 12: ~50% Sep hike / ~50% hold; ~55% Oct hike (pre-CPI baseline; may reprice slightly)
- Polymarket baselines: Sep hike ~38–53% (repricing); "hike in 2026?" ~56%; "zero cuts" ~84%
- EFFR: 3.63% stable
- Jobless Claims for week ending Aug 8: releases August 13 (Thu) at 8:30am ET
  - Prior: initial 199k / 4-wk avg 198,750 (cycle low) / continued 1,801k (+24k)
  - A reading below 200k again would be hawkish; above 210k could reinforce hold camp
  - Search "jobless claims August 13 2026" — this is a key next catalyst
- Retail Sales July 2026: releases ~Aug 14-15 — ROLL FORWARD dashboard sparkline (not fed-tracker)
- FOMC Minutes from July 29 meeting: releases ~August 19 — watch for context on 9-3 vote and internal debate
- Next big Fed-tracker catalysts: Jobless claims Aug 13, then FOMC Minutes Aug 19, then Jackson Hole Aug 27–29
- No new FOMC history row until Sep 16 decision
- MEANS-FOR-YOU: only update if Fed Funds Rate changes (hasn't changed since Dec 2025)
- Jackson Hole: Aug 27–29 — Warsh to speak; last major Fed communication before Sep 16 FOMC

### August 11, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (stable; Aug 10 data published today; confirmed stable)
- Next meeting: September 15–16, 2026 (decision Sep 16 at 2pm ET)
- CME September hike: ~40% (Aug 11; unchanged; hold leads ~60%)
- CME October hike: ~55% (Aug 11; unchanged)
- Kalshi September: ~65% hold / ~35% hike (Aug 11; stable)
- Polymarket September hike: ~38% / hold ~61% (Aug 11; marginally shifted from ~37%/63%)
- Polymarket "rate hike in 2026?": ~56% YES (Aug 11; stable)
- Polymarket "zero cuts in 2026?": ~84% (pre-jobs baseline; stable)
- Cleveland Fed Nowcast (Aug 11 update): July CPI ~3.42% YoY (unchanged from Aug 10); core CPI +0.21% MoM / 2.52% YoY. NEW August month nowcast: headline ~3.22% YoY (continued decline); core PCE ~3.36% (slight reacceleration — potential red flag)
- US-Iran: Negotiations at impasse; Brent crude near $90/bbl (updated from ~$88)
- Jackson Hole 2026: August 27–29 — Warsh to speak; key event before Sep 16 FOMC
- New FOMC row added: NO (next is September 16, 2026)
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-09-16T18:00:00Z (unchanged; correct)

### August 10, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (stable; Aug 8 data published today at ~9am ET; confirmed unchanged)
- Next meeting: September 15–16, 2026 (decision Sep 16 at 2pm ET)
- CME September hike: ~40% (Aug 10; unchanged from Aug 9 weekend close; hold leads ~60%)
- CME October hike: ~55% (Aug 10; unchanged)
- Kalshi September: ~65% hold / ~35% hike (unchanged)
- Polymarket September hike: ~37% / hold ~63% (stable from Aug 9)
- Polymarket "rate hike in 2026?": ~56% YES (Aug 10; stable from Aug 9; down from ~78% pre-jobs)
- Polymarket "zero cuts in 2026?": ~84% (pre-jobs baseline; post-jobs figure not yet confirmed)
- Cleveland Fed Nowcast (Aug 10): July CPI ~3.42% YoY (down from 3.5% June); monthly +0.09%; core +0.21% MoM / 2.52% YoY — pre-release estimate; actual releases Aug 12
- Jackson Hole 2026: August 27–29 — Warsh to speak; key event before Sep 16 FOMC
- New FOMC row added: NO (next is September 16, 2026)

### August 9, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (stable; weekend)
- CME September hike: ~40% (Aug 9; weekend, unchanged from Aug 8 close; hold leads ~60%)
- CME October hike: ~55% (Aug 9; unchanged)
- Kalshi September: ~65% hold / ~35% hike (Aug 9; first confirmed Kalshi reading for Sep)
- Polymarket September hike: ~37% / hold ~63% (Aug 9; repriced from ~48% pre-jobs Aug 6-7)
- Polymarket "rate hike in 2026?": ~56% YES (Aug 9; down from ~59% Aug 7–8, and ~78% pre-report Aug 6)
- Jackson Hole 2026: August 27–29 — NEW: added to cards; Warsh to speak; key event before Sep 16 FOMC

### August 8, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (stable)
- CME September hike: ~40% (Aug 8; continued drift lower from ~44% Aug 7)
- CME October hike: ~55% (Aug 8; down from ~58.3% Aug 7)
- Polymarket "rate hike in 2026?": ~59% YES (Aug 7–8, post-jobs; down sharply from ~78% pre-jobs Aug 6)

### August 7, 2026
- MAJOR EVENT: July 2026 Jobs Report (released Aug 7, 8:30am ET)
  - NFP: -23,000 (massive miss vs +83k consensus; first payroll contraction in months)
  - Unemployment: 4.1% (down from 4.2%, LFP fell to 61.4%)
  - Average hourly earnings: +0.1% MoM, +3.2% YoY (wages cooling)
  - Prior revisions: -103,000 combined (May -66k, June -37k)
- CME September hike: ~44% (sharply down from ~57% Aug 6; confirmed via LSEG post-jobs)
- CME September hold: ~60.4%; CME October hike: ~58.3% (post-jobs)

### August 6, 2026
- CME September hike: ~57%; Polymarket September hike: ~47%; ISM Services PMI July: 54.1

### August 3-5, 2026
- CME September hike: ~64.5% (Aug 3 post-ISM Mfg); ISM Manufacturing PMI July: 55.6

### August 2, 2026
- CME September hike: ~82%; Polymarket zero cuts: ~89.3%; Brent crude: ~$88/bbl

### August 1, 2026
- CME September hike: ~82%; Polymarket September hike: ~59.5%; Polymarket zero cuts: ~89%
