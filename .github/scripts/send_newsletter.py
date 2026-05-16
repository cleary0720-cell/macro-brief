import subprocess, os, json, urllib.request, urllib.parse, base64, re, smtplib, random, shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Only run for new article commits
commit_msg = subprocess.check_output(["git", "log", "-1", "--pretty=%s"], text=True).strip()
if not commit_msg.startswith("Add article:"):
    print(f'Skipping: "{commit_msg}" is not a new article commit')
    exit(0)

# Find the new article file
diff = subprocess.check_output(
    ["git", "diff", "--diff-filter=A", "--name-only", "HEAD~1", "HEAD"], text=True
).strip()
articles = [f for f in diff.split("\n") if f.startswith("articles/") and f.endswith(".html")]
if not articles:
    print("No new article file found in this commit")
    exit(0)

article_path = articles[0]
slug = article_path.replace("articles/", "").replace(".html", "")
article_url = f"https://themacrobrief.net/{article_path}"
print(f"Article: {article_path}")

with open(article_path) as f:
    html = f.read()

headline_m = re.search(r'class="article-hed"[^>]*>([^<]+)<', html)
subhead_m  = re.search(r'class="article-subhead">(.+?)</p>', html, re.DOTALL)
category_m = re.search(r'class="article-category"[^>]*>([^<]+)<', html)
paras = re.findall(r'<p>(?!.*class=)(.+?)</p>', html, re.DOTALL)

headline = headline_m.group(1).strip() if headline_m else commit_msg.replace("Add article: ", "")
subhead  = subhead_m.group(1).strip() if subhead_m else ""
category = category_m.group(1).strip() if category_m else "Macro"
date_str = datetime.now().strftime("%B %d, %Y")

BODY_HTML = "".join([
    f'<p style="font-size:15px;line-height:1.8;color:#333;margin:0 0 16px;">{p.strip()[:500]}</p>'
    for p in paras[:3] if len(p.strip()) > 20
])

# --- Fix thumbnail via Pexels API ---
PEXELS_KEY = os.environ.get("PEXELS_KEY", "")
thumb_path = f"images/{slug}-thumb.jpg"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO = os.environ.get("GITHUB_REPOSITORY", "")

if PEXELS_KEY and os.path.exists(thumb_path):
    # Derive keyword from headline
    keyword = re.sub(r'[^a-zA-Z ]', '', headline).strip()[:40]
    print(f"Searching Pexels for: {keyword}")
    try:
        q = urllib.parse.urlencode({"query": keyword, "per_page": 15, "orientation": "landscape"})
        req = urllib.request.Request(
            f"https://api.pexels.com/v1/search?{q}",
            headers={"Authorization": PEXELS_KEY, "User-Agent": "TheMacroBrief/1.0"}
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            pdata = json.loads(r.read())
        photos = pdata.get("photos", [])
        if photos:
            photo = random.choice(photos[:10])
            img_url = photo["src"]["large2x"]
            img_req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(img_req, timeout=15) as r:
                img_data = r.read()
            with open(thumb_path, "wb") as f:
                f.write(img_data)
            print(f"Downloaded new thumbnail (Pexels ID {photo['id']})")

            # Push updated thumbnail to GitHub
            sha_req = urllib.request.Request(
                f"https://api.github.com/repos/{REPO}/contents/{thumb_path}",
                headers={"Authorization": f"token {TOKEN}"}
            )
            with urllib.request.urlopen(sha_req) as r:
                sha = json.loads(r.read())["sha"]
            payload = {
                "message": f"Fix thumbnail for {slug} via Pexels API",
                "content": base64.b64encode(img_data).decode(),
                "sha": sha
            }
            push_req = urllib.request.Request(
                f"https://api.github.com/repos/{REPO}/contents/{thumb_path}",
                data=json.dumps(payload).encode(), method="PUT",
                headers={"Authorization": f"token {TOKEN}", "Content-Type": "application/json"}
            )
            with urllib.request.urlopen(push_req) as r:
                result = json.loads(r.read())
                print(f"Pushed thumbnail: {result.get('commit',{}).get('sha','ERROR')[:10]}")
    except Exception as e:
        print(f"Pexels thumbnail fix failed: {e} — keeping existing thumbnail")

# --- Send newsletter ---
BEEHIIV_KEY = base64.b64decode(os.environ["BEEHIIV_KEY"]).decode()
PUB_ID = "pub_7c236eb8-9009-4da1-bf40-903fee0558bf"

req = urllib.request.Request(
    f"https://api.beehiiv.com/v2/publications/{PUB_ID}/subscriptions?limit=100&status=active",
    headers={"Authorization": f"Bearer {BEEHIIV_KEY}"}
)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())

