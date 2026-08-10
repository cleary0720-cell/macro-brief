# Fed Tracker Agent Memory
Last updated: August 10, 2026

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
- IMPORTANT: CME FedWatch direction matters — always confirm if a % refers to a hike, hold, or cut. After July jobs report, "hold" is now the leading September outcome (~60%) vs "hike" (~40%).
- Dashboard agent site.md has repeatedly mislabeled CME hike probability as "cut" — always verify directional interpretation against memory notes.
- Polymarket annual odds ("rate hike in 2026?", "zero cuts in 2026?") update much more slowly than meeting-specific odds. Always note the date of the Polymarket reading.
- blockchain.news article titles with Polymarket odds can be from any day — cross-check dates in context before using.
- growbeansprout.com consistently returns cached pre-FOMC-decision data — completely stale. Ignore for directional analysis.
- defirate.com Polymarket/Kalshi data appears significantly lagged — don't use for real-time odds.
- Cleveland Fed Nowcast (confirmed Aug 10): July CPI ~3.42% YoY (down from 3.5% June); core +0.21% MoM / 2.52% YoY. This is PRE-RELEASE; actual BLS data may differ. Use as context/preview only.

## Run log

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
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-09-16T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → August 10, 2026
  - Card 1: Updated CME date ref to Aug 10; added Cleveland Fed Nowcast (July CPI ~3.42% YoY)
  - Card 2: Updated CME to Aug 10 and simplified date refs; Polymarket dates updated to Aug 10; added Cleveland Nowcast after CPI catalyst note
  - Card 3: Updated CME/Oct/Polymarket date refs to Aug 10; added Cleveland Nowcast at end
  - Rate path table: Sep row updated to Aug 10 dates, added Cleveland Nowcast bullet; Oct row updated to Aug 10
- Notes: Quiet Monday — no major data releases, no Fed speakers confirmed. EFFR stable at 3.63%. CME and Polymarket odds unchanged from Aug 9 weekend. Key new data point: Cleveland Fed Nowcast projects July CPI at ~3.42% YoY — slightly below June's 3.5%, which would confirm continued disinflation ahead of Sep 16 FOMC decision. The actual BLS CPI release on Aug 12 is the next major catalyst and could significantly reprice September hike odds.

### CRITICAL NOTE for NEXT RUN (Aug 11+):
- CME baselines as of Aug 10: ~40% Sep hike / ~60% hold / ~55% Oct hike (very stable since Aug 9)
- Kalshi Sep: ~65% hold / ~35% hike
- Polymarket baselines: Sep hike ~37% / hold ~63%; "rate hike in 2026?" ~56%; "zero cuts" ~84% (pre-jobs baseline)
- Cleveland Fed Nowcast: July CPI ~3.42% YoY / core 2.52% YoY (pre-release; actual Aug 12)
- EFFR: 3.63% stable
- CPI July 2026 releases August 12 (Tue) — THE KEY catalyst before September 16 FOMC
  - Cleveland Nowcast: headline ~3.42% YoY (down from 3.5%), monthly +0.09%
  - Core nowcast: +0.21% MoM / 2.52% YoY
  - Hawkish CPI (above 3.5% or hot core) would revive September hike odds dramatically
  - Dovish CPI (below 3.4% headline or cool core) would cement September hold
  - EXPECT MAJOR CME REPRICING on Aug 12 — update all three cards and rate path table
- Jobless Claims for week ending Aug 8: releases August 13 (Thu)
  - Prior: initial 199k / 4-wk avg 198,750 (cycle low) / continued 1,801k (+24k)
- Retail Sales July 2026: releases ~Aug 14-15 — ROLL FORWARD dashboard sparkline
- FOMC Minutes from July 29 meeting: releases ~August 19 — watch for additional context on 9-3 vote
- Aug 11: quiet, no major data; check for any Fed speaker commentary
- No new FOMC history row until Sep 16 decision
- MEANS-FOR-YOU: only update if Fed Funds Rate changes (hasn't changed since Dec 2025)
- Jackson Hole: Aug 27–29 — in all three cards; Warsh speech is next major Fed communication

### August 9, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (stable; weekend, no new EFFR publication; next release Mon Aug 10 at ~9am ET for Aug 8 data)
- CME September hike: ~40% (Aug 9; weekend, unchanged from Aug 8 close; hold leads ~60%)
- CME October hike: ~55% (Aug 9; unchanged)
- Kalshi September: ~65% hold / ~35% hike (Aug 9; first confirmed Kalshi reading for Sep)
- Polymarket September hike: ~37% / hold ~63% (Aug 9; repriced from ~48% pre-jobs Aug 6-7)
- Polymarket "rate hike in 2026?": ~56% YES (Aug 9; down from ~59% Aug 7-8, and ~78% pre-report Aug 6)
- Polymarket "zero cuts in 2026?": ~84% (Aug 5-6 pre-jobs baseline; post-jobs figure not yet confirmed)
- Jackson Hole 2026: August 27–29 — NEW: added to cards; Warsh to speak; key event before Sep 16 FOMC
- New FOMC row added: NO

### August 8, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (stable; confirmed Aug 7 from sofrrate.com)
- CME September hike: ~40% (Aug 8; continued drift lower from ~44% Aug 7)
- CME October hike: ~55% (Aug 8; down from ~58.3% Aug 7)
- Polymarket "rate hike in 2026?": ~59% YES (Aug 7–8, post-jobs; down sharply from ~78% pre-jobs Aug 6)
- New FOMC row added: NO

### August 7, 2026
- MAJOR EVENT: July 2026 Jobs Report (released Aug 7, 8:30am ET)
  - NFP: -23,000 (massive miss vs +83k consensus; first payroll contraction in months)
  - Unemployment: 4.1% (down from 4.2%, LFP fell to 61.4%)
  - Average hourly earnings: +0.1% MoM, +3.2% YoY (wages cooling)
  - Prior revisions: -103,000 combined (May -66k, June -37k)
- CME September hike: ~44% (sharply down from ~57% Aug 6; confirmed via LSEG post-jobs)
- CME September hold: ~60.4%; CME October hike: ~58.3% (post-jobs)
- New FOMC row added: NO

### August 6, 2026
- CME September hike: ~57%; Polymarket September hike: ~47%; ISM Services PMI July: 54.1

### August 3-5, 2026
- CME September hike: ~64.5% (Aug 3 post-ISM Mfg); ISM Manufacturing PMI July: 55.6

### August 2, 2026
- CME September hike: ~82%; Polymarket zero cuts: ~89.3%; Brent crude: ~$88/bbl

### August 1, 2026
- CME September hike: ~82%; Polymarket September hike: ~59.5%; Polymarket zero cuts: ~89%
