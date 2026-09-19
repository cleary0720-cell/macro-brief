# Fed Tracker Agent Memory
Last updated: September 19, 2026

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

## Run log

### September 19, 2026 — FRIDAY (3 days after FOMC decision)
- Target range: 3.75% – 4.00% (hiked Sep 16; unchanged)
- Effective rate: Sep 17 EFFR CONFIRMED at 3.88% (via FRED/WebSearch; first full business day at new range; IORB 3.90%)
  - Sep 18 EFFR (published Sep 19): ~3.88% (estimated; consistent with IORB 3.90%; second full day at new range; not explicitly confirmed in search snippets but logically expected)
- Next meeting: October 27–28, 2026 (decision October 28 at 2pm ET = 18:00 UTC)
- CME FedWatch October 28 hike: ~55% / hold ~45% (stable from Sep 17; Sep 19 search confirmed 55.1%)
- CME FedWatch December 9 second 2026 hike: ~64% (stable from Sep 17; no fresh figure in Sep 19 search but KuCoin article confirmed ~90% year-end-at-least-one-hike, consistent with ~55% Oct + ~64% Dec)
- New FOMC row added: NO (no new meeting)
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-10-28T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → September 19, 2026
  - EFFECTIVE RATE display updated from "~3.88%" to "3.88%" (now confirmed)
  - Card 1 note: Sep 18 "(today)" removed; Sep 17 EFFR updated to "confirmed at 3.88%"; Sep 19 (today) entry added with ~3.88% EFFR
  - Card 2 note: Sep 18 "(today)" removed; Sep 17 EFFR updated to "confirmed at 3.88%"; Sep 19 (today) entry added
  - Card 3 Oct rate path: updated "Sep 17" to "Sep 17–19" for stable probability range
- Sources: WebSearch FRED/NY Fed EFFR snippets (Sep 17 = 3.88% confirmed); CME FedWatch 55.1% Oct 28 via WebSearch snippet (stable)

## CRITICAL NOTE for NEXT RUN (Sep 20 Sat or Sep 21 Mon morning):
- **Sep 20 (Saturday)**: No EFFR published (weekend). No data releases. CME probabilities expected stable.
  - If running Sep 20: just update "Last updated" date and note no new data (weekend rules apply)
- **Sep 21 (Monday)**: EFFR for Sep 18 published (should be ~3.88%; confirm exact figure); EFFR for Sep 19 also expected ~3.88%.
  - If running Sep 21: confirm Sep 18 EFFR; add Sep 20 (no data/weekend) and Sep 21 (today) entries
- **No new FOMC meeting until October 27–28** (decision Oct 28, 2026)
- Next major data:
  - Sep 26 (Fri approx): Core PCE August 2026 (BEA) — first post-FOMC PCE read; previous 3.3% YoY
  - Oct 2 (Fri approx): September Jobs Report (BLS) — first post-hike labor data
  - Oct 10 (Fri approx): September CPI (BLS) — first post-hike inflation read
  - Oct 27–28: Next FOMC meeting (decision Oct 28)
  - Dec 8–9: Final 2026 FOMC meeting (decision Dec 9)
- Market probabilities entering next run:
  - October 28 hike: ~55% / hold ~45% (CME FedWatch, Sep 19)
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
  - Sep 18: ~3.88% (estimated; second full day; IORB 3.90%)
  - Sep 19: ~3.88% (estimated; third full day; IORB 3.90%)
