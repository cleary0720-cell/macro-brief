# Dashboard Agent Memory
Last updated: 2026-08-23

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.
Command: git add index.html archive.html about.html sitemap.xml && git commit -m "..." && git push origin HEAD:main

## Reliable data sources
- Fed Funds Rate: WebSearch "FOMC [month] 2026 decision federal funds rate" → stocktitan.net, cnbc.com
- CPI: WebSearch "BLS CPI [month] 2026 year over year" → bls.gov snippets via cnbc.com, usinflationcalculator.com
- Core CPI / Shelter / Energy: Same CPI search — confirmed: Core CPI 2.5%, Shelter 3.2%, Energy +14.7% for July 2026
- Core PCE: WebSearch "BEA core PCE [month] 2026 personal income outlays" → bea.gov snippets, cnbc.com
- ISM PMI: WebSearch "ISM Manufacturing PMI [month] 2026" → prnewswire.com carries official ISM press releases verbatim
- Jobless Claims: WebSearch "initial jobless claims week [date] 2026" → verifiedinvesting.com, qz.com, neilsethi.substack.com
  - NOTE: DOL releases on Thursday. Weekly + 4-week avg both appear in search snippets.
- Unemployment/Jobs: WebSearch "BLS employment situation [month] 2026" → cnbc.com, foxbusiness.com
- GDP: WebSearch "BEA GDP Q[n] 2026 [estimate]" → advisorperspectives.com, indexbox.io
- 10-yr Treasury / Yield Curve: WebSearch "treasury yields [date] 2026" → cnbc.com most reliable
  - Confirmed Aug 22: 2Y=4.19%, 10Y=4.74%, 30Y=5.25%
  - For full curve: estimate intermediate maturities from parallel shift off confirmed anchors
- Retail Sales: WebSearch "retail sales [month] 2026 census bureau year over year" → qz.com, etftrends.com
- M2: WebSearch "M2 money supply [month] 2026 federal reserve H.6" → fxmacrodata.com, tradingeconomics.com
- FOMC odds: WebSearch "CME FedWatch [meeting date] 2026 FOMC probability" → CNBC most timely; kucoin.com/news also carries post-event repricing
  - CRITICAL: Check EVERY run — odds moved 16 points (48→32 hike) in one week after FOMC minutes

## Known issues
- bls.gov, federalreserve.gov, fred.stlouisfed.org, treasury.gov ALL return HTTP 403 on direct WebFetch
- Use WebSearch only — all economic data is well-covered in search result snippets
- IMPORTANT: August 16 run had CPI component data discrepancy — sparkline note said Core CPI 3.2%/Energy 16.8% but actual July 2026 BLS data confirmed: Core CPI 2.5%, Shelter 3.2%, Energy +14.7%. Always verify components against BLS search results, not previous memory entries.
- Jobs date: Sep 5 jobs report (not Sep 4 as previously noted — verify each run)
- FOMC minutes can cause large repricing: Aug 19 minutes showed "several" members wanted to hike but market dovishly repriced 16 points to 68% hold / 32% hike
- Bessent Treasury buyback announcement (Aug 20) caused intra-week yield volatility — yields spiked then settled slightly higher

## Run log

### 2026-08-23
- Fed Rate: 3.50–3.75% (3.63%) — HELD; UNCHANGED
- CPI (July 2026): 3.4% — UNCHANGED; Core CPI: 2.5%; Shelter: 3.2%; Energy: +14.7% (corrected from prior memory error)
- Core PCE (June 2026): 3.3% YoY — UNCHANGED (July data due Aug 27)
- ISM PMI (July 2026): 55.6 — UNCHANGED
- Jobless Claims 4-wk avg (week ending Aug 15): 204k — IN-PLACE UPDATE (was 199k; weekly 206k, released Aug 21)
  - Continuing claims: 1,799,000 (up 18k)
