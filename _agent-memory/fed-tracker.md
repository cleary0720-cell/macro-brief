# Fed Tracker Agent Memory
Last updated: October 27, 2026

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.

## Reliable data sources
- Fed Funds Rate & FOMC decisions: federalreserve.gov press release pages; CNBC, NPR, Fox Business cover decisions same day
- Effective rate: EFFR via NY Fed / FRED — search "effective federal funds rate EFFR [date]"; sofrrate.com/policy-rates; IORB rate from Fed implementation notes gives ceiling/anchor
- Market probabilities: CME FedWatch (search for snippets via WebSearch); Kalshi; Polymarket; predictionmarketspicks.com; predictionnews.com (covers Kalshi/Polymarket post-decision well); benzinga.com carries specific CME/Kalshi/Polymarket figures together; defirate.com/prediction-markets/fed-decision-odds/ also useful; phemex.com carries CME figure in article title (reliable for specific %); investing.com Fed rate monitor (CME-based); tradingpedia.com/[date] for October 2026 CME figures; BeInCrypto for CME FedWatch daily summaries; PANews (panews.io) reliable for post-data-release CME figures with high precision (e.g., cited 43.7% exactly after Oct 14 CPI); stockpil.com reliable for exact CME FedWatch figures (cited 82.8%/17.2% on Oct 20); gobaker.com (Baker Group) reliable for weekly CME FedWatch summaries; finwire.io and futunn.com also carry CME figures
- Vote breakdown: federalreserve.gov FOMC statement pages; search "FOMC [date] vote statement"
- PCE data: fxstreet.com, cnbc.com, actionforex.com carry BEA PCE releases same day; first search for fxstreet headline which gives exact YoY figure in title
- GDP third estimates: bea.gov search results; cnbc.com carries with context
- Post-decision analysis: cnbc.com; seekingalpha.com; foxbusiness.com
- Extended WebSearch: Use "extended" mode when searching for specific current-day probability figures; synthesized standard results can reference stale data
- FOMC Minutes reaction: babypips.com market recaps; fxstreet.com; cnbc.com; ING FX Daily (think.ing.com)
- Fed speeches: bloomberg.com; pbs.org/newshour; americanbanker.com; federalreserve.gov/newsevents/speech/
- CPI releases: fxstreet.com headline gives exact figures; cnbc.com; foxbusiness.com; easternherald.com
- Dollar/yield movements: fxstreet.com daily forex recap (e.g., "Forex Today: US Dollar retreats from 18-month high")
- BNY Markets FOMC previews: FXStreet carries these with timestamp (e.g., "Federal Reserve: December hike expectations — BNY — 202610271258")
- FOMC day previews: admiralmarkets.com, tradingkey.com, ebc.com carry same-day FOMC meeting previews

## Known issues
- WEEKEND HALLUCINATION WARNING: WebSearch on weekends returns confused synthesized probability figures. Trust prior-day confirmed memory on weekends with no new data releases.
- Most aggregator sites (centralbank.watch, rateprobability.com, growbeansprout.com) return HTTP 403 on WebFetch. Use WebSearch snippets.
- Yahoo Finance, CBS News, CNBC article pages also return 403 on WebFetch — use WebSearch.
- tradingeconomics.com also returns 403 on WebFetch.
- EFFR data: NY Fed releases prior business day's data at approximately 9:00am ET. Weekends and federal holidays = no publication.
- EFFR RATE TRANSITION NOTE: When the Fed hikes at 2pm ET, implementation note says "effective [next business day]".
  - Hike day EFFR = still old rate; day after hike = first full day at new rate
- Warsh withheld his dot at June AND September meetings; 16 of 18 dots submitted at Sep meeting.
- CME FedWatch direction matters — always confirm if a % refers to a hike, hold, or cut.
- growbeansprout.com consistently returns cached/stale data — ignore for directional analysis.
- sofrrate.com/policy-rates can be stale — cross-reference with other sources.
- Bloomberg.com returns readable search snippets via WebSearch even if full article is paywalled.
- CME REPRICING WARNING: After a major hawkish/dovish catalyst, probabilities can jump 10-20pp intraday. Search for same-day CNBC/FXStreet for current figure.
  - CPI REPRICING EXAMPLE: Oct 14 Sep CPI (slightly hot core) moved October hike from ~21.6% to ~43.7% (CME)
  - AI SELLOFF REPRICING EXAMPLE (Oct 22): AI-stock selloff drove 10Y yield 19 bps lower to 4.95% — October hike dropped from ~15% to ~7%; December from ~90% to ~80%
  - FRIDAY REBALANCING (Oct 23): By Friday close, CME drifted back to ~10% hike / ~90% hold from the ~7% lows; Kalshi stayed at ~7%
