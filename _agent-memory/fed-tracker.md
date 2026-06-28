# Fed Tracker Agent Memory
Last updated: June 28, 2026

## Push method
git add/commit/push works directly. Pre-authenticated via GitHub App. Never use urllib, MCP base64, or hardcoded tokens.

## Reliable data sources
- Fed Funds Rate & FOMC decisions: federalreserve.gov press release pages (e.g. monetary20260617a.htm); CNBC, NPR, Fox Business cover decisions same day
- Effective rate: EFFR via NY Fed / FRED — search "effective federal funds rate EFFR [date]"; search snippets from federalreserve.gov H.15 / newyorkfed.org
- Market probabilities: CME FedWatch (search for snippets via WebSearch); Polymarket for binary year-end/meeting odds; Kalshi for pre-decision dissent odds
- Vote breakdown: federalreserve.gov FOMC statement pages; search "FOMC [date] vote statement"
- Dot plot / SEP: Seeking Alpha, TradingKey, CNBC post-decision summaries carry dot plot details
- Post-decision analysis: sherwood.news, coinpedia.org, forexfactory.com, interactivecrypto.com

## Known issues
- Most aggregator sites that display CME FedWatch data (centralbank.watch, rateprobability.com, atlantafed.org, growbeansprout.com, morningstar.com, interactivecrypto.com, sofrrate.com) return HTTP 403 on WebFetch. Use WebSearch and read snippets.
- Yahoo Finance, CBS News, CNBC article pages also return 403 on WebFetch — use WebSearch to pull snippets.
- tradingeconomics.com also returns 403 on WebFetch.
- fxstreet.com analysis pages return 403 (including AMP versions).
- kucoin.com also returns 403 on WebFetch.
- EFFR data: NY Fed releases prior business day's data at approximately 9:00am ET.
- Polymarket and CME FedWatch can diverge significantly — note both when available.
- Warsh withheld his dot at June meeting; 18 dots submitted going forward (not 19). May change at future meetings.
- sofrrate.com page title may show weekly average EFFR (3.62%) rather than daily EFFR (3.63%) — prefer ycharts/NY Fed for daily figure.
- WebSearch snippets about Polymarket may mix current odds with older quotes; cross-check against CME FedWatch for consistency.
- WebSearch snippets often recycle data from prior days — treat Polymarket snippets showing "79.5%/19.4%" as June 19 data, not current.
- IMPORTANT: CME FedWatch shows 69% hold / 31% HIKE (move to 3.75-4.00%). The dashboard agent (site.md) mistakenly labeled this 31% as "cut" on June 28 — it is definitely a HIKE. Always interpret CME's "3.75-4.00%" outcome as a hike from the current 3.50-3.75% range.
- CME hike odds trended: Jun 22 ~28% → Jun 23 ~28% → Jun 24 ~35% → Jun 25 ~35% → Jun 26 ~37% → Jun 27 (actual confirmed) ~31%. The Jun 27 CME figure was not confirmed during the Jun 27 run; it was confirmed on Jun 28 run at 69%/31%.

## Run log

### June 28, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (last confirmed Jun 25-26; Jun 27 data not found separately but assumed unchanged)
- FOMC meeting: No new meeting — last was June 16–17 (Hold, 12-0)
- Next meeting: July 28–29, 2026
- Market odds for July (Jun 28):
  - Polymarket: ~82% hold / ~18% hike (25bps) / ~1% cut (unchanged from Jun 27)
  - CME FedWatch: ~69% hold / ~31% hike (confirmed Jun 27 data; decreased from estimated ~37% on Jun 26)
- New FOMC row added: NO
- Changes made:
  - "Last updated" → June 28, 2026
  - Card 2 (Next FOMC): Updated "(Jun 27)" → "(Jun 28)"; updated CME from "~63% hold / ~37% hike" → "~69% hold / ~31% hike"
  - Card 3 (Policy Stance): Updated "(Jun 27, Polymarket)" → "(Jun 28, Polymarket)"; updated CME from "~63% hold / ~37% hike" → "~69% hold / ~31% hike"
- Notes: Rate unchanged so MEANS-FOR-YOU left untouched. CME hike odds modestly decreased (37%→31%) vs. Polymarket holding steady at 18%. Both sources agree July hold is most likely. Dashboard agent site.md mistakenly labeled 31% CME as "cut" — it's actually a 31% hike probability. Next major catalysts: July 2 Jobs Report, July 14 CPI, July 29 FOMC.

