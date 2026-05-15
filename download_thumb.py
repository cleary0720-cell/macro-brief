import urllib.request, shutil, sys

PHOTO_MAP = {
    "Monetary Policy": "3779760",
    "Inflation": "5632398",
    "Labor Markets": "3184292",
    "Economic Output": "1108101",
    "Fixed Income": "534216",
    "Consumer Economy": "1884581",
    "Money Supply": "164527",
    "Trade Policy": "1427541",
    "Energy & Commodities": "2101137",
    "Fiscal Policy": "1550337",
    "Housing Market": "106399",
    "Financial Markets": "6801874",
    "Banking": "1602726",
    "Technology Economy": "373543",
    "Global Economy": "1098515"
}
FALLBACK = '4386321'

category = sys.argv[1]
slug     = sys.argv[2]   # e.g. 2026-05-labor-markets

pid  = PHOTO_MAP.get(category, FALLBACK)
url  = f'https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?w=800&h=450&fit=crop&auto=compress'
out  = f'images/{slug}-thumb.jpg'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as r:
    with open(out, 'wb') as f:
        shutil.copyfileobj(r, f)
print(f'Saved: {out}')
