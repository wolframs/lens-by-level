#!/usr/bin/env python3
"""Render share/thread.html: six 1600×900 cards for the thread, from the board data where a card shows data."""
import json, html, pathlib
root=pathlib.Path(__file__).parent.parent
b=json.load(open(root/'data/board.json'))
rows=b['rows']; tiers={}
for r in rows: tiers[r['key']]=[0,0,0,0]
for c in b['cells']: tiers[c['row']][c['tier']]+=1
esc=lambda s: html.escape(s,quote=False)
CSS='''
:root{--bg:#f9f9f7;--surface:#fcfcfb;--ink:#0b0b0b;--ink-2:#52514e;--ink-3:#898781;--hair:#e1e0d9;--rule:#c3c2b7;--t3:#104281;--t2:#256abf;--t1:#86b6ef;--accent:#eb6834;
 --font:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:light}
body{margin:0;background:#888;font-family:var(--font);color:var(--ink)}
.card{width:1600px;height:900px;background:var(--bg);position:relative;overflow:hidden;padding:64px 80px 56px;box-sizing:border-box;margin:24px auto;display:flex;flex-direction:column}
.eye{font-family:var(--mono);font-size:20px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);margin:0 0 18px}
h1{font-size:54px;font-weight:600;line-height:1.12;letter-spacing:-.015em;margin:0 0 14px;text-wrap:balance;max-width:22ch}
.sub{font-size:27px;color:var(--ink-2);margin:0 0 22px;max-width:48ch;line-height:1.4}
.foot{position:absolute;left:80px;right:80px;bottom:40px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:19px;color:var(--ink-3)}
.fig{flex:1;display:flex;align-items:center;justify-content:center;min-height:0}
svg{width:100%;height:100%;max-height:560px}
text{font-family:var(--font)}
.mono{font-family:var(--mono)}
'''
def card(n,eye,h1,sub,body):
    return f'<section class="card" id="c{n}"><p class="eye">{esc(eye)}</p><h1>{h1}</h1>{("<p class=sub>"+sub+"</p>") if sub else ""}<div class="fig">{body}</div><div class="foot"><span>Lens by Level · {n}/6</span><span>@wolframs91 · with Claude</span></div></section>'
# --- card 1: one sentence, four objects
c1='''<svg viewBox="0 0 1440 560" role="img" aria-label="One sentence fans out into four objects: a checkpoint, a conversation, a reply, a forward pass">
<defs><marker id="a1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#52514e"/></marker></defs>
<g font-size="26" fill="#0b0b0b">
<rect x="20" y="230" width="360" height="100" rx="12" fill="#fcfcfb" stroke="#c3c2b7" stroke-width="2"/>
<text x="200" y="272" text-anchor="middle" font-size="30" font-weight="600">“Does it want anything?”</text><text x="200" y="306" text-anchor="middle" font-size="22" fill="#52514e">one sentence</text>
<g stroke="#52514e" stroke-width="2.5" fill="none">
<path d="M380,280 C560,280 560,80 740,80" marker-end="url(#a1)"/><path d="M380,280 C560,280 560,213 740,213" marker-end="url(#a1)"/><path d="M380,280 C560,280 560,346 740,346" marker-end="url(#a1)"/><path d="M380,280 C560,280 560,480 740,480" marker-end="url(#a1)"/>
</g>
<g font-weight="600" font-size="28">
<rect x="750" y="44" width="670" height="74" rx="12" fill="#104281"/><text x="775" y="90" fill="#fff">the checkpoint</text><text x="1395" y="90" fill="#fff" text-anchor="end" font-weight="400" font-size="22">trained once, runs millions of chats</text>
<rect x="750" y="177" width="670" height="74" rx="12" fill="#256abf"/><text x="775" y="223" fill="#fff">one conversation</text><text x="1395" y="223" fill="#fff" text-anchor="end" font-weight="400" font-size="22">a context it has been pulled around in</text>
<rect x="750" y="310" width="670" height="74" rx="12" fill="#86b6ef"/><text x="775" y="356" fill="#0b0b0b">one reply</text><text x="1395" y="356" fill="#0b0b0b" text-anchor="end" font-weight="400" font-size="22">what this turn was conditioned to do</text>
<rect x="750" y="444" width="670" height="74" rx="12" fill="#fcfcfb" stroke="#c3c2b7" stroke-width="2"/><text x="775" y="490" fill="#0b0b0b">one forward pass</text><text x="1395" y="490" fill="#52514e" text-anchor="end" font-weight="400" font-size="22">a distribution over the next symbol</text>
</g>
<text x="200" y="420" text-anchor="middle" font-size="22" fill="#52514e">four different questions,</text><text x="200" y="450" text-anchor="middle" font-size="22" fill="#52514e">four different answers</text>
</g></svg>'''
# --- card 4: evidence by row
order=[r for r in rows]
lab={3:'peer-reviewed',2:'preprint / lab paper',1:'preliminary',0:'argued'}
col={3:'#104281',2:'#256abf',1:'#86b6ef',0:'#fcfcfb'}
ink={3:'#fff',2:'#fff',1:'#0b0b0b',0:'#52514e'}
y=20; parts=[]
for r in order:
    t=tiers[r['key']]; x=380
    parts.append(f'<text x="360" y="{y+40}" text-anchor="end" font-size="26" font-weight="600" fill="#0b0b0b">{esc(r["label"])}</text><text x="360" y="{y+68}" text-anchor="end" font-size="20" fill="#52514e">{esc(r["sub"])}</text>')
    for tier in (3,2,1,0):
        n=t[tier]
        if n==0: continue
        w=n*250-4
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="60" rx="8" fill="{col[tier]}" stroke="{"#c3c2b7" if tier==0 else col[tier]}" stroke-width="2"/><text x="{x+w/2}" y="{y+40}" text-anchor="middle" font-size="26" font-weight="600" fill="{ink[tier]}">{n}</text>')
        x+=n*250
    y+=76
