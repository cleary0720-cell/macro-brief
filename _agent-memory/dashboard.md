# Dashboard Agent Memory
Last updated: 2026-07-19

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.
Command: git add index.html archive.html about.html sitemap.xml && git commit -m "..." && git push origin HEAD:main

## Reliable data sources
- Fed Funds Rate: WebSearch "FOMC June 17 2026 decision federal funds rate" → stocktitan.net, cnbc.com
- CPI: WebSearch "BLS CPI June 2026 year over year" → bls.gov snippets via cnbc.com, usinflationcalculator.com, advisorperspectives.com/dshort
- Core CPI / Shelter / Energy: Same CPI search — bls.gov PDF linked + cnbc breakdown chart
- Core PCE: WebSearch "BEA core PCE May 2026 personal income outlays" → bea.gov snippets, cnbc.com
- ISM PMI: WebSearch "ISM Manufacturing PMI June 2026" → prnewswire.com carries official ISM press releases verbatim
- Jobless Claims: WebSearch "initial jobless claims 4 week average July 2026" → tradingeconomics.com, advisorperspectives.com/dshort
- Unemployment/Jobs: WebSearch "BLS employment situation June 2026" → cnbc.com, bls.gov summary
- GDP: WebSearch "BEA GDP Q1 2026 third estimate" → advisorperspectives.com, indexbox.io
- 10-yr Treasury / Yield Curve: WebSearch "treasury yields July 17 2026" → etftrends.com treasury snapshots, forbes.com treasury rates
  - Confirmed maturities Jul 17: 3M=3.83% (Jul 15), 2Y=4.18%, 5Y=4.28%, 10Y=4.55%, 30Y=5.09%
  - Interpolate: 1M (near Fed funds ~3.65%), 6M (between 3M/1Y avg ~3.94%), 7Y (between 5Y/10Y ~4.39%), 20Y (between 10Y/30Y midpoint ~4.82%)
  - CAUTION: This week saw a spike to unusual levels on July 13 (Iran oil spike); search may show that outlier — use Jul 17 data
- Retail Sales: WebSearch "retail sales June 2026 census bureau year over year" → qz.com, advisorperspectives.com/dshort, etftrends.com
- M2: WebSearch "M2 money supply May 2026 federal reserve H.6" → fxmacrodata.com, tradingeconomics.com (June data due Jul 28)
- FOMC odds: WebSearch "CME FedWatch July 29 2026 FOMC probability" → growbeansprout.com, rateprobability.com
  - IMPORTANT: Post-CPI (July 14) odds collapsed dramatically. Most reliable = growbeansprout citing CME as of July 16 (90% hold)
  - Pre-CPI: 25% hike / 75% hold; Post-CPI: 10% hike / 90% hold — massive shift in one day

## Known issues
- bls.gov, federalreserve.gov, fred.stlouisfed.org, treasury.gov ALL return HTTP 403 on direct WebFetch
- advisorperspectives.com also returns 403 on WebFetch
- Use WebSearch only — all economic data is well-covered in search result snippets
- 20Y Treasury: if search shows 20Y = 30Y (implausible), interpolate 20Y between 10Y and 30Y
- sitemap.xml: always regenerate and include in commit even if unchanged
- FOMC odds: Check every run — market expectations can flip dramatically (this week: 25% hike → 46.5% hike → 10% hike, in ONE week, driven by Iran oil spike then soft CPI)
- Multiple sources will show DIFFERENT FOMC odds — prefer CME-specific results (growbeansprout.com best, then rateprobability.com); ignore Polymarket/Kalshi (different methodology)
- Conflicting sources post-CPI: some showed 37% hike (KuCoin, possibly stale data), others 8-15%, growbeansprout July 16 = 90% hold. Use most recent CME-sourced data.
- Treasury intraweek spikes: July 13 spike in yields may appear in search results — always use end-of-week (Thursday/Friday) data

## Run log

