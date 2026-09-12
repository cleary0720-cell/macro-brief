# Fed Tracker Agent Memory
Last updated: September 12, 2026

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
- Jobs Report: qz.com, foxbusiness.com, nbcnews.com all covered July 2026 jobs release well
- Jobless Claims: verifiedinvesting.com, bloomberg.com, fastcompact.com, academic-capital.com all cover weekly releases
- CME post-data repricing: Yahoo Finance (search "US rate futures [meeting] probability"), Convera ("weak jobs print resets Fed bets"), cryptobriefing.com all covered post-jobs CME repricing clearly with specific percentage figures
- CPI release: foxbusiness.com, nbcnews.com, cnbc.com, washingtonexaminer.com all covered July 2026 CPI well with specific figures
- Cleveland Fed Nowcast: clevelandfed.org/indicators-and-data/inflation-nowcasting — search snippets via WebSearch; good for pre-release CPI forecasts
- TD Securities / analyst research: mitrade.com/au/insights/news carries TD Securities research summaries; Kitco News, regardsofwallstreet.com carry Fed analysis
- Jackson Hole: kansascityfed.org/research/jackson-hole-economic-symposium; regardsofwallstreet.com/news for schedule; simianx.ai for analysis
- Post-Jackson Hole: benzinga.com (Benzinga Markets), thestreet.com, CNBC, NPR, finchannel.com, kalshi.com/news all covered Warsh speech reaction well
- Kalshi odds: kalshi.com/news (news.kalshi.com) carries September rate hike odds with specific figures post-speech; good source when CME FedWatch is unavailable
- Benzinga Prediction Markets: benzinga.com/news/26/09/ articles carry specific Kalshi, Polymarket, and CME figures together in one article — excellent for post-holiday first-trading-day repricing checks; URL pattern confirms September 2026 publication date
- CPI day repricing: cnbc.com September 11 CPI article (cnbc.com/2026/09/11/cpi-inflation-report-august-2026.html) — covers post-CPI CME repricing; predictionmarketspicks.com and 247wallst.com have post-CPI prediction market data; Nationwide Economics quoted as expecting quarter-point hike post-CPI
- Retail Sales: Census Bureau releases at 8:30am ET; financecalendar.com has accurate scheduled release dates; search "retail sales August 2026 release date Census" to confirm

