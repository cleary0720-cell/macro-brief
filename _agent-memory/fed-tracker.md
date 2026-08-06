# Fed Tracker Agent Memory
Last updated: August 6, 2026

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.

## Reliable data sources
- Fed Funds Rate & FOMC decisions: federalreserve.gov press release pages (e.g. monetary20260617a.htm); CNBC, NPR, Fox Business cover decisions same day
- Effective rate: EFFR via NY Fed / FRED — search "effective federal funds rate EFFR [date]"; search snippets from federalreserve.gov H.15 / newyorkfed.org; sofrrate.com/policy-rates
- Market probabilities: CME FedWatch (search for snippets via WebSearch); Polymarket for binary year-end/meeting odds; blockchain.news for Polymarket summary articles
- Vote breakdown: federalreserve.gov FOMC statement pages; search "FOMC [date] vote statement"
- Dot plot / SEP: Seeking Alpha, TradingKey, CNBC post-decision summaries carry dot plot details
- Post-decision analysis: sherwood.news, coinpedia.org, forexfactory.com, interactivecrypto.com
- FOMC minutes content: goldsilver.com, tradingview.com/news, thestreet.com, cnbc.com, interactivecrypto.com, ig.com/uk — all covered July 8 release well
- ISM PMI: prnewswire.com carries official ISM press releases; babypips.com, investinglive.com, forexfactory.com, neilsethi.substack.com good sources
- ISM Services (July 2026): ismworld.org, prnewswire.com, investinglive.com, forexfactory.com all had results within hours of release

## Known issues
- Most aggregator sites that display CME FedWatch data (centralbank.watch, rateprobability.com, atlantafed.org, growbeansprout.com, morningstar.com, interactivecrypto.com, sofrrate.com) return HTTP 403 on WebFetch. Use WebSearch and read snippets.
- Yahoo Finance, CBS News, CNBC article pages also return 403 on WebFetch — use WebSearch to pull snippets.
- tradingeconomics.com also returns 403 on WebFetch.
- fxstreet.com analysis pages return 403 (including AMP versions).
- kucoin.com also returns 403 on WebFetch.
- EFFR data: NY Fed releases prior business day's data at approximately 9:00am ET. Weekends and federal holidays = no publication.
- Polymarket and CME FedWatch can diverge significantly — note both when available.
- Warsh withheld his dot at June meeting; 18 dots submitted going forward (not 19). May change at future meetings.
- sofrrate.com page title may show weekly average EFFR (3.62%) rather than daily EFFR (3.63%) — prefer ycharts/NY Fed for daily figure.
- WebSearch snippets about Polymarket may mix current odds with older quotes; cross-check against CME FedWatch for consistency.
- IMPORTANT: CME FedWatch shows ~57% hike (move to 3.75-4.00%) as of Aug 6. Always interpret CME's "3.75-4.00%" outcome as a HIKE from the current 3.50-3.75% range. Do NOT label this as a "cut."
- Dashboard agent site.md has repeatedly mislabeled CME hike probability as "cut" — always verify directional interpretation against memory notes.
- Polymarket odds can shift significantly over short periods in response to macro data.
- blockchain.news/news articles often carry up-to-date Polymarket snapshots for Fed meetings — useful search source.
- CORRECTION: Q2 2026 GDP advance estimate is due July 30, 2026 (confirmed via bea.gov) — NOT June 30.
- WebSearch can be intermittently unavailable (July 6, 2026 run: most searches failed). If searches keep failing, retry with broader queries or different phrasings. Try at least 4-6 searches with different queries before giving up.
- On Sundays: CME FedWatch won't have new data beyond Friday's close. EFFR for Friday won't be published until Monday morning. Polymarket is 24/7 and may shift slightly.
- FOMC minutes preview articles (published before 2pm ET same day) will show "expected" content based on the already-known dot plot — actual new debate details only in post-release analysis.
- Blockchain.news article titles with Polymarket odds can be from any day — cross-check dates in context before using.
- EFFR note: July 9 EFFR confirmed as 3.62% daily rate. July 31 and Aug 1-5 EFFR stable at 3.63%.

## Known issues (added Aug 3-6, 2026)
- FXStreet URL pattern "202008031406" in search results for ISM Manufacturing PMI = August 3, **2020** article (54.2 vs 53.6 expected; prior 52.6). DO NOT use this as 2026 data.
- When searching for ISM data on release day (10am ET), searches run at 9am ET will NOT have the actual result yet.
- S&P Global flash PMI (released ~final week of month) tends to preview ISM direction but is a separate survey — reference as corroborating signal only.
- CME FedWatch search results may blend data from multiple dates; cross-check context (baseline always noted in memory).
- CME September hike repricing pattern since Jul 31: 82% (Jul 31) → 64.5% (Aug 3 post-ISM Mfg) → 61.9% (Aug 4) → 57% (Aug 6 post-ISM Services). Each ISM release has triggered repricing. Expect similar pattern with Jobs Report (Aug 7).
- ISM Services Prices Paid can diverge from Manufacturing PP: Jul Mfg PP eased to 71.1 (dovish), Jul Services PP reversed back above 70 (hawkish), but Employment weakness dominated net market read (mild dovish).
- growbeansprout.com consistently returns cached pre-FOMC-decision data (Jul 28, showing "54.4% cut") — completely stale. Ignore for directional analysis.
- defirate.com Polymarket/Kalshi data appears significantly lagged — showing "32% futures probability" which is inconsistent with confirmed CME data. Don't use.
- Polymarket September hike at 47% and annual "rate hike in 2026?" at 78% are coherent — three meetings remain (Sep, Oct, Dec) so annual probability exceeds single-meeting probability.
- KuCoin Polymarket articles tend to lag by 1-2 days; treat with caution when exact date is critical.
- "Zero cuts in 2026" Polymarket may have drifted to ~84% from ~89% — the specific 84.45% figure appeared in Aug 5-6 searches; treat as plausible.