- BEA REVISION WARNING: BEA annual revision releases (like Sep 30) can move Core PCE YoY significantly vs forecast — always note revision effect. Sep 30 Core PCE August 2026 came in at 3.0% vs 3.3% expected entirely due to BEA annual revision effect.
- PCE SYNTHESIS CONFLICT: First search result may synthesize an older/forecast figure (e.g., 3.40%). Cross-check with fxstreet.com headline which carries actual in title format "US core PCE inflation softens to X% in [month] vs. Y% expected". CNBC.com also reliable for exact figure.
- CARD 1 vs CARD 3 vs CARD 5 ENDING TEXT: After Oct 27 update:
  - Card 1 ends with "...CME Oct 28: <strong>~9.4% hike / ~90.6% hold</strong> (essentially unchanged; Kalshi ~7%). December 9: ~79.7% (~80%; stable).</div>"
  - Card 3 ends with "...CME Oct 28: <strong>~9.4% hike / ~90.6% hold</strong> (essentially unchanged; Kalshi ~7%). December 9: ~79.7% (~80%; stable).</div>"
  - Card 5 ends with "...CME Oct 28: <strong>~9.4% hike / ~90.6% hold</strong> (essentially unchanged; Kalshi ~7%). December 9: ~79.7% (~80%; stable).</div>"
  - NOTE: Cards 3 and 5 have IDENTICAL endings — must use Python positional replacement, not text search
- FOMC DECISION DAY TOMORROW: October 28, 2026 at 2pm ET = 18:00 UTC. HUGE session: decision + press conference.
  - Add new FOMC history row (hold expected; at least one dissent for hiking per BNY)
  - Update rate ONLY if changed (market expects hold ~90.6%)
  - Update MEANS-FOR-YOU ONLY if rate changes
  - Update JS countdown to 2026-12-09T19:00:00Z AFTER decision
  - Note: At least one dissent in favor of hiking expected (BNY Markets, FXStreet Oct 27)
- PARTIAL WRITE BUG: If Python script fails mid-way, the file is NOT written. Subsequent scripts read the unchanged original. Must apply ALL changes in ONE script and write once at the end. Verify with grep after writing.
- STALE TODAY REFERENCES: When updating the daily entry, also replace "release TODAY" or "tomorrow" references in prior entries with "released [date]" so they don't become stale.
- CPI RELEASE DAY CONFIRMED: October 14, 2026 is WEDNESDAY (BLS released Sep CPI at 8:30am ET).
- After Oct 28 decision, update JS countdown to 2026-12-09T19:00:00Z
- M2 September H.6: Scheduled for Oct 27 per FRED (FRED "Next Release Date: Oct 27, 2026"). September figure NOT confirmed in WebSearch as of Oct 27 morning — may not yet be indexed. August 2026 M2 was $23,342.8 billion SA (+5.7% YoY). Check again on Oct 28 or after.

## Run log

### October 27, 2026 — TUESDAY (FOMC Day 1; decision tomorrow Oct 28; blackout day 11)
- Target range: 3.75% – 4.00% (unchanged)
- Effective rate: 3.88% (stable since Sep 17; IORB 3.90%)
- Next meeting: Decision tomorrow, October 28, 2026 at 2pm ET = 18:00 UTC
- **FOMC blackout in effect (Oct 17–28); meeting underway (Day 1 of 2)**
- **No market-moving data releases today (FXStreet "Forex Today Oct 27" noted "mid-tier data")**
- **M2 September H.6 scheduled for today per FRED — but September figure not confirmed in WebSearch**
- **BNY Markets Velis (FXStreet Oct 27 12:58 UTC):**
  - Hold expected at Oct 28 meeting
  - At least one dissent favoring a hike expected
  - December seen as cycle peak; Warsh won't preview Dec at press conference
  - Market implies Fed funds peak just above 4.5% with ~3 more hikes by next year; BNY doubts full pricing delivered
