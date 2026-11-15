# Dashboard Agent Memory — The Macro Brief

## Last Run
- **Date:** November 15, 2026 (Sunday)
- **Edition:** Vol. I, No. 30

---

## Current Data (as of November 15, 2026)

| Indicator | Value | Direction | Source / Date |
|---|---|---|---|
| Fed Funds Rate | 3.75–4.00% (mid: 3.88%) | → HOLD 10-2 | FOMC Oct 28–29, 2026; dissents: Cook & Hammack (hike) |
| CPI (YoY) | **NO DATA** (last confirmed: 3.7% Sept) | — | BLS Oct 10 report: +0.4% MoM only; no YoY due to Oct 2025 data gap |
| CPI (MoM) | +0.4% Oct | ↑ | BLS, released Nov 10 (October data); no YoY due to Oct 2025 lapse |
| Core CPI (YoY) | 3.1% (last confirmed Sept) | ↑ | BLS, released Oct 14 (September data); no Oct YoY available |
| Shelter (YoY) | 4.2% (last confirmed Sept) | ↑ | BLS, released Oct 14 (September data) |
| Energy (YoY) | +20.4% (last confirmed Sept) | ↑ | BLS, released Oct 14 (September data) |
| Unemployment | 4.1% | ↓ | BLS, released Nov 6 (October data) |
| Payrolls | +165,000 | ↑ | BLS, released Nov 6 (October data); Sep revised +29K→+45K |
| GDP Q3 2026 | +3.4% annualized | ↑ ADVANCE | BEA, released Oct 30; second estimate due Nov 25 |
| GDP Q2 2026 | +2.2% annualized (final) | ↑ revised | BEA, revised Oct 30 |
| 10-Year Treasury | **5.15%** | ↑ SURGE | Nov 13, 2026 (post-CPI surge +29 bps from 4.86%) |
| Retail Sales (YoY) | +6.3% | ↑ | Census, released Oct 15 (September data); Oct due Nov 17 |
| M2 (YoY) | 5.7% | → | Fed H.6, released Oct 27 (September data); Oct due ~Nov 24–25 |
| Core PCE (YoY) | 3.1% | ↑ | BEA, released Oct 30 (September data); Oct due Nov 25 (BEFORE Dec 9) |
| ISM Manufacturing PMI | 55.5 | ↑ | ISM, released Nov 3 (October data); Prices Paid 75.2 |
| Jobless Claims (weekly) | 200,000 | — | DOL, released Nov 12 (week ending Nov 7); ninth week ≤200K |
| Jobless Claims (4-wk avg) | 195,000 | → | DOL, released Nov 12 (Nov 7 4-wk avg) |
| 30-yr Mortgage Rate | **7.11%** | ↓ | Freddie Mac PMMS, Nov 13 |
| Macro Sentiment | 50 / 100 | NEUTRAL | Dashboard calculation |

---

## CRITICAL NOTE — October CPI Data Gap
The BLS did not collect October 2025 CPI data during the federal appropriations lapse. As a result, the October 2026 CPI report (released November 10) contains monthly data (+0.4% MoM) but **no year-over-year figure**. The CPI sparkline was NOT rolled forward — it still shows September as the latest YoY data point (3.7%). Dashboard card shows "OCT: +0.4% MOM (NO YOY DATA AVAIL.)". Last confirmed YoY = September 3.7%.

---

## Yield Curve — November 13, 2026

| Tenor | Yield |
|---|---|
| 1-Month | 4.10% |
| 3-Month | 4.32% |
| 6-Month | 4.42% |
| 1-Year | 4.65% |
| 2-Year | 4.88% |
| 5-Year | 4.98% |
| 7-Year | 5.05% |
| 10-Year | 5.15% |
| 20-Year | 5.52% |
| 30-Year | 5.47% |

