# Dashboard Agent Memory
Last updated: 2026-08-02

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.
Command: git add index.html archive.html about.html sitemap.xml && git commit -m "..." && git push origin HEAD:main

## Reliable data sources
- Fed Funds Rate: WebSearch "FOMC June 17 2026 decision federal funds rate" → stocktitan.net, cnbc.com
- CPI: WebSearch "BLS CPI June 2026 year over year" → bls.gov snippets via cnbc.com, usinflationcalculator.com, advisorperspectives.com/dshort
- Core CPI / Shelter / Energy: Same CPI search — bls.gov PDF linked + cnbc breakdown chart
- Core PCE: WebSearch "BEA core PCE [month] 2026 personal income outlays" → bea.gov snippets, cnbc.com
- ISM PMI: WebSearch "ISM Manufacturing PMI [month] 2026" → prnewswire.com carries official ISM press releases verbatim
- Jobless Claims: WebSearch "initial jobless claims 4 week average [month] 2026" → tradingeconomics.com, advisorperspectives.com/dshort, qz.com, fxstreet.com
  - NOTE: DOL can release on Thursday (Jul 23 for Jul 18 week) — always search the Thursday date
- Unemployment/Jobs: WebSearch "BLS employment situation [month] 2026" → cnbc.com, bls.gov summary
- GDP: WebSearch "BEA GDP Q[n] 2026 [estimate]" → advisorperspectives.com, indexbox.io
- 10-yr Treasury / Yield Curve: WebSearch "treasury yields [date] 2026" → etftrends.com and advisorperspectives.com/dshort have full snapshots
  - Confirmed maturities Jul 31: 1M=3.78%, 3M=3.78%, 6M=3.98%*, 1Y=4.05%, 2Y=4.29%, 5Y=4.46%, 7Y=4.52%*, 10Y=4.74%, 20Y=5.22%*, 30Y=5.28%
  - Also check primerates.com/primerate/treasury-yield-curve/ for daily yield curve snapshots
- Retail Sales: WebSearch "retail sales [month] 2026 census bureau year over year" → qz.com, advisorperspectives.com/dshort, etftrends.com
- M2: WebSearch "M2 money supply [month] 2026 federal reserve H.6" → fxmacrodata.com, tradingeconomics.com
- FOMC odds: WebSearch "CME FedWatch [meeting date] 2026 FOMC probability" → growbeansprout.com, hngn.com, rateprobability.com
  - CRITICAL: Odds can flip dramatically in 24-48 hours (Iran geopolitical events)
  - Prefer hngn.com for latest headline %; growbeansprout.com for sustained CME-sourced data
  - Post-decision repricing: September odds shifted to 72% hike within 24h of July 29 hold

## Known issues
- bls.gov, federalreserve.gov, fred.stlouisfed.org, treasury.gov ALL return HTTP 403 on direct WebFetch
- advisorperspectives.com also returns 403 on WebFetch
- Use WebSearch only — all economic data is well-covered in search result snippets
- 20Y Treasury: may exceed 30Y occasionally (liquidity premium or single-source anomaly). If 20Y > 30Y from a single source, note with asterisk and use as-is if multiple sources agree; interpolate (10Y+30Y)/2 only if clearly anomalous
- sitemap.xml: always regenerate and include in commit even if unchanged
- FOMC odds: Check EVERY run — market expectations can flip dramatically (10%→38% in ONE WEEK Jul 19→26; then repriced to 72% hike post Jul 29 hold)
- Multiple sources will show DIFFERENT FOMC odds — prefer CME-specific (growbeansprout.com best, then hngn.com); ignore Polymarket/Kalshi
- jobless claims: always use 4-WEEK AVERAGE for card-val (not the weekly single print)
- jobless claims: update IN-PLACE when still in same calendar month; only roll forward when new month starts
- M2: June 2026 H.6 had methodology revision note — report with asterisk/note if present

## Run log

