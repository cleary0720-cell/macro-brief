# Fed Tracker Agent Memory
Last updated: August 31, 2026

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
- Jobless Claims: verifiedinvesting.com, bloomberg.com, fastcompany.com, academic-capital.com all cover weekly releases
- CME post-data repricing: Yahoo Finance (search "US rate futures [meeting] probability"), Convera ("weak jobs print resets Fed bets"), cryptobriefing.com all covered post-jobs CME repricing clearly with specific percentage figures
- CPI release: foxbusiness.com, nbcnews.com, cnbc.com, washingtonexaminer.com all covered July 2026 CPI well with specific figures
- Cleveland Fed Nowcast: clevelandfed.org/indicators-and-data/inflation-nowcasting — search snippets via WebSearch; good for pre-release CPI forecasts
- TD Securities / analyst research: mitrade.com/au/insights/news carries TD Securities research summaries; Kitco News, regardsofwallstreet.com carry Fed analysis
- Jackson Hole: kansascityfed.org/research/jackson-hole-economic-symposium; regardsofwallstreet.com/news for schedule; simianx.ai for analysis
- Post-Jackson Hole: benzinga.com (Benzinga Markets), thestreet.com, CNBC, NPR, finchannel.com, kalshi.com/news all covered Warsh speech reaction well
- Kalshi odds: kalshi.com/news (news.kalshi.com) carries September rate hike odds with specific figures post-speech; good source when CME FedWatch is unavailable

## Known issues
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
- Post-CPI repricing: CPI July 2026 (Aug 12) caused CME to reprice from ~40% hike to ~50% hike — even a "dovish" (in-line) CPI reading can shift markets toward hike if the headline remains elevated (3.4% >> 2% target).
- Polymarket September odds sometimes lag intraday CME moves by hours; when CME reprices on data day, cite Polymarket as "repricing" with a range rather than a precise figure.
- KuCoin article titled "Polymarket Prices 53% Odds of Fed Rate Hike in September 2026 vs. 32% in Futures" — this is an INTRADAY Aug 12 figure; confirmed stale; do not use as a current figure.
- growbeansprout.com consistently returns cached pre-FOMC-decision data — completely stale. Ignore for directional analysis.
- defirate.com Polymarket/Kalshi data appears significantly lagged — don't use for real-time odds.
- Weekend runs (Sat/Sun): no EFFR data published (NY Fed releases prior business day's data). No data releases. CME odds should be unchanged from Friday close. Market odds from Bloomberg/Yahoo Finance post-data articles are more reliable than real-time aggregators on weekends.
- Bloomberg.com returns readable search snippets (article titles + descriptions) via WebSearch even if the full article is paywalled. Good for confirming Treasury moves and rate repricing on data days.
- Polymarket "rate hike in 2026?" market can move MUCH larger than the specific September meeting market — post-Warsh it surged from ~47% to ~60-68% (intraday peak ~69%) while September-specific Polymarket moved from ~53% to ~51% (slight dovish drift on Aug 28). Always track both markets separately.
- Kalshi September hike odds post-Warsh: ~47% (Aug 28; +17pp surge) — lower than CME (~59%) but both directionally hawkish.

## Run log

### August 31, 2026 — MONDAY / QUIET WEEKEND CLOSE (POST-JACKSON HOLE)
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Aug 28 data published Aug 31; stable; confirmed via sofrrate.com snippet)
- Next meeting: September 15–16, 2026 (decision Sep 16 at 2pm ET)
- CME September hike: ~60% / hold ~40% (Aug 31; up from ~57-59% Aug 28-30 post-Warsh close)
- Kalshi September hike: ~48% (Aug 31; up from ~47% Aug 28)
- Polymarket September hike: ~53% (Aug 28; stable; no confirmed Aug 31 update)
- "Rate hike in 2026?" Polymarket: ~60-68% (Aug 28-29; stable post-Warsh)
- "Zero cuts in 2026?" Polymarket: ~84% (stable)
- New FOMC row added: NO (next is September 16, 2026)
- MEANS-FOR-YOU: not updated (rate unchanged since Dec 2025)
- JS countdown: 2026-09-16T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → August 31, 2026
  - Card 1 end note: CME figure updated to ~60% as of Aug 31; Polymarket noted "stable"
  - Card 2: CME updated from ~57% to ~60% (Aug 31); Kalshi updated from ~47% to ~48% (Aug 31)
  - Card 3 policy stance: CME updated from ~57% to ~60% (Aug 31); "~57%/~43%" → "~60%/~40%"
  - Card 3 rate path Sep row: CME updated from ~57% to ~60% (Aug 31); Kalshi updated from ~47% to ~48%
