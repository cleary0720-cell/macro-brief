# Dashboard Agent Memory
Last updated: 2026-08-30

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.
Command: git add index.html archive.html about.html sitemap.xml && git commit -m "..." && git push origin HEAD:main

## Reliable data sources
- Fed Funds Rate: WebSearch "FOMC [month] 2026 decision federal funds rate" → stocktitan.net, cnbc.com
- CPI: WebSearch "BLS CPI [month] 2026 year over year" → bls.gov snippets via cnbc.com, usinflationcalculator.com
- Core CPI / Shelter / Energy: Same CPI search — confirmed: Core CPI 2.5%, Shelter 3.2%, Energy +14.7% for July 2026
- Core PCE: WebSearch "BEA core PCE [month] 2026 personal income outlays" → indexbox.io, nchstats.com, bea.gov snippets
- ISM PMI: WebSearch "ISM Manufacturing PMI [month] 2026" → prnewswire.com carries official ISM press releases verbatim
- Jobless Claims: WebSearch "initial jobless claims week [date] 2026" → verifiedinvesting.com, seekingalpha.com
  - NOTE: DOL releases on Thursday. Weekly + 4-week avg both appear in search snippets.
- Unemployment/Jobs: WebSearch "BLS employment situation [month] 2026" → cnbc.com, foxbusiness.com
- GDP: WebSearch "BEA GDP Q[n] 2026 [estimate]" → advisorperspectives.com, indexbox.io
- 10-yr Treasury / Yield Curve: WebSearch "treasury yields [date] 2026" → cnbc.com, etftrends.com, depositquest.substack.com
  - Confirmed Aug 28: 2Y=4.34%, 10Y=4.73%, 30Y=5.20%
  - For full curve: depositquest.substack.com/p/treasury-par-yield-curve-rates carries all 10 maturities
- Retail Sales: WebSearch "retail sales [month] 2026 census bureau year over year" → qz.com, etftrends.com
- M2: WebSearch "M2 money supply [month] 2026 federal reserve H.6" → fxmacrodata.com, tradingeconomics.com
- FOMC odds: WebSearch "CME FedWatch [meeting date] 2026 FOMC probability" → CNBC most timely; cnbc.com, growbeansprout.com
  - CRITICAL: Check EVERY run — odds swung dramatically (32%→56% hike) after Warsh's Jackson Hole speech

## Known issues
- bls.gov, federalreserve.gov, fred.stlouisfed.org, treasury.gov ALL return HTTP 403 on direct WebFetch
- Use WebSearch only — all economic data is well-covered in search result snippets
- Jackson Hole 2026 (Aug 27-29) caused massive repricing: Warsh hawkish → hike odds 32%→56% in one day
- Core PCE stalled at 3.3% July (released Aug 26) — did not decline as Core CPI suggested (divergence: PCE weights services/healthcare more)
- Headline PCE: 3.7% YoY July (re-acceleration from energy base effects)
- M2 July H.6 released Aug 25 (slightly earlier than expected "late August")

## Run log

### 2026-08-30
- Fed Rate: 3.50–3.75% (3.63%) — HELD; UNCHANGED
- CPI (July 2026): 3.4% — UNCHANGED; Core CPI: 2.5%; Shelter: 3.2%; Energy: +14.7%
- Core PCE (July 2026): 3.3% YoY — ROLLED FORWARD (same as June; released Aug 26; DISAPPOINTED — no improvement)
  - Headline PCE: 3.7% YoY (re-acceleration)
- ISM PMI (July 2026): 55.6 — UNCHANGED (August ISM due Sep 2)
- Jobless Claims 4-wk avg (week ending Aug 22, released Aug 28): 205,500 — IN-PLACE UPDATE (was 204k)
  - Weekly: 203k (down 4k); 4-wk avg: 205.5k (up from 204k)
- Unemployment (July 2026): 4.1% — UNCHANGED
- GDP Q2 2026: +1.5% — UNCHANGED
- 10-yr Treasury (Aug 28): 4.73% — IN-PLACE UPDATE (was 4.74%)
  - MAJOR: 2Y surged from 4.19% to 4.34% (+15 bps) post-Warsh speech (bear flattening)
  - Full curve Aug 28: 1M=3.82%, 3M=3.88%, 6M=3.97%, 1Y=4.05%, 2Y=4.34%, 5Y=4.45%, 7Y=4.58%, 10Y=4.73%, 20Y=5.17%, 30Y=5.20%
  - 2s10s: +39 bps (from +55 bps — curve flattened); 3m10y: +85 bps; NORMAL (green)
