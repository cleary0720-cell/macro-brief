# Fed Tracker Agent Memory
Last updated: July 7, 2026

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.

## Reliable data sources
- Fed Funds Rate & FOMC decisions: federalreserve.gov press release pages (e.g. monetary20260617a.htm); CNBC, NPR, Fox Business cover decisions same day
- Effective rate: EFFR via NY Fed / FRED — search "effective federal funds rate EFFR [date]"; search snippets from federalreserve.gov H.15 / newyorkfed.org; sofrrate.com/policy-rates
- Market probabilities: CME FedWatch (search for snippets via WebSearch); Polymarket for binary year-end/meeting odds; blockchain.news for Polymarket summary articles
- Vote breakdown: federalreserve.gov FOMC statement pages; search "FOMC [date] vote statement"
- Dot plot / SEP: Seeking Alpha, TradingKey, CNBC post-decision summaries carry dot plot details
- Post-decision analysis: sherwood.news, coinpedia.org, forexfactory.com, interactivecrypto.com

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
- IMPORTANT: CME FedWatch shows ~26.6% hike (move to 3.75-4.00%). Always interpret CME's "3.75-4.00%" outcome as a HIKE from the current 3.50-3.75% range. Do NOT label this as a "cut."
- Dashboard agent site.md has repeatedly mislabeled CME hike probability as "cut" — always verify directional interpretation against memory notes.
- Polymarket odds can shift significantly over short periods in response to macro data.
- blockchain.news/news articles often carry up-to-date Polymarket snapshots for Fed meetings — useful search source.
- CORRECTION: Q2 2026 GDP advance estimate is due July 30, 2026 (confirmed via bea.gov) — NOT June 30. Prior memory note was wrong.
- WebSearch can be intermittently unavailable (July 6, 2026 run: most searches failed; retries eventually succeeded). If searches keep failing, retry with broader queries or different phrasings.
- July 6 experience: WebSearch was very unreliable at run time (9am ET Sunday). Multiple "web search error: unavailable" responses. Try at least 4-6 searches with different queries before giving up.
- On Sundays: CME FedWatch won't have new data beyond Friday's close. EFFR for Friday won't be published until Monday morning. Polymarket is 24/7 and may shift slightly.
- July 7 (Monday): EFFR data for July 3 is confirmed at 3.63% (published this morning per NY Fed schedule). WebSearch was reliable and quick on this run.

## Run log

