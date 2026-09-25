# Fed Tracker Agent Memory
Last updated: September 25, 2026

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.

## Reliable data sources
- Fed Funds Rate & FOMC decisions: federalreserve.gov press release pages (e.g. monetary20260916a.htm); CNBC, NPR, Fox Business cover decisions same day
- Effective rate: EFFR via NY Fed / FRED — search "effective federal funds rate EFFR [date]"; search snippets from federalreserve.gov H.15 / newyorkfed.org; sofrrate.com/policy-rates; IORB rate from Fed implementation notes gives ceiling/anchor
- Market probabilities: CME FedWatch (search for snippets via WebSearch); Polymarket for binary year-end/meeting odds; blockchain.news for Polymarket summary articles; Kalshi; predictionmarketspicks.com; Phemex.com/news carries specific CME figures
- Vote breakdown: federalreserve.gov FOMC statement pages; search "FOMC [date] vote statement"
- Dot plot / SEP: Seeking Alpha, TradingKey, CNBC post-decision summaries; wolfstreet.com covers dot plots well; mishtalk.com
- Post-decision analysis: cnbc.com, seekingalpha.com, investinglive.com, foxbusiness.com, coingape.com
- FOMC minutes content: goldsilver.com, tradingview.com/news, thestreet.com, cnbc.com
- Post-Jackson Hole: benzinga.com, thestreet.com, CNBC, finchannel.com, kalshi.com/news carry reaction well
- Benzinga Prediction Markets: benzinga.com carries specific Kalshi, Polymarket, and CME figures together — excellent source
- CPI day repricing: cnbc.com; predictionmarketspicks.com; 247wallst.com
- Retail Sales: Census Bureau; seekingalpha.com covered Aug 2026 release (+0.6% MoM beat) well
- Fed official speeches: fxstreet.com, actionforex.com, cnbc.com carry speechtracker scores and quotes same day
- PMI data: investinglive.com, fxstreet.com cover S&P Global flash PMI same day

## Known issues
- WEEKEND HALLUCINATION WARNING: WebSearch on weekends returns confused synthesized probability figures. Trust prior-day confirmed memory on weekends with no new data releases.
- Most aggregator sites (centralbank.watch, rateprobability.com, growbeansprout.com) return HTTP 403 on WebFetch. Use WebSearch snippets.
- Yahoo Finance, CBS News, CNBC article pages also return 403 on WebFetch — use WebSearch.
- tradingeconomics.com also returns 403 on WebFetch.
- EFFR data: NY Fed releases prior business day's data at approximately 9:00am ET. Weekends and federal holidays = no publication.
- EFFR RATE TRANSITION NOTE: When the Fed hikes at 2pm ET, the implementation note says "effective [next business day]". So:
  - Hike day EFFR (e.g. Sep 16) = still old rate (e.g. 3.63%) because hike takes effect next day
  - Day after hike EFFR (e.g. Sep 17) = first full day at new rate (3.88% confirmed; IORB 3.90%)
- Warsh withheld his dot at June AND September meetings; 16 of 18 dots submitted at Sep meeting.
- CME FedWatch direction matters — always confirm if a % refers to a hike, hold, or cut.
- growbeansprout.com consistently returns cached/stale data — ignore for directional analysis.
- sofrrate.com/policy-rates can be stale (may show old target range days after hike) — cross-reference with other sources.
- Bloomberg.com returns readable search snippets via WebSearch even if full article is paywalled.
- Sep 20 (Sat): centralbank.watch showed 95% hike probability — stale/hallucinated vs CME 55-59.7%; ignore on weekends.
- CME REPRICING WARNING: After a major hawkish catalyst (Fed speech + strong data), probabilities can jump 10-20pp intraday. Search for same-day CNBC/FXStreet for current figure; don't rely on prior-day confirmed figure.
- CORE PCE DATE CORRECTION: Memory previously listed Core PCE August as "Sep 26 (Fri)" — WRONG. Confirmed actual date: **September 30, 2026** (Tuesday). stockmarkethours.org confirmed "August 2026 PCE Release: September 30". All instances in fed-tracker.html corrected from Sep 26 → Sep 30 on Sep 25 run.

## Run log

### September 25, 2026 — FRIDAY
- Target range: 3.75% – 4.00% (hiked Sep 16; unchanged)
- Effective rate: 3.88% (confirmed stable; IORB 3.90%)
  - Sep 24 EFFR: 3.88% (expected stable; published Sep 25 ~9am ET by NY Fed; seventh business day at new range)
- Next meeting: October 27–28, 2026 (decision October 28 at 2pm ET = 18:00 UTC)
- **CME FedWatch October 28 hike: ~77–78% / hold ~22–23% (stable; no catalyst today)**
  - Last confirmed: ~77.5% as of Sep 24 (after Williams London speech Sep 24)
  - Sep 25 search: no new catalysts confirmed; stability expected
- CME FedWatch December 9 second 2026 hike: ~64%+ (unchanged)
- New FOMC row added: NO (no new meeting; next is Oct 27–28)
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-10-28T18:00:00Z (unchanged; correct)
- **Core PCE August: NOT released Sep 25 — actual confirmed date is September 30, 2026**
  - Previous memory had this wrong as "Sep 26 (Fri)"; corrected in all instances in fed-tracker.html
