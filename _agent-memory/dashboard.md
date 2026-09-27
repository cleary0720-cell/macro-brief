# Dashboard Agent Memory — The Macro Brief

## Last Run
- **Date:** September 27, 2026 (Sunday)
- **Edition:** Vol. I, No. 22

---

## Current Data (as of September 27, 2026)

| Indicator | Value | Direction | Source / Date |
|---|---|---|---|
| Fed Funds Rate | 3.75–4.00% (mid: 3.88%) | ↑ HIKED | FOMC Sep 16, 2026 (12-0 unanimous) |
| CPI (YoY) | 3.4% | → | BLS, released Sep 11 (August data) |
| Core CPI (YoY) | 2.4% | ↓ | BLS, released Sep 11 (August data) |
| Unemployment | 4.1% | ↑ | BLS, released Sep 5 (August data) |
| Payrolls | +162,000 | ↑ | BLS, released Sep 5 (August data) |
| GDP Q2 2026 | +1.5% annualized | ▼ | BEA final, released Aug 28 |
| 10-Year Treasury | 5.11% | ↑ | Sep 26, 2026 |
| Retail Sales (YoY) | +6.0% | ↑ | Census, released Sep 16 (August data) |
| M2 (YoY) | 5.7% | ↑ | Fed H.6, released Sep 22 (August data) |
| Core PCE (YoY) | 3.3% | → | BEA, released Aug 26 (July data); August delayed to Sep 30 |
| Headline PCE | 3.7% | ↑ | BEA, released Aug 26 (July data) |
| ISM PMI | 54.6 | ↓ | ISM, released Sep 2 (August data) |
| Jobless Claims (weekly) | 197,000 | ↓ | DOL, released Sep 25 (week ending Sep 19) |
| Jobless Claims (4-wk avg) | 202,250 (~202K) | ↓ | DOL, released Sep 25 |
| 30-yr Mortgage Rate | 7.03% | ↑ | Freddie Mac PMMS, Sep 24 (highest of 2026) |
| Macro Sentiment | 43 / 100 | CAUTIOUS | Dashboard calculation |

---

## Yield Curve — September 25–26, 2026

| Tenor | Yield |
|---|---|
| 1-Month | 4.04% |
| 3-Month | 4.19% |
| 6-Month | 4.33% |
| 1-Year | 4.49% |
| 2-Year | 4.85% |
| 5-Year | 4.99% |
| 7-Year | 5.05% |
| 10-Year | 5.11% |
| 20-Year | 5.45% |
| 30-Year | 5.40% |

- **Curve shape:** Normal (10Y > 2Y > 3M throughout)
- **Gradient color:** #1B5E20 (green)
- **2s10s spread:** +26 bps
- **3m10y spread:** +92 bps
- **Recession probability:** 13.9% (NY Fed yield curve model, data through August 2026)
- **SVG Y range:** 3.84% to 5.65%, span 1.81%, Y(v) = 30 + (5.65 - v) / 1.81 * 112
- **Grid lines:** 4.20% (y=119.7), 4.60% (y=95.0), 5.00% (y=70.2), 5.40% (y=45.5)

---

## FOMC Probability Bar

- **Next meeting:** October 27–28, 2026
- **Current rate:** 3.75–4.00%
- **HOLD:** 24% (flex: 24)
- **HIKE +25 bps:** 76% (flex: 76)
- **CUT:** hidden (flex: 0)
- **Drivers:** Vice Chair Barr Sep 23 comments; S&P Global Sep PMI input costs at 4-yr high

---

## Sparkline Arrays (as of Sep 27, 2026)

