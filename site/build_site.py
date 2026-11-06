#!/usr/bin/env python3
"""Build a static site in site/dist/ from the repository's pages and thread data.

The board, ledger, frame and plain pages are written as claude.ai artifact fragments (no doctype or head).
This wraps each in a full HTML document, rewrites links between the artifacts to relative paths,
adds a thread page from thread/thread.json and an index. Upload site/dist/ as-is to any static host.

  python3 build.py && python3 build_ledger.py   # refresh the pages from data first
  python3 site/build_site.py [--base /lens-by-level/] [--url https://wsiener.dev/lens-by-level/]

Fonts come from site/fonts/ (vendored by site/fetch_fonts.py), so no page loads anything from Google.
--url is the site's public address; with it every page gets absolute og:url and og:image for link previews.
"""
import argparse, html, json, pathlib, re, shutil
root=pathlib.Path(__file__).resolve().parent.parent
ART={'6ML12gS1wUcFp6y4kQw9dh':'ledger','GMuqxxCXsrJZ1bwKHowbPf':'board','98W62EWWBAnY8wec9iooEY':'frame','RcmP9swReSNY9VUbhkKW6p':'plain'}
PAGES=[('ledger','ledger.html'),('board','lens-by-level.html'),('frame','frame.html'),('plain','plain.html')]
TITLE={'':'Lens by Level','ledger':'The ledger · Lens by Level','board':'The full board · Lens by Level','frame':'The frame · Lens by Level',
       'plain':'Lens by Level, in plain words','thread':'The thread · Lens by Level'}
DESC={'':'Seven ways of looking at a language model, graded by evidence across four levels of description, with every source and every correction on the record.',
      'ledger':'The board: seven lenses by four levels, 28 cells. Open any cell for its sources, its grade and its history.',
      'board':'Every cell of the Lens by Level board at full length, with its sources.',
      'frame':'What the Lens by Level board is a picture of, the experiments that would settle its open cells, and how it was made.',
      'plain':'Why talking about AI is so hard: "it" can mean the trained model, one conversation, one reply or one step. The short version, no jargon.',
      'thread':'The Lens by Level thread as posted on X, with its images.'}
FONTS=re.compile(r'<link[^>]*href="https://fonts\.googleapis\.com/[^"]*"[^>]*>')
esc=lambda s: html.escape(s or '',quote=True)
def wrap(fragment, slug, url=''):
    up='../' if slug else ''
    fragment=FONTS.sub(f'<link rel="stylesheet" href="{up}fonts/fonts.css">',fragment)
    fragment=re.sub(r'<title>[^<]*</title>',f'<title>{esc(TITLE[slug])}</title>',fragment,count=1)
    meta=(f'<meta name="description" content="{esc(DESC[slug])}">\n<meta property="og:type" content="article">\n'
          f'<meta property="og:site_name" content="Lens by Level">\n<meta property="og:title" content="{esc(TITLE[slug])}">\n'
          f'<meta property="og:description" content="{esc(DESC[slug])}">\n<meta name="twitter:card" content="summary_large_image">\n')
    if url:
        meta+=(f'<link rel="canonical" href="{esc(url+(slug+"/" if slug else ""))}">\n<meta property="og:url" content="{esc(url+(slug+"/" if slug else ""))}">\n'
               f'<meta property="og:image" content="{esc(url)}og.png">\n<meta property="og:image:width" content="1600">\n<meta property="og:image:height" content="900">\n'
               '<meta property="og:image:alt" content="Two claims about AI, and the four things the word it can mean">\n')
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            +meta+'<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n'+fragment+'\n</body>\n</html>\n')
def relink(s):
    for aid,slug in ART.items():
        s=s.replace(f'https://claude.ai/artifact/{aid}',f'../{slug}/')
    return s
