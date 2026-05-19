"""
Auditoria profunda Pages Autos Soler + Inversiones Soler.
Extrae TODA la info accesible (sin pages_messaging).
"""
import sys, json, urllib.request, urllib.error
from pathlib import Path
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding='utf-8')

try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    pass

ROOT = Path(__file__).parent
env = (ROOT / '.env').read_text(encoding='utf-8')
def get(k):
    for l in env.splitlines():
        if l.startswith(f'{k}=') and not l.startswith('#'):
            return l.split('=',1)[1].strip()
    return ''

TOKEN = get('META_ACCESS_TOKEN')
API = 'v25.0'

ts = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M')
OUT = ROOT / f'audit-pages-{ts}'
OUT.mkdir(exist_ok=True)

PAGES = [
    {'id': '100123132505557', 'name': 'Autos Soler', 'slug': 'autos'},
    {'id': '796480326889963', 'name': 'Inversiones Soler', 'slug': 'inversiones'},
]

def api(path, params=None, page_tok=None):
    params = params or {}
    params['access_token'] = page_tok or TOKEN
    qs = '&'.join(f'{k}={v}' for k, v in params.items())
    url = f'https://graph.facebook.com/{API}/{path}?{qs}'
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {'_error': f'HTTP {e.code}', '_body': e.read().decode()[:200]}
    except Exception as e:
        return {'_error': str(e)[:200]}

def save(name, data):
    (OUT / f'{name}.json').write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

# Get page tokens
accs = api('me/accounts', {'fields': 'id,name,access_token', 'limit': 100})
page_tokens = {p['id']: p.get('access_token') for p in accs.get('data', [])}

print("="*70)
print("  AUDITORIA PROFUNDA Autos Soler + Inversiones Soler")
print("="*70)

