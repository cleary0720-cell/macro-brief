"""Replace duplicate article thumbnails with fresh, unique Pexels photos.

The Sunday article agent runs in a sandbox that cannot reach *.workers.dev, so it
falls back to copying an existing thumbnail. This runs on GitHub (open network),
finds any dated thumbnail that is byte-identical to an earlier one, and swaps in a
new photo searched from the article's hero alt text.
"""
import glob, hashlib, os, re, time, urllib.parse, urllib.request

WORKER_URL = "https://pexels-proxy.cleary0720.workers.dev"
DATED = re.compile(r"^images/(\d{4}-\d{2}-[\w-]+)-thumb\.jpg$")


def md5(data):
    return hashlib.md5(data).hexdigest()


def query_for(slug):
    """Search phrase: the hero image alt text, else the headline."""
    path = f"articles/{slug}.html"
    if not os.path.exists(path):
        return None
    page = open(path, encoding="utf-8").read()
    m = re.search(r'<img[^>]*src="\.\./images/' + re.escape(slug) + r'-thumb\.jpg"[^>]*alt="([^"]+)"', page)
    if not m:
        m = re.search(r'class="article-hed"[^>]*>([^<]+)<', page)
    if not m:
        return None
    words = re.sub(r"[^A-Za-z ]", " ", m.group(1)).split()
    stop = {"a", "an", "the", "of", "and", "to", "in", "on", "for", "with", "representing", "reflecting", "symbolizing"}
    return " ".join(w for w in words if w.lower() not in stop)[:60]


def fetch(query, category):
    params = urllib.parse.urlencode({"query": query, "category": category})
    req = urllib.request.Request(f"{WORKER_URL}?{params}", headers={"User-Agent": "TheMacroBrief/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


thumbs = sorted(p for p in glob.glob("images/*-thumb.jpg") if DATED.match(p))
seen = {md5(open(p, "rb").read()) for p in glob.glob("images/*.jpg")}
first_owner = {}
replaced = []

for path in thumbs:
    h = md5(open(path, "rb").read())
    if h not in first_owner:
        first_owner[h] = path
        continue

    slug = DATED.match(path).group(1)
    query = query_for(slug)
    if not query:
        print(f"skip {path}: no article or alt text to search from")
        continue

    print(f"{path} duplicates {first_owner[h]} — searching: {query!r}")
    for attempt in range(6):
        try:
            data = fetch(query, "economy")
        except Exception as e:
            print(f"  attempt {attempt + 1}: {e}")
            time.sleep(2)
            continue
        nh = md5(data)
        if data[:2] == b"\xff\xd8" and nh not in seen:
            open(path, "wb").write(data)
            seen.add(nh)
            replaced.append(path)
            print(f"  replaced ({len(data)} bytes)")
            break
        # the worker picks a random result per call, so retrying usually yields a new photo
    else:
        print(f"  gave up on {path} — leaving existing image")

print(f"Replaced {len(replaced)} thumbnail(s)")
if os.environ.get("GITHUB_OUTPUT"):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"replaced={len(replaced)}\n")