### fed-rate (12 months)
months: ["Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [3.83,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.88]

### cpi (12 months — no new data this run)
months: ["Sep '25","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug"]
values: [2.4,2.6,2.8,2.9,3.1,3.3,3.6,3.8,4.2,3.5,3.4,3.4]
Note: Last entry Aug = August CPI release; next release Sep CPI on Oct 14

### unemployment (12 months — no new data this run)
months: ["Sep '25","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug"]
values: [4.2,4.2,4.2,4.2,4.1,4.2,4.2,4.3,4.3,4.2,4.1,4.1]

### treasury (12 months — Sep updated in-place: 4.94 → 5.11)
months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [4.25,4.30,4.35,4.38,4.40,4.42,4.46,4.45,4.37,4.74,4.73,5.11]
Note: Sep = Sep 26 close of 5.11%; ROLL FORWARD next month when Oct data arrives

### retail (12 months — no new data this run)
months: ["Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [4.0,4.2,4.5,4.3,4.2,4.2,4.2,4.9,6.9,6.7,5.0,6.0]

### m2 (12 months — ROLLED FORWARD this run: Aug '25 dropped, "Aug" at 5.7% added)
months: ["Sep '25","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug"]
values: [4.2,4.2,4.3,4.4,4.5,4.6,4.6,4.7,5.6,5.5,5.4,5.7]
Note: H.6 released Sep 22; August M2 = 5.7% YoY, $23.3T total

### core-pce (12 months — no new data this run; August PCE delayed to Sep 30)
months: ["Aug '25","Sep","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul"]
values: [2.7, 2.7, 2.8, 2.9, 3.0, 3.1, 3.1, 3.2, 3.3, 3.4, 3.3, 3.3]
Note: ROLL FORWARD when Sep 30 BEA release arrives (drop "Aug '25", add "Aug" at new value)

### ism-pmi (12 months — no new data this run)
months: ["Sep '25","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug"]
values: [49.1, 48.7, 48.2, 47.9, 52.6, 52.4, 52.7, 52.7, 54.0, 53.3, 55.6, 54.6]
Note: ROLL FORWARD when Oct 1 ISM release arrives (drop "Sep '25", add "Sep" at new value)

### jobless-claims (12 months — Sep updated in-place: 203 → 202)
months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [225, 220, 218, 213, 216, 211, 202, 215, 222, 203, 207, 202]
Note: Sep value = 202K 4-wk avg (week ending Sep 19 release); weekly was 197K

### gdp (8 quarters — no new data this run)
months: ["Q3 '24","Q4 '24","Q1 '25","Q2 '25","Q3 '25","Q4 '25","Q1 '26","Q2 '26"]
values: [2.8,2.3,-0.3,2.8,1.9,0.5,2.1,1.5]
Note: ROLL FORWARD when Q3 2026 advance estimate arrives ~late October (drop Q3 '24, add Q3 '26)

---

## What to Watch (Next 4 Events)

1. **Sep 30** — Core PCE August 2026 (BEA) — MOST CRITICAL: delayed from Sep 26; 76% hike probability hinges on this
2. **Oct 01** — ISM Manufacturing PMI September 2026 — First post-hike factory read
3. **Oct 02** — Employment Situation September 2026 (BLS) — Labor market post-hike
4. **Oct 14** — CPI September 2026 (BLS) — Last major inflation read before Oct 28 FOMC

---

## Key Narratives This Week (Sep 27)

- **Core PCE delayed**: BEA moved the August release from Sep 26 to Sep 30 — markets in holding pattern
- **10Y surged to 5.11%** on Sep 26 (up 17 bps from Sep 18 post-FOMC close of 4.94%)
  - Driver: S&P Global Sep PMI (Sep 23) — input costs at highest since Oct 2022
  - Driver: Vice Chair Barr (Sep 23): "further policy adjustments are likely to be needed"
- **FOMC October 28 odds jumped from 57% → 76%** as of Sep 25 (CME FedWatch)
- **M2 August re-accelerated to 5.7%** (H.6 Sep 22) — up from 5.4% in July; $23.3T total
- **Jobless claims near 57-year lows**: 197K weekly (week ending Sep 19); 4-wk avg 202,250
- **Mortgage rates at 2026 high**: 7.03% (Freddie Mac PMMS Sep 24)
- **NY Fed recession probability**: 13.9% (data through August 2026)
- **Yield curve coordinates updated**: Y range 3.84%-5.65%, span 1.81%

---

## CPI Components (August 2026 — unchanged from Sep 20 run)
- Headline CPI: 3.4% (high class, easing trend)
- Core CPI: 2.4% (mod class, easing trend)
- Shelter: 3.0% (mod class, gradually easing)
- Energy: +16.3% (high class, re-accelerating)
Source: BLS, released Sep 11, 2026

---

## Next Run: October 4, 2026 (Sunday)
Expected new data released between Sep 27 and Oct 4:
- **Sep 30 (Tue)**: Core PCE August — THE most important release; will likely move FOMC odds dramatically
- **Oct 1 (Wed)**: ISM Manufacturing PMI September — ROLL FORWARD ism-pmi sparkline
- **Oct 2 (Thu, FRIDAY)**: Employment Situation September — ROLL FORWARD unemployment sparkline; potentially big labor revision

IMPORTANT: The Employment Situation is released on FRIDAY (per fact-checking rules). Oct 2 is a Thursday. Let me double-check — Oct 2, 2026. Sep 27 is Sunday, so Sep 28=Mon, Sep 29=Tue, Sep 30=Wed, Oct 1=Thu, Oct 2=**FRIDAY**. 
Yes, October 2, 2026 is a FRIDAY. ✓ That is correct per BLS rules (always released Friday).

IMPORTANT CORRECTIONS TO DASHBOARD FACTS:
- "Employment Situation September 2026 — Bureau of Labor Statistics · 8:30am ET" is on Oct 2 (FRIDAY) ✓ (already correct in the dashboard)
- Verify: The dashboard said "Oct 02" as the jobs report day — this is correct (Friday Oct 2, 2026)

## Run Log — September 27, 2026
- Fed Rate: 3.88% (midpoint 3.75-4.00%) — unchanged
- CPI: 3.4% / Core CPI: 2.4% / Shelter: 3.0% / Energy: +16.3% — unchanged
- Core PCE: 3.3% (July data; August delayed to Sep 30) — unchanged
- ISM PMI: 54.6 (August data) — unchanged until Oct 1
- Jobless Claims: 202K 4-wk avg (from 203K; 197K weekly week ending Sep 19)
- Unemployment: 4.1% (August) — unchanged
- GDP: +1.5% Q2 final — unchanged
- 10-yr Treasury: 5.11% (surged from 4.94%, Sep 26)
- Full yield curve: 1M=4.04%, 3M=4.19%, 6M=4.33%, 1Y=4.49%, 2Y=4.85%, 5Y=4.99%, 7Y=5.05%, 10Y=5.11%, 20Y=5.45%, 30Y=5.40%
- Retail Sales: +6.0% YoY (August) — unchanged
- M2: 5.7% (NEW — August H.6 released Sep 22, rolled sparkline forward)
- FOMC odds: CUT 0% / HOLD 24% / HIKE 76% — next meeting: Oct 27-28
- Mortgage rate: 7.03% (Freddie Mac PMMS Sep 24)
- Sentiment: 43/100 CAUTIOUS (down from 45)
- NY Fed recession probability: 13.9% (data through August 2026)
- Notes: No government data releases this week; market moved on private PMI data and Barr comments. PCE delayed to Sep 30. Big week ahead: PCE (Sep 30), ISM (Oct 1), Jobs (Oct 2).
