#!/usr/bin/env python3
"""Write share/themes/<key>/thread.html: the cards with one theme's colours and fonts swapped in."""
import re, sys, pathlib
sys.path.insert(0,str(pathlib.Path(__file__).parent))
from themes import ROLES, THEMES
root=pathlib.Path(__file__).parent
base=open(root/'thread.html').read()
for key,t in THEMES.items():
    m={ROLES[r].lower():v for r,v in t['c'].items()}
    s=re.sub(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b',lambda k:m.get(k.group(0).lower(),k.group(0)),base)
    body,mono,disp=t['fonts']
    s=s.replace('href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap"',f'href="https://fonts.googleapis.com/css2?family={t["gf"]}&display=swap"')
    s=s.replace('--font:"IBM Plex Sans",',f'--font:"{body}",').replace('--mono:"IBM Plex Mono",',f'--mono:"{mono}",').replace('--display:var(--font);',f'--display:"{disp}",var(--font);')
    s=s.replace('IBM Plex Sans,system-ui,sans-serif',f'{body},system-ui,sans-serif').replace('IBM Plex Mono,monospace',f'{mono},monospace')
    d=root/'themes'/key; d.mkdir(parents=True,exist_ok=True); open(d/'thread.html','w').write(s)
print('themes written:',', '.join(THEMES))
