#!/usr/bin/env python3
"""Generate thread.html (one <section id="cN"> per 1600x900 card) and thread.md (the post texts).

This is a TEMPLATE. Copy it into the project (e.g. share/build_cards.py), then replace the
DATA, POSTS and CARDS sections. Keep the CSS and the component helpers; they are written
against the colour roles in themes.py, so every theme can restyle every card.

The example topic is deliberately neutral and self-verifying: why riders on a
"bus every 10 minutes" route wait longer than 5 minutes on average when buses bunch.
Every number shown is computed below from the stated schedules, so it traces to a source
(the arithmetic in this file). In a real thread, every number, quote and attribution must
trace to a source the user has; keep a SOURCE comment next to each one.

Rules this file encodes (see SKILL.md for the reasons):
  * one concrete object per card (a chat, the chart itself, a diff), not a slide
  * no footer, handle, page counter or "1/6" on the image
  * colours only via var(--role); the ramp t1..t3 only for the ordered thing it encodes
  * text >= 19px at 1600 wide (titles >= 34px); class "meta" may go to 16px for sources

Usage: python build_cards.py --out DIR      (writes DIR/thread.html and DIR/thread.md)
"""
import argparse, html, os, pathlib, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from themes import DEFAULT, css_vars, font_href  # noqa: E402

esc = lambda s: html.escape(str(s), quote=False)
F = lambda role: f'style="fill:var(--{role})"'                      # SVG fill by role
S = lambda role, w=2: f'style="stroke:var(--{role});stroke-width:{w};fill:none"'  # SVG stroke by role

# ============================ DATA (replace) ============================
# SOURCE: arithmetic below. A rider arriving at a uniformly random time waits, on average,
# E[gap^2] / (2 * E[gap]). Each schedule repeats two gaps that sum to 20 minutes,
# i.e. the same 6 buses an hour in every case.
SCHEDULES = [(10, 10), (7, 13), (4, 16), (1, 19)]
def mean_wait(a, b): return (a * a + b * b) / (2 * (a + b))
WAITS = {s: mean_wait(*s) for s in SCHEDULES}                      # 5.0, 5.45, 6.8, 9.05
BUNCHED = (1, 19)
CYCLE = sum(BUNCHED)
SHARE_LONG = BUNCHED[1] / CYCLE                                       # share of riders landing in the long gap
assert abs(WAITS[(10, 10)] - 5.0) < 1e-9 and abs(WAITS[BUNCHED] - 9.05) < 1e-9

# ============================ POSTS (replace) ===========================
# The post text carries the claim; the image carries the evidence. One entry per card, same order.
POSTS = [
    "A bus that comes \"every 10 minutes\" should mean a 5-minute wait on average if you turn up at a random "
    "time. Once the buses bunch, it doesn't, even though all six buses an hour still run. What changed is "
    "the spacing, not the number of buses.",
    "Same six buses an hour, four spacings. Perfectly even: 5 minutes average wait. Bunched into pairs "
    f"a minute apart: just over {WAITS[BUNCHED]:.0f}. Uneven gaps cost riders time even when no bus is cancelled.",
    "So the rule of thumb \"you wait half the gap\" is only true when the gaps are equal. You are more "
    "likely to turn up during a long gap than a short one, so the long gaps count for more.",
]

# ============================ CSS (keep) ================================
CSS = '''
body{margin:0;background:#777;font-family:var(--font);color:var(--ink)}
.card{width:1600px;height:900px;background:var(--bg);position:relative;overflow:hidden;padding:60px 72px;
 box-sizing:border-box;margin:24px auto;display:flex;flex-direction:column;justify-content:center}
.ttl{font-family:var(--display);font-size:40px;font-weight:600;letter-spacing:-.01em;line-height:1.2;margin:0 0 28px;color:var(--ink)}
.meta{font-family:var(--mono);font-size:18px;color:var(--ink3)}
svg{font-family:var(--font);display:block}
/* chat */
.chat{background:var(--surface);border:2px solid var(--hair);border-radius:28px;padding:40px 44px;display:flex;flex-direction:column;gap:26px}
.bub{max-width:1080px;padding:22px 32px;border-radius:28px;font-size:36px;line-height:1.3}
.bub.u{align-self:flex-end;background:var(--user);color:var(--onUser);border-bottom-right-radius:8px}
.bub.a{align-self:flex-start;background:var(--asst);color:var(--onAsst);border-bottom-left-radius:8px;max-width:none}
.who{font-family:var(--mono);font-size:20px;color:var(--ink3);margin:0 0 -16px}
.who.r{align-self:flex-end}
/* diff */
.diff{border:2px solid var(--hair);border-radius:16px;overflow:hidden;font-family:var(--mono);font-size:46px;line-height:1.5;background:var(--surface)}
.diff .hd{background:var(--codeHd);padding:18px 28px;font-size:26px;color:var(--ink2);border-bottom:1px solid var(--hair)}
.diff .ln{padding:10px 28px;white-space:pre-wrap;color:var(--ink2)}
.diff .del{background:var(--delBg);color:var(--delInk)}.diff .add{background:var(--addBg);color:var(--addInk)}
.work{margin:44px 0 0;padding:26px 32px;border-left:8px solid var(--acc);font-size:38px;line-height:1.6;color:var(--ink)}
.work code{font-family:var(--mono);font-size:34px;color:var(--ink2)}
.tag{display:inline-block;font-family:var(--mono);font-size:22px;padding:4px 12px;border-radius:6px;background:var(--tagBg);color:var(--tagInk)}
'''

