# Dashboard Agent Memory — The Macro Brief

## Last Run
- **Date:** September 20, 2026 (Saturday)
- **Edition:** Vol. I, No. 21

---

## Current Data (as of September 20, 2026)

| Indicator | Value | Direction | Source / Date |
|---|---|---|---|
| Fed Funds Rate | 3.75–4.00% (mid: 3.88%) | ↑ HIKED | FOMC Sep 16, 2026 |
| CPI (YoY) | 3.4% | → | BLS, released Aug 13 (July data) |
| Core CPI (YoY) | 2.4% | ↓ | BLS, released Aug 13 (July data) |
| Unemployment | 4.1% | ↑ | BLS, released Sep 5 (August data) |
| Payrolls | +162,000 | ↑ | BLS, released Sep 5 (August data) |
| GDP Q2 2026 | +1.5% annualized | ▼ | BEA final, released Aug 28 |
| 10-Year Treasury | 4.94% | ↓ | Sep 18, 2026 (post-FOMC close) |
| Retail Sales (YoY) | +6.0% | ↑ | Census, released Sep 17 (August data) |
| Retail Sales (MoM) | +1.2% | ↑ | Census, released Sep 17 (August data) |
| M2 (YoY) | 5.4% | ↓ | Fed H.6, released Aug 25 (July data) |
| Core PCE (YoY) | 3.3% | → | BEA, released Aug 26 (July data) |
| Headline PCE | 3.7% | ↑ | BEA, released Aug 26 (July data) |
| ISM PMI | 54.6 | ↓ | ISM, released Sep 2 (August data) |
| Jobless Claims (weekly) | 196,000 | ↓ | DOL, released Sep 18 (week ending Sep 13) |
| Jobless Claims (4-wk avg) | ~203,000 | ↓ | DOL, released Sep 18 |
| Macro Sentiment | 45 / 100 | CAUTIOUS | Dashboard calculation |

---

## Yield Curve — September 18, 2026 (Post-FOMC)

| Tenor | Yield |
|---|---|
| 1-Month | 3.88% |
| 3-Month | 4.14% |
| 6-Month | 4.30% |
| 1-Year | 4.45% |
| 2-Year | 4.74% |
| 5-Year | 4.86% |
| 7-Year | 4.89% |
| 10-Year | 4.94% |
| 20-Year | 5.39% |
| 30-Year | 5.35% |

- **Curve shape:** Normal (10Y > 2Y > 3M throughout)
- **Gradient color:** #1B5E20 (green)
- **2s10s spread:** +20 bps
- **3m10y spread:** +80 bps
- **Recession probability:** ~7%

---

## FOMC Probability Bar

- **Next meeting:** October 27–28, 2026
- **Current rate:** 3.75–4.00%
- **HOLD:** 43% (flex: 43)
- **HIKE +25 bps:** 57% (flex: 57)
- **CUT:** hidden (flex: 0)

---

## Sparkline Arrays (as of Sep 20, 2026)

### fed-rate (12 months)
months: ["Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [3.83,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.63,3.88]
Note: Oct '25 = 3.83% (midpoint 3.75-3.88%), Nov '25–Jul '26 = 3.63% (3.50-3.75%), Sep '26 = 3.88% (3.75-4.00%)

### cpi (12 months — no new data this run)
months: ["Sep '25","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug"]
values: [2.4,2.6,2.8,2.9,3.1,3.3,3.6,3.8,4.2,3.5,3.4,3.4]
Note: Last entry Aug = July CPI release; next release ~Oct 10

### unemployment (12 months — no new data this run)
months: ["Sep '25","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug"]
values: [4.2,4.2,4.2,4.2,4.1,4.2,4.2,4.3,4.3,4.2,4.1,4.1]

### treasury (12 months — Sep updated in-place)
months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [4.25,4.30,4.35,4.38,4.40,4.42,4.46,4.45,4.37,4.74,4.73,4.94]

### retail (12 months — ROLLED FORWARD 1 month, Sep release added)
months: ["Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [4.0,4.2,4.5,4.3,4.2,4.2,4.2,4.9,6.9,6.7,5.0,6.0]
Note: "Sep" label = release month for August data

### m2 (12 months — no new data this run)
months: ["Aug '25","Sep","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul"]
values: [4.1,4.2,4.2,4.3,4.4,4.5,4.6,4.6,4.7,5.6,5.5,5.4]

### core-pce (12 months — no new data this run)
months: ["Aug '25","Sep","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul"]
values: [2.7, 2.7, 2.8, 2.9, 3.0, 3.1, 3.1, 3.2, 3.3, 3.4, 3.3, 3.3]

### ism-pmi (12 months — no new data this run)
months: ["Sep '25","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug"]
values: [49.1, 48.7, 48.2, 47.9, 52.6, 52.4, 52.7, 52.7, 54.0, 53.3, 55.6, 54.6]

### jobless-claims (12 months — Sep updated in-place: 206→203)
months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
values: [225, 220, 218, 213, 216, 211, 202, 215, 222, 203, 207, 203]
Note: Sep value = ~203K (4-wk avg post Sep 18 release; weekly 196K = 3-month low)

### gdp (8 quarters — no new data this run)
months: ["Q1 '25","Q2","Q3","Q4","Q1 '26","Q2","Q3E","Q4E"]
values: [2.1, 2.4, 2.3, 1.7, 1.9, 1.5, null, null]

---

## What to Watch (Next 4 Events)

1. **Sep 26** — Core PCE August 2026 (BEA) — Most critical: go/no-go for Oct 28 hike
2. **Oct 01** — ISM Manufacturing PMI September 2026 — First post-hike factory read
3. **Oct 02** — Employment Situation September 2026 (BLS) — Labor market post-hike
4. **Oct 28** — FOMC Rate Decision October 2026 — 57% probability of second hike

---

## Key Narratives This Week

- **Fed hiked 25 bps Sep 16 unanimously (12-0)** to 3.75–4.00%; first hike in ~3 years
- **Chair Warsh** (not Powell) led the decision
- **Dot plot raised** 2026 median to 4.10%; 16/18 participants see more hikes
- **August retail sales +6.0% YoY** eliminated the last argument for a pause
- **Jobless claims 196K** (3-month low) signals labor resilience post-hike
- **10Y settled at 4.94%** after briefly touching 5.00-5.02% on hike day ("buy the news")
- **Core PCE Sep 26** is the decisive data point for October 28

---

## Next Run: September 27, 2026
Expected new data: Core PCE August (Sep 26), GDP Q2 final if not already captured
