#!/usr/bin/env python3
"""Validate every theme in themes.py before showing it to anyone.

Checks, per theme:
  ramp       t1..t3 as a one-hue ordinal ramp (validate_palette.validate_ordinal) against
             bg and against surface: monotone lightness, visible steps, single hue,
             faint end >= 2:1 vs the surface it sits on
  text       every text-on-fill pair >= 4.5:1 (WCAG)
  meta       ink3 (sources, axis notes) >= 3:1 on bg and surface
  accent     accent fill >= 3:1 vs bg so arrows/highlights read; accent far from every tier
  no reuse   fills that are NOT tiers (chat bubbles, tags, diff rows) must not be mistaken
             for a tier swatch (OKLab dE x100 >= 10), so a reader who learned the legend
             never reads a chat bubble or a result box as "strong evidence"

Usage: python check_themes.py [-v] [theme ...]   (-v lists passes too)   exit 1 if any FAIL
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from themes import THEMES  # noqa: E402
from validate_palette import validate_ordinal, contrast, deltaE  # noqa: E402

TEXT_PAIRS = [('ink', 'bg'), ('ink', 'surface'), ('ink2', 'bg'), ('ink2', 'surface'),
              ('onT1', 't1'), ('onT2', 't2'), ('onT3', 't3'), ('onAcc', 'acc'), ('accInk', 'bg'),
              ('onUser', 'user'), ('onAsst', 'asst'), ('tagInk', 'tagBg'),
              ('delInk', 'delBg'), ('addInk', 'addBg'), ('ink2', 'codeHd')]
META_PAIRS = [('ink3', 'bg'), ('ink3', 'surface')]
NON_TIER_FILLS = ['user', 'asst', 'tagBg', 'delBg', 'addBg', 'acc']
TIER_CONFUSION_DE = 10.0
ACC_VS_TIER_DE = 15.0


def check(key):
    t = THEMES[key]; c = t['c']; mode = t['mode']
    rows, ok = [], True

    def add(state, name, detail):
        nonlocal ok
        if state == 'FAIL': ok = False
        rows.append((state, name, detail))

    ramp = [c['t1'], c['t2'], c['t3']]
    for surf in ('bg', 'surface'):
        report, rok = validate_ordinal(ramp, mode, c[surf])
        bad = [f'{n}: {d}' for n, s, d in report if s is False]
        add('PASS' if rok else 'FAIL', f'ramp vs {surf}', 'one hue, monotone, faint end clears surface' if rok else '; '.join(bad))
    for fg, bgk in TEXT_PAIRS:
        r = contrast(c[fg], c[bgk])
        add('PASS' if r >= 4.5 else 'FAIL', f'text {fg}/{bgk}', f'{r:.2f}:1')
    for fg, bgk in META_PAIRS:
        r = contrast(c[fg], c[bgk])
        add('PASS' if r >= 3.0 else 'FAIL', f'meta {fg}/{bgk}', f'{r:.2f}:1')
    r = contrast(c['acc'], c['bg'])
    add('PASS' if r >= 3.0 else ('WARN' if c['accInk'] != c['acc'] else 'FAIL'), 'accent fill vs bg',
        f'{r:.2f}:1' + ('' if r >= 3.0 else ' (use accInk for arrows/lines on bg)'))
    worst = min((deltaE(c['acc'], c[k]), k) for k in ('t1', 't2', 't3'))
    add('PASS' if worst[0] >= ACC_VS_TIER_DE else 'FAIL', 'accent vs ramp', f'closest {worst[1]} dE {worst[0]:.1f}')
    for f in NON_TIER_FILLS:
        if f == 'acc': continue
        d, k = min((deltaE(c[f], c[k]), k) for k in ('t1', 't2', 't3'))
        add('PASS' if d >= TIER_CONFUSION_DE else 'WARN', f'{f} not a tier', f'closest {k} dE {d:.1f}'
            + ('' if d >= TIER_CONFUSION_DE else ' - could be read as that evidence tier'))
    return rows, ok


def main():
    verbose = '-v' in sys.argv
    keys = [a for a in sys.argv[1:] if a != '-v'] or list(THEMES)
    all_ok = True
    for k in keys:
        rows, ok = check(k)
        all_ok &= ok
        print(f'\n{THEMES[k]["name"]} ({k}, {THEMES[k]["mode"]})  ->  {"PASS" if ok else "FAIL"}')
        for state, name, detail in rows:
            if state != 'PASS' or verbose:
                print(f'  [{state:4}] {name:22} {detail}')
    sys.exit(0 if all_ok else 1)


if __name__ == '__main__':
    main()
