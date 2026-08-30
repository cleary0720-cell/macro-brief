# Article Agent Memory

## Topics covered (do not repeat any of these)
1. Oil Prices / Energy Markets — "The Price of Energy: Inside the Oil Market Forces Threatening to Reignite Inflation" (2025-04-oil-prices.html) — Energy & Commodities
2. Consumer Spending / Debt — "The Debt-Fueled Consumer: America's Spending Resilience Is Running on Borrowed Time" (2026-05-consumer-spending.html) — Consumer Economy
3. Federal Debt / Interest Crisis — "The $1 Trillion Bill: America's Debt Interest Crisis Is Reshaping the Federal Budget" (2026-05-debt-interest-crisis.html) — Fiscal Policy
4. Housing Lock-in / Mortgage Rates — "The Locked Market: How the Mortgage Rate Trap Is Starving America's Housing Supply" (2026-05-housing-lock-in.html) — Housing Market
5. Inflation Relapse / April CPI Surge — "Inflation Relapse: The April Price Surge That Rewrites the Fed's 2026 Playbook" (2026-05-inflation-relapse.html) — Inflation
6. Labor Market Cooling — "The Soft Stall: America's Labor Market Is Cooling Without Breaking" (2026-05-labor-market-cooling.html) — Labor Markets
7. Money Supply / M2 — "Too Much Money: Why the Fed's M2 Surge Is Making the Inflation Fight Harder Than It Looks" (2026-05-money-supply.html) — Money Supply
8. Tariffs / Trade Deficit — "The Tariff Dividend: How America's Trade Gap Has Narrowed — and What It's Actually Costing" (2026-05-tariff-trade-deficit.html) — Trade Policy
9. AI Data Center Boom / Tech Economy — "The AI Crutch: How a Trillion-Dollar Data-Center Boom Became the Load-Bearing Wall of the US Economy" (2026-06-ai-data-center-boom.html) — Technology Economy
10. FOMC Dot Plot / Fed Rate Path — "Higher for Longer, Confirmed: The Fed's Dot Plot and the End of the 2026 Rate-Cut Window" (2026-06-fomc-dot-plot.html) — Monetary Policy
11. Fixed Income / Bond Market Repricing — "The Yield Reckoning: How a Hawkish Fed Is Rewriting the Rules of the Bond Market" (2026-06-fixed-income-repricing.html) — Fixed Income
12. Banking / Commercial Real Estate CRE Stress — "The $936 Billion Wall: How America's Commercial Real Estate Debt Crisis Is Rewriting Regional Banking" (2026-06-banking-cre-stress.html) — Banking
13. Stagflation / June 2026 Jobs Shock — "The Stagflation Signal: Why America's Jobs Collapse Is an Inflation Problem, Not Just a Growth One" (2026-07-stagflation-warning.html) — Economic Output
14. Equity Risk Premium / Stock Market Valuations — "The Vanishing Premium: America's Stock Market Is No Longer Rewarding Investors for Taking Risk" (2026-07-equity-risk-premium.html) — Financial Markets
15. June 2026 CPI Disinflation / Rate Pivot Case — "The Price Reversal: Inside June's Historic CPI Drop and the Question It Left Unanswered" (2026-07-cpi-june-disinflation.html) — Inflation
16. Iran Strait of Hormuz Oil Shock / Fed Rate Hike Repricing — "The Hormuz Premium: Iran's Oil Shock and the Rate Hike the Market Wasn't Expecting" (2026-07-hormuz-oil-fed.html) — Energy & Commodities
17. FOMC 9-3 Dissent / September Rate Hike Setup — "Three Against: The Fed's Historic 9-3 Dissent and What It Means for September" (2026-08-fed-dissent-september.html) — Monetary Policy
18. July 2026 Payroll Contraction / ISM Manufacturing Paradox — "Red Flag: America's First Payroll Loss in Years Forces the Fed Into an Impossible Corner" (2026-08-july-jobs-contraction.html) — Labor Markets
19. July 2026 Retail Sales Miss / Consumer Credit Stress — "Spending on Empty: July's Retail Slump Signals the Consumer Economy's First Real Crack" (2026-08-retail-sales-paradox.html) — Consumer Economy
20. China Near-Deflation / Global Growth Slowdown — "The China Discount: How Beijing's Near-Deflation Is Reshaping the Global Economy" (2026-08-china-global-slowdown.html) — Global Economy
21. Jackson Hole 2026 / Warsh Hawkish Keynote + Flat Core PCE — "The Warsh Doctrine: Jackson Hole Sets Up the Fed's Most Consequential September in a Decade" (2026-08-warsh-jackson-hole.html) — Monetary Policy

## Last run
- Date: August 30, 2026
- Article: "The Warsh Doctrine: Jackson Hole Sets Up the Fed's Most Consequential September in a Decade"
- Category: Monetary Policy (archive data-category="Policy")
- Issue: Vol. I, No. 21
- Filename: articles/2026-08-warsh-jackson-hole.html
- Thumbnail: fallback cp 2026-05-debt-interest-crisis-thumb.jpg → 2026-08-warsh-jackson-hole-thumb.jpg (pexels-proxy consistently blocked in CCR)
- Push: git push origin HEAD:main — SUCCESS (commit 5466ee0)