### 2026-08-02
- Fed Rate: 3.50–3.75% (3.63%) — HELD July 29, 9-3 vote; Hammack, Kashkari, Logan dissented (all wanted 25bps hike)
- CPI (June 2026): 3.5% YoY — UNCHANGED
- Core CPI (June 2026): 2.6%; Shelter: 3.3%; Energy: +15.7% — ALL UNCHANGED
- Core PCE (June 2026): 3.3% — ROLLED FORWARD (was May 3.4%; first monthly decline in 14 months; released July 30)
- ISM PMI (June 2026): 53.3 — UNCHANGED (July data due August 3)
- Jobless Claims 4-wk avg (week ending July 25): ~202,750 (~203k) — DOWN from 208k; weekly 197k; released July 31; UPDATED IN-PLACE July entry (208→203)
- Unemployment (June 2026): 4.2% — UNCHANGED
- GDP Q2 2026 advance: +1.5% — ROLLED FORWARD (was Q1 +2.1%; released July 30; 8 entries now Q3'24–Q2'26)
- 10-yr Treasury (July 31): 4.74% — UP from 4.69% (+5 bps); UPDATED IN-PLACE July entry (4.69→4.74)
  - Bear steepener post-FOMC: 2Y fell -4bps to 4.29%; 10Y +5bps; 30Y +12bps to 5.28%
- Retail Sales (June 2026): +6.7% YoY — UNCHANGED
- M2 (June 2026): 5.5% YoY — ROLLED FORWARD (was May 5.6%; June H.6 released July 28; methodology revision noted)
- Yield curve (July 31): 1M=3.78%, 3M=3.78%, 6M=3.98%*, 1Y=4.05%, 2Y=4.29%, 5Y=4.46%, 7Y=4.52%*, 10Y=4.74%, 20Y=5.22%*, 30Y=5.28%
  - Curve: NORMAL; 2s10s +45 bps; 3m10y +96 bps; recession prob 5%
  - Bear steepener from Jul 24: short end fell, long end rose; classic FOMC hold + future hike reaction
  - Notable: 1M=3M=3.78% — flat at very short end, consistent with funds rate 3.50-3.75% after hold
- FOMC odds (September 16-17 per CME FedWatch, as of Aug 2): CUT 1% / HOLD 27% / HIKE 72%
  - 9-3 vote on July 29 + dissenter hawkishness → dramatic repricing to 72% hike