## Known issues
- WEEKEND HALLUCINATION WARNING (Sep 5 observed): WebSearch on weekends returns confused synthesized probability figures mixing multiple time periods. On weekends with no new data releases, trust the prior-day confirmed memory over WebSearch synthesis. Stick with Friday close figures and note "stable, unchanged."
- Goldman Sachs "very unlikely" September hike call = published August 17, 2026 — PRE-Jackson Hole, PRE-jobs report. Now stale and superseded by subsequent data.
- Most aggregator sites that display CME FedWatch data (centralbank.watch, rateprobability.com, atlantafed.org, growbeansprout.com, morningstar.com, interactivecrypto.com, sofrrate.com) return HTTP 403 on WebFetch. Use WebSearch and read snippets.
- Yahoo Finance, CBS News, CNBC article pages also return 403 on WebFetch — use WebSearch to pull snippets.
- tradingeconomics.com also returns 403 on WebFetch.
- fxstreet.com analysis pages return 403 (including AMP versions).
- kucoin.com also returns 403 on WebFetch.
- EFFR data: NY Fed releases prior business day's data at approximately 9:00am ET. Weekends and federal holidays = no publication.
- Polymarket and CME FedWatch can diverge significantly — note both when available.
- Warsh withheld his dot at June meeting; 18 dots submitted going forward (not 19). May change at future meetings.
- sofrrate.com page title may show weekly average EFFR rather than daily EFFR — prefer ycharts/NY Fed for daily figure.
- WebSearch snippets about Polymarket may mix current odds with older quotes; cross-check against CME FedWatch for consistency.
- IMPORTANT: CME FedWatch direction matters — always confirm if a % refers to a hike, hold, or cut.
- HALLUCINATION WARNING: WebSearch CME results sometimes synthesize probability figures that contradict all other evidence. Cross-check against Polymarket, Kalshi, and prior-day baselines before using.
- Post-CPI repricing: CPI August 2026 (Sep 11) caused CME to reprice from ~55-57% (pre-CPI) to ~70-75% (post-CPI) — core MoM beat (0.3% vs 0.2% expected) drove the move.
- Polymarket September odds sometimes lag intraday CME moves; when CME reprices on data day, cite Polymarket as "repriced" with a range.
- growbeansprout.com consistently returns cached pre-FOMC-decision data — completely stale. Ignore for directional analysis.
- defirate.com Polymarket/Kalshi data appears significantly lagged — don't use for real-time odds.
- Weekend runs (Sat/Sun): no EFFR data published (NY Fed releases prior business day's data). No data releases. CME odds should be unchanged from Friday close.
- Bloomberg.com returns readable search snippets (article titles + descriptions) via WebSearch even if the full article is paywalled.
- Polymarket "rate hike in 2026?" market can move MUCH larger than the specific September meeting market.
- CPI August MoM data: sources conflicted between "0.4% MoM" and "0.1% MoM seasonally adjusted" — headline YoY is the reliable figure (3.4%); core MoM 0.3% was consistently cited as the beat.
- RELEASE DATE VERIFICATION: Always verify Retail Sales and other economic release dates via WebSearch before assuming the memory's expected date is correct. Census Bureau sometimes shifts release dates. In September 2026, Retail Sales August was moved to September 16 (same day as FOMC) — NOT September 12 as initially expected.
- tech-insider.org "Polymarket No Change Odds at 18%" interpretation is unclear — may not mean 18% hold; other sources consistently show Polymarket at 60-65% hike for Sep 16.

## Run log

### September 12, 2026 — FRIDAY / PRE-FOMC QUIET DAY
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Sep 11 data published Sep 12 ~9am ET; stable; unchanged)
- Next meeting: September 15–16, 2026 (decision Sep 16 at 2pm ET)
- KEY FINDING: Retail Sales August 2026 (Census) is scheduled for September 16 at 8:30am ET — NOT September 12. Memory had incorrect date.
- No data releases today. Quiet pre-FOMC day with FOMC blackout in effect.
- EFFR Sep 11: 3.63% (published Sep 12 ~9am ET; stable; unchanged)
- CME September hike: ~70–75% (stable from Sep 11 post-CPI close; no repricing catalyst on Sep 12)
- Polymarket September hike: ~60–65% (stable; cryptonews.com Sep 12 article: "62% September Hike Odds")
- Kalshi: ~57–60% (predictionmarketspicks.com Sep 12: "57% probability"; up from ~48% pre-CPI)
- New FOMC row added: NO (decision is September 16, 2026)
- MEANS-FOR-YOU: not updated (rate unchanged since Dec 2025)
- JS countdown: 2026-09-16T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → September 12, 2026
  - Card 1: Removed "(today)" from Sep 11 entry; added Sep 12 entry (no data, EFFR 3.63%, CME ~70-75% stable, Polymarket ~60-65% stable, Kalshi ~57-60%, FOMC blackout, Retail Sales moved to Sep 16)
  - Card 2: Updated top-level CME/Polymarket from "Sep 11" to "Sep 12" + added Kalshi figure; removed "(today)" from Sep 11; added Sep 12 entry
  - Card 3 Rate Path Sep row: Removed "(today)" from Sep 11; added Sep 12 entry
  - NO new FOMC history row (decision Sep 16)
  - NO changes to MEANS-FOR-YOU (rate unchanged)
  - NO changes to JS countdown (already set to 2026-09-16T18:00:00Z)
- Sources: census.gov (retail sales release schedule — Sep 16); sofrrate.com (EFFR 3.63%); predictionmarketspicks.com (Kalshi 57%); cryptonews.com (Polymarket 62%); yahoo finance / kucoin.com (CME 69.3% Sep 11 → stable ~70-75% Sep 12)

