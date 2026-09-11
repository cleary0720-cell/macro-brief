# Fed Tracker Agent Memory
Last updated: September 11, 2026

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

## Known issues
- WEEKEND HALLUCINATION WARNING (Sep 5 observed): WebSearch on weekends returns confused synthesized probability figures mixing multiple time periods. Searches returned figures ranging from "30% hike" (GS Aug 17 stale note) to "74-75% hold" (unverified Sep 5 source) alongside confirmed Sep 4 "70-75% hike" data. On weekends with no new data releases, trust the prior-day confirmed memory over WebSearch synthesis. Stick with Friday close figures and note "stable, unchanged."
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
- Post-CPI repricing: CPI August 2026 (Sep 11) caused CME to reprice from ~55-57% (pre-CPI) to ~70-75% (post-CPI) — core MoM beat (0.3% vs 0.2% expected) drove the move. Even an "in-line" headline can trigger large CME swings if core MoM surprises.
- Polymarket September odds sometimes lag intraday CME moves; when CME reprices on data day, cite Polymarket as "repriced" with a range.
- growbeansprout.com consistently returns cached pre-FOMC-decision data — completely stale. Ignore for directional analysis.
- defirate.com Polymarket/Kalshi data appears significantly lagged — don't use for real-time odds.
- Weekend runs (Sat/Sun): no EFFR data published (NY Fed releases prior business day's data). No data releases. CME odds should be unchanged from Friday close.
- Bloomberg.com returns readable search snippets (article titles + descriptions) via WebSearch even if the full article is paywalled.
- Polymarket "rate hike in 2026?" market can move MUCH larger than the specific September meeting market.
- CPI August MoM data: sources conflicted between "0.4% MoM" and "0.1% MoM seasonally adjusted" — headline YoY is the reliable figure (3.4%); core MoM 0.3% was consistently cited as the beat.

## Run log

### September 11, 2026 — FRIDAY / AUGUST CPI DAY (THE DECISIVE DATA RELEASE)
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Sep 10 data published Sep 11 ~9am ET; stable; unchanged)
- Next meeting: September 15–16, 2026 (decision Sep 16 at 2pm ET)
- KEY DATA: August CPI (BLS, released Sep 11, 8:30am ET):
  - Headline: 3.4% YoY (in-line vs. 3.4% consensus); core 2.4% YoY (in-line)
  - Core MoM: 0.3% (vs. 0.2% expected — slight beat; hawkish)
  - Energy: +16.3% YoY; gasoline: +3.9% MoM (Middle East tensions)
  - MoM headline: sources conflicted 0.1% vs 0.4% SA — use YoY/core for reliability
- KEY DATA: PPI August 2026 (released Sep 10, 8:30am ET):
  - +0.4% MoM, +5.4% YoY — hot wholesale inflation; energy +4.2% MoM
  - Post-PPI prediction markets moved to ~63% hike (from ~55-57% pre-PPI)
- EFFR Sep 10: 3.63% (published Sep 11 ~9am ET; stable; unchanged)
- CME September hike: ~70–75% (post-CPI; up from ~55–57% pre-CPI; sharp hawkish repricing)
- Polymarket September hike: ~60–65% (post-CPI; up from ~49–50%)
- Kalshi: ~48% (Sep 10; pre-CPI; likely higher post-CPI but not confirmed in search results)
- New FOMC row added: NO (decision is September 16, 2026)
- MEANS-FOR-YOU: not updated (rate unchanged since Dec 2025)
- JS countdown: 2026-09-16T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → September 11, 2026
  - Card 1: Removed "(today)" from Sep 10 entry; added Sep 10 PPI data; added Sep 11 (today) with CPI results, EFFR, post-CPI CME ~70-75%, Polymarket ~60-65%
  - Card 2: CME updated from "~55-57%" to "~70-75% (Sep 11; post-CPI)"; Polymarket from "~49-50%" to "~60-65%"; "August CPI releases TOMORROW" → "August CPI DELIVERED Sep 11"; "Next key catalysts" updated to "All key catalysts delivered"; Sep 10 "(today)" removed; Sep 11 entry added; CPI futures reference updated
  - Card 3 Policy Stance: CME updated from "~55-57%" to "~70-75% (Sep 11; post-CPI)"; Polymarket from "~49-50%" to "~60-65%"
  - Rate Path Sep row: CME updated to ~70-75%; Polymarket updated to ~60-65%; "next catalyst: August CPI (Sep 10)" updated to "August CPI DELIVERED Sep 11"; Sep 10 entry updated with PPI data; Sep 11 (today) entry added with CPI results