- Retail Sales (July 2026): +5.0% YoY — UNCHANGED
- M2 (July 2026): 5.4% YoY — ROLLED FORWARD (was June 5.5%; H.6 released Aug 25)
- FOMC odds (September 16-17, as of Aug 28 post-Warsh): CUT 0% / HOLD 44% / HIKE 56%
  - Before Warsh speech (Aug 25): Hold 58.6% / Hike 41.4%
  - After Jackson Hole (Aug 28): Hold 44% / Hike 56% — MASSIVE SWING
- Sentiment: 44/100 CAUTIOUS (down from 46 — hawkish Warsh speech + Core PCE stall)
- Edition: Vol. I, No. 18 · August 30, 2026
- Sparklines rolled/updated:
  - m2: ROLLED FORWARD (dropped "Jul '25", added "Jul" with 5.4)
  - core-pce: ROLLED FORWARD (dropped "Jul '25", added "Jul" with 3.3)
  - treasury: IN-PLACE (Aug entry: 4.74 → 4.73)
  - jobless-claims: IN-PLACE (Aug entry: 204 → 206)
  - All others: UNCHANGED
- Key events this week: Core PCE July (Aug 26, held at 3.3%), Warsh Jackson Hole keynote (Aug 28, hawkish)
- Key headline: Warsh's first Jackson Hole speech moved hike odds from 32% to 56%; Core PCE flat at 3.3% for 2nd month
- Upcoming: Sep 5 August Jobs Report (decisive swing vote), Sep 10 CPI August, Sep 12 Retail Sales, Sep 16-17 FOMC

### 2026-08-23
- Fed Rate: 3.50–3.75% (3.63%) — HELD; UNCHANGED
- CPI (July 2026): 3.4% — UNCHANGED; Core CPI: 2.5%; Shelter: 3.2%; Energy: +14.7%
- Core PCE (June 2026): 3.3% YoY — UNCHANGED (July data released Aug 26)
- ISM PMI (July 2026): 55.6 — UNCHANGED
- Jobless Claims 4-wk avg (week ending Aug 15): 204k — IN-PLACE UPDATE (was 199k; weekly 206k)
- Unemployment (July 2026): 4.1% — UNCHANGED
- GDP Q2 2026: +1.5% — UNCHANGED
- 10-yr Treasury (Aug 22): 4.74% — IN-PLACE UPDATE
  - Full curve: 1M=3.76%, 3M=3.82%, 6M=3.91%, 1Y=3.99%, 2Y=4.19%, 5Y=4.39%, 7Y=4.52%, 10Y=4.74%, 20Y=5.20%, 30Y=5.25%
- Retail Sales (July 2026): +5.0% YoY — UNCHANGED
- M2 (June 2026): 5.5% YoY — UNCHANGED
- FOMC odds (September 16-17): CUT 0% / HOLD 68% / HIKE 32%
- Sentiment: 46/100 CAUTIOUS
- Edition: Vol. I, No. 17

### 2026-08-16
- Fed Rate: 3.50–3.75% (3.63%) — HELD; CPI (July 2026): 3.4% — ROLLED FORWARD
- FOMC odds: CUT 0% / HOLD 52% / HIKE 48%; Sentiment: 45/100; Edition: Vol. I, No. 16

### 2026-08-09
- ISM PMI July: 55.6 — ROLLED FORWARD; Unemployment July: 4.1% — ROLLED FORWARD
- Treasury (Aug 7): 4.65%; FOMC odds: CUT 0% / HOLD 60% / HIKE 40%; Sentiment: 46/100; Edition: Vol. I, No. 15

### 2026-08-02
- GDP Q2 2026: +1.5% — ROLLED FORWARD; CPI (June): 3.5% — ROLLED FORWARD; FOMC odds: CUT 1% / HOLD 27% / HIKE 72%
- Sentiment: 43/100; Edition: Vol. I, No. 14