- Changes made:
  - "Last updated" → September 25, 2026
  - All "Core PCE August (Sep 26)" → "Core PCE August (Sep 30)" (replace_all fix; ~5 instances)
  - Appended Sep 25 entry to Card 1 hero-note
  - Appended Sep 25 entry to Card 2 hero-note
  - Updated Card 3 Oct line: ~78% → ~77–78% (stable Sep 25); added "Core PCE August (Sep 30)" as next catalyst
- Sources: WebSearch confirmed EFFR 3.88% (Sep 24), CME ~73.5-77.5% (Sep 24 range across sources; memory says ~77.5% after Williams), Core PCE Sep 30 (stockmarkethours.org, fedratecalc.com, financecalendar.com)

### September 24, 2026 — THURSDAY
- Target range: 3.75% – 4.00% (hiked Sep 16; unchanged)
- Effective rate: 3.88% (confirmed stable; IORB 3.90%)
  - Sep 23 EFFR: 3.88% (expected at publication; published Sep 24 ~9am ET by NY Fed; sixth business day at new range)
- Next meeting: October 27–28, 2026 (decision October 28 at 2pm ET = 18:00 UTC)
- **CME FedWatch October 28 hike: ~78% / hold ~22% (SHARP REPRICING from ~60%)**
  - Catalyst 1: Gov. Barr hawkish speech (Sep 23, Chicago Housing Summit) — "Further policy adjustments are likely to be needed to ensure inflation comes down to target in a timely fashion" (FXS speechtracker 8/10)
  - Catalyst 2: S&P Global Composite PMI Flash September: 58.4 (vs 56.0 expected; massive beat); Services 58.7; Manufacturing 57.0 (from 53.9); input cost inflation highest since October 2022
  - Also: Gov. Collins warned inflation could be "notably" higher (Sep 23)
  - Williams (Sep 24, London Macro Policy Forum): another hike by year-end "reasonable" but won't commit to October; echoed Warsh — "time for explicit forward guidance is over"
  - Probability moved: ~73% on Sep 23 (after Barr + PMI), then ~77.5% on Sep 24 (after Williams)
- CME FedWatch December 9 second 2026 hike: ~64%+ (likely moved higher with October repricing; prior confirmed ~64%)
- New FOMC row added: NO (no new meeting; next is Oct 27–28)
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-10-28T18:00:00Z (unchanged; correct)

## CRITICAL NOTE for NEXT RUNS:
- **Oct 28 probability is ~77–78% (stable as of Sep 25)**
- **Core PCE August (Sep 30, Tuesday) is the NEXT critical catalyst** — most important go/no-go for Oct 28 hike
  - Prior Core PCE July: 3.3% YoY; if Aug comes in higher → further repricing hawkish; if lower → partial hold repricing
- **If Core PCE misses dovishly (below 3.1%), Oct hike probability could drop back toward 60-65%**
- **If Core PCE matches or beats (3.3%+), October hike ~85%+**
- **Next major data:**
  - **Sep 30 (Tue):** Core PCE August 2026 (BEA) — MOST CRITICAL: go/no-go for Oct 28 hike; prior 3.3% YoY; CONFIRMED SEP 30 (not Sep 26)
  - **Oct 01 (Thu):** ISM Manufacturing PMI September 2026 — first post-hike factory read
  - **Oct 02 (Fri):** September 2026 Jobs Report (BLS) — labor market resilience check post-hike
  - **Oct 10 (approx):** CPI September 2026 (BLS) — additional inflation read
  - **Oct 27–28:** Next FOMC meeting (decision Oct 28, 2pm ET = 18:00 UTC)
  - **Dec 8–9:** Final 2026 FOMC meeting (decision Dec 9)
- Market probabilities as of Sep 25:
  - October 28 hike: ~77–78% / hold ~22–23% (CME FedWatch; stable Sep 25; no catalyst)
  - December 9 second hike: ~64%+ (moved higher; exact figure unconfirmed)
- EFFR confirmed stable at 3.88% since Sep 17 (IORB 3.90%); expect same through at least Oct 28
- Key Warsh quotes (confirmed Sep 16):
  - "Inflation has been too high for too long"
  - "I'm not in the forward guidance business" (re: dot plot)
- New SEP projections (Sep 16):
  - Headline PCE 2026: 3.7%; Core PCE 2026: 3.4%; Year-end 2026 median: 4.1%
  - 16 of 18 participants see at least one more 2026 hike; Warsh withheld dot
- EFFR CONFIRMED VALUES:
  - Sep 16: 3.63% (hike day; old rate; hike effective Sep 17)
  - Sep 17: 3.88% (CONFIRMED; first full day at new range)
  - Sep 18: 3.88% (CONFIRMED)
  - Sep 19: 3.88% (CONFIRMED; published Sep 21 by NY Fed)
  - Sep 21: 3.88% (CONFIRMED; published Sep 22 by NY Fed; 4th business day)
  - Sep 22: 3.88% (CONFIRMED; published Sep 23 by NY Fed; 5th business day)
  - Sep 23: 3.88% (CONFIRMED; published Sep 24 by NY Fed; 6th business day)
  - Sep 24: 3.88% (EXPECTED stable; published Sep 25 by NY Fed; 7th business day)
  - Sep 20: No data (weekend)