- Sources: WebSearch "effective federal funds rate EFFR August 28 2026" → sofrrate.com confirms 3.63%; WebSearch "CME FedWatch September 2026 probability August 31 2026" → AI summary citing ~60.4%; Kalshi ~48% per search snippet; CNBC Aug 28 article confirms coin-flip after Warsh speech
- Notes: Quiet Monday. No major data releases (Labor Day is Sep 7 — NOT Sep 1 as previous agent incorrectly noted; Sep 1 is a Tuesday in 2026; markets open today). EFFR for Aug 28 published today (Aug 31); stable at 3.63%. CME drifted ~+1-3pp higher to ~60% from Aug 30 close; Kalshi up 1pp to ~48%. Next critical data: August Jobs Report (~Sep 5) and August CPI (~Sep 10) before the Sep 16 FOMC decision. ISM Manufacturing Aug due Sep 2.
- CORRECTION NOTE: Prior memory stated "Labor Day: Monday September 1, 2026" — this is INCORRECT. Sep 1, 2026 is a TUESDAY. Labor Day 2026 = September 7, 2026 (first Monday of September). EFFR publications resume normally; no holiday gap.

### CRITICAL NOTE for NEXT RUN (Sep 1, Tue):
- EFFR for Aug 29 published Sep 1 (~9am ET); expect stable at 3.63%
- ISM Manufacturing August 2026: Sep 2 (~10am ET) — prior July: 55.6 (4-yr high)
- CME baselines entering this week: ~60% hike / ~40% hold (Aug 31)
- Polymarket baselines: September ~53%; "rate hike in 2026?" ~60-68%
- Kalshi: ~48% (Aug 31)
- KEY EVENTS:
  - Sep 2 (Tue): ISM Manufacturing PMI August 2026 (~10am ET)
  - Sep 3 (Wed): ISM Services PMI August (verify date)
  - Sep 5 (Fri): AUGUST JOBS REPORT (BLS) — MOST CONSEQUENTIAL PRINT OF 2026
  - Sep 10 (Wed): CPI August 2026
  - Sep 15-16: FOMC (decision Sep 16 2pm ET = 18:00 UTC; dot-plot meeting)
- No new FOMC history row until Sep 16 decision
- MEANS-FOR-YOU: only update if Fed Funds Rate changes (unchanged since Dec 2025)

### August 30, 2026 — SUNDAY / QUIET WEEKEND (POST-JACKSON HOLE)
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Aug 27 data; published Aug 29; no weekend EFFR; stable; Labor Day Sep 1 = no EFFR publication; next data Sep 2)
- Next meeting: September 15–16, 2026 (decision Sep 16 at 2pm ET)
- CME September hike: ~57-59% (Aug 28-29 post-Warsh close; Benzinga cited "59%"; prior memory "~57%"; consistent)
- Kalshi September hike: ~47% (Aug 28; +17pp surge post-speech per kalshi.com/news)
- Polymarket September hike: ~51-53% (Aug 28 post-speech; "September Meeting" at 51% per Polymarket dashboard)
- Polymarket "rate hike in 2026?": ~60-68% (Aug 28-29; surged post-Warsh; intraday peak ~69%; KuCoin confirmed ~60%; prior agent run had ~47% which was pre-speech or lagging)
- Polymarket "zero cuts in 2026?": ~84% (stable; unchanged)
- New FOMC row added: NO (next is September 16, 2026)
- MEANS-FOR-YOU: not updated (rate unchanged since Dec 2025)
- JS countdown: 2026-09-16T18:00:00Z (unchanged; correct)
- Changes made:
  - "Last updated" → August 30, 2026
  - Card 2: "Rate hike in 2026?" Polymarket updated from ~47% to ~60-68%; Kalshi ~47% September added
  - Card 3 / rate path Sep row: "Rate hike in 2026?" updated from ~47% to ~60-68%; Kalshi added
  - Rate path Oct and 2026 rows: "Rate hike in 2026?" updated from ~47% to ~60-68%
