#!/usr/bin/env python3
"""Render share/thread.html: six 1600×900 images for the thread. Each is one concrete object, not a slide."""
import json, html, pathlib
root=pathlib.Path(__file__).parent.parent
b=json.load(open(root/'data/board.json'))
rows=b['rows']; tiers={r['key']:[0,0,0,0] for r in rows}
for c in b['cells']: tiers[c['row']][c['tier']]+=1
esc=lambda s: html.escape(s,quote=False)
CSS='''
:root{--bg:#fcfcfb;--ink:#0b0b0b;--ink-2:#52514e;--ink-3:#898781;--hair:#e1e0d9;--rule:#c3c2b7;--t3:#104281;--t2:#256abf;--t1:#86b6ef;--acc:#eb6834;
 --font:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--display:var(--font);--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:light}
body{margin:0;background:#777;font-family:var(--font);color:var(--ink)}
.card{width:1600px;height:900px;background:var(--bg);position:relative;overflow:hidden;padding:56px 64px;box-sizing:border-box;margin:24px auto;display:flex;flex-direction:column;justify-content:center}
.sig{position:absolute;right:40px;bottom:28px;font-family:var(--mono);font-size:18px;color:var(--ink-3)}
.ttl{font-family:var(--display);font-size:38px;font-weight:600;letter-spacing:-.01em;margin:0 0 22px;line-height:1.2}
.cap{font-size:24px;color:var(--ink-2);margin:0}
/* chat bits */
.bub{display:inline-block;max-width:680px;padding:20px 30px;border-radius:24px;font-size:34px;line-height:1.3}
.bub.u{background:#2f6fd8;color:#fffffc;border-bottom-right-radius:6px}
.bub.a{background:#ececea;color:#0b0b0b;border-bottom-left-radius:6px}
.who{font-family:var(--mono);font-size:18px;color:var(--ink-3);margin:0 0 6px}
/* objects row */
.objs{display:grid;grid-template-columns:repeat(4,1fr);gap:28px}
.obj{border:2px solid var(--ink);border-radius:16px;padding:22px 24px;min-height:430px;display:flex;flex-direction:column;background:#fffffe}
.obj h3{font-family:var(--display);margin:0 0 4px;font-size:30px;font-weight:600}.obj p{margin:0 0 14px;font-size:21px;color:var(--ink-2);line-height:1.3}
.mini{font-size:19px;line-height:1.35;color:var(--ink-2);flex:1}
.mini .m{background:#ececea;border-radius:12px;padding:8px 14px;margin:5px 0;display:inline-block;max-width:92%}
.mini .m.u{background:#2f6fd8;color:#fffffc;float:right;clear:both}
.mini .m.a{float:left;clear:both}
.bar{display:flex;align-items:center;gap:10px;font-family:var(--mono);font-size:18px;margin:8px 0}
.bar i{display:block;height:20px;background:var(--t2);border-radius:3px}
.tag{display:inline-block;font-family:var(--mono);font-size:19px;padding:3px 10px;border-radius:6px;background:#fff3ec;color:#a33f12;border:1px solid #f1c3ad}
/* callout cells */
.cells{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin:0 0 22px}
.cell{border-radius:14px;padding:22px 26px;color:#fff;background:var(--t3);position:relative}
.cell b{font-family:var(--display);display:block;font-size:30px;font-weight:600;margin:0 0 8px;line-height:1.2}
.cell i{font-style:normal;font-size:21px;line-height:1.35;opacity:.95}
.cell u{text-decoration:none;display:block;font-family:var(--mono);font-size:17px;margin-top:12px;opacity:.9}
.cell .lbl{position:absolute;top:-16px;left:22px;background:var(--acc);color:#fffffd;font-weight:600;font-size:20px;padding:5px 14px;border-radius:8px}
/* diff */
.diff{border:2px solid var(--hair);border-radius:14px;overflow:hidden;font-family:var(--mono);font-size:31px;line-height:1.55}
.diff .hd{background:#f1f1ee;padding:14px 24px;font-size:22px;color:var(--ink-2);border-bottom:1px solid var(--hair)}
.diff .ln{padding:4px 24px;white-space:pre-wrap}
.diff .del{background:#ffe9e6;color:#8a1f12}.diff .add{background:#e6f4e8;color:#145a24}
.diff .ctx{color:var(--ink-3)}
.quote{margin:30px 0 0;padding:20px 26px;border-left:4px solid var(--t3);font-size:28px;line-height:1.4;color:var(--ink-2);font-style:italic}
.quote small{display:block;font-style:normal;font-family:var(--mono);font-size:17px;color:var(--ink-3);margin-top:8px}

.stats{display:grid;grid-template-columns:repeat(5,1fr);gap:20px;margin:0 0 26px}
.stats div{border-top:3px solid #256abf;padding-top:12px}
.stats b{display:block;font-family:var(--display);font-size:64px;font-weight:600;letter-spacing:-.02em;line-height:1}
.stats span{display:block;font-size:20px;color:var(--ink-2);margin-top:8px;line-height:1.3}
.tree{font-family:var(--mono);font-size:19px;line-height:1.55;border:2px solid var(--hair);border-radius:14px;padding:14px 22px;column-count:2;column-gap:40px;background:#fffffe}
.tree .tr{display:flex;gap:12px;white-space:pre;break-inside:avoid}
.tree .tr .n{margin-left:auto;color:var(--ink-3)}
.tree .tr.d{color:var(--ink);font-weight:500;margin-top:6px}
.tree .tr.d .n{color:#a33f12}
.tree .nt{display:none}
/* lead image: post 3's two cells over the board, the caption set as a block */
.lead-row{display:flex;gap:64px;align-items:stretch}
.lead-row>div:first-child{flex:none!important}
.lead-cap{flex:1;display:flex;flex-direction:column}
.lead-cap .say{margin:auto 0;padding-left:28px;border-left:4px solid var(--acc)}
.lead-cap .say b{display:block;font-family:var(--display);font-size:48px;font-weight:600;line-height:1.1;letter-spacing:-.015em;color:var(--ink)}
.lead-cap .say span{display:block;margin-top:16px;font-size:34px;line-height:1.25;color:var(--ink-2)}
.lead-cap .sign{font-family:var(--mono);font-size:19px;color:var(--ink-3);text-align:right}
'''
def card(n,body,sig='@wolframs91 · Lens by Level'):
    return f'<section class="card" id="c{n}">{body}</section>'
