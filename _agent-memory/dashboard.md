# Dashboard Agent Memory — The Macro Brief

## Last Run
- **Date:** November 8, 2026 (Sunday)
- **Edition:** Vol. I, No. 29

---

## Current Data (as of November 8, 2026)

| Indicator | Value | Direction | Source / Date |
|---|---|---|---|
| Fed Funds Rate | 3.75–4.00% (mid: 3.88%) | → HOLD 10-2 | FOMC Oct 28–29, 2026; dissents: Cook & Hammack (hike) |
| CPI (YoY) | 3.7% | ↑ | BLS, released Oct 14 (September data); Core CPI 3.1% |
| Core CPI (YoY) | 3.1% | ↑ | BLS, released Oct 14 (September data) |
| Shelter (YoY) | 4.2% | ↑ | BLS, released Oct 14 (September data) |
| Energy (YoY) | +20.4% | ↑ | BLS, released Oct 14 (September data) |
| Unemployment | 4.1% | ↓ | BLS, released Nov 6 (October data) |
| Payrolls | +165,000 | ↑ | BLS, released Nov 6 (October data); Sep revised +29K→+45K |
| GDP Q3 2026 | +3.4% annualized | ↑ ADVANCE | BEA, released Oct 30; Q2 final revised to +2.2% |
| GDP Q2 2026 | +2.2% annualized (final) | ↑ revised | BEA, revised Oct 30 |
| 10-Year Treasury | 4.86% | ↓ | Nov 6, 2026 (post-jobs easing from 4.94% Oct 30) |
| Retail Sales (YoY) | +6.3% | ↑ | Census, released Oct 15 (September data) |
| M2 (YoY) | 5.7% | → | Fed H.6, released Oct 27 (September data); $23.4T SA |
| Core PCE (YoY) | 3.1% | ↑ | BEA, released Oct 30 (September data) — up from 3.0% Aug |
| ISM Manufacturing PMI | 55.5 | ↑ | ISM, released Nov 3 (October data); Prices Paid 75.2 |
| Jobless Claims (weekly) | 189,000 | ↓ | DOL, released Nov 6 (week ending Nov 1) |
| Jobless Claims (4-wk avg) | 195,000 | ↓ | DOL, released Nov 6 (Nov 1 4-wk avg ~195K) |
| 30-yr Mortgage Rate | 7.18% | ↓ | Freddie Mac PMMS, Nov 6 |
| Macro Sentiment | 52 / 100 | NEUTRAL | Dashboard calculation |

---

## Yield Curve — November 6, 2026

| Tenor | Yield |
|---|---|
| 1-Month | 4.02% |
| 3-Month | 4.19% |
| 6-Month | 4.26% |
| 1-Year | 4.33% |
| 2-Year | 4.51% |
| 5-Year | 4.64% |
| 7-Year | 4.74% (interpolated) |
| 10-Year | 4.86% |
| 20-Year | 5.06% (interpolated) |
| 30-Year | 5.26% |

- **Curve shape:** Normal and upward-sloping (steepening)
- **Gradient color:** #1B5E20 (green)
- **2s10s spread:** +35 bps (narrowed from +38 bps)
- **3m10y spread:** +67 bps (narrowed from +85 bps — 3M yield rose from 4.09% to 4.19%)
- **SVG Y range:** 3.82% to 5.46%, span 1.64%, Y(v) = 30 + (5.46 - v) / 1.64 * 112
- **Grid lines at:** 4.00% (y=129.7), 4.40% (y=102.4), 4.80% (y=75.1), 5.20% (y=47.8)
- **SVG polyline coords:**
  - 1M(4.02%): (46.0, 128.3), 3M(4.19%): (96.7, 116.7), 6M(4.26%): (147.3, 111.9)
  - 1Y(4.33%): (198.0, 107.2), 2Y(4.51%): (248.7, 94.9), 5Y(4.64%): (299.3, 86.0)
  - 7Y(4.74%): (350.0, 79.2), 10Y(4.86%): (400.7, 71.0), 20Y(5.06%): (451.3, 57.3)
  - 30Y(5.26%): (502.0, 43.7)

