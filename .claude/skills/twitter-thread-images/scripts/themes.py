#!/usr/bin/env python3
"""Five colour/type systems for thread images, expressed as CSS custom properties.

Every colour the cards use is a *role* (a CSS variable), never a shared literal, so a
theme can move one role without dragging others with it: text on a tier swatch, the
card surface, and text on the accent are separate roles because they need different
values in light and dark themes.

Roles
  bg        card background                 surface   raised panels (chat window, object boxes)
  ink       main text                       ink2      secondary text      ink3  meta text (sources, axis notes)
  hair      hairlines / borders             rule      stronger rules, empty-tier outline
  t1 t2 t3  ONE-hue ordinal ramp, faint -> strong. Only for an ordered encoding the
            reader is told about (evidence tier, intensity). Never for decoration.
  onT1..3   text drawn on t1..t3
  acc       the single accent ("look here")  onAcc  text on acc   accInk  accent used as text/arrows on bg
  user onUser   chat: the person's bubble and its text
  asst onAsst   chat: the assistant's bubble and its text
  tagBg tagInk  small inline labels
  delBg delInk addBg addInk codeHd   diff rows and the diff header strip

Usage
  python themes.py                 list themes
  python themes.py --css moss      print the :root{...} block for one theme
"""
import sys

ROLES = ['bg', 'surface', 'ink', 'ink2', 'ink3', 'hair', 'rule', 't1', 't2', 't3', 'onT1', 'onT2', 'onT3',
         'acc', 'onAcc', 'accInk', 'user', 'onUser', 'asst', 'onAsst', 'tagBg', 'tagInk',
         'delBg', 'delInk', 'addBg', 'addInk', 'codeHd']