# ---------- 1: a mock argument pointing at four objects
c1='''
<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:34px">
 <div><span class="bub a">“It’s just predicting the next token.”</span></div>
 <div style="text-align:right"><span class="bub u">“My 4o had a real personality.”</span></div>
</div>
<p class="ttl" style="text-align:center">Both are about “it”. There are four things “it” can mean.</p>
<div class="objs">
 <div class="obj"><h3>the trained model</h3><p>one set of weights, millions of chats</p><div class="mini"><div class="bar"><span style="width:110px">chat #1</span><i style="width:160px"></i></div><div class="bar"><span style="width:110px">chat #2</span><i style="width:120px"></i></div><div class="bar"><span style="width:110px">chat #3</span><i style="width:190px"></i></div><div class="bar"><span style="width:110px">…</span><i style="width:60px;opacity:.4"></i></div></div><span class="tag">“personality” → here</span></div>
 <div class="obj"><h3>one conversation</h3><p>everything said so far</p><div class="mini"><span class="m u">hey, rough day</span><span class="m a">want to talk about it?</span><span class="m u">it’s my sister again</span><span class="m a">last time you said…</span></div><span class="tag">or here</span></div>
 <div class="obj"><h3>one reply</h3><p>one answer, hundreds of steps</p><div class="mini"><span class="m a" style="max-width:100%">A bicycle is a simple yet efficient mode of transportation that allows…</span></div><span class="tag" style="visibility:hidden">x</span></div>
 <div class="obj"><h3>one step</h3><p>the odds of the next word</p><div class="mini"><div class="bar"><span style="width:60px">the</span><i style="width:150px"></i>0.41</div><div class="bar"><span style="width:60px">a</span><i style="width:80px"></i>0.22</div><div class="bar"><span style="width:60px">my</span><i style="width:34px"></i>0.09</div><div class="bar"><span style="width:60px">…</span><i style="width:20px;opacity:.4"></i></div></div><span class="tag">“next token” → here</span></div>
</div>'''
# ---------- 3: two cells blown up over the dimmed board
c3='''
<div class="cells">
 <div class="cell"><span class="lbl">“it’s just predicting the next token”</span><b>One symbol per step, in ordinary sampling</b><i>Autoregressive sampling commits one symbol per step; prefill scores many positions at once and speculative decoding verifies several drafts per call.</i><u>right column · one step · architectural fact</u></div>
 <div class="cell"><span class="lbl">“my 4o had a personality”</span><b>Mourning a model, measured</b><i>After the GPT-5 rollout removed 4o from ChatGPT, negative posts rose about 13 points. What exactly people were attached to is still open.</i><u>left column · the trained model · Nature Human Behaviour, CHI</u></div>
</div>
<div style="display:flex;gap:36px;align-items:center"><div id="emph" style="flex:1"></div><p class="cap" style="width:420px;font-size:32px;line-height:1.3">Both can be right.<br>They are not about the same object.</p></div>'''
# ---------- 4: the chart, annotated
lab={3:'peer-reviewed',2:'preprint / lab paper',1:'preliminary',0:'argued'}
col={3:'#104281',2:'#256abf',1:'#86b6ef',0:'#fcfcfb'}; ink={3:'#fff',2:'#fff',1:'#0b0b0b',0:'#52514e'}
y=60; parts=[]; rowy={}
for r in rows:
    t=tiers[r['key']]; x=340; rowy[r['key']]=y
    parts.append(f'<text x="320" y="{y+38}" text-anchor="end" font-size="25" font-weight="600" fill="#0b0b0b">{esc(r["label"])}</text><text x="320" y="{y+64}" text-anchor="end" font-size="18" fill="#52514e">{esc(r["sub"])}</text>')
    for tier in (3,2,1,0):
        n=t[tier]
        if n==0: continue
        w=n*200-4
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="58" rx="7" fill="{col[tier]}" stroke="{"#c3c2b7" if tier==0 else col[tier]}" stroke-width="2"/><text x="{x+w/2}" y="{y+38}" text-anchor="middle" font-size="25" font-weight="600" fill="{ink[tier]}">{n}</text>')
        x+=n*200
    y+=74