## CRITICAL NOTE for NEXT RUN (Sep 13 Sat / Sep 14 Sun — weekend / Sep 15 Mon — FOMC Day 1 / Sep 16 Tue — FOMC DECISION):
- **Sep 13 (Sat) / Sep 14 (Sun):** Weekend; no EFFR; no data; CME stable from Friday close
- **Sep 15 (Mon):** FOMC Day 1 (meeting begins); EFFR for Sep 12 published; no Fed speeches (blackout)
- **Sep 16 (Tue): FOMC DECISION at 2pm ET = 18:00 UTC — THE EVENT**
  - ALSO: Retail Sales August 2026 (Census) at 8:30am ET on Sep 16
  - If HIKE (+25bps): target range → 3.75% – 4.00%; effective rate ~3.88%; add FOMC history row; update MEANS-FOR-YOU; update JS countdown to Oct 28
  - If HOLD: target range stays 3.50% – 3.75%; no history row needed; note vote count; update JS countdown to Oct 28
  - Current odds: CME ~70-75% hike; Polymarket ~60-65%; Kalshi ~57-60%
  - 3 prior dissenters (Hammack, Kashkari, Logan) wanted hike at July meeting — likely vote for hike Sep 16
  - Press conference at 2:30pm ET; SEP (dot plot) released — watch for revised dot plot and inflation forecasts
  - Vote breakdown: search "FOMC September 16 2026 vote statement" immediately after 2pm ET
  - MEANS-FOR-YOU: update ONLY if rate changes (hike → update four consumer boxes)
  - If HIKE: JS countdown → next meeting (Oct 27-28, 2026 decision Oct 28): `new Date('2026-10-28T18:00:00Z')`
  - If HOLD: JS countdown → next meeting (Oct 27-28): `new Date('2026-10-28T18:00:00Z')`
  - Policy stance badge: if HIKE → change badge class to "hike" and label to "Rate Hike"; if HOLD → keep "hold" badge
- CME baselines entering Sep 13: ~70-75% hike / ~25-30% hold
- Polymarket: ~60-65% hike
- Kalshi: ~57-60% hike
- EFFR: Sep 11 data published Sep 12 (3.63%); Sep 12 data published Sep 15 (expected 3.63%)
- KEY UPCOMING EVENTS:
  - Sep 13-14 (Sat-Sun): Weekend — no EFFR, no data, CME stable
  - Sep 15 (Mon): FOMC Day 1; EFFR Sep 12 published ~9am ET
  - **Sep 16 (Tue): FOMC DECISION at 2pm ET = 18:00 UTC — THE EVENT; ALSO Retail Sales August at 8:30am ET**
  - Sep 17+ (after): Fed Chair Warsh press conference recap; dot plot analysis
  - Sep 26 (Fri approx): Core PCE August 2026 (BEA)
  - Oct 2 (Fri approx): September Jobs Report (BLS)
  - Oct 27-28: Next FOMC meeting (decision Oct 28)
  - Dec 8-9: Final FOMC 2026 meeting (decision Dec 9)
- FOMC history row prep (have ready if HIKE):
  - date-cell: Sep 16, 2026
  - decision: decision-hike span ("Hike +25bps")
  - range-cell: 3.75% – 4.00%
  - vote-cell: TBD (expect 9-3 or 10-2; 3 prior dissenters Hammack/Kashkari/Logan likely vote for hike)
  - Notes td: Dot-plot meeting; [statement language from press release]; inflation forecasts revised; Retail Sales Aug released same day
- If HOLD history row:
  - date-cell: Sep 16, 2026
  - decision: decision-hold span ("Hold")
  - range-cell: 3.50% – 3.75%
  - vote-cell: TBD (expect tight vote given prior 9-3 and CME ~70-75% hike odds)
  - Notes td: SEP meeting; dot plot released; [statement language]; Retail Sales Aug also released today