- Unemployment (July 2026): 4.1% — UNCHANGED
- GDP Q2 2026: +1.5% — UNCHANGED
- 10-yr Treasury (Aug 22): 4.74% — IN-PLACE UPDATE (was 4.70%; bear-steepening from minutes + Bessent buyback)
  - Full curve: 1M=3.76%, 3M=3.82%, 6M=3.91%, 1Y=3.99%, 2Y=4.19%, 5Y=4.39%, 7Y=4.52%, 10Y=4.74%, 20Y=5.20%, 30Y=5.25%
  - 2s10s: +55 bps; 3m10y: +92 bps; NORMAL curve (green)
- Retail Sales (July 2026): +5.0% YoY — UNCHANGED
- M2 (June 2026): 5.5% YoY — UNCHANGED (July H.6 expected late August)
- FOMC odds (September 16-17, as of Aug 20-22): CUT 0% / HOLD 68% / HIKE 32%
  - FOMC minutes (Aug 19) showed "several" wanted to hike but market dovishly repriced from 52/48 to 68/32
  - Triggered by softening labor market backdrop (claims rising, payrolls -23k) outweighing hawkish minutes tone
- Sentiment: 46/100 CAUTIOUS (up from 45 — dovish FOMC repricing partially offset by rising yields and claims)
- Edition: Vol. I, No. 17 · August 23, 2026
- Sparklines rolled/updated:
  - treasury: IN-PLACE (Aug entry: 4.70 → 4.74)
  - jobless-claims: IN-PLACE (Aug entry: 199 → 204)
  - All others: UNCHANGED
- Key events this week: FOMC Minutes (Aug 19, hawkish but dovish repricing), Warsh Jackson Hole keynote (Aug 28), Core PCE (Aug 27)
- Key headline: FOMC minutes showed broader hawkish sentiment than vote implied; market priced 68% hold as labor data softened; 10Y drifted to 4.74%; Core PCE release Wednesday Aug 27 is decisive for September FOMC

### 2026-08-16
- Fed Rate: 3.50–3.75% (3.63%) — HELD; UNCHANGED
- CPI (July 2026): 3.4% YoY — ROLLED FORWARD; Core CPI: 2.5%; Shelter: 3.2%; Energy: +14.7%
  - NOTE: Memory entry for this run incorrectly listed Core CPI 3.2%/Energy 16.8% — BLS confirms 2.5%/14.7%
- Core PCE (June 2026): 3.3% — UNCHANGED
- ISM PMI (July 2026): 55.6 — UNCHANGED
- Jobless Claims 4-wk avg (week ending Aug 8): ~199k — IN-PLACE update
- Unemployment (July 2026): 4.1% — UNCHANGED
- GDP Q2 2026: +1.5% — UNCHANGED
- 10-yr Treasury (Aug 14): 4.70% — UPDATED IN-PLACE (Aug entry: 4.65% → 4.70%)
- Retail Sales (July 2026): +5.0% YoY — ROLLED FORWARD
- M2 (June 2026): 5.5% — UNCHANGED
- FOMC odds (September 16-17): CUT 0% / HOLD 52% / HIKE 48%
- Sentiment: 45/100 CAUTIOUS (corrected from memory — was listed as 44 in memory but HTML said 45)
- Edition: Vol. I, No. 16

### 2026-08-09
- Fed Rate: 3.50–3.75% — HELD; ISM PMI July: 55.6 — ROLLED FORWARD; Unemployment July: 4.1% — ROLLED FORWARD
- Treasury (Aug 7): 4.65%; FOMC odds: CUT 0% / HOLD 60% / HIKE 40%; Sentiment: 46/100; Edition: Vol. I, No. 15

### 2026-08-02
- GDP Q2 2026: +1.5% — ROLLED FORWARD; CPI (June): 3.5% — ROLLED FORWARD; FOMC odds: CUT 1% / HOLD 27% / HIKE 72%
- Sentiment: 43/100; Edition: Vol. I, No. 14