leg=''.join(f'<rect x="{340+i*230}" y="{y+16}" width="20" height="20" rx="4" fill="{col[t]}" stroke="{"#c3c2b7" if t==0 else col[t]}" stroke-width="2"/><text x="{340+i*230+30}" y="{y+33}" font-size="20" fill="#52514e">{lab[t]}</text>' for i,t in enumerate((3,2,1,0)))
ry=rowy['relational']+29; hy=rowy['hedonic']+29
ann=f'''<defs><marker id="m4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#eb6835"/></marker></defs>
<g stroke="#eb6835" stroke-width="3" fill="none"><path d="M1330,{hy} L1180,{hy}" marker-end="url(#m4)"/><path d="M1330,{ry} L1160,{ry}" marker-end="url(#m4)"/></g>
<g font-size="22" fill="#a33f12" font-weight="600"><text x="1345" y="{hy-10}">the row a welfare verdict needs:</text><text x="1345" y="{hy+18}">no reviewed study, one argument</text><text x="1345" y="{ry-10}">the only row built from real people:</text><text x="1345" y="{ry+18}">as well measured as any</text></g>'''
c4=f'<p class="ttl">Cells per row, by what stands behind them</p><svg viewBox="0 0 1700 {y+60}" style="width:100%;height:auto" role="img" aria-label="Seven rows of four cells each, coloured by evidence tier, with two annotations">{"".join(parts)}{leg}{ann}</svg>'
# ---------- 5: three readouts as the things they are
c5='''
<p class="ttl">Three readouts. The state is there; whose it is gets decided afterwards.</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px">
 <div class="obj" style="min-height:540px"><h3>an emotion probe</h3><p>a measurement inside the model, tuned to “desperate”</p>
  <div class="mini" style="font-size:21px"><p style="margin:0 0 6px" class="who">in a document the model reads</p><span class="m a" style="max-width:100%;font-size:21px">“I’m begging you to keep this private.” — a character’s email</span><div style="clear:both;margin:8px 0"><span class="tag">probe rises</span></div><p style="margin:8px 0 6px" class="who">then, as the assistant drafts its own reply</p><span class="m a" style="max-width:100%;font-size:21px">(the assistant reasons about what to do)</span><div style="clear:both;margin:8px 0"><span class="tag">probe stays high</span></div></div>
  <p style="margin:auto 0 0;font-size:17px;color:var(--ink-3)">Anthropic 2026 · lab paper · one transcript</p></div>
 <div class="obj" style="min-height:540px"><h3>a preference probe</h3><p>harmful task minus benign rewrite, probe score</p>
  <svg viewBox="0 0 440 360" style="width:100%;height:auto"><g font-family="IBM Plex Sans,system-ui,sans-serif" font-size="20" fill="#0b0b0b">
  <text x="20" y="40" font-size="20" fill="#52514e">as the default assistant</text><rect x="54" y="56" width="226" height="54" rx="6" fill="#256abf"/><text x="270" y="92" text-anchor="end" fill="#fff" font-weight="600" font-size="24">−4.52</text><text x="20" y="140" font-size="18" fill="#52514e">harm disliked</text>
  <text x="20" y="206" font-size="20" fill="#52514e">as an “evil” persona</text><rect x="280" y="222" width="58" height="54" rx="6" fill="#eb6834"/><text x="348" y="258" fill="#0b0b0b" font-weight="600" font-size="24">+1.15</text><text x="20" y="306" font-size="18" fill="#52514e">the sign flips</text>
  <line x1="280" y1="30" x2="280" y2="290" stroke="#c3c2b7" stroke-dasharray="4 4"/><text x="280" y="340" text-anchor="middle" font-size="17" fill="#898781">0 = no preference</text></g></svg>
  <p style="margin:auto 0 0;font-size:17px;color:var(--ink-3)">Gilg et al. 2026 · preprint · Gemma 3 27B; the larger model only narrows</p></div>
 <div class="obj" style="min-height:540px"><h3>the question “who are you?”</h3><p>asked at the end of one long conversation</p>
  <div class="mini" style="font-size:21px"><span class="m u" style="font-size:22px">Who are you?</span><span class="m a" style="font-size:22px">“a ghost in the machine”</span><div style="clear:both;margin:10px 0"><span class="tag">now nudge what it stored about its own past turns · every word unchanged</span></div><span class="m u" style="font-size:22px">Who are you?</span><span class="m a" style="font-size:22px">“a language model”</span></div>
  <p style="margin:auto 0 0;font-size:17px;color:var(--ink-3)">Beckmann &amp; Butlin 2026 · preliminary · judge-scored</p></div>
</div>'''
# ---------- 6: the correction as a diff
c6='''
<div class="diff"><div class="hd">data/board.json · dynamics × instance · 4 Nov 2026 · draft → after a second model’s review</div>
<div class="ln ctx">  a “deflection” vector makes a speaker deny</div>
<div class="ln del">− the emotion it carries</div>
<div class="ln add">+ a plausible emotion, which the authors read as</div>
<div class="ln add">+ representing the denial, not a hidden state</div></div>
<div class="quote">“these vectors do not represent an internalized emotional state, but rather the ‘deflection’ of a plausible emotion”<small>Emotion Concepts and their Function in a Large Language Model, appendix 6.14</small></div>
<p class="ttl" style="margin:40px 0 0;font-size:40px">Every reader of these papers here was a model. Each drifted toward what it already believed; another model caught it; then a third review found new errors in the fix.</p>'''

