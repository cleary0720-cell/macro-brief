# Fed Tracker Agent Memory
Last updated: October 5, 2026

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.

## Reliable data sources
- Fed Funds Rate & FOMC decisions: federalreserve.gov press release pages; CNBC, NPR, Fox Business cover decisions same day
- Effective rate: EFFR via NY Fed / FRED — search "effective federal funds rate EFFR [date]"; sofrrate.com/policy-rates; IORB rate from Fed implementation notes gives ceiling/anchor
- Market probabilities: CME FedWatch (search for snippets via WebSearch); Kalshi; Polymarket; predictionmarketspicks.com; predictionnews.com (covers Kalshi/Polymarket post-decision well); benzinga.com carries specific CME/Kalshi/Polymarket figures together; defirate.com/prediction-markets/fed-decision-odds/ also useful; phemex.com carries CME figure in article title (reliable for specific %)
- Vote breakdown: federalreserve.gov FOMC statement pages; search "FOMC [date] vote statement"
- PCE data: fxstreet.com, cnbc.com, actionforex.com carry BEA PCE releases same day; first search for fxstreet headline which gives exact YoY figure in title
- GDP third estimates: bea.gov search results; cnbc.com carries with context
- Post-decision analysis: cnbc.com, seekingalpha.com, foxbusiness.com

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
- BEA REVISION WARNING: BEA annual revision releases (like Sep 30) can move Core PCE YoY significantly vs forecast — always note revision effect. Sep 30 Core PCE August 2026 came in at 3.0% vs 3.3% expected entirely due to BEA annual revision effect.
- PCE SYNTHESIS CONFLICT: First search result may synthesize an older/forecast figure (e.g. 3.40%). Cross-check with fxstreet.com headline which carries actual in title format "US core PCE inflation softens to X% in [month] vs. Y% expected". CNBC.com also reliable for exact figure.
- CARD 1 vs CARD 2 ENDING TEXT: Card 1 (Current Target Range) and Card 2 (Next FOMC Meeting) hero-notes share identical endings when the same entry is appended to both. Always use Python line-specific replacement, not simple Edit tool, when both need updating.
- MONDAY POST-WEEKEND REPRICING: Probabilities confirmed via WebSearch on Monday morning may differ from Friday close figures held in memory. Always search fresh on Monday for actual current market pricing.

## Run log

### October 5, 2026 — MONDAY (first business day post-jobs weekend)
- Target range: 3.75% – 4.00% (hiked Sep 16; unchanged)
- Effective rate: 3.88% (EFFR Oct 2 published Oct 5 by NY Fed; fifteenth business day at new range; IORB 3.90%; stable)
- Next meeting: October 27–28, 2026 (decision October 28 at 2pm ET = 18:00 UTC)
- **PROBABILITY REPRICING CONFIRMED (post-jobs weekend drift into Monday):**
  - CME FedWatch: ~22% hike / ~78% hold (Phemex title: "77.9% Chance Fed Holds Rates in October"; down from Oct 2 close of ~34–38%)
  - Kalshi: ~20% hike / ~80% hold (up slightly from Oct 2–4 weekend ~15%)
  - Polymarket: ~17% hike / ~83% hold (down from Oct 2–4 ~34%)
  - Hold is the overwhelming market base case across all three venues
- No Fed speeches today; no major data releases
- Vice Chair Jefferson speech (Oct 1, already logged): "inflation too high"; risks tilted upside; supported Sep hike
- New FOMC row added: NO
- MEANS-FOR-YOU: not updated (rate unchanged)
- JS countdown: 2026-10-28T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → October 5, 2026
  - Card 1 hero-note: Appended Oct 5 Monday probability entry
  - Card 2 hero-note: Appended Oct 5 Monday probability entry
  - Card 3 rate path Oct line: Appended Oct 5 Monday probability entry
- Sources: phemex.com (CME 77.9% hold); predictionmarketspicks.com (Kalshi ~80% hold; Polymarket ~83% hold); defirate.com + macroodds.com (post-jobs repricing confirmation); NY Fed FRED (EFFR 3.88%)

## CRITICAL NOTE for NEXT RUNS:
- **EFFR: 3.88% since Sep 17 (confirmed through Oct 2; IORB 3.90%); expect stable through Oct 28**
- **Oct 14 (Wed) — CPI September 2026 (BLS)** — MOST CRITICAL upcoming release; last major inflation read before Oct 28 FOMC
  - If CPI comes in hot (≥3.4%), expect hawkish repricing; hike odds could jump back to 40–50%+
  - If CPI misses, hold probability could push to 90%+
- **Oct 27–28: Next FOMC meeting (decision Oct 28, 2pm ET = 18:00 UTC)**
- **Dec 8–9: Final 2026 FOMC meeting (decision Dec 9)**

- **Current October 28 probability (as of Oct 5 Monday):**
  - CME: ~22% hike / ~78% hold
  - Kalshi: ~20% hike / ~80% hold
  - Polymarket: ~17% hike / ~83% hold
  - HOLD IS THE OVERWHELMING MARKET BASE CASE
- **September Jobs Report (Oct 2, CONFIRMED):**
  - NFP: +29,000 (major miss vs ~90k expected)
  - Unemployment: 4.2% (up from 4.1%)
  - August revised: 162k → 133k; July revised: +21k → -10k; combined -60k
- **Core PCE August 2026 (CONFIRMED Sep 30):**
  - YoY: 3.0% (miss vs 3.3%; BEA annual revision effect)
  - MoM: 0.2% (below 0.3% expected)
- **Q2 GDP third estimate: +2.2% (revised up from +1.5% advance)**
- **ISM Manufacturing PMI September 2026 (Oct 1): 54.5% (ninth consecutive expansion; Prices Paid 77.9)**
- Key Warsh quotes (confirmed Sep 16):
  - "Inflation has been too high for too long"
  - "I'm not in the forward guidance business" (re: dot plot)
- New SEP projections (Sep 16):
  - Headline PCE 2026: 3.7%; Core PCE 2026: 3.4%; Year-end 2026 median: 4.1%
  - 16 of 18 participants see at least one more 2026 hike; Warsh withheld dot
- Oct 28 countdown JS: 2026-10-28T18:00:00Z (correct; no change needed)
