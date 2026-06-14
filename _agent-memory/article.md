# Article Agent Memory

## Topics covered (do not repeat any of these)
1. Oil Prices / Energy Markets — "The Price of Energy: Inside the Oil Market Forces Threatening to Reignite Inflation" (2025-04-oil-prices.html) — Energy & Commodities
2. Consumer Spending / Debt — "The Debt-Fueled Consumer: America's Spending Resilience Is Running on Borrowed Time" (2026-05-consumer-spending.html) — Consumer Economy
3. Federal Debt / Interest Crisis — "The $1 Trillion Bill: America's Debt Interest Crisis Is Reshaping the Federal Budget" (2026-05-debt-interest-crisis.html) — Fiscal Policy
4. Housing Lock-in / Mortgage Rates — "The Locked Market: How the Mortgage Rate Trap Is Starving America's Housing Supply" (2026-05-housing-lock-in.html) — Housing Market
5. Inflation Relapse / CPI Surge — "Inflation Relapse: The April Price Surge That Rewrites the Fed's 2026 Playbook" (2026-05-inflation-relapse.html) — Inflation
6. Labor Market Cooling — "The Soft Stall: America's Labor Market Is Cooling Without Breaking" (2026-05-labor-market-cooling.html) — Labor Markets
7. Money Supply / M2 — "Too Much Money: Why the Fed's M2 Surge Is Making the Inflation Fight Harder Than It Looks" (2026-05-money-supply.html) — Money Supply
8. Tariffs / Trade Deficit — "The Tariff Dividend: How America's Trade Gap Has Narrowed — and What It's Actually Costing" (2026-05-tariff-trade-deficit.html) — Trade Policy
9. AI Data Center Boom / Tech Economy — "The AI Crutch: How a Trillion-Dollar Data-Center Boom Became the Load-Bearing Wall of the US Economy" (2026-06-ai-data-center-boom.html) — Technology Economy
10. FOMC Dot Plot / Fed Rate Path — "Higher for Longer, Confirmed: The Fed's Dot Plot and the End of the 2026 Rate-Cut Window" (2026-06-fomc-dot-plot.html) — Monetary Policy

## Last run
- Date: June 14, 2026
- Article: "Higher for Longer, Confirmed: The Fed's Dot Plot and the End of the 2026 Rate-Cut Window"
- Category: Monetary Policy (filter bucket: Policy)
- Issue: Vol. I, No. 10
- Filename: articles/2026-06-fomc-dot-plot.html
- Thumbnail: fallback: cp 2026-05-debt-interest-crisis-thumb.jpg (pexels-proxy returned HTTP 403)
- Push: git push origin HEAD:main — SUCCESS (commit 5883545)

## Push method (confirmed working)
git add [files] && git commit -m "message" && git push origin HEAD:main
Do NOT use mcp__github__create_or_update_file for pushing — it fails on large or binary files.

## Thumbnail
download_thumb.py has leading whitespace on all lines causing IndentationError — do NOT call it directly.
Instead run the equivalent inline Python:
  python3 -c "import urllib.request, shutil, urllib.parse; ..."
Pexels proxy URL: pexels-proxy.cleary0720.workers.dev (NOT api.pexels.com — blocked)
June 2026 run: pexels-proxy returned HTTP 403 — use cp fallback every time until confirmed working.
Fallback mapping:
  Monetary Policy / Banking / Fixed Income / Debt → 2026-05-debt-interest-crisis-thumb.jpg
  Inflation → 2026-05-inflation-relapse-thumb.jpg
  Trade Policy / Tariffs → 2026-05-tariff-trade-deficit-thumb.jpg
  Labor Markets → 2026-05-labor-market-cooling-thumb.jpg
  Consumer Economy / Retail → 2026-05-consumer-spending-thumb.jpg
  Housing Market → 2026-05-housing-lock-in-thumb.jpg
  Money Supply / Fiscal Policy → 2026-05-money-supply-thumb.jpg
  Energy / Commodities / Oil → oil-thumb.jpg
  Technology Economy → 2026-06-ai-data-center-boom-thumb.jpg
  Any other category → 2026-05-debt-interest-crisis-thumb.jpg (default)

## Issue numbering
Next article will be Vol. I, No. 11

## Topic suggestions for future runs (not yet covered)
- Fixed Income / Bond market (yields, duration, credit spreads)
- Banking sector stress (regional bank exposure, CRE loans)
- Global Economy (China slowdown, EM capital flows, dollar strength)
- Fiscal Policy / Budget deficit trajectory (different angle from debt interest article)
- Financial Markets / Stock market valuations
- Technology Economy — different angle (semiconductors, chip supply chain)
