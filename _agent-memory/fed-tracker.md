# Fed Tracker Agent Memory
Last updated: August 4, 2026

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
- IMPORTANT: CME FedWatch shows ~36.3% hike (move to 3.75-4.00%). Always interpret CME's "3.75-4.00%" outcome as a HIKE from the current 3.50-3.75% range. Do NOT label this as a "cut."
- Dashboard agent site.md has repeatedly mislabeled CME hike probability as "cut" — always verify directional interpretation against memory notes.
- Polymarket odds can shift significantly over short periods in response to macro data.
- blockchain.news/news articles often carry up-to-date Polymarket snapshots for Fed meetings — useful search source.
- CORRECTION: Q2 2026 GDP advance estimate is due July 30, 2026 (confirmed via bea.gov) — NOT June 30. Prior memory note was wrong.
- WebSearch can be intermittently unavailable (July 6, 2026 run: most searches failed; retries eventually succeeded). If searches keep failing, retry with broader queries or different phrasings.
- July 6 experience: WebSearch was very unreliable at run time (9am ET Sunday). Multiple "web search error: unavailable" responses. Try at least 4-6 searches with different queries before giving up.
- On Sundays: CME FedWatch won't have new data beyond Friday's close. EFFR for Friday won't be published until Monday morning. Polymarket is 24/7 and may shift slightly.
- FOMC minutes preview articles (published before 2pm ET same day) will show "expected" content based on the already-known dot plot — actual new debate details only in post-release analysis. Don't present preview content as "minutes revealed" facts.
- Blockchain.news article titles with Polymarket odds can be from any day — cross-check dates in context before using.
- EFFR note: July 9 EFFR confirmed as 3.62% daily rate (multiple FRED/NY Fed searches confirmed; updated on page as of Jul 12). Previously showed 3.63% — now corrected. July 11 EFFR (Saturday) won't be published; July 10 (Friday) EFFR publishes Monday July 14.

## Known issues (added Aug 3, 2026)
- FXStreet URL pattern "202008031406" in search results for ISM Manufacturing PMI = August 3, **2020** article (54.2 vs 53.6 expected; prior 52.6). DO NOT use this as 2026 data. Prior 2026 June ISM was 53.3, not 52.6 — the 2020 article has different prior.
- When searching for ISM Manufacturing PMI on release day (10am ET), searches run at 9am ET will NOT have the actual result yet. Note expected vs. prior and flag actual as TBD.
- S&P Global flash PMI (released ~final week of month) tends to preview ISM direction but is a separate survey — reference as corroborating signal only.
- Polymarket "rate hike in 2026?" article confusion: multiple articles from different dates (37%, 60%, 63%, 64%, 78%) exist. Use memory's most recent confirmed figure and cross-check volume for recency.
- KuCoin articles on Polymarket odds appear to lag real-time by days; treat with caution.
- CME FedWatch search results may blend data from multiple dates; cross-check context (the ~29.7% figure seen Aug 3 searches was a pre-July-29-decision quote, not current).

## Known issues (added Aug 4, 2026)
- CME September hike odds fell significantly (82% → 64.5%) after ISM Manufacturing PMI (55.6 headline beat) because Prices Paid eased to 71.1 from 73.0 — third straight monthly decline. Strong headline PMI can actually be DOVISH for hike odds if Prices Paid are falling.
- TradingView/CoinNess article citing "74.5% September hike" was from the immediate post-July-29-FOMC-decision period (July 29-30), NOT post-ISM. Don't confuse these timestamps.
- KuCoin "61.4% probability" article for September hike appears to be from early August — possibly Aug 3 or 4 close data. Consistent with the 64.5% midday figure.
- Polymarket search results on Aug 4 showed ~56% for September hike (down from 59% on Aug 3) — ISM prices paid easing drove slight dovish repricing.
- CME FedWatch search queries sometimes return July 28-30 data as "current" — always cross-reference with memory baseline and confirm article date.
- CME search snippets on Aug 4 returned 82% as "current" — this was the Jul 31 close, NOT Aug 3 close. The Aug 3 close post-ISM was ~64.5%.

## Run log

### August 4, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (July 31 EFFR confirmed 3.63% — published Aug 4; stable)
- Next meeting: September 15–16, 2026 (SEP/dot plot meeting)
- CME September hike: ~64.5% (Aug 3 post-ISM midday; repriced from ~82% Jul 31 close; Prices Paid easing drove dovish repricing despite headline beat)
- Polymarket September hike: ~56% (Aug 4; down from 59% Aug 3 post-ISM)
- Polymarket "rate hike in 2026?": ~78% (unchanged)
- Polymarket "zero cuts in 2026?": ~89% (unchanged)
- ISM Manufacturing PMI July 2026: **55.6** (released Aug 3 at 10am ET; beat 54.0 consensus; prior 53.3; highest since May 2022)
  - Prices Paid: 71.1 (down from 73.0; third straight monthly decline; 5-month low; above 70 for 6th straight month)
  - Employment: broke into expansion for first time in 33 months
  - Production: surged +6.3pts to highest in almost 5 years
  - S&P Global final July PMI: 53.9 (vs 53.8 preliminary)
