# Fed Tracker Agent Memory
Last updated: July 5, 2026

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
- IMPORTANT: CME FedWatch shows ~75.6% hold / ~24.4% HIKE (move to 3.75-4.00%). Always interpret CME's "3.75-4.00%" outcome as a HIKE from the current 3.50-3.75% range. Do NOT label this as a "cut."
- Dashboard agent site.md has repeatedly mislabeled CME hike probability as "cut" — always verify directional interpretation against memory notes.
- Polymarket odds can shift significantly on weekends even without new data — post-jobs-report high of 89% hold (Jul 3-4) pulled back to ~80.5% by Jul 5.
- blockchain.news/news articles often carry up-to-date Polymarket snapshots for Fed meetings — useful search source.
- CORRECTION: Q2 2026 GDP advance estimate is due July 30, 2026 (confirmed via bea.gov) — NOT June 30. Prior memory note was wrong.

## Run log

### July 5, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (sofrrate.com confirms; Jul 4 was holiday, no NY Fed publication; Jul 3 EFFR assumed 3.63% unchanged)
- FOMC meeting: No new meeting — last was June 16–17 (Hold, 12-0)
- Next meeting: July 28–29, 2026
- Market odds for July (Jul 5):
  - Polymarket: ~80.5% hold / ~17.5% hike / <1% cut (pullback from post-jobs-report highs of 89%/10% on Jul 3-4)
  - CME FedWatch: ~75.6% hold / ~24.4% hike (Jul 4 confirmed — partial reversal from 81%/19% on Jul 3)
- New FOMC row added: NO
- Changes made:
  - "Last updated" → July 5, 2026
  - Card 2 (Next FOMC): Updated "(Jul 4)" → "(Jul 5)"; Polymarket ~89%/~10% → ~80.5%/~17.5%; CME ~81%/~19% → ~75.6%/~24.4%; added Supreme Court Cook ruling note (Jun 29, 5-4 ruling, Trump cannot fire Lisa Cook); removed "markets closed Jul 3-4" note
  - Card 3 (Policy Stance): Updated Jul line to "~80.5% hold / ~17.5% hike (Jul 5, Polymarket); CME: ~75.6% hold / ~24.4% hike (Jul 4)"
- Notes: Rate unchanged so MEANS-FOR-YOU left untouched. Saturday July 5 — no major economic releases. Next catalyst: FOMC minutes July 8 (2pm ET), CPI June July 14, FOMC July 29. Supreme Court Cook ruling (Jun 29) added to Card 2 as significant Fed independence development. Polymarket weekend pullback from 89% → 80.5% noted in card. CME partial hawkish reversal (19% → 24.4%) from post-jobs lows also noted.

### July 4, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (last confirmed Jul 1-2; Jul 3 data not published — markets/Fed closed Jul 3-4 for Independence Day; next release Jul 6)
- FOMC meeting: No new meeting — last was June 16–17 (Hold, 12-0)
- Next meeting: July 28–29, 2026
- Market odds for July (Jul 4):
  - Polymarket: ~89% hold / ~10% hike / <1% cut (unchanged from Jul 3 post-jobs levels; Polymarket trades 24/7)
  - CME FedWatch: ~81% hold / ~19% hike (Jul 3 confirmed — significant drop from ~30% hike odds pre-jobs; markets closed Jul 4)
- New FOMC row added: NO

