# Fed Tracker Agent Memory
Last updated: September 23, 2026

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
- Bloomberg.com returns readable search snippets via WebSearch even if full article is paywalled.
- Sep 20 (Sat): centralbank.watch showed 95% hike probability — stale/hallucinated vs CME 55-59.7%; ignore on weekends.

## Run log

### September 23, 2026 — WEDNESDAY
- Target range: 3.75% – 4.00% (hiked Sep 16; unchanged)
- Effective rate: 3.88% (confirmed stable; IORB 3.90%)
  - Sep 22 EFFR: 3.88% (confirmed; fifth full business day at new range; published Sep 23 ~9am ET by NY Fed)
- Next meeting: October 27–28, 2026 (decision October 28 at 2pm ET = 18:00 UTC)
- CME FedWatch October 28 hike: ~60% / hold ~40% (stable; no repricing Sep 23; last confirmed 59.7% as of Sep 20)
- CME FedWatch December 9 second 2026 hike: ~64% (stable; unchanged)
- New FOMC row added: NO (no new meeting; next is Oct 27–28)
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-10-28T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → September 23, 2026
  - Appended Sep 23 entry to Card 1 hero-note (EFFR Sep 22 = 3.88%, CME stable ~60%)
  - Appended Sep 23 entry to Card 2 hero-note (stable; no repricing)
  - Updated Card 3 Oct line: "stable Sep 22" → "stable Sep 22–23"
- Sources: WebSearch for EFFR Sep 22 (confirmed 3.88%), CME FedWatch (59.7% as of Sep 20; no new catalyst Sep 23)
- No major Fed events today; VP Jefferson spoke Sep 22 on discount window (not rate-moving)
- Next catalyst: Core PCE August 2026 (BEA, Sep 26) — most critical go/no-go for Oct 28 hike

### September 22, 2026 — TUESDAY
- Target range: 3.75% – 4.00% (hiked Sep 16; unchanged)
- Effective rate: 3.88% (confirmed stable; IORB 3.90%)
  - Sep 17 EFFR: 3.88% (confirmed; first full day at new range)
  - Sep 18 EFFR: 3.88% (confirmed)
  - Sep 19 EFFR: 3.88% (confirmed; published Mon Sep 21 by NY Fed)
  - Sep 21 EFFR: 3.88% (expected stable; published Tue Sep 22 ~9am ET by NY Fed; 4th business day at 3.75–4.00%)
- Next meeting: October 27–28, 2026 (decision October 28 at 2pm ET = 18:00 UTC)
- CME FedWatch October 28 hike: ~60% / hold ~40% (stable; no repricing Sep 22; last confirmed 59.7% as of Sep 20)
- CME FedWatch December 9 second 2026 hike: ~64% (stable; unchanged)
- New FOMC row added: NO (no new meeting; next is Oct 27–28)
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-10-28T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → September 22, 2026
  - Added Sep 22 entry to Cards 1, 2 (EFFR Sep 21 = 3.88%, CME stable ~60%)
  - Updated Card 3 Oct line: noted stable Sep 22
- Sources: WebSearch for EFFR (Sep 18 confirmed 3.88%; Sep 21 expected same), CME FedWatch (59.7% as of Sep 20; no new catalyst Sep 22)

### September 21, 2026 — MONDAY (first trading day of week)
- Target range: 3.75% – 4.00% (hiked Sep 16; unchanged)
- Effective rate: 3.88% (confirmed stable through Sep 19; IORB 3.90%)
  - Sep 17 EFFR: 3.88% (confirmed; first full day at new range)
  - Sep 18 EFFR: 3.88% (confirmed via WebSearch Sep 21 run)
  - Sep 19 EFFR: 3.88% (confirmed; published Mon Sep 21 by NY Fed)
- Next meeting: October 27–28, 2026 (decision October 28 at 2pm ET = 18:00 UTC)
- CME FedWatch October 28 hike: ~60% / hold ~40% (updated; was ~55% post-hike Sep 17-19; rose to 59.7% as of Sep 20; using ~60%)
- CME FedWatch December 9 second 2026 hike: ~64% (stable; unchanged)
- New FOMC row added: NO (no new meeting; next is Oct 27–28)
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-10-28T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → September 21, 2026
  - Added Sep 21 entry to both hero-note committee notes (Card 1 and Card 2)
  - Updated Oct 28 rate path probability in Card 3 from ~55% to ~60%
- Sources: WebSearch for EFFR Sep 18/19 (confirmed 3.88%), CME FedWatch Oct 28 (59.7% as of Sep 20)

## CRITICAL NOTE for NEXT RUNS:
- **Oct 28 probability is ~60% (stable as of Sep 22–23)**. Watch for repricing after Core PCE Aug (Sep 26).
- **Next major data:**
  - **Sep 26 (Fri):** Core PCE August 2026 (BEA) — MOST CRITICAL: go/no-go for Oct 28 hike; prior 3.3% YoY; could cause major CME repricing
  - **Oct 01 (Thu):** ISM Manufacturing PMI September 2026 — first post-hike factory read
  - **Oct 02 (Fri):** September 2026 Jobs Report (BLS) — labor market resilience check post-hike
  - **Oct 10 (Fri approx):** CPI September 2026 (BLS) — additional inflation read
  - **Oct 27–28:** Next FOMC meeting (decision Oct 28, 2pm ET = 18:00 UTC)
  - **Dec 8–9:** Final 2026 FOMC meeting (decision Dec 9)
- Market probabilities as of Sep 22 run:
  - October 28 hike: ~60% / hold ~40% (CME FedWatch; stable Sep 22)
  - December 9 second hike: ~64% (CME FedWatch; stable)
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
  - Sep 21: 3.88% (EXPECTED; published Sep 22 by NY Fed; 4th business day)
  - Sep 22: 3.88% (CONFIRMED; published Sep 23 by NY Fed; 5th business day)
  - Sep 20: No data (weekend)