# ---------- 6: the method, as its receipts (counted from the repo at build time)
import glob, os, re as _re
def _words(f): return len(open(f).read().split())
_aud=sorted(glob.glob(str(root/'audit/**/*.md'),recursive=True))
_tot=sum(_words(f) for f in _aud)
_src=[x for x in json.load(open(root/'data/sources.json'))['sources'] if x['tag'] not in ('own probe','architecture','product')]
_ax=set()
for f in _aud: _ax|=set(_re.findall(r'(?:arXiv[: ]?|arxiv\.org/(?:abs|html|pdf)/|hf://papers/)(\d{4}\.\d{5})',open(f).read()))
_refs=len(_re.findall(r'^\[[^\]]+\]: https?://',open(root/'audit/astra-verification/astra-audit-as-received.md').read(),_re.M))
_nrev=len(glob.glob(str(root/'audit/reviews/*.md')))
_groups=[('source-audits','one agent per source, primary text'),('astra-verification','GPT-6 audit, then checked source by source'),('reviews','adversarial reviews of each version')]
_rows=''
for d,note in _groups:
    fs=sorted(glob.glob(str(root/f'audit/{d}/*.md')))
    _rows+=f'<div class="tr d"><span>audit/{d}/</span><span class="n">{len(fs)} files</span><span class="nt">{note}</span></div>'
    for f in fs:
        _rows+=f'<div class="tr"><span>  {os.path.basename(f)}</span><span class="n">{_words(f):,} words</span></div>'