subscribers = [s["email"] for s in data.get("data", [])
    if s.get("email") and s["email"] != "test@example.com"]
print(f"Sending to {len(subscribers)} subscribers")

email_html = (
    '<!DOCTYPE html><html><head><meta charset="UTF-8"></head>'
    '<body style="margin:0;padding:0;background:#f0ebe0;font-family:Georgia,serif;">'
    '<table width="100%" cellpadding="0" cellspacing="0" style="background:#f0ebe0;padding:20px 0;">'
    '<tr><td align="center"><table width="600" cellpadding="0" cellspacing="0" style="background:#fff;max-width:600px;width:100%;">'
    '<tr><td style="background:#1a1a1a;padding:24px 32px;text-align:center;border-bottom:3px solid #C41E3A;">'
    '<div style="font-size:24px;font-weight:bold;color:#F6F1E7;letter-spacing:2px;text-transform:uppercase;">THE MACRO BRIEF</div>'
    '<div style="font-size:11px;color:#999;letter-spacing:1px;text-transform:uppercase;margin-top:4px;">Independent Economic Analysis</div></td></tr>'
    f'<tr><td style="background:#C41E3A;padding:8px 32px;"><span style="font-size:11px;color:#fff;letter-spacing:2px;text-transform:uppercase;">{category.upper()} &mdash; {date_str}</span></td></tr>'
    f'<tr><td style="padding:32px;color:#1a1a1a;">'
    f'<h1 style="font-size:24px;line-height:1.3;margin:0 0 8px;">{headline}</h1>'
    f'<p style="font-size:15px;color:#555;margin:0 0 24px;font-style:italic;border-bottom:1px solid #e0d9cc;padding-bottom:16px;">{subhead}</p>'
    '<p style="font-size:13px;color:#888;margin:0 0 24px;">By Connor Leary &mdash; The Macro Brief</p>'
    + BODY_HTML +
    f'<p style="margin-top:32px;padding-top:16px;border-top:1px solid #e0d9cc;"><a href="{article_url}" style="background:#C41E3A;color:#fff;padding:12px 24px;text-decoration:none;font-size:13px;text-transform:uppercase;letter-spacing:1px;">Read Full Article &rarr;</a></p>'
    '<p style="margin-top:24px;font-size:13px;color:#555;">See the dashboard at <a href="https://themacrobrief.net" style="color:#C41E3A;">themacrobrief.net</a></p>'
    '</td></tr><tr><td style="background:#1a1a1a;padding:20px 32px;text-align:center;">'
    '<p style="color:#888;font-size:11px;margin:0;">&copy; 2026 Connor Leary / The Macro Brief &mdash; themacrobrief.net</p>'
    '<p style="color:#666;font-size:10px;margin:8px 0 0;">To unsubscribe, reply with "unsubscribe" in the subject line.</p>'
    '</td></tr></table></td></tr></table></body></html>'
)

GMAIL_USER = "macrobriefnews@gmail.com"
GMAIL_PASS = os.environ["GMAIL_PASS"]

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.login(GMAIL_USER, GMAIL_PASS)
    for email in subscribers:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = headline
        msg["From"]    = f"The Macro Brief <{GMAIL_USER}>"
        msg["To"]      = email
        msg.attach(MIMEText(email_html, "html"))
        server.send_message(msg)
        print(f"Sent to {email}")

print("Newsletter sent successfully.")
