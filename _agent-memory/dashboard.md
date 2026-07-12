# Dashboard Agent Memory
Last updated: 2026-07-12

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.
Command: git add index.html archive.html about.html sitemap.xml && git commit -m "..." && git push origin HEAD:main

## Reliable data sources
- Fed Funds Rate: WebSearch "FOMC June 17 2026 decision federal funds rate" → stocktitan.net, cnbc.com
- CPI: WebSearch "BLS CPI [Month] 2026 year over year" → advisorperspectives.com/dshort, cnbc.com
- Core CPI / Shelter / Energy: Same CPI search
- Core PCE: WebSearch "BEA core PCE [Month] 2026 personal income outlays" → bea.gov snippets, babypips.com
- ISM PMI: WebSearch "ISM Manufacturing PMI [Month] 2026" → prnewswire.com carries official ISM press releases verbatim
- Jobless Claims: WebSearch "initial jobless claims 4 week average [Month] 2026" → tradingeconomics.com, DOL (verifiedinvesting.com also has weekly detail)
- Unemployment/Jobs: WebSearch "BLS employment situation [Month] 2026" → cnbc.com, Indeed Hiring Lab
- GDP: WebSearch "BEA GDP Q1 2026 third estimate" → advisorperspectives.com, indexbox.io
- 10-yr Treasury / Yield Curve: WebSearch "treasury yields [Date] 2026" → primerates.com, seekingalpha.com, streetstats.finance
  - Confirmed maturities: 3M, 1Y, 2Y, 5Y, 7Y, 10Y, 30Y usually available
  - Interpolate: 1M (near Fed funds rate), 6M (between 3M and 1Y avg), 20Y (between 10Y and 30Y midpoint)
  - CAUTION: If search shows 20Y = 30Y (implausible), interpolate 20Y instead
- Retail Sales: WebSearch "retail sales [Month] 2026 census bureau" → nrf.com, advisorperspectives.com/dshort
- M2: WebSearch "M2 money supply [Month] 2026 federal reserve H.6" → fxmacrodata.com, tradingeconomics.com
- FOMC odds: WebSearch "CME FedWatch July 29 2026 FOMC probability" → cmegroup.com, growbeansprout.com, rateprobability.com
  - Always prefer CME-specific results over prediction markets (Polymarket, Kalshi give different numbers)
  - IMPORTANT: Odds can change dramatically week to week (this week: 24% cut last week → 25% HIKE this week)

## Known issues
- bls.gov, federalreserve.gov, fred.stlouisfed.org, treasury.gov ALL return HTTP 403 on direct WebFetch
- advisorperspectives.com also returns 403 on WebFetch
- Use WebSearch only — all economic data is well-covered in search result snippets
- 20Y Treasury: if search shows 20Y = 30Y (implausible), interpolate 20Y between 10Y and 30Y
- sitemap.xml: always regenerate and include in commit even if unchanged
- FOMC odds: Check every run — market expectations can flip dramatically without data releases

## Run log