### June 27, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Jun 25 confirmed; Jun 26 data likely same; no updated figure found)
- FOMC meeting: No new meeting — last was June 16–17 (Hold, 12-0)
- Next meeting: July 28–29, 2026
- Market odds for July (Jun 27):
  - Polymarket: ~82% hold / ~18% hike (25bps) / ~1% cut (notable dovish shift from 76%/24%/2% on Jun 26)
  - CME FedWatch: ~63% hold / ~37% hike (last confirmed Jun 23-26; no fresh Jun 27 CME data found)
- New FOMC row added: NO
- Changes made:
  - "Last updated" → June 27, 2026
  - Card 2 (Next FOMC): Updated "(Jun 26)" → "(Jun 27)"; Polymarket odds updated to ~82%/~18%/~1%
  - Card 3 (Policy Stance): Updated Jul line from "(Jun 26, Polymarket)" → "(Jun 27, Polymarket)"; updated 76%→82%/24%→18%/2%→1%; updated yr-end line from "~76% hold Jul" → "~82% hold Jul"
- Notes: Rate unchanged so MEANS-FOR-YOU left untouched. CME FedWatch divergence with Polymarket widening: CME still ~37% hike vs Polymarket only ~18% hike. Next major catalyst: July 2 Jobs Report, July 14 CPI, July 29 FOMC.

### June 26, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Jun 24/25 confirmed; Jun 26 data published today at 9am ET but not confirmed different)
- FOMC meeting: No new meeting — last was June 16–17 (Hold, 12-0)
- Next meeting: July 28–29, 2026
- Market odds for July (Jun 26):
  - Polymarket: ~76% hold / ~24% hike (25bps) / ~2% cut (essentially unchanged from Jun 25)
  - CME FedWatch: ~62.6% hold / ~37.4% hike (continued hawkish drift from ~65%/~35% on Jun 25)
- New FOMC row added: NO

### June 25, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jun 25):
  - Polymarket: ~76% hold / ~24% hike (25bps) / ~2% cut
- New FOMC row added: NO
- Key data released: Core PCE May 2026: 3.4% YoY (above Fed's 3.3% forecast); GDP Q1 final: +2.1%

### June 24, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jun 24):
  - Polymarket: ~74% hold / ~25% hike / ~2% cut
  - CME FedWatch: ~65% hold / ~35% hike
- New FOMC row added: NO

### June 23, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jun 23):
  - Polymarket: ~75% hold / ~25% hike
  - CME FedWatch: ~72% hold / ~28% hike
- New FOMC row added: NO

### June 22, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jun 22):
  - Polymarket: ~79% hold / ~21% hike
  - CME FedWatch: ~72% hold / ~28% hike
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
- EFFR daily: 3.63% (last confirmed Jun 25-26); IORB: 3.65% (effective Jun 18)
- Market odds as of Jun 28: ~82% hold / ~18% hike / ~1% cut (Polymarket); CME: ~69% hold / ~31% hike
- Core PCE May 2026: 3.4% YoY (released Jun 25) — above Fed's own 3.3% June forecast
- GDP Q1 2026 FINAL: +2.1% (revised up from +1.6% 2nd estimate, released June 25)
- June CPI (July 14) and July 2 Jobs Report are next major data catalysts before the July 29 FOMC meeting
- Polymarket odds trend: Jun 20 ~79%/19% → Jun 21 ~74%/25% → Jun 22 ~79%/21% → Jun 23 ~75%/25% → Jun 24 ~74%/25% → Jun 25 ~76%/24% → Jun 26 ~76%/24% → Jun 27 ~82%/18% → Jun 28 ~82%/18% (stable)
- CME hike odds trend: Jun 22 ~28% → Jun 23 ~28% → Jun 24 ~35% → Jun 25 ~35% → Jun 26 ~37% → Jun 27 (confirmed Jun 28): ~31%
- CRITICAL NOTE for next runs: CME "31% hike" = probability of rate moving to 3.75-4.00% (UP from 3.50-3.75%) — this is a HIKE, not a cut. Dashboard agent site.md confused this as "cut" on Jun 28.
