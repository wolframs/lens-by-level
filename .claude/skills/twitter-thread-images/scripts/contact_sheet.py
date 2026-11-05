#!/usr/bin/env python3
"""Build one comparison image of every theme: a header row per theme, then the same cards side by side.

  python contact_sheet.py out/themes --cards 1,2,3 --out out/style-options.png

Expects out/themes/<theme-key>/post-N.png (render.py --theme all writes exactly that).
Pick three representative cards: the hero (post 1), the one with the ordinal ramp, and the
densest text card, so the user judges each style on colour, on data and on legibility at once.
"""
import argparse, pathlib, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from themes import THEMES  # noqa: E402

FONT_DIRS = ['/usr/share/fonts', '/System/Library/Fonts', '/Library/Fonts', 'C:/Windows/Fonts']


def font(size, bold=False):
    names = ['DejaVuSans-Bold.ttf', 'Arial Bold.ttf', 'arialbd.ttf'] if bold else ['DejaVuSans.ttf', 'Arial.ttf', 'arial.ttf']
    for d in FONT_DIRS:
        for n in names:
            for p in pathlib.Path(d).rglob(n) if pathlib.Path(d).exists() else []:
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default(size=size)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('root', help='folder holding one sub-folder per theme')
    ap.add_argument('--cards', default='1,2,3')
    ap.add_argument('--themes', default='', help='comma list; default every theme in themes.py that was rendered')
    ap.add_argument('--out', default='style-options.png')
    ap.add_argument('--thumb', type=int, default=560, help='thumbnail width in px')
    a = ap.parse_args()
    root = pathlib.Path(a.root); cards = [int(c) for c in a.cards.split(',')]
    keys = a.themes.split(',') if a.themes else [k for k in THEMES if (root / k).is_dir()]
    if not keys: sys.exit(f'no theme folders under {root}; run render.py --theme all first')
    tw = a.thumb; th = round(tw * 9 / 16); pad, gap, head = 24, 24, 78
    W = pad * 2 + len(cards) * tw + (len(cards) - 1) * gap
    H = pad + len(keys) * (head + th + gap)
    sheet = Image.new('RGB', (W, H), '#e9e8e4'); d = ImageDraw.Draw(sheet)
    fb, fr = font(34, True), font(24)
    y = pad
    for i, k in enumerate(keys, 1):
        t = THEMES[k]
        d.text((pad, y + 22), f'{i}. {t["name"]}', font=fb, fill='#151515')
        d.text((pad + 300, y + 30), t['note'], font=fr, fill='#4a4a46')
        y += head
        for j, n in enumerate(cards):
            p = root / k / f'post-{n}.png'
            if not p.exists(): sys.exit(f'missing {p}')
            im = Image.open(p).convert('RGB').resize((tw, th), Image.LANCZOS)
            sheet.paste(im, (pad + j * (tw + gap), y))
        y += th + gap
    sheet.save(a.out)
    print(f'wrote {a.out} ({W}x{H}, {len(keys)} styles x {len(cards)} cards)')


if __name__ == '__main__':
    main()