- Sentiment: 43/100 CAUTIOUS (up from 40)
- Edition: Vol. I, No. 14 · August 2, 2026 · Q3 2026 MACRO OUTLOOK
- Sparklines rolled/updated:
  - GDP: ROLLED FORWARD (added Q2'26 1.5%; was 7 entries Q3'24–Q1'26, now 8 entries Q3'24–Q2'26)
  - core-pce: ROLLED FORWARD (dropped Jun '25 2.6, added Jun '26 3.3)
  - m2: ROLLED FORWARD (added Jun '26 5.5; now 12 entries Jul '25–Jun '26)
  - treasury Jul: IN-PLACE 4.69→4.74
  - jobless-claims Jul: IN-PLACE 208→203
- Key headline: Fed's 9-3 hawkish hold; dissenters named; September hike market odds 72%; GDP decelerating to +1.5%

### 2026-07-26
- Fed Rate: 3.50–3.75% (3.63%) — HELD, no change
- CPI (June 2026): 3.5% YoY — UNCHANGED
- Core CPI (June 2026): 2.6%; Shelter: 3.3%; Energy: +15.7% — ALL UNCHANGED
- Core PCE (May 2026): 3.4% — UNCHANGED (June data due July 30)
- ISM PMI (June 2026): 53.3 — UNCHANGED (July data due August 3)
- Jobless Claims 4-wk avg (week ending July 18): 207,500 (~208k) — DOWN from 214k; weekly print 187,000 (LOWEST SINCE 1969!); released July 23; UPDATED IN-PLACE July entry (214→208)
- Unemployment (June 2026): 4.2% — UNCHANGED
- GDP Q1 2026 final: +2.1% — UNCHANGED (Q2 advance due July 30; GDPNow +1.7% as of Jul 17)
- 10-yr Treasury (July 24): 4.69% — UP from 4.55% (+14 bps); UPDATED IN-PLACE July entry (4.55→4.69)
- Retail Sales (June 2026): +6.7% YoY — UNCHANGED
- M2 (May 2026): 5.6% YoY — UNCHANGED (June data due July 28)
- Yield curve (July 24): 1M 3.82%, 3M 3.90%, 6M 4.09%*, 1Y 4.15%, 2Y 4.33%, 5Y 4.46%, 7Y 4.58%*, 10Y 4.69%, 20Y 4.93%*, 30Y 5.16%
  - Curve: NORMAL; 2s10s +36 bps; 3m10y +79 bps; recession prob ~7%
  - Full curve shifted materially higher: +7 to +18 bps across all maturities
- FOMC odds (July 29 per CME FedWatch/hngn.com July 24): CUT 0% / HOLD 62% / HIKE 38%
  - MAJOR REVERSAL from Jul 19: 90%/10% → 62%/38% in ONE WEEK
  - Driver: Iran Strait of Hormuz re-escalation (new port attacks), oil toward $90/barrel
- Sentiment: 40/100 CAUTIOUS (down from 42)
- Edition: Vol. I, No. 13 · July 26, 2026 · Q3 2026 MACRO OUTLOOK
- Sparklines: NO ROLL (no new monthly data); IN-PLACE updates only
  - treasury Jul: 4.55→4.69; jobless-claims Jul: 214→208
- Other data this week: New home sales Jun 628k (Jul 24); Durable goods Jun advance (Jul 25, less than feared)

### 2026-07-19
- Fed Rate: 3.50–3.75% (3.63%) — HELD, no change
- CPI (June 2026): 3.5% YoY — DOWN from 4.2% (released July 14); ROLLED FORWARD (dropped Jun '25=2.6%, added Jun '26=3.5%)
- Core CPI (June 2026): 2.6%; Shelter: 3.3%; Energy: +15.7%
- Core PCE (May 2026): 3.4% — UNCHANGED
- ISM PMI (June 2026): 53.3 — UNCHANGED
- Jobless Claims 4-wk avg (week ending July 11): 214,250 (~214k); UPDATED IN-PLACE July entry (219→214)
- Unemployment (June 2026): 4.2% — UNCHANGED
- GDP Q1 2026 final: +2.1% — UNCHANGED
- 10-yr Treasury (July 17): 4.55% — UNCHANGED
- Retail Sales (June 2026): +6.7% YoY — DOWN from 6.9% (released July 16); ROLLED FORWARD
- M2 (May 2026): 5.6% YoY — UNCHANGED
- FOMC odds (July 29): CUT 0% / HOLD 90% / HIKE 10%
- Sentiment: 42/100 CAUTIOUS; Edition: Vol. I, No. 12

### 2026-07-12
- Fed Rate: 3.50–3.75% (3.63%); CPI May 4.2%; Core PCE May 3.4%; ISM PMI June 53.3
- Jobless Claims 4-wk avg (week ending July 4): 218,750 (~219k); Unemployment 4.2%; GDP Q1 +2.1%; 10Y 4.55%; Retail May +6.9%; M2 5.6%
- FOMC odds (July 29): CUT 0% / HOLD 75% / HIKE 25%; Sentiment: 35/100; Edition: Vol. I, No. 11

### 2026-07-05
- ISM PMI June: 53.3; Jobless Claims 4-wk avg: 222,000; Unemployment June 4.2%; GDP Q1 +2.1%; 10Y 4.49%; Retail May +6.9%; M2 5.6%
- FOMC odds (July 29): CUT 24% / HOLD 76% / HIKE 0%; Sentiment 37/100; Edition: Vol. I, No. 10

### 2026-06-28
- Fed Rate HELD June 17; CPI 4.2%; Core PCE 3.4%; ISM PMI 54.0; Unemployment 4.3%; Jobs +172k (May)
- 10Y 4.37%; Retail +6.9%; M2 5.6%; FOMC odds: CUT 31% / HOLD 69% / HIKE 0%; Sentiment 39/100
- GDP Q1 final: +2.1% (revised up from +1.6%)
