# Dashboard Agent Memory — The Macro Brief

## Last Run
- **Date:** November 22, 2026 (Sunday)
- **Edition:** Vol. I, No. 31

---

## Current Data (as of November 22, 2026)

| Indicator | Value | Direction | Source / Date |
|---|---|---|---|
| Fed Funds Rate | 3.75–4.00% (mid: 3.88%) | → HOLD | FOMC Oct 28–29, 2026; next meeting Dec 9 |
| CPI (YoY) | **NO DATA** (last confirmed: 3.7% Sept) | — | BLS Oct 10 report: +0.4% MoM only; no YoY due to Oct 2025 data gap |
| CPI (MoM) | +0.4% Oct | ↑ | BLS, released Nov 10 (October data) |
| Core CPI (YoY) | 3.1% (last confirmed Sept) | ↑ | BLS, released Oct 14 (September data) |
| Shelter (YoY) | 4.2% (last confirmed Sept) | ↑ | BLS, released Oct 14 (September data) |
| Energy (YoY) | +20.4% (last confirmed Sept) | ↑ | BLS, released Oct 14 (September data) |
| Unemployment | 4.1% | ↓ | BLS, released Nov 6 (October data) |
| Payrolls | +165,000 | ↑ | BLS, released Nov 6 (October data) |
| GDP Q3 2026 | +3.4% annualized | ↑ ADVANCE | BEA, released Oct 30; second estimate due Nov 25 |
| 10-Year Treasury | **4.92%** | ↓ RALLY | Nov 20, 2026 (rally from 5.15% post-CPI peak; down 23 bps on week) |
| Retail Sales (YoY) | +6.8% | ↑ | Census, released Nov 17 (October data); ROLLED FORWARD this run |
| M2 (YoY) | 5.7% | → | Fed H.6, released Oct 27 (September data); Oct due ~Nov 24–25 |
| Core PCE (YoY) | 3.1% | ↑ | BEA, released Oct 30 (September data); Oct due Nov 25 |
| ISM Manufacturing PMI | 55.5 | ↑ | ISM, released Nov 3 (October data) |
| Jobless Claims (weekly) | 203,000 | — | DOL, released Nov 19 (week ending Nov 14) |
| Jobless Claims (4-wk avg) | 198,000 | → | DOL, released Nov 19 (Nov 14 4-wk avg = 197,750 ≈ 198K) |
| Continuing Claims | 1,763,000 | ↑ | DOL, released Nov 19 (highest since late Aug — monitoring) |
| 30-yr Mortgage Rate | **7.28%** | ↑ | Freddie Mac PMMS, Nov 19 (up from 7.11%; survey captured pre-rally rates) |
| Macro Sentiment | 52 / 100 | NEUTRAL+ | Dashboard calculation |

---

## CRITICAL NOTE — October CPI Data Gap
The BLS did not collect October 2025 CPI data during the federal appropriations lapse. As a result, the October 2026 CPI report (released November 10) contains monthly data (+0.4% MoM) but **no year-over-year figure**. The CPI sparkline was NOT rolled forward — it still shows September as the latest YoY data point (3.7%). Dashboard card shows "OCT: +0.4% MOM (NO YOY DATA AVAIL.)". Last confirmed YoY = September 3.7%.

---

## Yield Curve — November 20, 2026

| Tenor | Yield |
|---|---|
| 1-Month | 4.19% |
| 3-Month | 4.32% |
| 6-Month | 4.38% |
| 1-Year | 4.51% |
| 2-Year | 4.63% |
| 5-Year | 4.71% |
| 7-Year | 4.80% |
| 10-Year | 4.92% |
| 20-Year | 5.34% |
| 30-Year | 5.31% |

- **Curve shape:** Normal overall (mild kink: 20Y 5.34% > 30Y 5.31%, same as prior week)
- **Gradient color:** #1B5E20 (green)
- **Badge:** ▲ Normal
- **2s10s spread:** +29 bps
- **3m10y spread:** +60 bps
- **SVG Y range:** 3.99% to 5.54%, span 1.55%, Y(v) = 30 + (5.54 - v) / 1.55 * 112
- **Polygon baseline:** y=142
- **Grid lines at:** 4.20% (y=126.8), 4.60% (y=97.9), 5.00% (y=69.0), 5.40% (y=40.1)
- **SVG polyline coords:**
  - 1M(4.19%): (46.0, 127.5), 3M(4.32%): (96.7, 118.2), 6M(4.38%): (147.3, 113.8)
  - 1Y(4.51%): (198.0, 104.4), 2Y(4.63%): (248.7, 95.8), 5Y(4.71%): (299.3, 90.0)
  - 7Y(4.80%): (350.0, 83.5), 10Y(4.92%): (400.7, 74.8), 20Y(5.34%): (451.3, 44.4)
  - 30Y(5.31%): (502.0, 46.6)

