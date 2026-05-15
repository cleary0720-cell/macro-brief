import urllib.request, urllib.parse, shutil, sys, json, random

PEXELS_KEY = 'gKfA0uAiln84lEEyFzf64iuizHKdeSKCiWG2xebCsFpE24ViqIOG0ufD'

# Fallback photo IDs per category if search returns no results
FALLBACK_MAP = {
    'Monetary Policy':      ['3779760', '4386321', '534216'],
    'Inflation':            ['5632398', '4386321', '3943716'],
    'Labor Markets':        ['3184292', '3183197', '1181533'],
    'Economic Output':      ['1108101', '3943716', '4386321'],
    'Fixed Income':         ['534216',  '3779760', '6801874'],
    'Consumer Economy':     ['1884581', '3943716', '1098515'],
    'Money Supply':         ['164527',  '534216',  '3779760'],
    'Trade Policy':         ['1427541', '1098515', '906494'],
    'Energy and Commodities': ['2101137', '1098515', '4386321'],
    'Fiscal Policy':        ['1550337', '3779760', '534216'],
    'Housing Market':       ['106399',  '1550337', '1181533'],
    'Financial Markets':    ['6801874', '534216',  '3779760'],
    'Banking':              ['1602726', '534216',  '6801874'],
    'Technology Economy':   ['373543',  '1181533', '3184292'],
    'Global Economy':       ['1098515', '1427541', '3779760'],
}

category = sys.argv[1]
slug     = sys.argv[2]
keyword  = sys.argv[3] if len(sys.argv) > 3 else category
out      = f'images/{slug}-thumb.jpg'

def download_by_id(pid):
    url = f'https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?w=800&h=450&fit=crop&auto=compress'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as r:
        with open(out, 'wb') as f:
            shutil.copyfileobj(r, f)

# Search Pexels for the keyword
query = urllib.parse.urlencode({'query': keyword, 'per_page': 15, 'orientation': 'landscape'})
req = urllib.request.Request(
    f'https://api.pexels.com/v1/search?{query}',
    headers={'Authorization': PEXELS_KEY}
)
try:
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read())
    photos = data.get('photos', [])
    if photos:
        # Pick a random photo from the results to avoid repeats
        photo = random.choice(photos[:10])
        pid = str(photo['id'])
        img_url = photo['src']['large2x']
        img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(img_req, timeout=15) as r:
            with open(out, 'wb') as f:
                shutil.copyfileobj(r, f)
        print(f'Saved: {out} (Pexels ID {pid}, keyword: {keyword})')
    else:
        raise ValueError('No results')
except Exception as e:
    print(f'Search failed ({e}), using fallback for {category}')
    fallbacks = FALLBACK_MAP.get(category, ['4386321'])
    download_by_id(random.choice(fallbacks))
    print(f'Saved: {out} (fallback)')
