# Dashboard Agent Memory — Last Run

**Run date:** 2026-09-13  
**Edition:** Vol. I, No. 20  
**Headline:** Three Days to Decision: August CPI Holds at 3.4%, Core Eases to 2.4%, Energy Surges — FOMC Hike Odds Hit 85%

---

## Economic Data (as of run date)

### CPI — August 2026 (BLS, released Sep 11, 2026)
- Headline CPI YoY: **3.4%** (unchanged from July)
- Core CPI YoY: **2.4%** (down from 2.5%; lowest since March 2021)
- Shelter CPI: **3.0%** (down from 3.2%)
- Energy CPI: **+16.3%** YoY (up from +14.7%; gasoline +27.4% YoY)
- Food: ~2.5% (stable)

### Fed / FOMC
- Current fed funds rate: 5.25–5.50% (held since prior hike cycle)
- FOMC meeting: **September 16–17, 2026** (3 days from run date)
- CME FedWatch hike probability: **85.5%** (25 bps hike)
- Hold probability: **15%** (flex bar: hold=15, hike=85)

### Treasury Yields — September 11, 2026
- 1M: 3.81%
- 3M: 4.01%
- 6M: 4.17% (interpolated)
- 1Y: 4.32%
- 2Y: 4.63%
- 5Y: 4.79%
- 7Y: 4.86% (interpolated)
- 10Y: **4.96%** (up from 4.78% prior week; +18 bps post-CPI)
- 20Y: 5.26%
- 30Y: 5.36%
- 2s10s spread: **+33 bps** (compressed from +41 bps; bear flattening)
- 3m10y spread: **+95 bps**
- Yield curve shape: **Normal** (badge: ▲ Normal, color: #1B5E20 green)
- Recession probability model: **~8-10%**

### Labor Market
- Jobless Claims (week ending Sep 6): **206,000** (4-wk avg 206k)
- Unemployment rate: ~4.2% (last reported; unchanged)

### GDP
- Most recent: Q2 2026 advance estimate (prior run; no new release this week)

### Retail Sales
- August 2026 retail sales: **NOT YET RELEASED** (rescheduled to Sep 16, 2026)

### Core PCE
- Most recent: July 2026 (prior run data; August due Sep 26)

### M2
- No new data this week

### ISM PMI
- No new data this week

---

## Macro Sentiment Score
- **47 / 100** (needle left: 47%)
- Prior: 48/100

---

## Inflation Breakdown (August 2026)
| Component | Value | Class | Trend |
|-----------|-------|-------|-------|
| Core CPI | 2.4% | mod | Easing |
| Shelter | 3.0% | mod | Gradually Easing |
| Energy | +16.3% | high | Re-Accelerating ↑ |
| Food | ~2.5% | ok | Stable |

---

## SVG Yield Curve Parameters
- Y-axis range: 3.61% (min) to 5.56% (max), span 1.95%
- Formula: `y = 30 + (5.56 - yield) / 1.95 * 112`
- Grid lines: 4.00% (y≈119.5), 4.39% (y≈97.2), 4.78% (y≈74.8), 5.17% (y≈52.4)
- Gradient/line color: #1B5E20 (green = normal curve)

---

## Sparkline Arrays (current state)

### CPI (monthly, 12 entries, rolled forward this run)
- months: ["Sep '25","Oct","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug"]
- values: [2.4,2.6,2.8,2.9,3.1,3.3,3.6,3.8,4.2,3.5,3.4,3.4]
- Last entry: Aug 2026 = 3.4%
- Next roll: when Sep 2026 CPI releases (~Oct 2026)

### 10Y Treasury (monthly, 12 entries, in-place updated Sep entry)
- months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
- values: [4.25,4.30,4.35,4.38,4.40,4.42,4.46,4.45,4.37,4.74,4.73,4.96]
- Last entry: Sep 2026 = 4.96%
- Next: roll forward when Oct month begins

### Jobless Claims (monthly, 12 entries, rolled forward this run)
- months: ["Oct '25","Nov","Dec","Jan '26","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep"]
- values: [225,220,218,213,216,211,202,215,222,203,207,206]
- Last entry: Sep 2026 = 206k
- Next roll: when Oct 2026 data releases

### Fed Rate, Unemployment, GDP, Retail Sales, M2, Core PCE, ISM PMI
- UNCHANGED this run

---

## What to Watch (next events)
1. **Sep 16** — Retail Sales August (Census, 8:30am ET)
2. **Sep 16–17** — FOMC September Decision (85% hike probability; dot-plot meeting; Decision 2pm ET Sep 17)
3. **Sep 26** — Core PCE August (BEA; first post-FOMC inflation read)
4. **Oct 2** — September Jobs Report (BLS; first post-FOMC labor read)

---

## Git State
- Commit: 99e5bc3
- Branch: main
- Files pushed: index.html, archive.html, about.html, sitemap.xml
- Sitemap articles: 22
