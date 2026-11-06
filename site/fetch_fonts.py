#!/usr/bin/env python3
"""Vendor the pages' Google Fonts into site/fonts/ so the static site loads nothing from Google.

Run once when a page changes its font list; build_site.py copies site/fonts/ into dist/ and points
every page at fonts/fonts.css. Only the latin and latin-ext subsets are kept. All families are
under the SIL Open Font License, which allows redistribution.

  python3 site/fetch_fonts.py
"""
import pathlib, re, urllib.request
root = pathlib.Path(__file__).resolve().parent
out = root / 'fonts'
CSS = ('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600'
       '&family=IBM+Plex+Serif:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400;500'
       '&family=Hanken+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap')
LICENSES = ['ibmplexsans', 'ibmplexserif', 'ibmplexmono', 'hankengrotesk', 'jetbrainsmono']  # google/fonts ofl/ dirs
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=30).read()

def main():
    css = get(CSS).decode()
    blocks = re.findall(r'/\* ([\w-]+) \*/\s*(@font-face \{.*?\})', css, re.S)
    out.mkdir(exist_ok=True)
    for f in out.glob('*.woff2'): f.unlink()
    kept, names = [], {}
    for subset, block in blocks:
        if subset not in ('latin', 'latin-ext'): continue
        fam = re.search(r"font-family: '([^']+)'", block).group(1)
        style = re.search(r'font-style: (\w+)', block).group(1)
        url = re.search(r'url\((https://[^)]+\.woff2)\)', block).group(1)
        if url not in names:  # variable fonts serve one file for several weights
            names[url] = f"{fam.lower().replace(' ', '-')}{'-italic' if style == 'italic' else ''}-{len(names)}-{subset}.woff2"
            (out / names[url]).write_bytes(get(url))
        name = names[url]
        kept.append(f'/* {subset} */\n' + block.replace(url, name))
    (out / 'fonts.css').write_text('/* Vendored by site/fetch_fonts.py from Google Fonts (SIL Open Font License). */\n' + '\n'.join(kept) + '\n')
    # The OFL requires its text to travel with the fonts: one file per family, as published by Google Fonts.
    for d in LICENSES:
        (out / f'OFL-{d}.txt').write_bytes(get(f'https://raw.githubusercontent.com/google/fonts/main/ofl/{d}/OFL.txt'))
    print('fonts:', len(kept), 'faces,', sum(f.stat().st_size for f in out.glob('*.woff2')) // 1024, 'KB')

if __name__ == '__main__': main()
