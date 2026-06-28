# Dashboard Agent Memory
Last updated: 2026-06-28

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.
Command: git add index.html archive.html about.html sitemap.xml && git commit -m "..." && git push origin HEAD:main

## Reliable data sources
- Fed Funds Rate: WebSearch "FOMC June 17 2026 decision federal funds rate" → stocktitan.net, cnbc.com cover fully
- CPI: WebSearch "BLS CPI May 2026 year over year" → advisorperspectives.com/dshort, cnbc.com summarize BLS data
- Core CPI / Shelter / Energy: Same CPI search
- Core PCE: WebSearch "BEA core PCE May 2026 personal income outlays" → bea.gov snippets, babypips.com, employamerica.org
- ISM PMI: WebSearch "ISM Manufacturing PMI May 2026" → prnewswire.com carries official ISM press releases verbatim
- Jobless Claims: WebSearch "initial jobless claims 4 week average June 2026" → verifiedinvesting.com, DOL ETA
- Unemployment: WebSearch "BLS unemployment rate May 2026" → 4.3%
- GDP: WebSearch "BEA GDP Q1 2026 third estimate June 25" → advisorperspectives.com, indexbox.io cover BEA releases
- 10-yr Treasury / Yield Curve: WebSearch "treasury yields June 26 2026" → CNBC, FRED, StreetStats
  - Confirmed: 3M=3.75%, 1Y=3.93%, 2Y=4.10%, 5Y=4.13%, 10Y=4.37%, 30Y=4.87%
  - Interpolated: 1M=3.65%, 6M=3.84%, 7Y=4.22%, 20Y=4.62%
- Retail Sales: WebSearch "retail sales May 2026 census bureau" → nrf.com, advisorperspectives.com/dshort
- M2: WebSearch "M2 money supply May 2026 federal reserve H.6" → fxmacrodata.com, tradingeconomics.com
- FOMC odds: WebSearch "CME FedWatch July 29 2026 FOMC probability" → cmegroup.com, centralbank.watch, growbeansprout.com

## Known issues
- bls.gov, federalreserve.gov, fred.stlouisfed.org, treasury.gov ALL return HTTP 403 on direct WebFetch
- advisorperspectives.com also returns 403 on WebFetch
- Use WebSearch only — all economic data is well-covered in search result snippets
- 1M, 6M, 7Y, and 20Y Treasury yields not confirmed in search results — interpolate from confirmed points
- sitemap.xml: if no new articles added since last run, it won't show as changed in git diff. Just skip if unchanged.

## Run log
### 2026-06-28
- Fed Rate: 3.50–3.75% (3.63% midpoint) — HELD June 17, UNCHANGED
- CPI (May 2026): 4.2% YoY — UNCHANGED
- Core CPI (May 2026): 2.9% YoY — UNCHANGED
- Shelter (May 2026): 3.4% YoY — UNCHANGED
- Energy (May 2026): +23.5% YoY — UNCHANGED
- Core PCE (May 2026): 3.4% — UP from 3.3% (April) — released June 25
- ISM PMI (May 2026): 54.0 — UNCHANGED (June data due July 1)
- Jobless Claims 4-wk avg (week ending June 21): 224,250 — UP from 223,250; continued claims 1,821k (multi-month high)
- Unemployment (May 2026): 4.3% — UNCHANGED
- GDP Q1 2026 (3rd/final estimate): +2.1% — UP from +1.6% (2nd est.); released June 25
- 10-yr Treasury (June 26): 4.37% — DOWN from 4.45% (June 18)
- Retail Sales (May 2026): +6.9% YoY — UNCHANGED
- M2 (May 2026): 5.6% YoY — UP sharply from 4.7% (April); H.6 released June 23
- Yield curve (June 26): 1M 3.65%, 3M 3.75%, 6M 3.84%, 1Y 3.93%, 2Y 4.10%, 5Y 4.13%, 7Y 4.22%, 10Y 4.37%, 20Y 4.62%, 30Y 4.87%
  - 1M/6M/7Y/20Y interpolated; 3M/1Y/2Y/5Y/10Y/30Y confirmed
  - Curve: NORMAL; 2s10s +27 bps (unchanged); 3m10y +62 bps (was +70)