THEMES = {
    'highlighter': dict(
        name='Highlighter', note='graphite on paper, one yellow marker', mode='light',
        fonts=('IBM Plex Sans', 'IBM Plex Mono', 'IBM Plex Sans'),
        gf='IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500',
        c=dict(bg='#fafaf7', surface='#ffffff', ink='#121211', ink2='#4a4a46', ink3='#77776f', hair='#e3e3dc', rule='#c2c2b9',
               t1='#a9a99f', t2='#6b6b62', t3='#2a2a25', onT1='#121211', onT2='#ffffff', onT3='#ffffff',
               acc='#ffd43b', onAcc='#121211', accInk='#121211',
               user='#2f4a66', onUser='#ffffff', asst='#ececE6', onAsst='#121211',
               tagBg='#fff3b8', tagInk='#5c4a00', delBg='#ffe7e3', delInk='#8a1f12', addBg='#fff3b8', addInk='#4d3f00',
               codeHd='#efefe9')),
    'moss': dict(
        name='Moss', note='field-notebook greens, plum for the point', mode='light',
        fonts=('Source Sans 3', 'Source Code Pro', 'Source Serif 4'),
        gf='Source+Sans+3:wght@400;600&family=Source+Code+Pro:wght@400;500&family=Source+Serif+4:opsz,wght@8..60,600',
        c=dict(bg='#f6f7f2', surface='#ffffff', ink='#101a12', ink2='#48534a', ink3='#6f7a71', hair='#dde3da', rule='#bcc6ba',
               t1='#82b691', t2='#3a7a4c', t3='#1e4a2b', onT1='#101a12', onT2='#ffffff', onT3='#ffffff',
               acc='#7b2d6b', onAcc='#ffffff', accInk='#7b2d6b',
               user='#5e5a66', onUser='#ffffff', asst='#e7ebe4', onAsst='#101a12',
               tagBg='#f5e8f2', tagInk='#6a2259', delBg='#f8e6ee', delInk='#7b2d6b', addBg='#e3f0e6', addInk='#1e4a2b',
               codeHd='#eceee8')),
    'midnight': dict(
        name='Midnight', note='dark, ice-blue ramp, amber for the point', mode='dark',
        fonts=('Hanken Grotesk', 'JetBrains Mono', 'Hanken Grotesk'),
        gf='Hanken+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500',
        c=dict(bg='#0e1320', surface='#141b2b', ink='#eef2f8', ink2='#b4bdcc', ink3='#8a94a7', hair='#26304a', rule='#3d4a66',
               t1='#2b5689', t2='#5b97da', t3='#aed6ff', onT1='#eef2f8', onT2='#0b1220', onT3='#0b1220',
               acc='#ffb54d', onAcc='#1a1205', accInk='#ffb54d',
               user='#3d3f4a', onUser='#ffffff', asst='#1d2537', onAsst='#eef2f8',
               tagBg='#2b2314', tagInk='#ffd08a', delBg='#3a1d21', delInk='#ffb4ab', addBg='#14301f', addInk='#a2e2b2',
               codeHd='#182032')),
    'plum': dict(
        name='Plum', note='aubergine ramp, ochre for the point, a serif for headings', mode='light',
        fonts=('Figtree', 'DM Mono', 'Fraunces'),
        gf='Figtree:wght@400;500;600&family=DM+Mono:wght@400;500&family=Fraunces:opsz,wght@9..144,600',
        c=dict(bg='#faf8fb', surface='#ffffff', ink='#1b1221', ink2='#564a5d', ink3='#7d7383', hair='#e8e0ec', rule='#cabed1',
               t1='#b9a1dc', t2='#6c46a0', t3='#3b1f5a', onT1='#1b1221', onT2='#ffffff', onT3='#ffffff',
               acc='#d4930f', onAcc='#1b1221', accInk='#8a5a00',
               user='#5a4a3a', onUser='#ffffff', asst='#eee8f2', onAsst='#1b1221',
               tagBg='#fbefd6', tagInk='#764f00', delBg='#fbe7e5', delInk='#8a2219', addBg='#efe8f8', addInk='#3b1f5a',
               codeHd='#f1edf4')),
    'riso': dict(
        name='Riso', note='two-ink print: teal and fluorescent pink on paper', mode='light',
        fonts=('Archivo', 'Space Mono', 'Archivo'),
        gf='Archivo:wght@400;500;700&family=Space+Mono:wght@400;700',
        c=dict(bg='#f5f2ea', surface='#fbf9f3', ink='#1a2a32', ink2='#4b5a61', ink3='#6c767c', hair='#e1dccf', rule='#c7beae',
               t1='#62b4ba', t2='#1c7d87', t3='#0a5761', onT1='#1a2a32', onT2='#ffffff', onT3='#ffffff',
               acc='#ff4f8b', onAcc='#1a2a32', accInk='#c2185b',
               user='#1a2a32', onUser='#ffffff', asst='#eae4d8', onAsst='#1a2a32',
               tagBg='#ffe2ed', tagInk='#a9134a', delBg='#ffe2ed', delInk='#a9134a', addBg='#dcefef', addInk='#0a5761',
               codeHd='#ece8de')),
}
DEFAULT = 'highlighter'


def css_vars(key):
    """The <style id="theme-vars"> body for one theme: colour roles plus the three font stacks."""
    t = THEMES[key]
    body, mono, disp = t['fonts']
    roles = ';'.join(f'--{r}:{t["c"][r]}' for r in ROLES)
    return (f':root{{{roles};--font:"{body}",system-ui,sans-serif;--mono:"{mono}",ui-monospace,monospace;'
            f'--display:"{disp}","{body}",system-ui,sans-serif;color-scheme:{t["mode"]}}}')


def font_href(key):
    return f'https://fonts.googleapis.com/css2?family={THEMES[key]["gf"]}&display=swap'


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--css':
        print(css_vars(sys.argv[2]))
    else:
        for k, t in THEMES.items():
            missing = [r for r in ROLES if r not in t['c']]
            print(f'{k:12} {t["name"]:12} {t["mode"]:5}  {t["note"]}' + (f'  MISSING {missing}' if missing else ''))
