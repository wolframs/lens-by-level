#!/usr/bin/env python3
"""Render lens-by-level.html from data/*.json + templates/. Single source of truth is data/."""
import json, html, pathlib
NB=' '
root=pathlib.Path(__file__).parent
board=json.load(open(root/'data/board.json')); src=json.load(open(root/'data/sources.json'))
notes=open(root/'data/notes.html').read()
head=open(root/'templates/head.html').read(); legend=open(root/'templates/legend.html').read()
m=board['meta']; cols=m['columns']
def esc(t): return html.escape(t,quote=False)
def tagfmt(t):
    import re
    parts=re.split(r'( · | ↔ )',t)
    return ''.join(p if p in (' · ',' ↔ ') else esc(p).replace(' ',NB) for p in parts)
out=[head,'<div class="wrap">\n  <div class="fig">\n',f'   <h1>{esc(m["title"])}</h1>\n',f'   <p class="sub">{esc(m["sub"])}</p>\n',
     '   <div class="scroll">\n    <div class="mx" role="group" aria-label="Seven lenses by four levels, cells graded by evidence, persona-relative cells marked">\n',
     '      <div class="corner">lens ↓ / level →</div>\n']
for c in cols: out.append(f'      <div class="h">{esc(c["label"])}<span>{esc(c["sub"])}</span></div>\n')
out.append(f'\n      <div class="csl">{esc(m["strip_label"])}</div>\n')
for st in board['strip']: out.append(f'      <div class="cs"><b>{esc(st["label"])}</b>{esc(st["text"])}</div>\n')
cells={(c['row'],c['col']):c for c in board['cells']}
first=True
for g in board['groups']:
    out.append(f'\n      <div class="g{" first" if first else ""}">{esc(g["label"])}<em>{esc(g["note"])}</em></div>\n'); first=False
    for r in [r for r in board['rows'] if r['group']==g['key']]:
        out.append(f'\n      <div class="r">{esc(r["label"])}<span>{esc(r["sub"])}</span></div>\n')
        for c in cols:
            x=cells[(r['key'],c['key'])]
            cls={3:' t3',2:' t2',1:' t1',0:''}[x['tier']]
            pers='<em>◆</em>' if x['persona'] else ''
            out.append(f'      <div class="c{cls}"><b>{pers}{esc(x["headline"])}</b><i>{esc(x["gloss"])}</i><u><span>{tagfmt(x["tags"])}</span><s>{x["glyph"]}</s></u></div>\n')
out.append('    </div>\n   </div>\n')
out.append(legend)
out.append('<div class="keys">'+' · '.join(f'<b>{esc(k["tag"])}</b> {esc(k["short"])}' for k in src['keys'])+'</div>\n')
out.append('   <div class="foot">'+''.join(f'<span>{esc(f)}</span>' for f in m['foot'])+'</div>\n  </div>\n\n')
out.append(notes)
out.append('  <div class="src">\n    <h2>Sources, with venue and models</h2>\n    <ol>\n'+''.join(f'      <li><b>{esc(s["tag"])}</b> — {s["html"]}</li>\n' for s in src['sources'])+'    </ol>\n  </div>\n</div>\n')
open(root/'lens-by-level.html','w').write(''.join(out))
print('built', len(''.join(out)), 'bytes')
