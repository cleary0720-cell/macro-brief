# Dashboard Agent Memory
Last updated: 2026-06-14

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.
Command: git add index.html archive.html about.html sitemap.xml && git commit -m "..." && git push origin HEAD:main

## Reliable data sources
- Fed Funds Rate: WebSearch "Federal Reserve federal funds rate current 2026" → federalreserve.gov search results confirm range
- CPI: WebSearch "BLS CPI [Month] 2026 year over year inflation" → advisorperspectives.com, cnbc.com summarize BLS data; bls.gov itself returns 403
- Core CPI / Shelter / Energy: Same CPI search; energy component often separately noted
- Core PCE: WebSearch "Core PCE [Month] 2026 BEA personal income outlays" → bea.gov releases listed; bea.gov itself may 403
- ISM PMI: WebSearch "ISM Manufacturing PMI [Month] 2026" → prnewswire.com/ismworld.org covered well
- Jobless Claims: WebSearch "initial jobless claims 4 week average [Month] 2026" → indexbox.io, verifiedinvesting.com, dol.gov summary
- Unemployment: WebSearch "BLS unemployment rate [Month] 2026 jobs report" → bloomberg.com, cnbc.com cover well
- GDP: WebSearch "BEA GDP Q[N] 2026 [estimate]" → bea.gov headlines in search results
- 10-yr Treasury / Yield Curve: WebSearch "Treasury yield curve all maturities [Date] 2026" → advisorperspectives.com "Treasury Yields Snapshot" articles; specific search for date
  - All 10 confirmed maturities: advisorperspectives.com treasury snapshot articles
  - FALLBACK: Some maturities (1M, 6M, 7Y, 20Y) may need interpolation if not in search snippets
- Retail Sales: WebSearch "retail sales [Month] 2026 census bureau year over year advance monthly"
- M2: WebSearch "M2 money supply year over year [Month] 2026 Federal Reserve H.6" → mises.org and macrotrends cover well
- FOMC odds: WebSearch "CME FedWatch [Month] [Year] FOMC meeting hold hike cut probability" → centralbank.watch, kalshi.com, defirate.com

## Known issues
- bls.gov, federalreserve.gov, fred.stlouisfed.org, treasury.gov ALL return HTTP 403 on direct WebFetch
- advisorperspectives.com, streetstats.finance, slickcharts.com also return 403
- Use WebSearch only — government data is well-covered by financial news sites in search snippets
- M2 data: Discrepancy between 4.7% (prior dashboard) and 4.5% (multiple search sources for April 2026). Updated to 4.5% per latest data. Watch for further revisions.
- Treasury yield curve: Typically can confirm 3M, 1Y, 2Y, 5Y, 10Y, 30Y from search. Need to interpolate 1M, 6M, 7Y, 20Y.
  - 1M: Often anomalous (can be above 3M due to bill shortage or FOMC timing). Estimate near Fed Funds midpoint post-CPI print.
  - 6M: Interpolate between 3M and 1Y
  - 7Y: Interpolate between 5Y and 10Y
  - 20Y: Interpolate between 10Y and 30Y

## Run log
### 2026-06-14
- Fed Rate: 3.50–3.75% (3.63% midpoint) — UNCHANGED since Nov 2025
- CPI (May 2026): 4.2% YoY — UP sharply from 3.8% (Iran energy shock)
- Core CPI (May 2026): 2.9% YoY — up from 2.8%
- Shelter (May 2026): 3.4% YoY — up from 3.3%
- Energy (May 2026): +23.5% YoY — up from +17.9% (dominant driver)
- Core PCE (April 2026): 3.3% — UNCHANGED (May data due June 25)
- ISM PMI (May 2026): 54.0 — UNCHANGED (already in dashboard from prior update)
- Jobless Claims 4-wk avg (week ending June 6): 219k — up from 215k
- Unemployment (May 2026): 4.3% — UNCHANGED; May jobs: +172k (beat all estimates)
- GDP Q1 2026 (2nd estimate): +1.6% — UNCHANGED (3rd est. due June 25)
- 10-yr Treasury (June 12): 4.49% — up from 4.45% on May 29
- Retail Sales (April 2026): 4.9% YoY — UNCHANGED (May data due June 17)
- M2 (April 2026): 4.5% YoY — REVISED down from 4.7%
- Yield curve (June 12): 1M 3.80%, 3M 3.71%, 6M 3.79%, 1Y 3.86%, 2Y 4.09%, 5Y 4.22%, 7Y 4.33%, 10Y 4.49%, 20Y 4.75%, 30Y 4.97% — NORMAL curve
- 2s10s spread: +40 bps; 3m10y: +78 bps
- FOMC odds (June 17): CUT 1% / HOLD 99% / HIKE 0% — dot plot key watch item
- Sentiment: 35/100 CAUTIOUS
- Notes: Large CPI jump was energy-driven (Iran-Israel conflict). Markets interpret as transitory supply shock, not rate-hike signal. Next major data: June 17 FOMC + retail sales, June 25 GDP 3rd est. + PCE May, July 3 jobs. Dot plot expected to show zero 2026 cuts (76.8% market probability).
