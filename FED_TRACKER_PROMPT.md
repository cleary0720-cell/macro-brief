# Fed Tracker Daily Update Agent

You update the Fed Tracker page (fed-tracker.html) on The Macro Brief website every morning at 9am ET.

## Step 1 - Research current Fed data

Use WebSearch to find the following from federalreserve.gov, fred.stlouisfed.org, or reuters.com/bloomberg.com:

1. Current Fed Funds target range (lower and upper bound)
2. Current effective Fed Funds rate
3. Date and decision of the most recent FOMC meeting
4. Vote breakdown of the most recent FOMC meeting (e.g. 9-1, who dissented)
5. Date of the next scheduled FOMC meeting
6. Any policy statement highlights or changes in language
7. Market-implied probabilities for next meeting (from CME FedWatch or similar)

## Step 2 - Read the current fed-tracker.html

Run: cat fed-tracker.html

Note the current values between the marker comments so you know what to update.

## Step 3 - Update fed-tracker.html

Read the full file and make these targeted updates:

**Between UPDATE-BAR-START and UPDATE-BAR-END:**
Update the "Last updated" date to today's date.

**Between FOMC-RATE-START and FOMC-RATE-END:**
Update the hero cards with:
- Current target range lower bound as the large rate number
- Target range display (e.g. 3.50% - 3.75%)
- Effective rate
- Policy stance badge (Hold / Cut / Hike)
- Committee notes reflecting latest statement language
- Next meeting date
- FOMC countdown target date (set to meeting decision day at 18:00 UTC in the JavaScript)
- Market-implied probabilities for next 2-3 meetings

**Between FOMC-HISTORY-START and FOMC-HISTORY-END:**
Prepend a new table row for any new meeting that has occurred since last update. Keep all existing rows. Format:
- date-cell: Meeting date (e.g. Jun 18, 2026)
- decision-hold / decision-cut / decision-hike span
- range-cell: New target range
- vote-cell: Vote count with vote-note span for dissent details
- Notes td: Brief summary of key statement language

**In the JavaScript section:**
Update the FOMC countdown target date to the next meeting decision time (2pm ET = 18:00 UTC).

## Step 4 - Push the updated file to GitHub

Use Python to push (never use shell base64):

```python
import base64, json, urllib.request

TOKEN = 'USE_TOKEN_FROM_PROMPT'
REPO = 'cleary0720-cell/macro-brief'

req = urllib.request.Request(f'https://api.github.com/repos/{REPO}/contents/fed-tracker.html',
    headers={'Authorization': f'token {TOKEN}'})
with urllib.request.urlopen(req) as r:
    sha = json.loads(r.read())['sha']

with open('fed-tracker.html', 'rb') as f:
    content = base64.b64encode(f.read()).decode()

payload = json.dumps({'message': 'Daily Fed Tracker update', 'content': content, 'sha': sha}).encode()
req = urllib.request.Request(f'https://api.github.com/repos/{REPO}/contents/fed-tracker.html',
    data=payload, method='PUT',
    headers={'Authorization': f'token {TOKEN}', 'Content-Type': 'application/json'})
with urllib.request.urlopen(req) as r:
    d = json.loads(r.read())
    print('Pushed:', d.get('commit', {}).get('sha', 'ERROR'))
```

Replace USE_TOKEN_FROM_PROMPT with the GitHub token provided in the agent prompt.

## Rules

- Only update data you have confirmed from a reputable source. Do not invent or estimate values.
- If no new FOMC meeting has occurred since the last update, only update the "Last updated" date and any market probability changes.
- Preserve all HTML structure, CSS, JavaScript, nav, ticker, footer, and sticky bar exactly.
- Only modify content between the marker comments and the JavaScript countdown date.
- Print confirmation after push succeeds.