- **Curve shape:** Normal overall (mild kink: 20Y 5.52% > 30Y 5.47%, but short end well below long end)
- **Gradient color:** #1B5E20 (green)
- **Badge:** ▲ Normal
- **2s10s spread:** +27 bps
- **3m10y spread:** +83 bps
- **SVG Y range:** 3.90% to 5.72%, span 1.82%, Y(v) = 30 + (5.72 - v) / 1.82 * 112
- **Polygon baseline:** y=142
- **Grid lines at:** 4.20% (y=123.5), 4.60% (y=98.9), 5.00% (y=74.3), 5.40% (y=49.7)
- **SVG polyline coords:**
  - 1M(4.10%): (46.0, 129.6), 3M(4.32%): (96.7, 116.2), 6M(4.42%): (147.3, 109.9)
  - 1Y(4.65%): (198.0, 95.8), 2Y(4.88%): (248.7, 81.6), 5Y(4.98%): (299.3, 75.5)
  - 7Y(5.05%): (350.0, 71.2), 10Y(5.15%): (400.7, 65.0), 20Y(5.52%): (451.3, 42.3)
  - 30Y(5.47%): (502.0, 45.4)

---

## FOMC Probability Bar

- **Next meeting:** December 9, 2026
- **Current rate:** 3.75–4.00% (held Oct 28–29, 10-2; Cook & Hammack dissented for hike)
- **HIKE +25 bps:** ~90% of hike contracts
- **HIKE +50 bps:** ~10% of hike contracts
- **HIKE total:** 100% (flex: 100)
- **HOLD:** 0% (flex: 0)
- **CUT -25 bps:** 0% (flex: 0)
- **Source:** CME FedWatch snapshot November 13, 2026 (post Oct CPI release)
- **Context:** Oct CPI +0.4% MoM (hot, no YoY), 10Y at 5.15%, nine weeks ≤200K claims → Dec 9 at ~100% hike

---

## Sparkline Arrays (as of November 15, 2026)