---

## FOMC Probability Bar

- **Next meeting:** December 9, 2026
- **Current rate:** 3.75–4.00% (held Oct 28–29, 10-2; Cook & Hammack dissented for hike)
- **HIKE +25 bps:** ~97% (essentially all of hike contracts)
- **HOLD:** ~3%
- **CUT:** 0%
- **Source:** CME FedWatch snapshot November 20, 2026 (10Y rally week; 50bps hike priced away)
- **Context:** 10Y eased to 4.92%; retail +6.8%; claims 203K; Nov 25 Core PCE is pivotal

---

## Sparkline Arrays (as of November 22, 2026)

### fed-rate (12 months — unchanged this run)
months: ["Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [3.83,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.88]
Note: ROLL FORWARD when December 9 FOMC acts (drop "Oct", add "Dec" at new mid-rate; if +25 bps → 4.13%)

### cpi (12 months — UNCHANGED — NO YoY for October due to data gap)
months: ["Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [2.6,2.8,2.9,3.1,3.3,3.6,3.8,4.2,3.5,3.4,3.4,3.7]
Note: NOT rolled forward — Oct 2026 CPI has no YoY figure. ROLL FORWARD when Nov CPI released ~Dec 10

### unemployment (12 months — unchanged this run)
months: ["Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
values: [4.2,4.2,4.1,4.2,4.2,4.3,4.3,4.2,4.1,4.1,4.2,4.1]
Note: Next: ROLL FORWARD when Nov jobs released ~Dec 5 (drop "Nov", add "Nov")

### treasury (12 months — UPDATED IN-PLACE this run)
months: ["Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"]
values: [4.35,4.38,4.40,4.42,4.46,4.45,4.37,4.74,4.73,5.11,4.94,4.92]
Note: Updated "Nov" in-place from 5.15 → 4.92 (Nov 20 close — same calendar month).
Next: ROLL FORWARD when Dec data arrives (drop "Dec", add "Dec" at new value)

### retail (12 months — ROLLED FORWARD this run)
months: ["Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"]
values: [4.5,4.3,4.2,4.2,4.2,4.9,6.9,6.7,5.0,6.0,6.3,6.8]
Note: Rolled forward Nov 22 — dropped "Nov" (4.2%), added "Nov" (6.8%) for October data released Nov 17.
Next: ROLL FORWARD when Nov retail released ~Dec 15 (drop "Dec", add "Dec" at new value)

### m2 (12 months — unchanged this run)
months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [4.2,4.3,4.4,4.5,4.6,4.6,4.7,5.6,5.5,5.4,5.7,5.7]
Note: ROLL FORWARD when Oct H.6 released ~Nov 24–25 (drop "Oct '25", add "Oct")

### core-pce (12 months — unchanged this run)
months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [2.8, 2.9, 3.0, 3.1, 3.1, 3.2, 3.3, 3.4, 3.3, 3.0, 3.0, 3.1]
Note: ROLL FORWARD when Oct Core PCE released Nov 25 (drop "Oct '25", add "Oct")

### ism-pmi (12 months — unchanged this run)
months: ["Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
values: [48.2, 47.9, 52.6, 52.4, 52.7, 52.7, 54.0, 53.3, 55.6, 54.6, 54.5, 55.5]
Note: ROLL FORWARD when Nov ISM Manufacturing released Dec 1 (drop "Nov", add "Nov")

### jobless-claims (12 months — UPDATED IN-PLACE this run)
months: ["Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"]
values: [218, 213, 216, 211, 202, 215, 222, 203, 207, 200, 195, 198]
Note: Updated "Nov" in-place from 195 → 198 (DOL Nov 19; Nov 14 4-wk avg 197,750 ≈ 198K).
Next: ROLL FORWARD when Dec data arrives (drop "Dec", add "Dec" at new value)

### gdp (8 quarters — unchanged this run)
months: ["Q4 '24","Q1 '25","Q2 '25","Q3 '25","Q4 '25","Q1 '26","Q2 '26","Q3 '26"]
values: [2.3,-0.3,2.8,1.9,0.5,2.1,2.2,3.4]
Note: UPDATE IN-PLACE Q3 '26 if second estimate revises (due Nov 25); ROLL FORWARD when Q4 '26 advance arrives (~Jan 29, 2027)

---

## What to Watch (Next 4 Events)

1. **Nov 25 (Tue)** — Core PCE + GDP 2nd estimate + M2 H.6 (BEA/Fed) — ROLL FORWARD core-pce, m2; UPDATE IN-PLACE gdp; PIVOTAL for Dec 9 hike odds
2. **Dec 1 (Mon)** — ISM Manufacturing PMI, November 2026 — ROLL FORWARD ism-pmi sparkline
3. **Dec 5 (Fri)** — Jobs Report, November 2026 (BLS) — ROLL FORWARD unemployment sparkline
4. **Dec 9 (Wed)** — FOMC Decision — if hike: ROLL FORWARD fed-rate sparkline (drop "Oct", add "Dec" at 4.13% if +25bps)

---

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App.
NOTE: Fed Tracker agent also pushes to main — pull --rebase before push if rejected.

## Reliable data sources
- Fed Funds Rate: WebSearch → stocktitan.net, cnbc.com
- CPI / Core CPI / Shelter / Energy: WebSearch → cnbc.com, wsj.com
- Core PCE: WebSearch → bea.gov snippets, cnbc.com, stocktitan.net
- ISM PMI: WebSearch → prnewswire.com, textileworld.com, industrytoday.com
- Jobless Claims: WebSearch → fxstreet.com, ctasc.com, verifiedinvesting.com, qz.com
- Unemployment: WebSearch → roberthalf.com, cnbc.com
- GDP: WebSearch → indexbox.io, bondstats.org, advisorperspectives.com
- 10-yr Treasury / Yield Curve: WebSearch → etftrends.com (Treasury yields snapshot), treasury.gov snippets
- Retail Sales: WebSearch → census.gov snippets, programbusiness.com, proinvestorinsights.substack.com
- M2: WebSearch → FRED snippets, tradingeconomics.com, fxmacrodata.com
- FOMC odds: WebSearch "CME FedWatch [meeting date] probability" → CNBC, biggo.com/finance, centralbank.watch
- Mortgage rate: WebSearch "Freddie Mac PMMS" → globenewswire.com, wrenews.com, unitedstatesrealestateinvestor.com

## Run Log — November 22, 2026
- Fed Rate: 3.88% midpoint — HELD; Dec 9 at ~97% hike (CME FedWatch Nov 20)
- CPI: **Oct MoM +0.4% / NO YoY** — data gap; sparkline NOT rolled
- Core CPI: 3.1% last confirmed Sept — no change
- Core PCE: 3.1% — unchanged (Oct Core PCE due Nov 25 — pivotal for Dec 9)
- ISM Manufacturing PMI: 55.5 — unchanged (Nov data Dec 1)
- Unemployment: 4.1% — unchanged (Nov jobs Dec 5)
- GDP: +3.4% advance — unchanged (second estimate Nov 25)
- 10-yr Treasury: **4.92%** (UPDATED IN-PLACE — Nov 20 rally from 5.15%; -23 bps on week)
- Jobless Claims: 203K weekly / **198K 4-wk avg** (UPDATED IN-PLACE — DOL Nov 19; continuing claims 1,763K = highest since late Aug)
- Retail Sales: **+6.8% YoY** (ROLLED FORWARD — Census Nov 17; +0.2% MoM to $748.2B)
- M2: 5.7% — unchanged (Oct H.6 due ~Nov 24–25)
- 30-yr Mortgage: **7.28%** (Freddie Mac PMMS, Nov 19; up from 7.11%; survey pre-dates rally)
- FOMC odds: CUT 0% / HOLD 3% / HIKE 97% — Dec 9; 50bp scenario priced away
- Sentiment: **52/100 NEUTRAL** (up from 50 — yield rally + retail beat partially offset by mortgage spike and continuing claims uptick)
- Sparklines updated in-place: treasury (5.15→4.92), jobless-claims (195→198)
- Sparklines rolled forward: retail (Nov '25/4.2 dropped; Nov/6.8 added)
- Unchanged: cpi, m2, core-pce, fed-rate, gdp, unemployment, ism-pmi