- Sources: cnbc.com/2026/09/11/cpi-inflation-report-august-2026.html; nowflation.com (3.36% sealed call vs 3.4% street); babypips.com (PPI August +0.4% MoM, +5.4% YoY); nchstats.com (PPI +5.4% YoY); predictionmarketspicks.com; 247wallst.com; yahoo finance (CME ~70%); sofrrate.com (EFFR 3.63%)
- Notes: BIG DATA DAY — AUGUST CPI. Headline in-line at 3.4% YoY. Core MoM 0.3% vs 0.2% expected — slight beat. Hot energy (+16.3% YoY, gasoline +3.9%). Post-CPI CME repriced sharply to ~70-75% hike from ~55-57% pre-CPI. Nationwide Economics now expects quarter-point hike. Polymarket repriced to ~60-65%. PPI August (released Sep 10) was already hot at +5.4% YoY. ALL MAJOR PRE-FOMC DATA RELEASED. FOMC decision September 16 at 2pm ET is next.

## CRITICAL NOTE for NEXT RUN (Sep 12 Fri — FOMC BLACKOUT / Sep 13 Sat — quiet / Sep 16 Tue — FOMC DECISION):
- FOMC blackout period: typically starts ~10 days before meeting (around Sep 6 for Sep 16 decision); no Fed speeches until post-decision
- **Sep 12 (Fri): Retail Sales August 2026 (Census, 8:30am ET)**
  - Previous: -0.6% MoM monthly / +5.0% YoY; prior miss was June tax refund fading
  - Consensus: rebound expected given jobs revision upward
  - With jobs revised to +21k (July) and +162k (Aug), consumer spending expected stronger
  - Retail Sales unlikely to dramatically move CME from ~70-75% at this point — data decision is basically made
- **Sep 13 (Sat) / Sep 14 (Sun):** Weekend; no EFFR; no data; CME stable from Friday close
- **Sep 15 (Mon):** FOMC Day 1 (begins); no EFFR (fed holiday? No — Columbus Day is Oct. Check if Sep 15 is a holiday); EFFR for Sep 12 published Sep 15
- **Sep 16 (Tue): FOMC DECISION at 2pm ET = 18:00 UTC**
  - If HIKE (+25bps): target range → 3.75% – 4.00%; effective rate ~3.88%; add FOMC history row
  - If HOLD: target range stays 3.50% – 3.75%; no history row needed; note vote count
  - Current odds: CME ~70-75% hike; Polymarket ~60-65%; 3 dissenters (Hammack, Kashkari, Logan) wanted hike at July meeting — likely vote for hike Sep 16
  - Press conference at 2:30pm ET; SEP (dot plot) released — watch for revised dot plot and inflation forecasts
  - Vote breakdown: search "FOMC September 16 2026 vote statement" immediately after 2pm ET
  - MEANS-FOR-YOU: update ONLY if rate changes (hike → update four consumer boxes)
  - If HIKE: JS countdown → next meeting (Oct 27-28, 2026 decision Oct 28): `new Date('2026-10-28T18:00:00Z')`
  - If HOLD: JS countdown stays at next meeting (Oct 27-28): `new Date('2026-10-28T18:00:00Z')`
  - Policy stance badge: if HIKE → change badge class to "hike" and label to "Rate Hike"; if HOLD → keep "hold" badge
- CME baselines entering Sep 12: ~70-75% hike / ~25-30% hold
- Polymarket: ~60-65% hike
- Kalshi: unknown (pre-CPI was ~48%; likely moved higher post-CPI; search specifically)
- EFFR: Sep 11 data published Sep 12 ~9am ET (expected 3.63% stable)
- KEY UPCOMING EVENTS:
  - **Sep 12 (Fri): Retail Sales August 2026 (Census, 8:30am ET)**
  - Sep 13-14 (Sat-Sun): Weekend — no EFFR, no data, CME stable
  - Sep 15 (Mon): FOMC Day 1; EFFR Sep 12 published
  - **Sep 16 (Tue): FOMC DECISION at 2pm ET = 18:00 UTC — THE EVENT**
  - Sep 17+ (after): Fed Chair Warsh press conference recap; dot plot analysis
  - Sep 26 (Fri approx): Core PCE August 2026 (BEA)
  - Oct 2 (Fri approx): September Jobs Report (BLS)
  - Oct 27-28: Next FOMC meeting (decision Oct 28)
  - Dec 8-9: Final FOMC 2026 meeting (decision Dec 9)
- FOMC history row prep (have ready if HIKE):
  - date-cell: Sep 16, 2026
  - decision: decision-hike span ("Hike +25bps")
  - range-cell: 3.75% – 4.00%
  - vote-cell: TBD (expect 9-3 or 10-2; 3 prior dissenters Hammack/Kashkari/Logan likely vote for hike; others may join)
  - Notes td: Dot-plot meeting; [statement language from press release]; inflation forecasts revised