### July 7, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (July 3 data confirmed published July 7 per NY Fed schedule)
- FOMC meeting: No new meeting — last was June 16–17 (Hold, 12-0)
- Next meeting: July 28–29, 2026
- Market odds for July (Jul 7):
  - Polymarket: ~84% hold / ~15% hike / ~0% cut (significant dovish shift from Jul 6's 79.5%/19.4%)
  - CME FedWatch: ~73.4% hold / ~26.6% hike (slight hawkish shift from Jul 4-6's 75.6%/24.4%)
- New FOMC row added: NO
- Changes made:
  - "Last updated" → July 7, 2026
  - Card 2 (Next FOMC): Updated market odds to Jul 7 figures; Polymarket 79.5%/19.4% → 84%/15%; CME 75.6%/24.4% → 73.4%/26.6%; updated FOMC minutes note to "tomorrow (July 8)"
  - Card 3 (Policy Stance): Updated Jul line to "~84% hold / ~15% hike (Jul 7, Polymarket); CME: ~73.4% hold / ~26.6% hike (Jul 7)"
- Notes: Monday July 7. EFFR July 3 confirmed 3.63%. Polymarket moved significantly toward hold (84% vs 79.5% on Jul 6). CME moved slightly more hawkish. FOMC minutes tomorrow (July 8 at 2pm ET) is next major catalyst. Rate unchanged so MEANS-FOR-YOU left untouched.

### July 6, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (last confirmed Jul 2 published Jul 3; Jul 6 Sunday = no new EFFR until Monday Jul 7)
- FOMC meeting: No new meeting — last was June 16–17 (Hold, 12-0)
- Next meeting: July 28–29, 2026
- Market odds for July (Jul 6):
  - Polymarket: ~79.5% hold / ~19.4% hike / ~0% cut (slight hawkish shift from Jul 5's 80.5%/17.5%)
  - CME FedWatch: ~75.6% hold / ~24.4% hike (Jul 4 confirmed — no new data on weekend)
  - Polymarket "zero cuts in 2026": 79.8%
- New FOMC row added: NO

### July 5, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jul 5):
  - Polymarket: ~80.5% hold / ~17.5% hike / <1% cut
  - CME FedWatch: ~75.6% hold / ~24.4% hike
- New FOMC row added: NO

### July 4, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jul 4):
  - Polymarket: ~89% hold / ~10% hike / <1% cut
  - CME FedWatch: ~81% hold / ~19% hike
- New FOMC row added: NO

### July 3, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jul 3):
  - Polymarket: ~89% hold / ~10% hike
  - CME FedWatch: ~70% hold / ~30% hike (hike odds dropped sharply post-June jobs miss)
- New FOMC row added: NO

### July 2, 2026
- Target range: 3.50% – 3.75% (no change); Effective rate: 3.63%
- Polymarket: ~81% hold / ~18% hike / ~1% cut; CME: ~70% hold / ~30% hike
- New FOMC row added: NO

### July 1, 2026
- Target range: 3.50% – 3.75% (no change); Effective rate: 3.63%
- Polymarket: ~80% hold / ~19% hike / ~1% cut; CME: ~70% hold / ~30% hike
- New FOMC row added: NO

### June 30, 2026
- Target range: 3.50% – 3.75% (no change); Effective rate: 3.63%
- Polymarket: ~81% hold / ~18% hike / ~1% cut; CME: ~70% hold / ~30% hike
- New FOMC row added: NO

### June 29, 2026
- Target range: 3.50% – 3.75% (no change); Effective rate: 3.63%
- Polymarket: ~82% hold / ~16% hike / ~1% cut; CME: ~70% hold / ~30% hike
- New FOMC row added: NO
- Key event: Supreme Court ruled 5-4 (Trump v. Cook) — Trump cannot fire Fed Governor Lisa Cook for now

### June 28, 2026
- Target range: 3.50% – 3.75% (no change); Effective rate: 3.63%
- Polymarket: ~82% hold / ~18% hike / ~1% cut; CME: ~69% hold / ~31% hike
- New FOMC row added: NO

### June 18, 2026
- Target range: 3.50% – 3.75% (HOLD — confirmed June 17, 2026 unanimous 12-0 vote)
- Effective rate: 3.63%
- New FOMC row added: YES — Jun 17, 2026 (Hold, 12-0)

## FOMC 2026 meeting schedule (remaining)
- July 28–29, 2026 ← NEXT meeting
- September 15–16, 2026 ← SEP/dot plot meeting
- October 27–28, 2026
- December 8–9, 2026 ← SEP/dot plot meeting

## Key context for next runs
- Rate held at 3.50%-3.75% since Nov 2025 (75bps of cuts since late 2024)
- Warsh era: hawkish; communication overhaul underway (task forces announced Jun 17)
- Warsh withholds his dot — 18 dots submitted (not 19) going forward
- Statement format is now very short (~130 words) with no forward guidance
- Easing bias REMOVED as of June 17, 2026
- Dot plot signals one hike in H2 2026: 9 of 18 participants see at least one hike; median 2026 year-end at 3.8%
- No MEANS-FOR-YOU update needed unless rate actually changes (still 3.50-3.75%)
- Next countdown target: 2026-07-29T18:00:00Z (already set correctly in JS)
- Next FOMC row to add: July 29, 2026 (expect Hold or first Hike to 3.75-4.00%)
- EFFR daily: 3.63% (July 3 data confirmed published July 7); IORB: 3.65% (effective Jun 18)
- Market odds as of Jul 7: ~84% hold / ~15% hike / ~0% cut (Polymarket); CME: ~73.4% hold / ~26.6% hike
- Polymarket "zero cuts in 2026": 79.8% (unchanged from Jul 6)
- Core PCE May 2026: 3.4% YoY (released Jun 25) — above Fed's own 3.3% June forecast
- GDP Q1 2026 FINAL: +2.1% (revised up from +1.6%, released June 25)
- Q2 2026 GDP advance estimate: due July 30, 2026
- ISM Manufacturing PMI June 2026: 53.3% (released July 1) — down from 54.0% May but still expansionary
- ADP June private payrolls: 98k (released Jul 1) — below 110k expected
- June BLS Jobs Report (released Jul 2): +57,000 payrolls (vs. 115k expected — major miss); May revised down to 129k; 720,000 left labor force; participation rate fell to 61.5% (lowest since Mar 2021); unemployment 4.2%; avg hourly earnings +0.3% MoM ($37.64)
- Supreme Court Cook ruling (Jun 29, 2026): Trump v. Cook, 5-4; Trump CANNOT fire Gov. Lisa Cook for now
- FOMC minutes (June meeting) release: July 8, 2026 at 2pm ET — key catalyst before FOMC July 29
- June CPI (July 14) is next major catalyst before July 29 FOMC
- Warsh at ECB Forum (Jul 1): said inflation "too high," declined to hint at July rate decision
- Treasury yields on Jul 7: 2Y=4.114%, 10Y=4.469%, 30Y=4.984% (little changed; investors await FOMC minutes)
- Polymarket odds trend: Jul 3 ~89%/10% → Jul 4 ~89%/10% → Jul 5 ~80.5%/17.5% → Jul 6 ~79.5%/19.4% → Jul 7 ~84%/15%
- CME hike odds trend: Jul 3 ~19% → Jul 4-6 ~24.4% → Jul 7 ~26.6%
- CRITICAL NOTE: CME "26.6% hike" = probability of rate moving to 3.75-4.00% (UP from 3.50-3.75%) — HIKE, not cut.
- Next major catalysts: Jul 8 FOMC minutes (2pm ET), Jul 14 CPI, Jul 16 Retail Sales, Jul 29 FOMC, Jul 30 GDP Q2 advance
