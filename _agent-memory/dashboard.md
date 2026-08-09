# Dashboard Agent Memory
Last updated: 2026-08-09

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.
Command: git add index.html archive.html about.html sitemap.xml && git commit -m "..." && git push origin HEAD:main

## Reliable data sources
- Fed Funds Rate: WebSearch "FOMC [month] 2026 decision federal funds rate" → stocktitan.net, cnbc.com
- CPI: WebSearch "BLS CPI [month] 2026 year over year" → bls.gov snippets via cnbc.com, usinflationcalculator.com
- Core CPI / Shelter / Energy: Same CPI search — bls.gov PDF linked + cnbc breakdown chart
- Core PCE: WebSearch "BEA core PCE [month] 2026 personal income outlays" → bea.gov snippets, cnbc.com
- ISM PMI: WebSearch "ISM Manufacturing PMI [month] 2026" → prnewswire.com carries official ISM press releases verbatim; emsnow.com and investinglive.com also reliable
- Jobless Claims: WebSearch "initial jobless claims 4 week average [date] 2026" → verifiedinvesting.com, tradingeconomics.com, seekingalpha.com
  - NOTE: DOL releases on Thursday. Weekly + 4-week avg both appear in search snippets.
- Unemployment/Jobs: WebSearch "BLS employment situation [month] 2026" → cnbc.com, foxbusiness.com, resumehog.com (bizarrely good for BLS summaries)
  - NOTE: Always check for prior-month revisions — they can be large (146k combined in July release!)
  - NOTE: Unemployment rate and payrolls can diverge (rate fell to 4.1% even as payrolls -23k July)
- GDP: WebSearch "BEA GDP Q[n] 2026 [estimate]" → advisorperspectives.com, indexbox.io
- 10-yr Treasury / Yield Curve: WebSearch "treasury yields [date] 2026" → cnbc.com most reliable for post-data-release moves; briefs.co, nwaonline.com for coverage
  - IMPORTANT: Fetch yields AFTER the week's biggest data release — yields move on the day of the release
  - Confirmed Aug 7: 2Y=4.20%, 10Y=4.65%, 30Y=5.21% (all sources consistent)
  - For full curve, estimate non-reported maturities based on parallel shift of confirmed maturities
- Retail Sales: WebSearch "retail sales [month] 2026 census bureau year over year" → qz.com, etftrends.com
- M2: WebSearch "M2 money supply [month] 2026 federal reserve H.6" → fxmacrodata.com, tradingeconomics.com
- FOMC odds: WebSearch "CME FedWatch [meeting date] 2026 FOMC probability" → CNBC most reliable for post-event repricing; growbeansprout.com for steady-state tracking
  - CRITICAL: Check EVERY run — odds can move 30+ percentage points in HOURS on a major data release
  - After July jobs miss, September hike fell from 72% → 40% within hours

## Known issues
- bls.gov, federalreserve.gov, fred.stlouisfed.org, treasury.gov ALL return HTTP 403 on direct WebFetch
- Use WebSearch only — all economic data is well-covered in search result snippets
- When payrolls are negative, unemployment rate can STILL fall if participation drops — always report both and note the mechanism
- Prior month revisions often buried in search results — actively search for them ("BLS July 2026 revision May June")
- ISM PMI: Official at prnewswire.com and emsnow.com — also investinglive.com has good context
- sitemap.xml: always regenerate and include in commit even if unchanged
- FOMC odds: After major data (jobs, CPI, FOMC decision), always re-search with the post-release date

## Run log

### 2026-08-09
- Fed Rate: 3.50–3.75% (3.63%) — HELD, 8th consecutive hold; unchanged
- CPI (June 2026): 3.5% YoY — UNCHANGED (July CPI due Aug 12 — critical for September FOMC)
- Core CPI (June 2026): 2.6%; Shelter: 3.3%; Energy: +15.7% — ALL UNCHANGED
- Core PCE (June 2026): 3.3% — UNCHANGED
- ISM PMI (July 2026): 55.6 — ROLLED FORWARD (was June 53.3; four-year high; 7th consecutive expansion month)
  - Production 58.5 (5-year high); Employment 52.8 (crossed 50 for first time in 33 months)
  - Prices Index 71.1 (third consecutive monthly decline)
- Jobless Claims 4-wk avg (week ending Aug 1): 198,750 (~199k) — ROLLED FORWARD to new August entry
  - Weekly: 199k; released Aug 6. Prior 4-wk avg 203,250. First time below 200k in years.