- Sources: Benzinga ("59% CME after Warsh speech"); benzinga.com/markets/prediction-markets/26/08/61499396; CNBC Aug 28 (coin flip comment); kalshi.com/news ("47%, +17pp surge"); cryptobriefing.com/polymarket-fed-rate-hike-odds-2026 ("60% odds"); kucoin.com/news/flash/polymarket-predicts-60-odds ("60% odds"); FRED/NY Fed EFFR 3.63% Aug 27
- Notes: Quiet Sunday. No new data releases or EFFR publication (Labor Day Sep 1 = no EFFR Mon Sep 1 either; next EFFR publication Sep 2 for Aug 29 data). Key update today: discovered that prior Aug 29 run used a pre-speech Polymarket "rate hike in 2026?" figure (~47%) that had already surged post-speech to ~60-68% by end of Aug 28. Updated all references across three cards and rate path table. The post-Warsh repricing is now fully reflected on the page. CME at ~57-59%, Kalshi at ~47%, Polymarket September at ~51-53%, "rate hike in 2026?" at ~60-68%. Next critical data: August Jobs Report (~Sep 5) and August CPI (~Sep 10) before the Sep 16 FOMC decision.

### CRITICAL NOTE for NEXT RUN (Sep 1, Mon — LABOR DAY / or Sep 2, Tue — FIRST TRADING DAY):
- **Monday Sep 1 = LABOR DAY**: no EFFR publication; markets closed; no data releases
  - If run fires Sep 1: date-only update; carry all figures from Aug 29-30 close
- **Tuesday Sep 2**: EFFR for Aug 29 published (~9am ET); expect stable at 3.63%; first ISM Manufacturing August data (Sep 2 ~10am ET)
  - ISM Manufacturing August 2026 (Sep 2 ~10am ET) — prior July: 55.6 (4-yr high); watch for continuation vs. pullback
  - If strong ISM: could add marginal hawkish pressure on CME (already at ~57-59%)
  - If weak ISM: moderate dovish signal; CME may drift toward 50%
- **CME baselines entering this week**: ~57-59% hike / ~41-43% hold (post-Warsh)
- **Polymarket baselines**: September ~51-53%; "rate hike in 2026?" ~60-68%
- **Kalshi**: September ~47%
- **EFFR**: 3.63% (no change expected through Sep 16 FOMC)
- **KEY EVENTS THIS WEEK**:
  - Sep 2 (Tue): ISM Manufacturing PMI August 2026 (~10am ET); EFFR Aug 29 published
  - Sep 3 (Wed): ISM Services PMI August? (CHECK DATE — may be Sep 4 Thu)
  - Sep 5 (Fri): **AUGUST JOBS REPORT (BLS)** — MOST CONSEQUENTIAL PRINT OF 2026
    - Entering: CME ~57-59% hike; Post-Warsh hawkish baseline
    - Strong (>100k NFP, unemployment ≤4.1%): CME could jump to 65-75% → significant hawkish repricing
    - Weak (<0 NFP, repeat of July shock): CME could fall to 35-45% → significant dovish repricing
    - In-line (50-100k NFP): CME could hold 55-60%
    - This is the single most important data release before the Sep 16 FOMC decision
- **September 10 (Wed)**: CPI August 2026 — second most important; Cleveland Nowcast: ~3.22% YoY headline
- **September 15-16 FOMC**: DECISION Sep 16 at 2pm ET; DOT-PLOT MEETING (new SEP)
  - A hike would push target to 3.75-4.00% (highest since 2024)
  - Warsh has 3 formal dissenters who already wanted to hike; May be 6+ if data stays hawkish