### fed-rate (12 months — unchanged this run; FOMC held)
months: ["Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [3.83,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.88]
Note: ROLL FORWARD when December 9 FOMC acts (drop "Oct", add "Dec" at new mid-rate; if +25 bps → 4.13%)

### cpi (12 months — UNCHANGED this run — NO YoY for October due to data gap)
months: ["Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [2.6,2.8,2.9,3.1,3.3,3.6,3.8,4.2,3.5,3.4,3.4,3.7]
Note: NOT rolled forward — Oct 2026 CPI has no YoY figure. ROLL FORWARD when Nov CPI released ~Dec 10 (drop "Oct", add "Nov" at new YoY value — Nov YoY will be calculable once Nov 2025 base is available)

### unemployment (12 months — unchanged this run)
months: ["Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
values: [4.2,4.2,4.1,4.2,4.2,4.3,4.3,4.2,4.1,4.1,4.2,4.1]
Note: Next: ROLL FORWARD when Nov jobs released ~Dec 5 (drop "Nov", add "Nov")

### treasury (12 months — UPDATED IN-PLACE this run)
months: ["Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"]
values: [4.35,4.38,4.40,4.42,4.46,4.45,4.37,4.74,4.73,5.11,4.94,5.15]
Note: Updated "Nov" in-place from 4.86 → 5.15 (Nov 13 close after CPI shock). Still same calendar month.
Next: ROLL FORWARD when Dec data arrives (drop "Dec", add "Dec" at new value)

### retail (12 months — unchanged this run)
months: ["Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
values: [4.2,4.5,4.3,4.2,4.2,4.2,4.9,6.9,6.7,5.0,6.0,6.3]
Note: ROLL FORWARD when Oct retail sales released Nov 17 (drop "Nov", add "Nov" at new value)

### m2 (12 months — unchanged this run)
months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [4.2,4.3,4.4,4.5,4.6,4.6,4.7,5.6,5.5,5.4,5.7,5.7]
Note: ROLL FORWARD when Oct H.6 released ~Nov 24–25 (drop "Oct '25", add "Oct")

### core-pce (12 months — unchanged this run)
months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [2.8, 2.9, 3.0, 3.1, 3.1, 3.2, 3.3, 3.4, 3.3, 3.0, 3.0, 3.1]
Note: ROLL FORWARD when Oct Core PCE released Nov 25 (drop "Oct '25", add "Oct") — arrives BEFORE Dec 9

### ism-pmi (12 months — unchanged this run)
months: ["Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
values: [48.2, 47.9, 52.6, 52.4, 52.7, 52.7, 54.0, 53.3, 55.6, 54.6, 54.5, 55.5]
Note: Next: ROLL FORWARD when Nov ISM Manufacturing released Dec 1 (drop "Nov", add "Nov")

### jobless-claims (12 months — ROLLED FORWARD this run)
months: ["Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"]
values: [218, 213, 216, 211, 202, 215, 222, 203, 207, 200, 195, 195]
Note: Rolled forward Nov 12; Nov = 195K 4-wk avg (200K weekly for week ending Nov 7). Dropped "Nov '25"/220.
Next: ROLL FORWARD when Dec data arrives (drop "Dec", add "Dec" at new value)

### gdp (8 quarters — unchanged this run)
months: ["Q4 '24","Q1 '25","Q2 '25","Q3 '25","Q4 '25","Q1 '26","Q2 '26","Q3 '26"]
values: [2.3,-0.3,2.8,1.9,0.5,2.1,2.2,3.4]
Note: UPDATE IN-PLACE Q3 '26 if second estimate revises (due Nov 25); ROLL FORWARD when Q4 '26 advance arrives (~Jan 29, 2027)

---

## What to Watch (Next 4 Events)

1. **Nov 17 (Mon)** — Retail Sales, October 2026 (Census) — ROLL FORWARD retail sparkline
2. **Nov 25 (Tue)** — Core PCE + GDP 2nd estimate + M2 H.6 (BEA/Fed) — ROLL FORWARD core-pce, m2; UPDATE IN-PLACE gdp if revised; Oct Core PCE arrives BEFORE Dec 9
3. **Dec 1 (Mon)** — ISM Manufacturing PMI, November 2026 — ROLL FORWARD ism-pmi sparkline
4. **Dec 9 (Wed)** — FOMC Decision — if hike: ROLL FORWARD fed-rate sparkline (drop "Oct", add "Dec" at 4.13% if +25bps)

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

## Run Log — November 15, 2026
- Fed Rate: 3.88% midpoint — FOMC HELD 10-2 (Oct 28–29); no new data
- CPI: **Oct MoM +0.4% / NO YoY** (BLS Nov 10; Oct 2025 data gap — CPI sparkline NOT rolled forward)
- Core CPI: 3.1% last confirmed Sept — no Oct YoY; dashboard shows data gap explanation
- Core PCE: 3.1% — unchanged (Oct Core PCE due Nov 25, arrives BEFORE Dec 9 — CORRECTED from prior run error)
- ISM Manufacturing PMI: 55.5 — unchanged
- Unemployment: 4.1% — unchanged
- GDP: +3.4% advance — unchanged (second estimate due Nov 25)
- 10-yr Treasury: **5.15%** (UPDATED IN-PLACE — Nov 13 surge from 4.86%; +29 bps on CPI shock)
- Jobless Claims: 200K weekly / **195K 4-wk avg** (ROLLED FORWARD — DOL Nov 12; ninth week ≤200K; dropped Nov '25/220)
- Retail Sales: +6.3% YoY — unchanged (Oct retail due Nov 17)
- M2: 5.7% — unchanged (Oct H.6 due ~Nov 24–25)
- 30-yr Mortgage: **7.11%** (Freddie Mac PMMS, Nov 13; eased from 7.18%)
- FOMC odds: CUT 0% / HOLD 0% / HIKE 100% — December 9 at ~100% hike (90% +25bps / 10% +50bps)
- Sentiment: **50/100 NEUTRAL** (down from 52 — data gap uncertainty, 10Y surge to 5.15%, affordability pressure)
- Sparklines updated in-place: treasury (4.86→5.15)
- Sparklines rolled forward: jobless-claims (Nov '25/220 dropped; Nov/195 added)
- Unchanged: cpi (no YoY roll), retail, fed-rate, m2, core-pce, gdp, unemployment, ism-pmi