NAV=[('','Lens by Level'),('ledger','Ledger'),('plain','In plain words'),('frame','Frame'),('thread','Thread'),('board','Full board')]
def navbar(slug):
    """A thin bar over the artifact pages, which were written to stand alone and link nowhere else on the site."""
    items=''.join(f'<b aria-current="page">{t}</b>' if s==slug else f'<a href="../{s+"/" if s else ""}">{t}</a>' for s,t in NAV)
    return ('<nav class="lbl-nav" aria-label="Lens by Level">'+items+'</nav>\n'
            '<style>.lbl-nav{display:flex;flex-wrap:wrap;justify-content:center;gap:4px 18px;margin:0 0 22px;padding:0 0 12px;border-bottom:1px solid rgba(128,128,128,.25);'
            'font:500 13px/1.5 "IBM Plex Sans",system-ui,sans-serif}.lbl-nav a{color:inherit;opacity:.7;text-decoration:none}'
            '.lbl-nav a:hover{opacity:1;text-decoration:underline}.lbl-nav b{font-weight:600}</style>\n')
def thread_page(d):
    posts=''.join(
        f'<article class="p" id="p{p["n"]}"><div class="m"><span>{p["n"]}/{len(d["posts"])}</span>'
        + (f'<a href="{esc(p["url"])}">on X</a>' if p.get('url') else '')
        + '</div>'
        + ''.join(f'<p>{esc(line)}</p>' if line else '' for line in p['text'].split('\n'))
        + (f'<img src="img/{esc(p["image"])}" alt="image for post {p["n"]}" loading="lazy">' if p.get('image') else '')
        + (('<div class="mt">'+' · '.join(f'{esc(k.replace("_count",""))} {v:,}' for k,v in p['metrics'].items())+'</div>') if p.get('metrics') else '')
        + '</article>' for p in d['posts'])
    reps=''.join(f'<li><b>{esc(r.get("author"))}</b> {esc(r.get("text"))}'+(f' <a href="{esc(r["url"])}">link</a>' if r.get('url') else '')+'</li>' for r in d.get('replies',[]))
    root_link=f'<a href="{esc(d["root_url"])}">the thread on X</a>' if d.get('root_url') else 'posted on X'
    return f'''<title>The Thread · Lens by Level</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root{{--bg:#0e1320;--sf:#141b2b;--ink:#eef2f8;--ink2:#b4bdcc;--ink3:#7e889b;--hair:#212a3b;--acc:#ffb54d;color-scheme:dark}}
body{{background:var(--bg);color:var(--ink);font-family:"Hanken Grotesk",system-ui,sans-serif;font-size:17px;line-height:1.55;padding:32px max(16px,env(safe-area-inset-left,0px)) 64px max(16px,env(safe-area-inset-right,0px))}}
.w{{max-width:760px;margin:0 auto}} h1{{font-size:28px;margin:0 0 6px}} .lede{{color:var(--ink2);margin:0 0 28px}}
nav{{font-size:14px;margin:0 0 24px;display:flex;gap:16px;flex-wrap:wrap}} a{{color:var(--acc)}}
.p{{background:var(--sf);border:1px solid var(--hair);border-radius:12px;padding:18px 20px;margin:0 0 16px}}
.p p{{margin:0 0 10px;white-space:pre-wrap}} .p img{{display:block;border-radius:8px;margin-top:8px;border:1px solid var(--hair)}}
.m{{font-family:"JetBrains Mono",monospace;font-size:12px;color:var(--ink3);display:flex;justify-content:space-between;margin:0 0 10px}}
.mt{{font-family:"JetBrains Mono",monospace;font-size:12px;color:var(--ink3);margin-top:10px}}
h2{{font-size:18px;margin:32px 0 10px}} ul{{padding-left:18px;color:var(--ink2)}}
</style>
<div class="w"><nav><a href="../">Lens by Level</a><a href="../ledger/">Ledger</a><a href="../frame/">Frame</a><a href="../plain/">Plain</a><a href="../board/">Full board</a></nav>
<h1>The thread</h1><p class="lede">{esc(d.get("author"))}, {esc((d.get("posted_local") or "")[:10])}, {root_link}. {len(d["posts"])} posts.</p>
{posts}{('<h2>Replies</h2><ul>'+reps+'</ul>') if reps else ''}</div>'''
def index_page():
    return '''<title>Lens by Level</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root{--bg:#0e1320;--sf:#141b2b;--ink:#eef2f8;--ink2:#b4bdcc;--ink3:#7e889b;--hair:#212a3b;--acc:#ffb54d;color-scheme:dark}
body{background:var(--bg);color:var(--ink);font-family:"Hanken Grotesk",system-ui,sans-serif;font-size:17px;line-height:1.55;padding:48px max(16px,env(safe-area-inset-left,0px)) 64px max(16px,env(safe-area-inset-right,0px))}
.w{max-width:760px;margin:0 auto} h1{font-size:34px;line-height:1.15;margin:0 0 10px} .lede{color:var(--ink2);margin:0 0 30px;font-size:19px}
.g{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px} a.c{display:block;background:var(--sf);border:1px solid var(--hair);border-radius:12px;padding:16px 18px;color:var(--ink);text-decoration:none}
a.c b{display:block;font-size:18px;margin-bottom:4px} a.c span{color:var(--ink2);font-size:15px} a.c:hover{border-color:var(--acc)} .f{font-family:"JetBrains Mono",monospace;font-size:12px;color:var(--ink3);margin-top:36px} .f a{color:var(--acc)}
img{display:block;border-radius:10px;margin:0 0 28px;border:1px solid var(--hair)}
</style>
<div class="w"><h1>Lens by Level</h1><p class="lede">Seven ways of looking at a language model, graded by evidence across four levels of description, with every source and every correction on the record.</p>
<img src="thread/img/post-1.png" alt="Two claims about AI, and the four things the word it can mean">
<div class="g">
<a class="c" href="ledger/"><b>The ledger</b><span>The board. Click any cell for its sources, grade and history.</span></a>
<a class="c" href="plain/"><b>In plain words</b><span>The short version, no jargon.</span></a>
<a class="c" href="frame/"><b>The frame</b><span>What the board is a picture of, and how it was made.</span></a>
<a class="c" href="thread/"><b>The thread</b><span>As posted on X, with its images.</span></a>
<a class="c" href="board/"><b>Full board</b><span>Every cell at full length.</span></a>
</div><p class="f">Wolfram Siener with Claude (Fable 5.1, Opus 5.5) · external audit by GPT-6 Astra · November 2026<br>
<a href="https://github.com/wolframs/lens-by-level">Data, sources and audit trail</a> · <a href="https://wsiener.dev/">wsiener.dev</a></p></div>'''
def main():
    a=argparse.ArgumentParser(); a.add_argument('--base',default=''); a.add_argument('--url',default=''); o=a.parse_args()
    if o.url and not o.url.endswith('/'): o.url+='/'
    dist=root/'site'/'dist'
    if dist.exists(): shutil.rmtree(dist)
    for slug,f in PAGES:
        (dist/slug).mkdir(parents=True); (dist/slug/'index.html').write_text(wrap(navbar(slug)+relink((root/f).read_text()),slug,o.url))
    d=json.load(open(root/'thread'/'thread.json'))
    (dist/'thread'/'img').mkdir(parents=True)
    for p in d['posts']:
        if p.get('image'): shutil.copy(root/'share'/p['image'],dist/'thread'/'img'/p['image'])
    (dist/'thread'/'index.html').write_text(wrap(thread_page(d),'thread',o.url))
    (dist/'index.html').write_text(wrap(index_page(),'',o.url))
    shutil.copytree(root/'site'/'fonts',dist/'fonts'); shutil.copy(root/'share'/'post-1.png',dist/'og.png')
    if o.base:
        for f in dist.rglob('index.html'):
            s=f.read_text(); f.write_text(s.replace('<head>\n',f'<head>\n<base href="{o.base}{f.parent.relative_to(dist).as_posix()+"/" if f.parent!=dist else ""}">\n',1))
    left=[str(f.relative_to(dist)) for f in dist.rglob('*.html') if ('claude.ai/artifact' in f.read_text() or 'fonts.googleapis' in f.read_text()) and 'thread' not in f.parts]
    print('built',dist,'·',sum(1 for _ in dist.rglob('*') if _.is_file()),'files','· remaining artifact or Google Fonts links:',left or 'none')
if __name__=='__main__': main()