# ============================ COMPONENTS (keep, extend) ================
def chat(turns):
    """turns: list of (who, html) with who in {'u','a'}; html may contain an <svg>."""
    out = []
    for who, body in turns:
        out.append(f'<div class="bub {who}">{body}</div>')
    return '<div class="chat">' + ''.join(out) + '</div>'


def diff(header, lines):
    """lines: list of (kind, text) with kind in {' ', '-', '+'}."""
    cls = {' ': 'ctx', '-': 'del', '+': 'add'}
    rows = ''.join(f'<div class="ln {cls[k]}">{"−" if k == "-" else k} {esc(t)}</div>' for k, t in lines)
    return f'<div class="diff"><div class="hd">{esc(header)}</div>{rows}</div>'


def hbars(rows, vmax, width=1456, label_w=330, bar_h=104, gap=40, top=64, ref=None, notes=()):
    """Horizontal bars drawn as the actual chart, labels and values on the marks.
    rows: (label, value, value_text, fill_role, text_role); fill_role None = empty/outlined.
    ref: (value, label) dashed reference line. notes: (row_index, text_lines) accent callouts
    drawn to the right of the row's bar end, with an arrow pointing back at the bar."""
    x0, plot_w = label_w, width - label_w - 400   # keep 400 units on the right for callouts
    sx = plot_w / vmax
    h = top + len(rows) * (bar_h + gap)
    p = []
    if ref:  # drawn first so the bars cover it and it never runs through a value label
        rx = x0 + ref[0] * sx
        p.append(f'<line x1="{rx:.1f}" y1="{top - 14}" x2="{rx:.1f}" y2="{h - gap + 10}" {S("ink3", 2)} stroke-dasharray="6 6"/>')
        p.append(f'<text x="{rx:.1f}" y="{top - 26}" text-anchor="middle" font-size="24" {F("ink2")}>{esc(ref[1])}</text>')
    for i, (lab, v, vt, fill, ink) in enumerate(rows):
        y = top + i * (bar_h + gap); w = v * sx
        p.append(f'<text x="{x0 - 24}" y="{y + bar_h / 2 + 10}" text-anchor="end" font-size="30" font-weight="600" {F("ink")}>{esc(lab)}</text>')
        if fill:
            p.append(f'<rect x="{x0}" y="{y}" width="{w:.1f}" height="{bar_h}" rx="8" {F(fill)}/>')
        else:
            p.append(f'<rect x="{x0 + 1}" y="{y + 1}" width="{w - 2:.1f}" height="{bar_h - 2}" rx="8" style="fill:var(--bg);stroke:var(--rule);stroke-width:2"/>')
        p.append(f'<text x="{x0 + w - 20:.1f}" y="{y + bar_h / 2 + 11}" text-anchor="end" font-size="32" font-weight="600" {F(ink)}>{esc(vt)}</text>')
    p.append('<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
             '<path d="M0,0 L10,5 L0,10 z" style="fill:var(--accInk)"/></marker></defs>')
    for i, lines in notes:
        lab, v = rows[i][0], rows[i][1]
        y = top + i * (bar_h + gap) + bar_h / 2; xe = x0 + v * sx
        tx = width - 380
        p.append(f'<path d="M{tx - 16},{y} L{xe + 16:.1f},{y}" {S("accInk", 4)} marker-end="url(#arr)"/>')
        for k, line in enumerate(lines):
            p.append(f'<text x="{tx}" y="{y - (len(lines) - 1) * 17 + k * 34 + 9}" font-size="28" font-weight="600" {F("accInk")}>{esc(line)}</text>')
    return f'<svg viewBox="0 0 {width} {h}" style="width:100%;height:auto" role="img">{"".join(p)}</svg>'