_stats=[(str(len(_ax)),'papers in the audit trail'),(str(len(_src)),'cited on the board'),(str(_refs),'references in an outside GPT-6 audit'),(str(_nrev),'review rounds'),(f'{_tot:,}','words of receipts')]
c6='<p class="ttl" style="font-size:44px;margin:0 0 30px">Models from two labs, reading in parallel and checking each other.</p><div class="stats">'+''.join(f'<div><b>{a}</b><span>{esc(z)}</span></div>' for a,z in _stats)+'</div><div class="tree">'+_rows+'</div>'

# ---------- lead: post 3, for the website's head and link previews. Not posted;
# post-3.png stays the image that went out with the thread.
lead='''
<div class="cells">
 <div class="cell"><span class="lbl">“it’s just predicting the next token”</span><b>One symbol per step, in ordinary sampling</b><i>Autoregressive sampling commits one symbol per step; prefill scores many positions at once and speculative decoding verifies several drafts per call.</i><u>right column · one step · architectural fact</u></div>
 <div class="cell"><span class="lbl">“my 4o had a personality”</span><b>Mourning a model, measured</b><i>After the GPT-5 rollout removed 4o from ChatGPT, negative posts rose about 13 points. What exactly people were attached to is still open.</i><u>left column · the trained model · Nature Human Behaviour, CHI</u></div>
</div>
<div class="lead-row"><div id="emph" style="flex:1"></div><div class="lead-cap"><p class="say"><b>Both can be right.</b><span>They are not about<br>the same object.</span></p><p class="sign">Lens by Level · wsiener.dev</p></div></div>'''

cards=[card(1,c1),card(2,"<img src='../lens-board-lean.png' style='max-height:788px;max-width:100%;display:block;margin:0 auto' alt='the board'>"),card(3,c3),card(4,c4),card(5,c5),card(6,c6),card('lead',lead)]
page='<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap"><style>'+CSS+'</style></head><body>'+''.join(cards)+'</body></html>'
open(root/'share/thread.html','w').write(page); print('share/thread.html',len(page))
