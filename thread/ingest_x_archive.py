#!/usr/bin/env python3
"""Fill thread/thread.json from your X data export.

Usage:
  python3 thread/ingest_x_archive.py PATH_TO_ARCHIVE --root TWEET_ID [--extra extra.json]

PATH_TO_ARCHIVE is the unzipped export folder, the .zip itself, or the data/tweets.js file.
--root is the id of the thread's first post (the number at the end of its URL).

What it does:
  - reads data/tweets.js (and tweets-part1.js, ... if present), which X writes as
    `window.YTD.tweets.part0 = [ ... ]`
  - follows your own replies from the root: each next post is your tweet whose
    in_reply_to_status_id is the previous post's id
  - writes id, url, created_at, full_text and the counts the export carries
    (favorite_count, retweet_count) onto the posts in thread.json, matched by order;
    the transcribed text is kept as `text_transcribed` when it differs
  - --extra merges a hand-made JSON file with keys "replies", "quotes" or per-post
    "metrics" (views, bookmarks, replies), since the export does not contain other
    people's replies or view counts
Nothing is fetched from the network.
"""
import argparse, json, pathlib, re, sys, zipfile
HERE=pathlib.Path(__file__).parent
def load_js(text):
    return json.loads(text[text.index('['):])
def read_tweets(path):
    p=pathlib.Path(path); out=[]
    if p.suffix=='.zip':
        with zipfile.ZipFile(p) as z:
            for n in z.namelist():
                if re.search(r'(^|/)data/tweets(-part\d+)?\.js$',n): out+=load_js(z.read(n).decode('utf-8'))
    elif p.is_file(): out=load_js(p.read_text('utf-8'))
    else:
        for f in sorted((p/'data').glob('tweets*.js')): out+=load_js(f.read_text('utf-8'))
    if not out: sys.exit(f'no tweets found in {path}')
    return [t.get('tweet',t) for t in out]
def main():
    a=argparse.ArgumentParser(); a.add_argument('archive'); a.add_argument('--root',required=True); a.add_argument('--extra'); a.add_argument('--out',default=str(HERE/'thread.json'))
    o=a.parse_args()
    tw=read_tweets(o.archive); by={t['id_str']:t for t in tw}
    if o.root not in by: sys.exit(f'root {o.root} not in archive ({len(tw)} tweets read)')
    kids={}
    for t in tw:
        r=t.get('in_reply_to_status_id_str')
        if r: kids.setdefault(r,[]).append(t)
    chain=[by[o.root]]
    while True:
        nxt=[k for k in kids.get(chain[-1]['id_str'],[]) if k.get('in_reply_to_user_id_str')==by[o.root].get('user_id_str',k.get('in_reply_to_user_id_str'))]
        if not nxt: break
        chain.append(sorted(nxt,key=lambda k:k['id_str'])[0])
    d=json.load(open(o.out)); handle=d.get('author','').lstrip('@') or 'i'
    if len(chain)!=len(d['posts']): print(f'note: archive chain has {len(chain)} posts, thread.json has {len(d["posts"])}; matching by order',file=sys.stderr)
    for post,t in zip(d['posts'],chain):
        text=t.get('full_text',t.get('text',''))
        if post.get('text') and post['text']!=text: post['text_transcribed']=post['text']
        post.update(id=t['id_str'],url=f'https://x.com/{handle}/status/{t["id_str"]}',created_at=t.get('created_at'),text=text)
        post['metrics'].update({k:int(t[k]) for k in ('favorite_count','retweet_count') if k in t})
    d['root_id']=chain[0]['id_str']; d['root_url']=d['posts'][0]['url']; d['source']='X data export, ingested by thread/ingest_x_archive.py'
    if o.extra:
        e=json.load(open(o.extra))
        d['replies']+=e.get('replies',[]); d['quotes']+=e.get('quotes',[])
        for n,m in (e.get('metrics') or {}).items():
            for post in d['posts']:
                if str(post['n'])==str(n): post['metrics'].update(m)
    json.dump(d,open(o.out,'w'),ensure_ascii=False,indent=1); print(f'wrote {o.out}: {len(chain)} posts from the archive')
if __name__=='__main__': main()