### 2026-07-19
- Fed Rate: 3.50–3.75% (3.63%) — HELD, no change
- CPI (June 2026): 3.5% YoY — DOWN from 4.2% (released July 14); ROLLED FORWARD (dropped Jun '25=2.6%, added Jun '26=3.5%)
- Core CPI (June 2026): 2.6% — DOWN from 2.9%; Shelter: 3.3% (down from 3.4%); Energy: +15.7% (down from +23.5%)
- Core PCE (May 2026): 3.4% — UNCHANGED (June data due late July, likely Jul 30 with personal income)
- ISM PMI (June 2026): 53.3 — UNCHANGED (July data due August 3, 2026)
- Jobless Claims 4-wk avg (week ending July 11): 214,250 (~214k) — DOWN from 218,750; reported July 17; UPDATED IN-PLACE July entry (219→214)
- Unemployment (June 2026): 4.2% — UNCHANGED
- GDP Q1 2026 final: +2.1% — UNCHANGED (Q2 advance due July 30)
- 10-yr Treasury (July 17): 4.55% — UNCHANGED (round-trip spike on July 13 then reversed on CPI)
- Retail Sales (June 2026): +6.7% YoY — DOWN from 6.9% (released July 16); ROLLED FORWARD (dropped Jul '25=4.3%, added Jul=6.7%)
- M2 (May 2026): 5.6% YoY — UNCHANGED (June data due July 28)
- Yield curve (July 17): 1M 3.65%*, 3M 3.83%, 6M 3.94%*, 1Y 4.05%, 2Y 4.18%, 5Y 4.28%, 7Y 4.39%*, 10Y 4.55%, 20Y 4.82%*, 30Y 5.09%
  (* = interpolated)
  - Curve: NORMAL; 2s10s +37 bps (from +36); 3m10y +72 bps (from +69); recession prob ~6%
  - 30Y rose from 5.05% to 5.09%
- FOMC odds (July 29 per CME FedWatch, growbeansprout July 16): CUT 0% / HOLD 90% / HIKE 10%
  - MAJOR REVERSAL from last week: 25% hike → 46.5% hike (July 13 Iran spike) → 10% hike (July 14-16 after CPI)
- Sentiment: 42/100 CAUTIOUS (up from 35; CPI improvement, hike risk reduced)
- Edition: Vol. I, No. 12 · July 19, 2026 · Q3 2026 MACRO OUTLOOK
- Sparklines rolled: CPI (dropped Jun '25=2.6%, added Jun '26=3.5%); retail (dropped Jul '25=4.3%, added Jul=6.7%)
- Sparklines updated in-place: jobless-claims Jul entry: 219→214
- NO ROLL on: unemployment, gdp, m2, core-pce, ism-pmi, fed-rate, treasury (all unchanged)

### 2026-07-12
- Fed Rate: 3.50–3.75% (3.63%) — HELD, no change
- CPI (May 2026): 4.2% YoY — UNCHANGED; Core CPI: 2.9%; Shelter: 3.4%; Energy: +23.5%
- Core PCE (May 2026): 3.4% — UNCHANGED
- ISM PMI (June 2026): 53.3 — UNCHANGED
- Jobless Claims 4-wk avg (week ending July 4): 218,750 (~219k) — ROLLED FORWARD
- Unemployment (June 2026): 4.2% — UNCHANGED
- GDP Q1 2026 final: +2.1% — UNCHANGED
- 10-yr Treasury (July 10): 4.55%
- Retail Sales (May 2026): +6.9% YoY — UNCHANGED
- M2 (May 2026): 5.6% YoY — UNCHANGED
- FOMC odds (July 29): CUT 0% / HOLD 75% / HIKE 25%
- Sentiment: 35/100 CAUTIOUS; Edition: Vol. I, No. 11

### 2026-07-05
- Fed Rate: 3.50–3.75% (3.63%) — HELD; ISM PMI June: 53.3; Jobless Claims 4-wk avg: 222,000
- Unemployment (June 2026): 4.2%; GDP Q1: +2.1%; 10Y: 4.49%; Retail May: +6.9%; M2: 5.6%
- FOMC odds (July 29): CUT 24% / HOLD 76% / HIKE 0%; Sentiment 37/100; Edition: Vol. I, No. 10

### 2026-06-28
- Fed Rate: 3.50–3.75% — HELD June 17; CPI 4.2%; Core PCE 3.4%; ISM PMI 54.0; Unemployment 4.3%
- Jobs +172k (May); 10Y 4.37%; Retail +6.9%; M2 5.6%
- FOMC odds: CUT 31% / HOLD 69% / HIKE 0%; Sentiment 39/100
- GDP Q1 final: +2.1% (revised up from +1.6%)