## Run log

### August 6, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (stable; Aug 5 EFFR publishes today ~9am ET; expected stable at 3.63%)
- Next meeting: September 15–16, 2026 (SEP/dot plot meeting; decision Sep 16 at 2pm ET)
- CME September hike: ~57% (Aug 6; repriced from ~64.5% Aug 3; ISM Services miss and Employment weakness drove further dovish drift)
- Polymarket September hike: ~47% (Aug 5, post-ISM Services; "No change" leads at 53%)
- Polymarket "rate hike in 2026?": ~78% YES (unchanged)
- Polymarket "zero cuts in 2026?": ~84% (Aug 5-6; down from ~89%; mild dovish drift from ISM Services)
- ISM Services PMI July 2026: ACTUAL 54.1 (released Aug 5 at 10am ET)
  - vs 54.5 expected; prior 54.0; 25th consecutive expansion month
  - Prices Paid: reversed higher +2.6pts, back above 70 for 4th time in 5 months (hawkish)
  - Employment: dropped back into contraction (12 of last 18 months below 50)
  - Business Activity: surged +3.7pts
  - New Orders: 57.2 (accelerated)
  - Net market read: mild dovish (headline miss + Employment weakness > Prices Paid reversal)
- New FOMC row added: NO (next is September 16, 2026)
- JS countdown: 2026-09-16T18:00:00Z (unchanged; correct)
- MEANS-FOR-YOU: not updated (rate unchanged)
- Changes made:
  - "Last updated" → August 6, 2026
  - Card 2: CME ~64.5% → ~57% (Aug 6); Polymarket Sep ~53% → ~47% (Aug 5 post-ISM Services)
  - Card 2: ISM Services "releasing today" → actual 54.1 result with sub-components
  - Card 2: Zero cuts ~89% (~89.3%) → ~84% (Aug 5-6)
  - Card 3 hero-note: CME ~64.5% → ~57%; Polymarket ~53% → ~47%; zero cuts ~89% → ~84%; added ISM Services actual result
  - Rate path table: Sep line updated; ISM Services "releasing" → actual 54.1; Oct date Aug 5 → Aug 6; 2026 zero cuts ~89% → ~84%
- Notes: ISM Services July = 54.1 (slight miss vs 54.5; prior 54.0). Prices Paid reversed BACK above 70 (hawkish) but Employment weakness dominated — CME fell to ~57%, Polymarket to ~47%. Zero cuts drifted to ~84%. Today (Aug 6, Wednesday) is quiet — no major data. Jobs Report July (Aug 7) is the next major catalyst.
- CRITICAL NOTE for NEXT RUN (Aug 7+):
  - Jobs Report July (Aug 7 8:30am ET): MAJOR catalyst. Consensus +91k NFP, unemployment 4.3%. June was +57k (near 3-year low). CME baseline ~57% hike — strong NFP could push back to 65-70%+; weak NFP (<50k) could push below 50% and make "hold" the leading outcome.
  - Aug 7 is ALSO Jobless Claims (week ending Aug 1) — prior July 25 week was 197k (near historic lows).
  - CPI July releases Aug 12 — second key pre-September FOMC input.
  - CME search baseline: ~57% (Aug 6, post-ISM Services).
  - Polymarket baselines: ~47% September hike; ~84% zero cuts; ~78% hike in 2026.
  - No new FOMC history row until Sep 16 decision.

### August 5, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (stable)
- CME September hike: ~64.5% (Aug 3 post-ISM Mfg; no update before 10am ISM Services release)
- Polymarket September hike: ~53% (Aug 5 morning; down from ~56% on Aug 4)
- ISM Services PMI July: RELEASED today Aug 5 at 10am ET — actual 54.1 (captured in Aug 6 run)
- New FOMC row added: NO

### August 4, 2026
- CME September hike: ~64.5% (Aug 3 post-ISM; repriced from ~82%)
- Polymarket September hike: ~56% (Aug 4)
- ISM Manufacturing PMI July 2026: 55.6 (beat 54.0; highest since May 2022; Prices Paid 71.1 eased from 73.0)
- EFFR July 31: 3.63% (confirmed stable; published Aug 4)

### August 3, 2026
- CME September hike: ~82% (Jul 31 Friday close)
- Polymarket September hike: ~59% (Aug 3)
- Polymarket zero cuts: ~89%

### August 2, 2026
- CME September hike: ~82% (Jul 31 close)
- Polymarket September hike: ~60% (Aug 2)
- Polymarket zero cuts: ~89.3%
- Brent crude: ~$88/bbl (settled from $92 spike on Jul 31; Iran conflict ongoing)

### August 1, 2026
- CME September hike: ~82%
- Polymarket September hike: ~59.5% ($10.177M volume)
- Polymarket zero cuts: ~89% (up from 85% Jul 31; multiple sources confirmed)
- Iran: ceasefire ended (Trump declared over Jul 31); conflict ongoing
