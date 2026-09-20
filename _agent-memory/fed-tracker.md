# Fed Tracker Agent Memory
Last updated: September 20, 2026

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.

## Reliable data sources
- Fed Funds Rate & FOMC decisions: federalreserve.gov press release pages (e.g. monetary20260916a.htm); CNBC, NPR, Fox Business cover decisions same day
- Effective rate: EFFR via NY Fed / FRED — search "effective federal funds rate EFFR [date]"; search snippets from federalreserve.gov H.15 / newyorkfed.org; sofrrate.com/policy-rates; IORB rate from Fed implementation notes gives ceiling/anchor
- Market probabilities: CME FedWatch (search for snippets via WebSearch); Polymarket for binary year-end/meeting odds; blockchain.news for Polymarket summary articles; Kalshi; predictionmarketspicks.com
- Vote breakdown: federalreserve.gov FOMC statement pages; search "FOMC [date] vote statement"
- Dot plot / SEP: Seeking Alpha, TradingKey, CNBC post-decision summaries; wolfstreet.com covers dot plots well; mishtalk.com
- Post-decision analysis: cnbc.com, seekingalpha.com, investinglive.com, foxbusiness.com, coingape.com
- FOMC minutes content: goldsilver.com, tradingview.com/news, thestreet.com, cnbc.com
- Post-Jackson Hole: benzinga.com, thestreet.com, CNBC, finchannel.com, kalshi.com/news carry reaction well
- Benzinga Prediction Markets: benzinga.com carries specific Kalshi, Polymarket, and CME figures together — excellent source
- CPI day repricing: cnbc.com; predictionmarketspicks.com; 247wallst.com
- Retail Sales: Census Bureau; seekingalpha.com covered Aug 2026 release (+0.6% MoM beat) well

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
- centralbank.watch showed 95% hike probability on weekend search (Sep 20) — likely stale/hallucinated; much higher than CME FedWatch 55.1% — ignore on weekends.
- Bloomberg.com returns readable search snippets via WebSearch even if full article is paywalled.

## Run log

### September 20, 2026 — SATURDAY (weekend, no new data)
- Target range: 3.75% – 4.00% (hiked Sep 16; unchanged)
- Effective rate: No new EFFR published (Saturday — NY Fed does not publish on weekends)
  - Last confirmed: Sep 17 EFFR = 3.88% (first full day at new range)
  - Sep 18–19 EFFR: ~3.88% (estimated; consistent with IORB 3.90%)
  - Sep 20: No publication (Saturday)
- Next meeting: October 27–28, 2026 (decision October 28 at 2pm ET = 18:00 UTC)
- CME FedWatch October 28 hike: ~55% / hold ~45% (last confirmed Sep 19 at 55.1%; stable — NOT updated today per weekend rules)
- CME FedWatch December 9 second 2026 hike: ~64% (stable; not updated today per weekend rules)
- New FOMC row added: NO (no new meeting)
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-10-28T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → September 20, 2026 (ONLY CHANGE — weekend rules apply)
- Sources: No new data sources; relying on prior-day confirmed memory per weekend hallucination policy

## CRITICAL NOTE for NEXT RUN (Sep 21 Mon morning):
- **Sep 21 (Monday)**: EFFR for Sep 18 and Sep 19 expected to be published (~3.88% both days; confirm exact figures from NY Fed/FRED)
  - Search: "effective federal funds rate September 18 2026" and "EFFR September 19 2026"
  - Update effective rate display with confirmed figures
  - Update committee notes in hero cards with the confirmed EFFR figures
- **No new FOMC meeting until October 27–28** (decision Oct 28, 2026)
- Next major data:
  - **Sep 26 (Fri approx):** Core PCE August 2026 (BEA) — MOST CRITICAL: go/no-go for Oct 28 hike; previous 3.3% YoY
  - **Oct 01 (Thu):** ISM Manufacturing PMI September 2026
  - **Oct 02 (Fri):** September 2026 Jobs Report (BLS)
  - **Oct 10 (Fri approx):** CPI September 2026 (BLS)
  - **Oct 27–28:** Next FOMC meeting (decision Oct 28)
  - **Dec 8–9:** Final 2026 FOMC meeting (decision Dec 9)
- Market probabilities entering next run:
  - October 28 hike: ~55% / hold ~45% (CME FedWatch, last confirmed Sep 19 at 55.1%)
  - December 9 second hike: ~64% (CME FedWatch, Sep 18-19; stable)
- Ticker note: Ticker at top of page still shows "FED FUNDS RATE 3.63%" (stale; should be ~3.88%). Rules say to preserve ticker exactly — do NOT update unless ticker is within a marker zone. Leave for now.
- Key Warsh quotes (confirmed Sep 16):
  - "Inflation has been too high for too long"
  - "I'm not in the forward guidance business" (re: dot plot)
- New SEP projections (Sep 16):
  - Headline PCE 2026: 3.7%; Core PCE 2026: 3.4%; Year-end 2026 median: 4.1%
  - 16 of 18 participants see at least one more 2026 hike; Warsh withheld dot
- EFFR CONFIRMED VALUES (for reference):
  - Sep 16: 3.63% (hike day; old rate; hike effective Sep 17)
  - Sep 17: 3.88% (CONFIRMED via FRED; first full day at new range)
  - Sep 18: ~3.88% (estimated; second full day; IORB 3.90%) — confirm Mon Sep 21
  - Sep 19: ~3.88% (estimated; third full day; IORB 3.90%) — confirm Mon Sep 21
  - Sep 20: No data (Saturday)