- Unemployment (July 2026): 4.1% — ROLLED FORWARD (was June 4.2%)
  - NFP: -23,000 (first negative payroll print in years; consensus was +83,000)
  - Prior month revisions: May+June revised down combined 146,000
  - Participation: 61.4% (down from 61.5%); long-term unemployed 1.8M
- GDP Q2 2026 advance: +1.5% — UNCHANGED
- 10-yr Treasury (Aug 7): 4.65% — ROLLED FORWARD to August entry (was July 4.74%; -9 bps on jobs miss)
  - 2Y: 4.20% (confirmed); 30Y: 5.21% (confirmed); bull flattener, all maturities -7 to -9 bps
- Retail Sales (June 2026): +6.7% YoY — UNCHANGED (July data due ~Aug 15)
- M2 (June 2026): 5.5% YoY — UNCHANGED
- Yield curve (Aug 7): 1M=3.73%, 3M=3.73%, 6M=3.89%, 1Y=3.96%, 2Y=4.20%, 5Y=4.37%, 7Y=4.43%, 10Y=4.65%, 20Y=5.13%, 30Y=5.21%
  - Curve: NORMAL; 2s10s +45 bps; 3m10y +92 bps; recession prob 5%
- FOMC odds (September 16-17, as of Aug 8-9): CUT 0% / HOLD 60% / HIKE 40%
  - Fell from HOLD 27% / HIKE 72% (Aug 2) to HOLD 60% / HIKE 40% on Aug 7-8 after jobs miss
  - Source: CNBC Aug 7 article confirmed 60% hold / 40% hike
- Sentiment: 46/100 CAUTIOUS (up from 43)
- Edition: Vol. I, No. 15 · August 9, 2026
- Sparklines rolled/updated:
  - unemployment: ROLLED FORWARD (dropped Jul '25 4.2; added Jul '26 4.1; oldest now Aug '25)
  - ism-pmi: ROLLED FORWARD (dropped Jul '25 48.0; added Jul '26 55.6; oldest now Aug '25)
  - jobless-claims: ROLLED FORWARD (dropped Aug '25 224; added Aug '26 199; oldest now Sep '25)
  - treasury: ROLLED FORWARD (dropped Aug '25 4.15; added Aug '26 4.65; oldest now Sep '25)
- Key headline: First payroll loss in years (-23k); ISM PMI four-year high (55.6); bifurcated economy; September hike odds collapsed from 72% → 40%

### 2026-08-02
- Fed Rate: 3.50–3.75% (3.63%) — HELD July 29, 9-3 vote; Hammack, Kashkari, Logan dissented
- CPI (June 2026): 3.5% YoY; Core PCE (June 2026): 3.3% — ROLLED FORWARD; GDP Q2 2026: +1.5% — ROLLED FORWARD
- ISM PMI (June 2026): 53.3; Jobless Claims 4-wk: ~203k; Unemployment 4.2%; 10Y 4.74%; Retail +6.7%; M2 5.5%
- FOMC odds: CUT 1% / HOLD 27% / HIKE 72%; Sentiment: 43/100; Edition: Vol. I, No. 14

### 2026-07-26
- 10-yr Treasury 4.69% (IN-PLACE); Jobless Claims 4-wk 208k (IN-PLACE); all else unchanged
- FOMC odds (July 29): CUT 0% / HOLD 62% / HIKE 38%; Sentiment: 40/100; Edition: Vol. I, No. 13

### 2026-07-19
- CPI (June 2026): 3.5% — ROLLED FORWARD; Retail (June): +6.7% — ROLLED FORWARD
- FOMC odds (July 29): CUT 0% / HOLD 90% / HIKE 10%; Sentiment: 42/100; Edition: Vol. I, No. 12

### 2026-07-12
- CPI May 4.2%; ISM PMI June 53.3; Unemployment 4.2%; GDP Q1 +2.1%; 10Y 4.55%; Retail May +6.9%; M2 5.6%
- FOMC odds (July 29): CUT 0% / HOLD 75% / HIKE 25%; Sentiment: 35/100; Edition: Vol. I, No. 11

### 2026-07-05
- ISM PMI June: 53.3; Jobless Claims 4-wk: 222k; 10Y 4.49%; FOMC odds CUT 24% / HOLD 76%
- Sentiment 37/100; Edition: Vol. I, No. 10

### 2026-06-28
- Fed Rate HELD June 17; CPI 4.2%; Core PCE 3.4%; ISM PMI 54.0; Unemployment 4.3%
- 10Y 4.37%; Retail +6.9%; M2 5.6%; FOMC odds CUT 31% / HOLD 69%; Sentiment 39/100