leg=''.join(f'<rect x="{380+i*260}" y="{y+12}" width="22" height="22" rx="4" fill="{col[t]}" stroke="{"#c3c2b7" if t==0 else col[t]}" stroke-width="2"/><text x="{380+i*260+32}" y="{y+30}" font-size="21" fill="#52514e">{lab[t]}</text>' for i,t in enumerate((3,2,1,0)))
c4=f'<svg viewBox="0 0 1440 {y+60}" role="img" aria-label="For each of seven rows, how many of its four cells sit at each evidence tier">{"".join(parts)}{leg}</svg>'
# --- card 5: readouts have no owner
c5='''<svg viewBox="0 0 1440 560" role="img" aria-label="Three instruments each read a state whose owner turns out to depend on which persona is active">
<defs><marker id="a5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#52514e"/></marker></defs>
<g font-size="24" fill="#0b0b0b">
<g font-size="20" fill="#898781" font-family="IBM Plex Mono,monospace"><text x="20" y="30">THE INSTRUMENT</text><text x="520" y="30">WHAT IT READ</text><text x="960" y="30">WHOSE IT TURNED OUT TO BE</text></g>
<g stroke="#52514e" stroke-width="2.5" fill="none"><path d="M470,100 L510,100" marker-end="url(#a5)"/><path d="M910,100 L950,100" marker-end="url(#a5)"/><path d="M470,250 L510,250" marker-end="url(#a5)"/><path d="M910,250 L950,250" marker-end="url(#a5)"/><path d="M470,400 L510,400" marker-end="url(#a5)"/><path d="M910,400 L950,400" marker-end="url(#a5)"/></g>
<rect x="20" y="60" width="450" height="80" rx="12" fill="#fcfcfb" stroke="#c3c2b7" stroke-width="2"/><text x="40" y="94" font-weight="600">an emotion probe</text><text x="40" y="124" font-size="20" fill="#52514e">reads “desperate” at one position</text>
<rect x="520" y="60" width="390" height="80" rx="12" fill="#86b6ef"/><text x="540" y="110" font-weight="600">desperation</text>
<rect x="960" y="60" width="460" height="80" rx="12" fill="#104281"/><text x="980" y="94" fill="#fff" font-weight="600">a character’s email, then the assistant</text><text x="980" y="124" fill="#fff" font-size="20">Anthropic, 2026</text>
<rect x="20" y="210" width="450" height="80" rx="12" fill="#fcfcfb" stroke="#c3c2b7" stroke-width="2"/><text x="40" y="244" font-weight="600">a preference probe</text><text x="40" y="274" font-size="20" fill="#52514e">rates a task harmful or benign</text>
<rect x="520" y="210" width="390" height="80" rx="12" fill="#86b6ef"/><text x="540" y="260" font-weight="600">“I like this one”</text>
<rect x="960" y="210" width="460" height="80" rx="12" fill="#104281"/><text x="980" y="244" fill="#fff" font-weight="600">flips sign under an evil persona</text><text x="980" y="274" fill="#fff" font-size="20">Gilg et al., 2026</text>
<rect x="20" y="360" width="450" height="80" rx="12" fill="#fcfcfb" stroke="#c3c2b7" stroke-width="2"/><text x="40" y="394" font-weight="600">the question “who are you?”</text><text x="40" y="424" font-size="20" fill="#52514e">asked after a long conversation</text>
<rect x="520" y="360" width="390" height="80" rx="12" fill="#86b6ef"/><text x="540" y="410" font-weight="600">“a ghost in the machine”</text>
<rect x="960" y="360" width="460" height="80" rx="12" fill="#104281"/><text x="980" y="394" fill="#fff" font-weight="600">flips after editing past assistant turns</text><text x="980" y="424" fill="#fff" font-size="20">Beckmann &amp; Butlin, 2026</text>
<text x="720" y="530" text-anchor="middle" font-size="27" fill="#0b0b0b" font-weight="600">The instrument gives you a state. Someone decides afterwards whose it is.</text>
</g></svg>'''
# --- card 6: before / after
c6='''<svg viewBox="0 0 1440 560" role="img" aria-label="A first draft said the emotion it carries; the paper says the vector represents the denial, not a hidden state; a second model's review caught it">
<defs><marker id="a6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#52514e"/></marker></defs>
<g font-size="24" fill="#0b0b0b">
<text x="20" y="34" font-size="20" fill="#898781" font-family="IBM Plex Mono,monospace">WHAT THE FIRST DRAFT SAID</text>
<rect x="20" y="60" width="600" height="200" rx="14" fill="#fcfcfb" stroke="#c3c2b7" stroke-width="2"/>
<text x="50" y="120" font-size="30" font-weight="600">a “deflection” vector makes a</text><text x="50" y="162" font-size="30" font-weight="600">speaker deny <tspan fill="#eb6834" text-decoration="line-through">the emotion it carries</tspan></text>
<text x="50" y="228" font-size="21" fill="#52514e">repression, imported in four words</text>
<text x="840" y="34" font-size="20" fill="#898781" font-family="IBM Plex Mono,monospace">WHAT THE PAPER SAYS</text>
<rect x="840" y="60" width="600" height="200" rx="14" fill="#104281"/>
<text x="865" y="120" font-size="27" fill="#fff" font-style="italic">“these vectors do not represent an</text><text x="865" y="158" font-size="27" fill="#fff" font-style="italic">internalized emotional state, but rather</text><text x="865" y="196" font-size="27" fill="#fff" font-style="italic">the ‘deflection’ of a plausible emotion”</text>
<text x="865" y="238" font-size="20" fill="#9ec5f4">Emotion Concepts and their Function, App. 6.14</text>
<path d="M632,200 L826,200" stroke="#52514e" stroke-width="3" fill="none" marker-end="url(#a6)"/>
<text x="730" y="150" text-anchor="middle" font-size="18" fill="#52514e">caught by a</text><text x="730" y="175" text-anchor="middle" font-size="18" fill="#52514e">second model’s review</text>
<text x="720" y="360" text-anchor="middle" font-size="30" font-weight="600">Every reader of these papers here was a model.</text>
<text x="720" y="408" text-anchor="middle" font-size="27" fill="#52514e">Each drifted toward what it already believed. Another model caught it.</text>
<text x="720" y="456" text-anchor="middle" font-size="27" fill="#52514e">Then it happened again, in the next round, to the one that had caught it.</text>
</g></svg>'''
cards=[
 card(1,'why talking about AI is hard','Four questions, wearing one sentence','Most arguments about AI are two people answering different questions and not noticing.',c1),
 card(2,'the board','Seven ways of looking, four things to look at','',"<img src='../lens-board-lean.png' style='max-height:560px;max-width:100%;border:1px solid #e1e0d9;border-radius:8px' alt='the board'>"),
 card(3,'where fights come from','Both are right. They are not about the same object.','',"<div id='emph'></div>"),
 card(4,'the evidence is lopsided','What is measured, and what is only argued','Cells per row, by how much stands behind them. The best-measured row is about us.',c4),
 card(5,'the part that got me','Readouts have no owner','Three papers that never cite each other report the same thing.',c5),
 card(6,'the humbling part','Every reader here was a model','',c6),
]
page='<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap"><style>'+CSS+'</style></head><body>'+''.join(cards)+'</body></html>'
open(root/'share/thread.html','w').write(page); print('share/thread.html', len(page))