- IMPORTANT: No new FOMC history row until Sep 16 decision
- MEANS-FOR-YOU: only update if Fed Funds Rate changes (unchanged since Dec 2025)
- JS countdown: 2026-09-16T18:00:00Z (correct; no change needed)

### August 29, 2026 — SATURDAY / POST-WARSH JACKSON HOLE SPEECH
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Aug 27 data; published Aug 29 ~9am ET; stable unchanged)
- Next meeting: September 15–16, 2026 (decision Sep 16 at 2pm ET)
- KEY EVENT: Warsh Jackson Hole keynote delivered Fri Aug 28 at 10am ET — HAWKISH
  - Key quotes: "While this summer's readings were better than expected, they do not tell me that underlying trends have meaningfully improved." / "I stand here today committed to a discipline, not a decision." / Fed "has more work to do."
  - Tone: Hawkish — warned inflation not durably improved; dismissed forward guidance; called for "quieter" central bank
  - 2-year Treasury yield: +6.6bps to 4.29% on the day
  - CME post-speech: ~57% hike / ~43% hold (Aug 29); pre-speech baseline was ~36%/~64%
  - Polymarket post-speech: ~53% hike (Aug 28; from ~31% pre-speech)
  - Repricing: approximately +20pp on CME in single session
- CME September hike: ~57% (post-Warsh speech, Aug 29)
- Polymarket September hike: ~53% (post-Warsh speech, Aug 28)
- "Rate hike in 2026?" Polymarket: ~47% YES (Aug 28; NOTE: this was pre-speech or lagging; actually surged to ~60-68% — corrected in Aug 30 run)
- "Zero cuts in 2026?" Polymarket: ~84% (Aug 5–6; stable)
- New FOMC row added: NO (next is September 16, 2026)
- MEANS-FOR-YOU: not updated (rate unchanged since Dec 2025)
- JS countdown: 2026-09-16T18:00:00Z (unchanged; correct)

### August 28, 2026 — FRIDAY / WARSH JACKSON HOLE KEYNOTE DAY (PRE-SPEECH 9am ET RUN)
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Aug 26 data confirmed via FRED/NY Fed; stable unchanged; published Aug 27 ~9am ET)
- Next meeting: September 15–16, 2026 (decision Sep 16 at 2pm ET)
- CME entering speech: ~36% hike / ~64% hold
- Polymarket entering speech: ~31% hike / ~68% hold
- Warsh Jackson Hole keynote at 10am ET — HAWKISH (post-speech data in Aug 29 run)

### August 27, 2026 — THURSDAY / JACKSON HOLE DAY 1 + CORE PCE + JOBLESS CLAIMS
- Target range: 3.50% – 3.75% (no change)
- Effective rate: 3.63% (Aug 25 data; published Aug 26 ~9am ET; stable unchanged)
- Core PCE July 2026 (released Aug 26): 3.3% YoY / 0.2% MoM — in line; Headline PCE 3.7% (above forecast)
- Jobless Claims (week ending Aug 22, released Aug 27): 203,000 initial; 4-week avg 205,500
- CME September hike: ~40% (Aug 27); Polymarket: ~34%

### August 26, 2026 — WEDNESDAY / JACKSON HOLE EVE
- CME: ~38-40% (Aug 26); Polymarket: ~31-34%; EFFR: 3.63% (Aug 24 data)

### August 25, 2026 — TUESDAY / PRE-SYMPOSIUM
- CME: ~30% (Aug 25); Polymarket: ~31%; EFFR: 3.63%

### UPCOMING EVENTS:
  - Labor Day: Monday September 1, 2026 (no EFFR publication; markets closed)
  - ISM Manufacturing August: Tuesday September 2, 2026 (~10am ET)
  - August Jobs Report: Friday, September 5, 2026 (MOST IMPORTANT DATA BEFORE SEP 16 FOMC)
  - August CPI: Wednesday, September 10, 2026
  - September 15–16 FOMC: decision September 16 at 2pm ET = 18:00 UTC (dot-plot meeting)