def timeline(width=1380, minutes=60):
    """The example's hero object: the timetable vs the bunched buses, and riders arriving each minute."""
    x0, x1 = 210, width - 20; sx = (x1 - x0) / minutes
    X = lambda m: x0 + m * sx
    p = []
    rows = [('timetable', 60, [m for m in range(0, minutes + 1, 10)], False),
            ('what comes', 170, [m for k in range(0, minutes + 1, CYCLE) for m in (k, k + BUNCHED[0]) if m <= minutes], True)]
    for lab, y, buses, solid in rows:
        p.append(f'<text x="{x0 - 28}" y="{y + 9}" text-anchor="end" font-size="26" font-weight="600" {F("ink2")}>{lab}</text>')
        p.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" {S("rule", 2)}/>')
        for m in buses:
            style = F('onAsst') if solid else f'style="fill:var(--asst);stroke:var(--ink3);stroke-width:2"'
            p.append(f'<rect x="{X(m) - 8:.1f}" y="{y - 22}" width="16" height="44" rx="4" {style}/>')
    yr = 250
    long_n = 0
    for i in range(minutes):
        m = i + 0.5; in_long = (m % CYCLE) >= BUNCHED[0]
        long_n += in_long
        dot = 'style="fill:var(--acc);stroke:var(--accInk);stroke-width:2"' if in_long else F('ink3')
        p.append(f'<circle cx="{X(m):.1f}" cy="{yr}" r="8" {dot}/>')
    p.append(f'<text x="{x0 - 28}" y="{yr + 9}" text-anchor="end" font-size="26" font-weight="600" {F("ink2")}>riders</text>')
    p.append(f'<text x="{x0}" y="{yr + 62}" font-size="27" {F("onAsst")}>one rider each minute: '
             f'<tspan font-weight="700" {F("accInk")}>{long_n} of {minutes}</tspan> arrive during a {BUNCHED[1]}-minute gap</text>')
    assert long_n / minutes == SHARE_LONG
    return f'<svg viewBox="0 0 {width} 330" style="width:100%;height:auto;margin-top:18px" role="img">{"".join(p)}</svg>'


# ============================ CARDS (replace) ===========================
def card(n, body):
    return f'<section class="card" id="c{n}">{body}</section>'

# 1 - the most arresting image: the question as a person would ask it, and the thing itself
c1 = chat([
    ('u', 'My bus is supposed to come every 10 minutes. Why does it feel like I always wait longer than 5?'),
    ('a', 'If the buses bunch, they don’t really come every 10 minutes. Say they arrive in pairs: two buses '
          'a minute apart, then nineteen minutes of nothing.' + timeline()),
])

# 2 - the actual chart, annotated on the data; ramp = how uneven the spacing is (ordered), accent = "look here"
ramp = {(10, 10): (None, 'ink2'), (7, 13): ('t1', 'onT1'), (4, 16): ('t2', 'onT2'), (1, 19): ('t3', 'onT3')}
lab = {(10, 10): 'every 10 min'} | {s: f'{s[0]} min, then {s[1]}' for s in SCHEDULES if s != (10, 10)}
c2 = ('<p class="ttl">Average wait for someone who turns up at a random time, six buses an hour</p>' +
      hbars([(lab[s], WAITS[s], f'{WAITS[s]:.2f}'.rstrip('0').rstrip('.') + ' min', *ramp[s]) for s in SCHEDULES],
            vmax=10, ref=(5, 'half of 10 minutes'),
            notes=[(3, ['same buses an hour,', 'nearly twice the wait'])]))

# 3 - the correction as a diff of the actual text, plus the arithmetic that forced it
a, b = BUNCHED
c3 = (diff('rule of thumb · before → after doing the arithmetic', [
        (' ', 'If a bus comes every N minutes,'),
        ('-', 'you wait N/2 on average.'),
        ('+', 'you wait N/2 only if the gaps are equal;'),
        ('+', 'uneven gaps make the average wait longer.')]) +
      '<div class="work">average wait = average of (gap × gap) ÷ (2 × average gap)' +
      ''.join(f'<br><code>gaps {x} and {y}: ({x}×{x} + {y}×{y}) ÷ 2 = {(x*x + y*y) / 2:g};  '
              f'{(x*x + y*y) / 2:g} ÷ (2 × {(x + y) / 2:g}) = {WAITS[(x, y)]:g} min</code>' for x, y in [(10, 10), BUNCHED]) +
      '</div>')

CARDS = [c1, c2, c3]
assert len(CARDS) == len(POSTS), 'one post text per card'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='thread-out')
    out = pathlib.Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    page = ('<!doctype html><html><head><meta charset="utf-8">'
            f'<link id="theme-fonts" rel="stylesheet" href="{font_href(DEFAULT)}">'
            f'<style id="theme-vars">{css_vars(DEFAULT)}</style><style>{CSS}</style></head><body>'
            + ''.join(card(i + 1, c) for i, c in enumerate(CARDS)) + '</body></html>')
    (out / 'thread.html').write_text(page)
    md = ['# Thread', '', f'{len(POSTS)} posts, one image each (post-N.png).', '']
    for i, t in enumerate(POSTS, 1):
        flag = '' if len(t) <= 280 else f'  (over 280: needs X Premium or a cut)'
        md += [f'**{i} · post-{i}.png** ({len(t)} chars){flag}', t, '']
    (out / 'thread.md').write_text('\n'.join(md))
    print(f'wrote {out / "thread.html"} ({len(CARDS)} cards) and {out / "thread.md"}')


if __name__ == '__main__':
    main()
