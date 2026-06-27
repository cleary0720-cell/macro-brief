# Fed Tracker Agent Memory
Last updated: June 27, 2026

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
- June 27 note: Polymarket shifted notably dovish from Jun 26 (76%/24%/2%) to Jun 27 (~82%/~18%/~1%). CME FedWatch remains at ~63%/~37%; no firm June 27 CME data found — most recent confirmed figure is June 23 at ~64.6%.

## Run log

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
- Key data today: University of Michigan final June sentiment scheduled (preliminary was 48.9); no major Fed-relevant release
- Changes made:
  - "Last updated" → June 26, 2026
  - Card 2 (Next FOMC): Updated "(Jun 25)" → "(Jun 26)"; added CME FedWatch ~63%/~37% note
  - Card 3 (Policy Stance): Updated Jul line from "(Jun 25, Polymarket)" → "(Jun 26, Polymarket); CME: ~63% hold / ~37% hike"
- Notes: Rate unchanged so MEANS-FOR-YOU left untouched. CME hike odds continued slight hawkish drift (35%→37%) while Polymarket held at 76%/24%. Next major catalyst: July 2 Jobs Report, July 14 CPI, July 29 FOMC.

### June 25, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Jun 22 most recently confirmed; Jun 24 not yet published by NY Fed at run time)
- FOMC meeting: No new meeting — last was June 16–17 (Hold, 12-0)
- Next meeting: July 28–29, 2026
- Market odds for July (Jun 25):
  - Polymarket: ~76% hold / ~24% hike (25bps) / ~2% cut (slightly more hold vs. yesterday's 74%/25%/2%)
- New FOMC row added: NO
- Key data released today:
  - Core PCE May 2026: 3.4% YoY (up from 3.3% April); 0.3% MoM — slightly above the Fed's own June forecast of 3.3%
  - Personal Income May: +0.7% MoM; Personal Spending May: +0.7% MoM — both above estimates
  - GDP Q1 2026 3rd estimate: scheduled for today but actual figure not confirmed in search results (2nd est. was 1.6%)
  - Durable Goods May (preliminary): -4.5% MoM (less than the -5.0% consensus)
- Notes: Rate unchanged so MEANS-FOR-YOU left untouched. Core PCE rose to 3.4% — top-side surprise relative to Fed's own 3.3% June forecast.

### June 24, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Jun 22 confirmed)
- Market odds for July (Jun 24):
  - Polymarket: ~74% hold / ~25% hike / ~2% cut
  - CME FedWatch: ~65% hold / ~35% hike (notable shift from ~72%/~28% on Jun 23)
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

### June 21, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jun 21):
  - Polymarket: ~74% hold / ~25% hike / ~2% cut
  - CME FedWatch: ~72% hold / ~28% hike
- New FOMC row added: NO

### June 20, 2026
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63%
- Market odds for July (Jun 20):
  - Hold: ~79% (Polymarket: 79.5%); Hike 25bps: ~19% (Polymarket: 19.4%)
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
- EFFR daily: 3.63% (last confirmed Jun 25); IORB: 3.65% (effective Jun 18)
- Market odds as of Jun 27: ~82% hold / ~18% hike / ~1% cut (Polymarket); CME: ~63% hold / ~37% hike
- Core PCE May 2026: 3.4% YoY (released Jun 25) — above Fed's own 3.3% June forecast
- Durable Goods May (preliminary, Jun 25): -4.5% MoM
- June CPI (July 14) and July 2 Jobs Report are next major data catalysts before the July 29 FOMC meeting
- Polymarket odds trend: Jun 20 ~79%/19% → Jun 21 ~74%/25% → Jun 22 ~79%/21% → Jun 23 ~75%/25% → Jun 24 ~74%/25% → Jun 25 ~76%/24% → Jun 26 ~76%/24% → Jun 27 ~82%/18% (notable dovish shift)
- CME hike odds trend: Jun 22 ~28% → Jun 23 ~28% → Jun 24 ~35% → Jun 25 ~35% → Jun 26 ~37% → Jun 27 ~37% (last firm data Jun 23 at ~35%; Jun 26 estimate 37%)