- **CME Oct 28: ~9.4% hike / ~90.6% hold (FXStreet Oct 26; essentially unchanged from Oct 26)**
  - One source (pomegra.io) cited 73% December hike / 93% October hold — slightly more dovish framing
- **Kalshi: ~7% hike / ~93% hold (stable)**
- **December 9: ~79.7% (FXStreet Oct 26; ~80%; stable)**
- New FOMC row added: NO (decision tomorrow)
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-10-28T18:00:00Z (unchanged; correct; decision TOMORROW)
- Changes made:
  - "Last updated" → October 27, 2026
  - Card 1 hero-note: Appended Oct 27 entry (FOMC Day 1, meeting underway, BNY hold call, CME ~9.4%/~90.6%, Kalshi ~7%, Dec ~79.7%)
  - Card 3 hero-note: Appended Oct 27 entry (same summary)
  - Card 5 hero-note: Appended Oct 27 entry (same summary)
- Sources: FXStreet fxstreet.com Oct 27 (BNY preview, Velis); FXStreet Oct 26 (90.6% hold / 79.7% Dec hike)

### October 26, 2026 — MONDAY (Day before FOMC starts; blackout day 10)
- Target range: 3.75% – 4.00% (unchanged)
- Effective rate: 3.88% (stable since Sep 17; IORB 3.90%)
- Next meeting: October 27–28, 2026 (decision October 28 at 2pm ET = 18:00 UTC)
- CME Oct 28: ~9.4% hike / ~90.6% hold (FXStreet Oct 26; essentially unchanged; Kalshi ~7%). December 9: ~79.7% (FXStreet Oct 26; ~80%; stable).
- New FOMC row added: NO

## CRITICAL NOTE for NEXT RUNS:
- **EFFR: 3.88% since Sep 17 (stable; IORB 3.90%)**
- **Oct 28 (Wed) — FOMC Rate Decision (2pm ET = 18:00 UTC):**
  - Market: ~9.4% hike / ~90.6% hold (CME); ~7% hike (Kalshi); HOLD near-certain
  - At least one dissent in favor of hiking expected (BNY Markets)
  - Add new FOMC history row (format: "Oct 28, 2026"; decision-hold or decision-hike span; range-cell; vote-cell; Notes td)
  - Update rate if changed; update MEANS-FOR-YOU if rate changes
  - Update JS countdown to 2026-12-09T19:00:00Z after decision
  - Card 1 / Card 3 / Card 5 have identical Oct 27 tails — use Python positional replacement for Oct 28 entry
- **Oct 29 (Thu) — GDP Q3 2026 Advance Estimate (BEA) + Initial Jobless Claims (week ending Oct 25)**
- **Oct 30 (Fri) — Core PCE September 2026 (BEA)** — CRITICAL: above 3.0% cements December hike
- **Dec 8–9: Final 2026 FOMC meeting (decision Dec 9)**
  - ~79.7% hike probability (CME; ~80%; stable)

- **Current October 28 probability (as of Oct 27 Tuesday):**
  - CME: ~9.4% hike / ~90.6% hold (essentially unchanged since Oct 26)
  - Kalshi: ~7% hike / ~93% hold (stable)
  - HOLD is near-certain; BNY expects at least one dissent in favor of hiking
  - FOMC blackout in effect Oct 17–28 — no Fed speeches before decision
- **December 9 hike: ~79.7% / ~80% (FXStreet Oct 26; stable)**
- **Key Warsh quotes (confirmed Sep 16):**
  - "Inflation has been too high for too long"
  - "I'm not in the forward guidance business" (re: dot plot)
- **Sep CPI (Oct 14, CONFIRMED):** Headline 3.7% YoY; Core 0.3% MoM / 2.6% YoY; hot
- **Sep PPI (Oct 15, CONFIRMED):** 6.3% YoY (vs 5.3% forecast; hot); monthly +1.3%
- **Sep Retail Sales (Oct 15, CONFIRMED):** +0.8% MoM (vs +0.3% expected); control +0.1%
- **10Y Treasury (Oct 23):** 5.00% (pre-FOMC calm; down from 5.10% Oct 17)
- Oct 28 countdown JS: 2026-10-28T18:00:00Z (correct; decision TOMORROW)