---

## FOMC Probability Bar

- **Next meeting:** December 9, 2026
- **Current rate:** 3.75–4.00% (held Oct 28–29, 10-2; Cook & Hammack dissented for hike)
- **HIKE +25 bps:** 79% (flex: 79)
- **HOLD:** 21% (flex: 21)
- **CUT -25 bps:** 0% (flex: 0)
- **Source:** CME FedWatch snapshot November 6, 2026 (post Oct jobs report)
- **Context:** Oct jobs +165K, unemployment 4.1%, ISM 55.5, Q3 GDP +3.4% → Dec 9 at 79% hike

---

## Sparkline Arrays (as of November 8, 2026)

### fed-rate (12 months — unchanged this run; FOMC held)
months: ["Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [3.83,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.88]
Note: ROLL FORWARD when December 9 FOMC acts (drop "Oct", add "Dec" at new mid-rate; if +25 bps → 4.13%)

### cpi (12 months — unchanged this run)
months: ["Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [2.6,2.8,2.9,3.1,3.3,3.6,3.8,4.2,3.5,3.4,3.4,3.7]
Note: ROLL FORWARD when Oct CPI released Nov 12 (drop "Oct"/2.6, add "Oct" at new value)

### unemployment (12 months — ROLLED FORWARD this run)
months: ["Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
values: [4.2,4.2,4.1,4.2,4.2,4.3,4.3,4.2,4.1,4.1,4.2,4.1]
Note: Rolled forward Nov 6; Oct unemployment = 4.1% (down from 4.2%). Dropped "Oct '25".
Next: ROLL FORWARD when Nov jobs released ~Dec 5 (drop "Nov", add "Nov")

### treasury (12 months — ROLLED FORWARD this run)
months: ["Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"]
values: [4.35,4.38,4.40,4.42,4.46,4.45,4.37,4.74,4.73,5.11,4.94,4.86]
Note: Rolled forward Nov 6; Nov = 4.86% (Nov 6 close). Dropped "Nov '25"/4.30.
Next: ROLL FORWARD when Dec data arrives (drop "Dec", add "Dec" at new value)

### retail (12 months — unchanged this run)
months: ["Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
values: [4.2,4.5,4.3,4.2,4.2,4.2,4.9,6.9,6.7,5.0,6.0,6.3]
Note: ROLL FORWARD when Oct retail sales released Nov 17 (drop "Nov", add "Nov" at new value)

### m2 (12 months — unchanged this run)
months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [4.2,4.3,4.4,4.5,4.6,4.6,4.7,5.6,5.5,5.4,5.7,5.7]
Note: ROLL FORWARD when Oct H.6 released ~late November (drop "Oct '25", add "Oct")

### core-pce (12 months — unchanged this run)
months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [2.8, 2.9, 3.0, 3.1, 3.1, 3.2, 3.3, 3.4, 3.3, 3.0, 3.0, 3.1]
Note: ROLL FORWARD when Oct Core PCE released Nov 25 (drop "Oct '25", add "Oct")

### ism-pmi (12 months — ROLLED FORWARD this run)
months: ["Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
values: [48.2, 47.9, 52.6, 52.4, 52.7, 52.7, 54.0, 53.3, 55.6, 54.6, 54.5, 55.5]
Note: Rolled forward Nov 3; Oct ISM = 55.5 (10th consecutive expansion). Dropped "Oct '25"/48.7.
Next: ROLL FORWARD when Nov ISM Manufacturing released Dec 1 (drop "Nov", add "Nov")

### jobless-claims (12 months — UPDATED IN-PLACE this run)
months: ["Nov '25","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
values: [220, 218, 213, 216, 211, 202, 215, 222, 203, 207, 200, 195]
Note: Updated "Oct" from 197 → 195 (week ending Nov 1, DOL released Nov 6; 189K weekly / 195K 4-wk avg).
Next: ROLL FORWARD when Nov data arrives (drop "Nov '25", add "Nov")

### gdp (8 quarters — unchanged this run)
months: ["Q4 '24","Q1 '25","Q2 '25","Q3 '25","Q4 '25","Q1 '26","Q2 '26","Q3 '26"]
values: [2.3,-0.3,2.8,1.9,0.5,2.1,2.2,3.4]
Note: UPDATE IN-PLACE Q3 '26 if second estimate revises (due late November); ROLL FORWARD when Q4 '26 advance arrives (~Jan 29, 2027)

---

## What to Watch (Next 4 Events)

1. **Nov 12 (Wed)** — CPI, October 2026 (BLS) — ROLL FORWARD cpi sparkline; LAST inflation data before December 9
2. **Nov 17 (Mon)** — Retail Sales, October 2026 (Census) — ROLL FORWARD retail sparkline
3. **Nov 25 (Tue)** — Core PCE, October 2026 (BEA) — ROLL FORWARD core-pce sparkline; arrives AFTER Dec 9 decision
4. **Dec 9 (Wed)** — FOMC Decision — if hike: ROLL FORWARD fed-rate sparkline (drop "Oct", add "Dec" at 4.13%)

---

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App.

## Reliable data sources
- Fed Funds Rate: WebSearch → stocktitan.net, cnbc.com
- CPI / Core CPI / Shelter / Energy: WebSearch → cnbc.com, wsj.com
- Core PCE: WebSearch → bea.gov snippets, cnbc.com, stocktitan.net
- ISM PMI: WebSearch → prnewswire.com, textileworld.com, industrytoday.com
- Jobless Claims: WebSearch → bloomberg.com/news, fxstreet.com
- Unemployment: WebSearch → roberthalf.com, cnbc.com
- GDP: WebSearch → indexbox.io, bondstats.org, advisorperspectives.com
- 10-yr Treasury / Yield Curve: WebSearch → fminvest.com (Treasury curve daily), seekingalpha.com, etftrends.com
- Retail Sales: WebSearch → census.gov snippets, qz.com, etftrends.com
- M2: WebSearch → FRED snippets, tradingeconomics.com, fxmacrodata.com
- FOMC odds: WebSearch "CME FedWatch [meeting date] probability" → CNBC, phemex.com
- Mortgage rate: WebSearch "Freddie Mac PMMS" → globenewswire.com

## Run Log — November 8, 2026
- Fed Rate: 3.88% midpoint — FOMC HELD 10-2 (Oct 28–29); no new data
- CPI: 3.7% / Core CPI: 3.1% / Shelter: 4.2% — unchanged (Oct CPI due Nov 12)
- Core PCE: 3.1% — unchanged (Oct Core PCE due Nov 25)
- ISM Manufacturing PMI: **55.5** (ROLLED FORWARD — ISM Nov 3; Oct print = 55.5; Prices Paid 75.2)
- Unemployment: **4.1%** (ROLLED FORWARD — BLS Nov 6; Oct payrolls +165K, Sep revised +45K)
- GDP: +3.4% advance — unchanged (second estimate due late Nov)
- 10-yr Treasury: **4.86%** (ROLLED FORWARD — Nov 6 close; was 4.94%)
- Jobless Claims: 189K weekly / **195K 4-wk avg** (UPDATED IN-PLACE — DOL Nov 6; was 197K)
- Retail Sales: +6.3% YoY — unchanged (Oct retail due Nov 17)
- M2: 5.7% — unchanged (Oct H.6 due late November)
- 30-yr Mortgage: 7.18% (Freddie Mac PMMS, Nov 6)
- FOMC odds: CUT 0% / HOLD 21% / HIKE 79% — December 9 at ~79% hike
- Sentiment: 52/100 NEUTRAL (up from 48 — jobs +165K, unemployment 4.1%, ISM 55.5)
- Sparklines rolled: unemployment (Oct 4.1% added), ism-pmi (Oct 55.5 added), treasury (Nov 4.86% added)
- Sparklines updated in-place: jobless-claims (197→195)
- Unchanged: cpi, retail, fed-rate, m2, core-pce, gdp