### July 3, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jul 3):
  - Polymarket: ~89% hold / ~10% hike (significant dovish shift from Jul 2's ~81%/~18%, driven by weak June jobs report)
  - CME FedWatch: ~70% hold / ~30% hike (last confirmed Jun 29; hike odds dropped sharply after jobs)
- New FOMC row added: NO

### July 2, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jul 2):
  - Polymarket: ~81% hold / ~18% hike (25bps) / ~1% cut
  - CME FedWatch: ~70% hold / ~30% hike (most recent confirmed: Jun 29)
- New FOMC row added: NO

### July 1, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jul 1):
  - Polymarket: ~80% hold / ~19% hike (25bps) / ~1% cut
  - CME FedWatch: ~70% hold / ~30% hike (most recent confirmed: Jun 29)
- New FOMC row added: NO

### June 30, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jun 30):
  - Polymarket: ~81% hold / ~18% hike (25bps) / ~1% cut
  - CME FedWatch: ~70% hold / ~30% hike
- New FOMC row added: NO

### June 29, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jun 29):
  - Polymarket: ~82% hold / ~16% hike (25bps) / ~1% cut
  - CME FedWatch: ~70% hold / ~30% hike
- New FOMC row added: NO
- Key event: Supreme Court ruled 5-4 (Trump v. Cook) that Trump cannot fire Fed Governor Lisa Cook for now; affirms Fed independence while case continues.

### June 28, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jun 28):
  - Polymarket: ~82% hold / ~18% hike (25bps) / ~1% cut
  - CME FedWatch: ~69% hold / ~31% hike
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
- Next countdown target: 2026-07-29T18:00:00Z
- Next FOMC row to add: July 29, 2026 (expect Hold or first Hike to 3.75-4.00%)
- EFFR daily: 3.63% (last confirmed Jul 1-3; assumed unchanged); IORB: 3.65% (effective Jun 18)
- Market odds as of Jul 5: ~80.5% hold / ~17.5% hike / <1% cut (Polymarket); CME: ~75.6% hold / ~24.4% hike (Jul 4 confirmed)
- Core PCE May 2026: 3.4% YoY (released Jun 25) — above Fed's own 3.3% June forecast
- GDP Q1 2026 FINAL: +2.1% (revised up from +1.6% 2nd estimate, released June 25)
- Q2 2026 GDP advance estimate: due July 30, 2026 (corrected — NOT June 30)
- ISM Manufacturing PMI June 2026: 53.3% (released July 1, confirmed via prnewswire.com) — down from 54.0% May but still expansionary
- ADP June private payrolls: 98k (released Jul 1, via CNBC) — below 110k expected
- June BLS Jobs Report (released Jul 2): +57,000 payrolls (vs. 115k expected — major miss); May revised down to 129k; 720,000 left labor force; participation rate fell to 61.5% (lowest since Mar 2021); unemployment 4.2% (from 4.3%); avg hourly earnings +0.3% MoM ($37.64)
- Supreme Court Cook ruling (Jun 29, 2026): Trump v. Cook, 5-4; Trump CANNOT fire Gov. Lisa Cook for now; affirms Fed independence while case continues
- FOMC minutes (June meeting) release: July 8, 2026 at 2pm ET — key catalyst before FOMC
- June CPI (July 14) is next major catalyst before July 29 FOMC
- Warsh at ECB Forum (Jul 1): said inflation "too high," declined to hint at July rate decision
- Polymarket odds trend: Jun 27 ~82%/18% → Jun 28 ~82%/18% → Jun 29 ~82%/16% → Jun 30 ~81%/18% → Jul 1 ~80%/19% → Jul 2 ~81%/18% → Jul 3 ~89%/10% (major dovish shift post-June BLS jobs miss) → Jul 4 ~89%/10% (unchanged; Polymarket 24/7) → Jul 5 ~80.5%/17.5% (weekend pullback)
- CME hike odds trend: Jun 27 ~31% → Jun 28 ~31% → Jun 29 ~30% → Jun 30 ~30% → Jul 1 ~30% → Jul 2 ~30% (estimated) → Jul 3 ~19% (confirmed — major drop post-June jobs miss) → Jul 4 ~24.4% (partial reversal, holiday market) → Jul 5 ~24.4% (Jul 4 data, latest confirmed)
- CRITICAL NOTE: CME "24.4% hike" = probability of rate moving to 3.75-4.00% (UP from 3.50-3.75%) — this is a HIKE, not a cut.
- Next major catalysts: Jul 8 FOMC minutes (2pm ET), Jul 14 CPI, Jul 16 Retail Sales, Jul 29 FOMC, Jul 30 GDP Q2 advance