### 2026-07-12
- Fed Rate: 3.50–3.75% (3.63%) — HELD, no change
- CPI (May 2026): 4.2% YoY — UNCHANGED (June CPI due July 14, CRITICAL release)
- Core CPI (May 2026): 2.9% — UNCHANGED; Shelter: 3.4%; Energy: +23.5%
- Core PCE (May 2026): 3.4% — UNCHANGED (June data due late July)
- ISM PMI (June 2026): 53.3 — UNCHANGED
- Jobless Claims 4-wk avg (week ending July 4): 218,750 (~219k) — DOWN from 222,000; released July 9; ROLLED FORWARD (added Jul, dropped oldest Aug '25)
- Unemployment (June 2026): 4.2% — UNCHANGED
- GDP Q1 2026 final: +2.1% — UNCHANGED
- 10-yr Treasury (July 10): 4.55% — UP 6 bps from 4.49%
- Retail Sales (May 2026): +6.9% YoY — UNCHANGED (June data due July 16)
- M2 (May 2026): 5.6% YoY — UNCHANGED
- Yield curve (July 10): 1M 3.73%*, 3M 3.86%, 6M 3.96%*, 1Y 4.06%, 2Y 4.19%, 5Y 4.27%, 7Y 4.40%, 10Y 4.55%, 20Y 4.80%*, 30Y 5.05%
  (* = interpolated)
  - Curve: NORMAL; 2s10s +36 bps (from +31); 3m10y +69 bps; recession prob ~7%
  - 30Y crossed 5.00% for first time this cycle
- FOMC odds (July 29 per CME FedWatch ~July 8-10): CUT 0% / HOLD 75% / HIKE 25%
  - MAJOR REVERSAL: Last week was CUT 24% / HOLD 76% / HIKE 0%
  - No major data release triggered this — pure market repricing on inflation backdrop
- Sentiment: 35/100 CAUTIOUS (down from 37; hawkish repricing)
- Edition: Vol. I, No. 11 · July 12, 2026 · Q3 2026 MACRO OUTLOOK
- Sparklines rolled: jobless-claims (added Jul=219, dropped oldest; new months: Aug'25 thru Jul)
- Sparklines updated: treasury Jul entry: 4.49→4.55
- NO ROLL on: cpi, unemployment, gdp, retail, m2, core-pce, ism-pmi, fed-rate (no new monthly data)

### 2026-07-05
- Fed Rate: 3.50–3.75% (3.63%) — HELD, 5th consecutive hold in 2026
- CPI (May 2026): 4.2% YoY — UNCHANGED (June CPI due July 14)
- Core CPI (May 2026): 2.9% — UNCHANGED; Shelter: 3.4%; Energy: +23.5%
- Core PCE (May 2026): 3.4% — UNCHANGED (June data due late July)
- ISM PMI (June 2026): 53.3 — DOWN from 54.0; released July 1; Prices Paid -9.1 pts; 6th expansion month
- Jobless Claims 4-wk avg (week ending June 27): 222,000 — DOWN from 224,250; released July 3; UPDATED June entry (no roll)
- Unemployment (June 2026): 4.2% — DOWN from 4.3%, participation 61.5% (lowest since March 2021)
  - June payrolls: +57,000 (very weak, expected +115,000)
- GDP Q1 2026 final: +2.1% — UNCHANGED
- 10-yr Treasury (July 2): 4.49% — UP 12 bps from 4.37%
- Retail Sales (May 2026): +6.9% YoY — UNCHANGED
- M2 (May 2026): 5.6% YoY — UNCHANGED
- Yield curve (July 2): 1M 3.69%*, 3M 3.79%*, 6M 3.88%*, 1Y 3.98%*, 2Y 4.17%, 5Y 4.24%, 7Y 4.35%, 10Y 4.49%, 20Y 4.75%*, 30Y 4.97%
  - Curve: NORMAL; 2s10s +31 bps; 3m10y +69 bps; recession prob ~8%
- FOMC odds (July 29 per CME FedWatch July 4): CUT 24% / HOLD 76% / HIKE 0%
- Sentiment: 37/100 CAUTIOUS
- Edition: Vol. I, No. 10 · July 5, 2026 · Q3 2026 MACRO OUTLOOK

### 2026-06-28
- Fed Rate: 3.50–3.75% — HELD June 17; CPI 4.2%; Core PCE 3.4%; ISM PMI 54.0; Unemployment 4.3%
- Jobs +172k (May); 10Y 4.37%; Retail +6.9%; M2 5.6%
- FOMC odds: CUT 31% / HOLD 69% / HIKE 0%; Sentiment 39/100
- GDP Q1 final: +2.1% (revised up from +1.6%)

### 2026-06-21
- Fed Rate: 3.50–3.75% — HELD June 17; hawkish dot plot (9/18 project hike, median 3.8% year-end)
- 10Y: 4.45%; FOMC odds: CUT 1% / HOLD 80% / HIKE 19%; Sentiment 37/100