## Push method (confirmed working)
git add [files] && git commit -m "message" && git push origin HEAD:main
Do NOT use mcp__github__create_or_update_file for pushing — it fails on large or binary files.

## Thumbnail
download_thumb.py consistently returns 403 (Tunnel connection failed) in CCR — use the cp fallback IMMEDIATELY (do not attempt pexels-proxy).
Fallback mapping:
- Monetary Policy / Banking / Fixed Income / Debt → 2026-05-debt-interest-crisis-thumb.jpg
- Inflation → 2026-05-inflation-relapse-thumb.jpg
- Trade Policy / Tariffs → 2026-05-tariff-trade-deficit-thumb.jpg
- Labor Markets → 2026-05-labor-market-cooling-thumb.jpg
- Consumer Economy / Retail → 2026-05-consumer-spending-thumb.jpg
- Housing Market → 2026-05-housing-lock-in-thumb.jpg
- Money Supply / Fiscal Policy → 2026-05-money-supply-thumb.jpg
- Energy / Commodities / Oil → oil-thumb.jpg
- Global Economy / Technology / Financial Markets → 2026-05-debt-interest-crisis-thumb.jpg (default)
- Any other category → 2026-05-debt-interest-crisis-thumb.jpg (default)

## Archive filter buckets (confirmed working)
The 4 fixed filter buckets in archive.html — do NOT add new ones:
  Monetary Policy / Fiscal Policy / Trade Policy → data-category="Policy"
  Labor Markets / Housing / Consumer / Economic Output / Global / Technology → data-category="Economy"
  Fixed Income / Money Supply / Financial Markets / Banking → data-category="Markets & Money"
  Inflation / Energy & Commodities → data-category="Prices"

## Issue numbering
Next article will be Vol. I, No. 22

## Key data verified August 30, 2026
- Fed Funds: 3.50-3.75%, HELD July 29 (9-3 vote); dissenters: Hammack, Kashkari, Logan (all wanted hike)
- Jackson Hole 2026 (Aug 28): Warsh hawkish keynote
  - Exact quote: "while this summer's readings were better than expected, they do not tell me that underlying trends have meaningfully improved"
  - Called 2% PCE a "firm, fixed target"
  - Called for "quieter Fed, more purposeful in its communications"
  - September FOMC odds post-speech: CUT 0% / HOLD 44% / HIKE 56%
  - 2Y Treasury surged 15 bps to 4.34% on speech day
- July Jobs (released Aug 7): -23,000 NFP; Unemployment 4.1%; participation 61.4%
- Jobless Claims (week ending Aug 22): 203k weekly; 4-week avg 205,500
- CPI July: 3.4% YoY; Core CPI July: 2.5%
- Core PCE July (released Aug 26): 3.3% YoY — FLAT for 2nd consecutive month; 0.2% MoM (in line)
  - Headline PCE July: 3.7% YoY (re-acceleration from energy base effects)
- GDP Q2 2026 advance: +1.5%; Q1 2026 final: +2.1%
- ISM PMI July: 55.6 (four-year high; 7th consecutive expansion) — August data due Sep 2
- Retail Sales July: +5.0% YoY; monthly -0.6%
- M2 July: 5.4% YoY
- Treasury yields (Aug 28): 2Y=4.34%, 10Y=4.73%, 30Y=5.20%
  - 2s10s: +39 bps (bear flattened from +55 bps post-Warsh)

## Upcoming releases (as of August 30, 2026)
- Sep 2 (Tue): ISM Manufacturing PMI August 2026 (prev: 55.6)
- Sep 5 (Fri): August Jobs Report (BLS) — MOST CONSEQUENTIAL PRINT OF 2026
  - A second payroll loss → near-certain September hold; rebound >100k → cements September hike
  - Consensus: ~+85,000 (modest recovery from July shock)
- Sep 10 (Wed): CPI August 2026 (BLS) — last inflation input before September FOMC
- Sep 12 (Fri): Retail Sales August 2026 (Census)
- Sep 16-17: FOMC September 2026 — 44% hold / 56% hike; dot-plot meeting
  - A hike would push target to 3.75-4.00% (highest since 2024)

## Topic suggestions for future runs (not yet covered)
- August Jobs Report reaction (Sep 5/6) — second payroll loss or strong rebound, major story
- September FOMC reaction (Sep 16/17) — rate decision and dot plot update
- Fiscal Policy — 2026 budget deficit trajectory post-"One Big Beautiful Bill" (still uncovered)
- Housing Market — update on affordability, starts/permits (last covered May 2026)
- Financial Markets — equity market reaction to September FOMC outcome
- Economic Output — GDP Q3 2026 preliminary estimate (due ~Oct)

## Data source strategy (confirmed August 2026)
Government sites return 403 on WebFetch — use WebSearch for all economic data.
- CNBC: cnbc.com — best source for most releases (CPI, PCE, jobs, retail sales, Fed speeches)
- Bloomberg: bloomberg.com — good for analysis and market reactions
- Fed/FOMC: cnbc.com, stocktitan.net
- Treasury yields: cnbc.com, tradingeconomics.com
- FOMC odds: WebSearch "CME FedWatch [meeting date] FOMC probability"
- Jackson Hole / Fed speeches: cnbc.com most timely; bloomberg.com for analysis