- EFFR July 31 (Friday): 3.63% (confirmed stable; published Aug 4 at ~9am ET)
- New FOMC row added: NO (next is September 16, 2026)
- JS countdown: 2026-09-16T18:00:00Z (unchanged)
- MEANS-FOR-YOU: not updated (rate unchanged)
- Changes made:
  - "Last updated" → August 4, 2026
  - Card 2: CME ~82% (Jul 31) → ~64.5% (Aug 3 post-ISM); Polymarket Sep ~59% (Aug 3) → ~56% (Aug 4)
  - Card 2: ISM note updated from "due today, consensus 54.0" to actual "55.6 (beat); Prices Paid 71.1"; added Jobs Report Jul (Aug 7) preview (+91k consensus)
  - Card 3 hero-note: CME ~82% → ~64.5%; Polymarket ~59% → ~56%; zero cuts date Aug 3 → Aug 4; ISM note updated to actual result; added Jobs Report preview
  - Card 3 rate path: Sep line updated CME/Polymarket; ISM result added; Jobs Report preview added; Oct/2026 dates Aug 3 → Aug 4
- Notes: ISM Manufacturing PMI July 2026 came in at 55.6 (big beat vs 54.0 consensus; highest since May 2022). Prices Paid 71.1 eased from 73.0 — 3rd consecutive monthly decline, 5-month low. Despite the strong headline PMI, Prices Paid easing drove CME September hike odds DOWN from 82% to ~64.5% midday Monday — counterintuitive but markets are pricing in a less inflationary manufacturing outlook. Polymarket September also ticked down from 59% to ~56%. EFFR July 31 confirmed 3.63% (stable). Next major catalyst: Jobs Report July (Aug 7) — consensus +91k NFP, unemployment 4.3%. June was +57k near 3-year low. Strong NFP could reprice September hike odds significantly higher.
- CRITICAL NOTE for NEXT RUN (Aug 5+):
  - No major economic data releases on Tuesday Aug 5 or Wednesday Aug 6
  - Jobs Report (July) releases Friday Aug 7 — MAJOR catalyst for September hike odds; consensus +91k NFP, unemployment 4.3%; June was +57k (near 3-year low)
  - CPI July releases Aug 12 — second key pre-September FOMC input
  - September FOMC (Sep 15-16) is a SEP meeting — new dot plot
  - FOMC history row: No new row until Sep 16 decision
  - CME September baseline as of Aug 4: ~64.5% (post-ISM); will reprice significantly on Jobs Report
  - Polymarket September baseline: ~56% (Aug 4)
  - Iran conflict ongoing; monitor Brent crude — was ~$88/bbl
  - ISM Services PMI due this week — check release date (typically 1-2 business days after ISM Manufacturing)

### August 3, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (July 31 EFFR not yet published; publishes Monday Aug 4; stable)
- Next meeting: September 15–16, 2026 (SEP/dot plot meeting)
- CME September hike: ~82% (Jul 31 Friday close; most recent confirmed; Monday Aug 3 markets will reprice post-ISM data)
- Polymarket September hike: ~59% (Aug 3; down slightly from ~60% on Aug 2 — essentially flat)
- Polymarket "rate hike in 2026?": ~78% YES (unchanged)
- Polymarket "zero cuts in 2026?": ~89% (Aug 2/3 confirmed)
- ISM Manufacturing PMI July 2026: Released today Aug 3 at 10am ET (after 9am ET agent run). June was 53.3. Consensus ~54.0. S&P Global flash July PMI: 53.8 (from 53.9 in June). ISM Prices Paid expected 70.0 vs prior 73.0. Actual not confirmed in this run.
- EFFR for July 31 (Friday): Publishes tomorrow Aug 4 — check for stability at 3.63%
- New FOMC row added: NO (next is September 16, 2026)
- JS countdown: 2026-09-16T18:00:00Z (unchanged)
- MEANS-FOR-YOU: not updated (rate unchanged)
- Changes made:
  - "Last updated" → August 3, 2026
  - Card 2: Polymarket Sep ~60% (Aug 2) → ~59% (Aug 3); Iran update (Aug 2) → (Aug 3); added ISM PMI July note (consensus ~54.0, S&P flash 53.8)
  - Card 3 hero-note: ~60% (Aug 2) → ~59% (Aug 3); zero cuts date updated to Aug 3; added ISM note at end
  - Card 3 rate path table: Sep Polymarket → 59% (Aug 3); Oct date → Aug 3; 2026 zero cuts date → Aug 3; added ISM PMI note to Sep line

### August 2, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (July 31 EFFR not yet published; publishes Monday Aug 4; stable at 3.63%)
- Next meeting: September 15–16, 2026 (SEP/dot plot meeting)
- CME September hike: ~82% (Jul 31 Friday close; no weekend update)
- Polymarket September hike: ~60% (Aug 2; up from 59.5% on Aug 1; slight hawkish tick)
- Polymarket "zero cuts in 2026": ~89% (~89.3% confirmed Aug 2)
- Polymarket "rate hike in 2026?": ~78% YES (unchanged from Aug 1)
- Brent crude: ~$88/bbl (Aug 2; settled from $92 spike on Jul 31 morning; Iran conflict ongoing)
- Iran: Ceasefire ended July 31; conflict ongoing; oil stabilized near $88/bbl
- New FOMC row added: NO (next is September 16, 2026)

### August 1, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (July 29 EFFR still latest confirmed; July 30 published July 31; July 31 EFFR publishes Monday Aug 4)
- Next meeting: September 15–16, 2026 (SEP/dot plot meeting)
- CME September hike: ~82% (Jul 31 Friday close; essentially same as prior ~81%)
- Polymarket September hike: ~59.5% (Aug 1 confirmed, $10.177M volume on market — UP from ~53% immediately post-decision)
- Polymarket "rate hike in 2026?": ~78% YES (Jul 30-31 confirmed)
- Polymarket "zero cuts in 2026": ~89% (up from 85% on July 31; multiple Aug 1 search results confirmed ~89.3%)
- Iran: ceasefire ended (Trump declared it over Jul 31); conflict ongoing; Brent crude holding above $88/bbl
- New FOMC row added: NO (next is September 16, 2026)
