#!/usr/bin/env python3
"""Render a cards HTML file to post-N.png in one theme, or in every theme, and report problems.

  python render.py thread.html --out out/                       # as generated (default theme)
  python render.py thread.html --theme moss --out out/moss      # one theme
  python render.py thread.html --theme all --out out/themes     # out/themes/<key>/post-N.png for each theme
  python render.py thread.html --theme all --cards 1,2,4 --out out/themes   # only the cards for the contact sheet

Theming swaps the <style id="theme-vars"> block and the <link id="theme-fonts"> href that
build_cards.py writes; nothing else in the HTML changes, so a wording edit is one edit in the
generator and a re-render. A temporary themed copy (_render.html, removed afterwards) is written
next to the PNGs with a <base href> pointing back at the original folder, so relative images and
data-shot pages resolve; the source HTML is never modified, so --out may be its own folder.

Exit status 1 if any card has an error (clipped, out of frame, overlapping text). Warnings
(small text, unfilled frame, fallback fonts) are printed but do not fail the run: look at them.
"""
import argparse, json, os, pathlib, re, shutil, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from themes import THEMES, css_vars, font_href  # noqa: E402


def themed(html, key, base_dir):
    if key:
        html, n1 = re.subn(r'<style id="theme-vars">.*?</style>', lambda m: f'<style id="theme-vars">{css_vars(key)}</style>', html, flags=re.S)
        html, n2 = re.subn(r'(<link id="theme-fonts"[^>]*href=")[^"]*(")', lambda m: m.group(1) + font_href(key) + m.group(2), html)
        if not (n1 and n2):
            sys.exit('render.py: the HTML needs <style id="theme-vars"> and <link id="theme-fonts" ...> (see build_cards.py)')
    return html.replace('<head>', f'<head><base href="{base_dir.as_uri()}/">', 1)


def render_one(src, key, out, cards, scale):
    out.mkdir(parents=True, exist_ok=True)
    page = out / '_render.html'   # temporary themed copy; never overwrite the source, even when --out is its folder
    page.write_text(themed(src.read_text(), key, src.parent))
    cmd = ['node', str(HERE / 'shoot.js'), str(page), str(out), '--scale', str(scale)] + (['--cards', cards] if cards else [])
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        sys.stderr.write(p.stderr); sys.exit(f'render.py: shoot.js failed for theme {key or "(as generated)"}')
    page.unlink()
    rep = json.loads(p.stdout.strip().splitlines()[-1])
    label = THEMES[key]['name'] if key else '(as generated)'
    bad = 0
    missing = [f for f, ok in rep['fonts'].items() if not ok]
    print(f'\n== {label} -> {out}' + (f'   fonts NOT loaded (fallback used): {", ".join(missing)}' if missing else ''))
    for c in rep['cards']:
        status = 'ERROR' if c['errors'] else ('warn' if c['warnings'] else 'ok')
        print(f'  post-{c["n"]}.png  {status:5}  min text {c["minFont"] if c["minFont"] is not None else "-"}px  fills {int(c["fill"] * 100)}% of height')
        for e in c['errors']: print(f'      ERROR {e}')
        for w in c['warnings']: print(f'      warn  {w}')
        bad += bool(c['errors'])
    return bad


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('html')
    ap.add_argument('--theme', default='', help='theme key from themes.py, or "all"; omit to render as generated')
    ap.add_argument('--out', required=True)
    ap.add_argument('--cards', default='', help='comma list of card numbers, default all')
    ap.add_argument('--scale', type=float, default=1, help='device scale; 2 gives 3200x1800 files')
    a = ap.parse_args()
    if not shutil.which('node'): sys.exit('render.py: node not found')
    src = pathlib.Path(a.html).resolve(); out = pathlib.Path(a.out)
    if a.theme and a.theme != 'all' and a.theme not in THEMES:
        sys.exit(f'unknown theme {a.theme!r}; choose from {", ".join(THEMES)} or all')
    keys = list(THEMES) if a.theme == 'all' else [a.theme]
    bad = sum(render_one(src, k, out / k if a.theme == 'all' else out, a.cards, a.scale) for k in keys)
    print(f'\n{"FAILED: " + str(bad) + " card(s) with errors" if bad else "no clipping or overlap errors"}'
          ' - now open every PNG and look at it; the checks do not see meaning, only geometry.')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