- FOMC odds (July 29): CUT 31% / HOLD 69% / HIKE 0% — DRAMATIC REVERSAL from CUT 1% / HOLD 80% / HIKE 19%
- Sentiment: 39/100 CAUTIOUS (up from 37)
- Edition: Vol. I, No. 9
- Notes: Main story this week was FOMC odds flip — from 19% hike to 31% cut in 7 days. Driven by GDP revision to +2.1%, Core PCE at 3.4% (slightly below worst fears), and continued claims hitting multi-month high (1,821k). M2 surge to 5.6% is worrying but largely ignored by markets short-term. Card for M2 changed from neu to neg.
- Sparkline rolls: m2 (dropped May '25=3.9, added May '26=5.6); core-pce (dropped May '25=2.6, added May '26=3.4); treasury (updated Jun 4.45→4.37); gdp (updated Q1 '26 1.6→2.1); jobless-claims (updated Jun 223→224)

### 2026-06-21
- Fed Rate: 3.50–3.75% (3.63% midpoint) — HELD June 17, unanimous 12-0, new Chair Kevin Warsh
- Dot Plot: HAWKISH shift — year-end median jumped to 3.8% from 3.4%; 9/18 members project hike; 6 project 2+ hikes; Warsh didn't submit a dot
- CPI (May 2026): 4.2% YoY — UNCHANGED
- Core CPI (May 2026): 2.9% YoY — UNCHANGED
- Shelter (May 2026): 3.4% YoY — UNCHANGED
- Energy (May 2026): +23.5% YoY — UNCHANGED
- Core PCE (April 2026): 3.3% — UNCHANGED (May data due June 25)
- ISM PMI (May 2026): 54.0 — UNCHANGED (June data due July 1)
- Jobless Claims 4-wk avg (week ending June 13): 223,250 — UP from 219,000
- Unemployment (May 2026): 4.3% — UNCHANGED
- GDP Q1 2026 (2nd estimate): +1.6% — UNCHANGED (3rd est. due June 25)
- 10-yr Treasury (June 18): 4.45%
- Retail Sales (May 2026): +6.9% YoY — strongest in over a year
- M2 (April 2026): 4.7% YoY — revised UP from 4.5%
- Yield curve (June 18): 1M 3.78%, 3M 3.75%, 6M 3.86%, 1Y 3.95%, 2Y 4.18%, 5Y 4.30%, 7Y 4.37%, 10Y 4.45%, 20Y 4.68%, 30Y 4.90%
- 2s10s spread: +27 bps; 3m10y: +70 bps
- FOMC odds (July 29): CUT 1% / HOLD 80% / HIKE 19%
- Sentiment: 37/100 CAUTIOUS

### 2026-06-14
- Fed Rate: 3.50–3.75% (3.63% midpoint) — UNCHANGED since Nov 2025
- CPI (May 2026): 4.2% YoY — UP sharply from 3.8% (Iran energy shock)
- Core CPI (May 2026): 2.9% YoY — up from 2.8%
- Shelter (May 2026): 3.4% YoY — up from 3.3%
- Energy (May 2026): +23.5% YoY — up from +17.9% (dominant driver)
- Core PCE (April 2026): 3.3% — UNCHANGED
- ISM PMI (May 2026): 54.0 — UNCHANGED
- Jobless Claims 4-wk avg (week ending June 6): 219k
- Unemployment (May 2026): 4.3% — UNCHANGED; May jobs: +172k
- GDP Q1 2026 (2nd estimate): +1.6%
- 10-yr Treasury (June 12): 4.49%
- Retail Sales (April 2026): 4.9% YoY
- M2 (April 2026): 4.5% YoY
- Yield curve (June 12): 1M 3.80%, 3M 3.71%, 6M 3.79%, 1Y 3.86%, 2Y 4.09%, 5Y 4.22%, 7Y 4.33%, 10Y 4.49%, 20Y 4.75%, 30Y 4.97%
- FOMC odds (June 17): CUT 1% / HOLD 99% / HIKE 0%
- Sentiment: 35/100 CAUTIOUS