for page in PAGES:
    pid = page['id']
    pname = page['name']
    slug = page['slug']
    ptok = page_tokens.get(pid, TOKEN)
    print(f"\n\n{'='*70}\n  {pname} ({pid})\n{'='*70}")

    # === 1. Info basica completa ===
    print(f"\n[1] Info basica")
    fields = ','.join([
        'id', 'name', 'about', 'category', 'category_list',
        'fan_count', 'followers_count', 'rating_count', 'overall_star_rating',
        'phone', 'emails', 'website', 'link',
        'location', 'single_line_address', 'hours',
        'description', 'description_html', 'mission',
        'general_info', 'company_overview', 'founded',
        'parking', 'public_transit', 'price_range',
        'is_published', 'is_webhooks_subscribed',
        'can_post', 'can_checkin', 'checkins',
        'username', 'verification_status',
        'instagram_business_account{id,username,name,followers_count,media_count,biography,profile_picture_url,website}',
        'cover{source,offset_y}', 'picture{data{url,width,height}}',
        'engagement{count,social_sentence}',
        'talking_about_count',
        'page_token', 'access_token',
        'connected_instagram_account{username,id}',
        'whatsapp_number',
    ])
    d = api(pid, {'fields': fields}, page_tok=ptok)
    save(f'{slug}-01-info', d)
    if '_error' not in d:
        print(f"  Fans: {d.get('fan_count','?')}, Followers: {d.get('followers_count','?')}")
        print(f"  Rating: {d.get('overall_star_rating','?')} ({d.get('rating_count',0)} ratings)")
        print(f"  Username: @{d.get('username','?')}")
        print(f"  Phone: {d.get('phone','?')}, Email: {d.get('emails','?')}")
        print(f"  Web: {d.get('website','?')}")
        print(f"  Categoria: {d.get('category','?')}")
        if d.get('hours'):
            print(f"  Horario: {list(d['hours'].keys())[:7]}")
        ig = d.get('instagram_business_account')
        if ig:
            print(f"  IG: @{ig.get('username')} ({ig.get('followers_count','?')} followers, {ig.get('media_count','?')} posts)")
        else:
            print(f"  ❌ Sin IG vinculado")
        if d.get('is_published') is False:
            print(f"  ⚠️ Pagina NO PUBLICADA")
        if d.get('whatsapp_number'):
            print(f"  WhatsApp: {d['whatsapp_number']}")

    # === 2. Feed posts publicos ===
    print(f"\n[2] Feed posts")
    posts = api(f'{pid}/posts', {
        'fields': 'id,message,created_time,permalink_url,full_picture,attachments,shares,reactions.summary(true),comments.summary(true)',
        'limit': 25
    }, page_tok=ptok)
    save(f'{slug}-02-posts', posts)
    if 'data' in posts:
        n = len(posts['data'])
        print(f"  {n} posts publicos")
        for p in posts['data'][:5]:
            msg = (p.get('message') or '')[:80].replace('\n', ' ')
            shares = p.get('shares', {}).get('count', 0)
            likes = p.get('reactions', {}).get('summary', {}).get('total_count', 0)
            comms = p.get('comments', {}).get('summary', {}).get('total_count', 0)
            print(f"    • {p.get('created_time','?')[:10]} | {likes}❤️ {comms}💬 {shares}↗️ | {msg}")
    else:
        print(f"  Error: {posts.get('_error','?')}")

    # === 3. Photos ===
    print(f"\n[3] Photos albums")
    albums = api(f'{pid}/albums', {'fields': 'id,name,description,count,cover_photo{source}', 'limit': 20}, page_tok=ptok)
    save(f'{slug}-03-albums', albums)
    if 'data' in albums:
        print(f"  {len(albums['data'])} albums")
        for a in albums['data'][:10]:
            print(f"    • {a.get('name','?')}: {a.get('count',0)} fotos")

    # === 4. Videos ===
    print(f"\n[4] Videos")
    videos = api(f'{pid}/videos', {'fields': 'id,title,description,created_time,length,permalink_url,views', 'limit': 20}, page_tok=ptok)
    save(f'{slug}-04-videos', videos)
    if 'data' in videos:
        print(f"  {len(videos['data'])} videos")
        for v in videos['data'][:5]:
            title = v.get('title') or 'Sin titulo'
            print(f"    • {title[:60]} ({v.get('length',0):.1f}s, {v.get('views','?')} views)")

    # === 5. Events ===
    print(f"\n[5] Eventos")
    events = api(f'{pid}/events', {'fields': 'id,name,start_time,description,place', 'limit': 10}, page_tok=ptok)
    save(f'{slug}-05-events', events)
    if 'data' in events:
        print(f"  {len(events['data'])} eventos")
    else:
        print(f"  {events.get('_error','no events')}")

    # === 6. Ratings/Reviews ===
    print(f"\n[6] Ratings")
    ratings = api(f'{pid}/ratings', {'fields': 'rating,review_text,reviewer,created_time', 'limit': 20}, page_tok=ptok)
    save(f'{slug}-06-ratings', ratings)
    if 'data' in ratings:
        print(f"  {len(ratings['data'])} reviews:")
        for r in ratings['data'][:5]:
            stars = '⭐' * int(r.get('rating', 0))
            print(f"    {stars} {r.get('reviewer',{}).get('name','?')}: {(r.get('review_text','') or '')[:60]}")
    else:
        print(f"  {ratings.get('_error','no ratings')}")

    # === 7. Tabs configuradas ===
    print(f"\n[7] Tabs configuradas")
    tabs = api(f'{pid}/tabs', {'fields': 'name,application,is_permanent,position'}, page_tok=ptok)
    save(f'{slug}-07-tabs', tabs)
    if 'data' in tabs:
        print(f"  {len(tabs['data'])} tabs")
        for t in tabs['data'][:5]:
            print(f"    • {t.get('name','?')}")

    # === 8. Custom labels (engagement audience) ===
    print(f"\n[8] Custom audiences (page-level)")
    cs = api(f'{pid}/custom_labels', {}, page_tok=ptok)
    save(f'{slug}-08-custom_labels', cs)

    # === 9. Page insights ===
    print(f"\n[9] Page insights ultimo mes")
    insights = api(f'{pid}/insights', {
        'metric': 'page_impressions,page_engaged_users,page_post_engagements,page_fans,page_actions_post_reactions_total,page_views_total',
        'period': 'days_28',
    }, page_tok=ptok)
    save(f'{slug}-09-insights', insights)
    if 'data' in insights:
        for m in insights['data'][:6]:
            vals = m.get('values', [])
            if vals:
                v = vals[-1].get('value', '?')
                print(f"    • {m.get('name'):40s} = {v}")
    else:
        print(f"    {insights.get('_error','sin acceso')}")

    # === 10. Featured ===
    print(f"\n[10] Featured videos / posts")
    feat_video = api(f'{pid}/featured_videos', {}, page_tok=ptok)
    save(f'{slug}-10-featured_videos', feat_video)
    featured = api(f'{pid}', {'fields': 'featured_video,about'}, page_tok=ptok)
    save(f'{slug}-10-featured-post', featured)

print(f"\n\n{'='*70}\n  AUDIT COMPLETO\n{'='*70}")
print(f"\nOutput: {OUT}")
print(f"Total archivos: {len(list(OUT.glob('*.json')))}")
