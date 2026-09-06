# Dashboard Agent Memory
Last updated: 2026-09-06

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.
Command: git add index.html archive.html about.html sitemap.xml && git commit -m "..." && git push origin HEAD:main

## Reliable data sources
- Fed Funds Rate: WebSearch "FOMC [month] 2026 decision federal funds rate" → stocktitan.net, cnbc.com
- CPI: WebSearch "BLS CPI [month] 2026 year over year" → bls.gov snippets via cnbc.com, usinflationcalculator.com
- Core CPI / Shelter / Energy: Same CPI search — confirmed: Core CPI 2.5%, Shelter 3.2%, Energy +14.7% for July 2026
- Core PCE: WebSearch "BEA core PCE [month] 2026 personal income outlays" → indexbox.io, nchstats.com, bea.gov snippets
- ISM PMI: WebSearch "ISM Manufacturing PMI [month] 2026" → prnewswire.com carries official ISM press releases verbatim; textileworld.com, industrytoday.com also carry full ISM releases
- Jobless Claims: WebSearch "initial jobless claims week ending [date] 2026" → verifiedinvesting.com, haver.com, cryptobriefing.com
  - NOTE: DOL releases on Thursday. Weekly + 4-week avg both appear in search snippets.
- Unemployment/Jobs: WebSearch "BLS employment situation [month] 2026" → cnbc.com (roberthalf.com carries "jobs report" summaries with NFP and unemployment in title/snippet)
  - KEY: Jobs reports often contain REVISIONS — check prior month revisions in snippet; they can completely change the narrative (July -23k revised to +21k in Aug report)
- GDP: WebSearch "BEA GDP Q[n] 2026 [estimate]" → advisorperspectives.com, indexbox.io
- 10-yr Treasury / Yield Curve: WebSearch "treasury yields [date] 2026" → cnbc.com, etftrends.com, forbes.com/advisor/investing/treasury-rates
  - For 7Y and 20Y: WebSearch "treasury yields [date] 2026 7 year 20 year" — forbes.com/advisor and depositquest.substack.com carry most maturities
  - Confirmed Sep 4: 1M=3.79%, 3M=3.91%, 6M=3.98%, 1Y=4.13%, 2Y=4.37%, 5Y=4.54%, 7Y=4.65%, 10Y=4.78%, 20Y=5.25%, 30Y=5.24%
- Retail Sales: WebSearch "retail sales [month] 2026 census bureau year over year" → qz.com, etftrends.com
- M2: WebSearch "M2 money supply [month] 2026 federal reserve H.6" → fxmacrodata.com, tradingeconomics.com
- FOMC odds: WebSearch "CME FedWatch [meeting date] 2026 FOMC probability" → CNBC most timely; cnbc.com, growbeansprout.com, cryptorank.io
  - CRITICAL: Check EVERY run — major data releases (jobs, PCE) cause immediate large moves
  - After strong jobs report (Sep 5): hold 42% / hike 58% (from 50/50 pre-report)

## Known issues
- bls.gov, federalreserve.gov, fred.stlouisfed.org, treasury.gov ALL return HTTP 403 on direct WebFetch
- Use WebSearch only — all economic data is well-covered in search result snippets
- REVISION TRAP: Jobs report preliminary estimates can be revised dramatically. July 2026 initially -23k, revised +21k. ALWAYS check revision figures in snippet (look for "June was revised", "July was revised" language)
- Core PCE and Core CPI can diverge significantly — report both and explain why in card text (PCE weights healthcare/services more)

## Run log

### 2026-09-06
- Fed Rate: 3.50–3.75% (3.63%) — HELD; UNCHANGED
- CPI (July 2026): 3.4% — UNCHANGED; Core CPI: 2.5%; Shelter: 3.2%; Energy: +14.7%
- Core PCE (July 2026): 3.3% YoY — UNCHANGED (August Core PCE due ~Sep 26)
- ISM PMI (August 2026): 54.6% — ROLLED FORWARD (was 55.6% July; 8th consecutive expansion month; released Sep 2)
  - New orders: 53.7, Production: 58.3, Employment: 51.2
- Jobless Claims 4-wk avg (week ending Aug 29, released Sep 4): 207k — IN-PLACE UPDATE (was 206k)
  - Weekly: 206k (up from 203k); 4-wk avg: 207,250
- Unemployment (August 2026): 4.1% — ROLLED FORWARD (August jobs report: NFP +162k, unemp 4.1%)
  - KEY: July revised from -23k to +21k (+44k revision). June revised up +11k. "First job loss in years" narrative erased.
  - Unemployment card: neg→pos; signal updated to "HIRING SURGE: +162K ↑"
- GDP Q2 2026: +1.5% — UNCHANGED (Q3 advance est ~late October)
- 10-yr Treasury (Sep 4): 4.78% — ROLLED FORWARD (was 4.73% Aug; Sep is new month)
  - Full curve Sep 4: 1M=3.79%, 3M=3.91%, 6M=3.98%, 1Y=4.13%, 2Y=4.37%, 5Y=4.54%, 7Y=4.65%, 10Y=4.78%, 20Y=5.25%, 30Y=5.24%
  - 2s10s: +41 bps (slightly wider from +39 bps — modest bear steepening post-jobs); 3m10y: +87 bps; NORMAL (green)
- Retail Sales (July 2026): +5.0% YoY — UNCHANGED (August data due Sep 12)
- M2 (July 2026): 5.4% YoY — UNCHANGED (August H.6 due ~late Sep)
- FOMC odds (September 16-17, as of Sep 5 post-jobs): CUT 0% / HOLD 42% / HIKE 58%
  - Before jobs report: ~50/50 hold/hike; after: 42/58 hold/hike
- Sentiment: 48/100 CAUTIOUS (up from 44 — labor market reversal, but inflation still sticky)
- Edition: Vol. I, No. 19 · September 6, 2026
- Sparklines rolled/updated:
  - ism-pmi: ROLLED FORWARD (dropped "Aug '25" 48.7, added "Aug" with 54.6)
  - unemployment: ROLLED FORWARD (dropped "Aug '25" 4.2, added "Aug" with 4.1)
  - treasury: ROLLED FORWARD (dropped "Sep '25" 4.20, added "Sep" with 4.78)
  - jobless-claims: IN-PLACE UPDATE (Aug entry: 206 → 207)
  - All others: UNCHANGED
- What to Watch: Removed Sep 2 ISM (past), Sep 5 Jobs (past); updated Sep 16 FOMC context; added Sep 26 Core PCE August
- Key headline: August jobs +162k erased July -23k scare; July revised to +21k; FOMC hike odds 58%
- Key narrative: Labor market reversal + sticky inflation = Fed has cover to hike Sep 16-17
- Upcoming: Sep 10 CPI August (last inflation before FOMC), Sep 12 Retail Sales, Sep 16-17 FOMC, Sep 26 Core PCE August

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
- Sentiment: 44/100 CAUTIOUS (down from 46 — hawkish Warsh speech + Core PCE stall)
- Edition: Vol. I, No. 18 · August 30, 2026

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
