// Screenshot every <section id="cN"> of a cards HTML file to OUTDIR/post-N.png and check each card.
//
// Usage: node shoot.js CARDS.html OUTDIR [--cards 1,3] [--scale 1]
//   Prints one JSON line: {cards:[{n,file,errors[],warnings[],minFont,fill}], fonts:{...}}
//   render.py calls this; you rarely need to call it directly.
//
// Embedded screenshots: an <img data-shot="page.html" data-selector=".board" data-css="nav{display:none}"
//   data-viewport="1240x1300"> is replaced, before the cards are shot, by an element screenshot of that
//   page (a URL, or a path relative to the cards file / its <base href>). The theme's <style id="theme-vars"> is injected into
//   the embedded page too, so a page written with the same --role variables picks up the theme.
//
// Checks (errors fail the render; warnings are printed):
//   error  any element or SVG text drawn outside its card (the card clips it)
//   error  content cut off inside an overflow:hidden box, or SVG text outside its <svg>
//   error  two different text runs overlapping (colliding labels)
//   warn   text below 19px at 1600 wide (".meta" elements: below 16px)
//   warn   content spans less than 75% of the card height, or leaves an empty band > 22% of it
//   warn   a requested web font did not load (render fell back to a system font)
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const [src, outdir] = args.filter((a, i) => !a.startsWith('--') && !(i > 0 && args[i - 1].startsWith('--')));
if (!src || !outdir) { console.error('usage: node shoot.js CARDS.html OUTDIR [--cards 1,3] [--scale 1]'); process.exit(2); }
const only = opt('--cards', '') ? opt('--cards').split(',').map(Number) : null;
const scale = Number(opt('--scale', '1'));

(async () => {
  fs.mkdirSync(outdir, { recursive: true });
  const br = await chromium.launch();
  const file = path.resolve(src); const html = fs.readFileSync(file, 'utf8');
  const themeVars = (html.match(/<style id="theme-vars">([\s\S]*?)<\/style>/) || [, ''])[1];
  const fontHref = (html.match(/<link id="theme-fonts"[^>]*href="([^"]+)"/) || [, ''])[1];
  const ctx = await br.newContext({ viewport: { width: 1700, height: 1000 }, deviceScaleFactor: scale });
  const page = await ctx.newPage();
  await page.goto('file://' + file, { waitUntil: 'networkidle', timeout: 30000 }).catch(() => {});

  // 1. embedded screenshots
  const shots = await page.$$eval('img[data-shot]', els => els.map((e, i) => ({ i, shot: new URL(e.dataset.shot, document.baseURI).href, sel: e.dataset.selector || 'body', css: e.dataset.css || '', vp: e.dataset.viewport || '1240x1300' })));
  for (const s of shots) {
    const [w, h] = s.vp.split('x').map(Number);
    const c2 = await br.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 2 }); const p2 = await c2.newPage();
    await p2.goto(s.shot, { waitUntil: 'networkidle', timeout: 30000 }).catch(() => {});
    if (fontHref) await p2.addStyleTag({ url: fontHref }).catch(() => {});
    if (themeVars) await p2.addStyleTag({ content: themeVars });
    if (s.css) await p2.addStyleTag({ content: s.css });
    await p2.evaluate(() => document.fonts.ready); await p2.waitForTimeout(150);
    const el = await p2.$(s.sel);
    if (!el) { console.error(`data-shot: selector ${s.sel} not found in ${s.shot}`); process.exit(1); }
    const b64 = (await el.screenshot()).toString('base64'); await c2.close();
    await page.$$eval('img[data-shot]', (els, [i, d]) => { els[i].src = 'data:image/png;base64,' + d; }, [s.i, b64]);
  }
  await page.evaluate(async () => { await document.fonts.ready; await Promise.all([...document.images].map(im => im.complete ? 0 : new Promise(r => { im.onload = im.onerror = r; }))); });
  await page.waitForTimeout(200);

  // 2. fonts that were asked for but not loaded
  const fonts = await page.evaluate(() => {
    const used = new Set(); const out = {};
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    while (w.nextNode()) if (w.currentNode.textContent.trim() && w.currentNode.parentElement.closest('section'))
      used.add(getComputedStyle(w.currentNode.parentElement).fontFamily.split(',')[0].trim().replace(/"/g, ''));
    for (const fam of used) if (!/^(system-ui|ui-monospace|sans-serif|serif|monospace)$/.test(fam))
      out[fam] = [...document.fonts].some(f => f.family.replace(/"/g, '') === fam && f.status === 'loaded');
    return out;
  });

  // 3. per-card checks and screenshots
  const ids = await page.$$eval('section[id^="c"]', els => els.map(e => e.id).filter(id => /^c\d+$/.test(id)));
  const report = { cards: [], fonts };
  for (const id of ids) {
    const n = Number(id.slice(1)); if (only && !only.includes(n)) continue;
    const r = await page.evaluate((id) => {
      const card = document.getElementById(id); const C = card.getBoundingClientRect();
      const errors = [], warnings = []; const tol = 1;
      const name = el => el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.classList && el.classList.length ? '.' + [...el.classList].join('.') : '');
      const snippet = t => JSON.stringify(t.trim().replace(/\s+/g, ' ').slice(0, 50));
      const visible = el => { const s = getComputedStyle(el); return s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0; };
      // text runs: one rect per line box of each text node
      const runs = []; const walker = document.createTreeWalker(card, NodeFilter.SHOW_TEXT);
      let minFont = 999;
      while (walker.nextNode()) {
        const t = walker.currentNode; if (!t.textContent.trim()) continue;
        const el = t.parentElement; if (!visible(el)) continue;
        const range = document.createRange(); range.selectNodeContents(t);
        const rects = [...range.getClientRects()].filter(q => q.width > 0 && q.height > 0);
        // effective font size: CSS px, times the SVG's user-unit scale for SVG text
        let fs = parseFloat(getComputedStyle(el).fontSize); const svg = el.closest('svg');
        if (svg && svg.viewBox && svg.viewBox.baseVal && svg.viewBox.baseVal.width) fs *= svg.getBoundingClientRect().width / svg.viewBox.baseVal.width;
        const floor = el.closest('.meta') ? 16 : 19;
        if (fs < floor - 0.5) warnings.push(`small text ${fs.toFixed(1)}px (< ${floor}) in ${name(el)}: ${snippet(t.textContent)}`);
        minFont = Math.min(minFont, fs);
        const nErr = errors.length;
        for (const q of rects) {
          if (q.left < C.left - tol || q.right > C.right + tol || q.top < C.top - tol || q.bottom > C.bottom + tol)
            errors.push(`text outside card: ${snippet(t.textContent)} in ${name(el)}`);
          if (svg) { const S = svg.getBoundingClientRect();
            if (q.left < S.left - tol || q.right > S.right + tol || q.top < S.top - tol || q.bottom > S.bottom + tol)
              errors.push(`SVG text cut by its <svg> box: ${snippet(t.textContent)}`); }
        }
        // clipped by an overflow:hidden ancestor inside the card
        for (let a = el; a && a !== card; a = a.parentElement) {
          const s = getComputedStyle(a); if (a instanceof SVGElement) continue;
          if (/(hidden|clip)/.test(s.overflow + s.overflowX + s.overflowY)) {
            const A = a.getBoundingClientRect();
            for (const q of rects) if (q.right > A.right + tol || q.bottom > A.bottom + tol || q.left < A.left - tol || q.top < A.top - tol)
              { errors.push(`text cut off by ${name(a)}: ${snippet(t.textContent)}`); break; }
          }
        }
        // runs already reported as clipped are left out of the overlap check (they are not visible)
        if (errors.length === nErr) rects.forEach(q => runs.push({ q, node: t, el, txt: t.textContent }));
      }
      // non-text elements sticking out of the card
      for (const el of card.querySelectorAll('*')) {
        if (!visible(el) || el.closest('defs,marker')) continue;
        const q = el.getBoundingClientRect(); if (!q.width || !q.height) continue;
        if (q.left < C.left - tol || q.right > C.right + tol || q.top < C.top - tol || q.bottom > C.bottom + tol)
          errors.push(`${name(el)} extends outside the card (${Math.round(q.left - C.left)},${Math.round(q.top - C.top)} ${Math.round(q.width)}x${Math.round(q.height)})`);
      }
      // colliding text runs (different text nodes overlapping by more than a sliver)
      for (let i = 0; i < runs.length; i++) for (let j = i + 1; j < runs.length; j++) {
        const a = runs[i], b = runs[j]; if (a.node === b.node) continue;
        const w = Math.min(a.q.right, b.q.right) - Math.max(a.q.left, b.q.left);
        const h = Math.min(a.q.bottom, b.q.bottom) - Math.max(a.q.top, b.q.top);
        if (w > 4 && h > Math.min(a.q.height, b.q.height) * 0.35) errors.push(`overlapping text: ${snippet(a.txt)} / ${snippet(b.txt)}`);
      }
      // fill: vertical coverage by content (text runs, svg, img, boxes with a background or border)
      const boxes = runs.map(r => r.q);
      for (const el of card.querySelectorAll('svg,img,canvas,*')) {
        if (el.closest('svg') && el.tagName.toLowerCase() !== 'svg') continue;
        const s = getComputedStyle(el); const q = el.getBoundingClientRect(); if (!q.width || !q.height || !visible(el)) continue;
        if (/^(svg|img|canvas)$/i.test(el.tagName) || (s.backgroundColor !== 'rgba(0, 0, 0, 0)' && el !== card) || parseFloat(s.borderTopWidth) > 0) boxes.push(q);
      }
      const iv = boxes.map(q => [Math.max(q.top, C.top) - C.top, Math.min(q.bottom, C.bottom) - C.top]).filter(([a, b]) => b > a).sort((x, y) => x[0] - y[0]);
      let cur = 0, gap = 0, top = iv.length ? iv[0][0] : 0, bottom = 0;
      for (const [a, b] of iv) { gap = Math.max(gap, a - cur); cur = Math.max(cur, b); bottom = Math.max(bottom, b); }
      gap = Math.max(gap, C.height - cur);
      const span = (bottom - top) / C.height;
      if (span < 0.75) warnings.push(`content spans only ${(span * 100).toFixed(0)}% of the card height; enlarge it to fill the frame`);
      if (gap > 0.22 * C.height) warnings.push(`empty band of ${Math.round(gap)}px (${(gap / C.height * 100).toFixed(0)}% of height)`);
      return { errors: [...new Set(errors)], warnings: [...new Set(warnings)], minFont: minFont === 999 ? null : +minFont.toFixed(1), fill: +span.toFixed(2), size: [Math.round(C.width), Math.round(C.height)] };
    }, id);
    const out = path.join(outdir, `post-${n}.png`);
    await (await page.$('#' + id)).screenshot({ path: out });
    report.cards.push({ n, file: out, ...r });
  }
  await br.close();
  console.log(JSON.stringify(report));
})().catch(e => { console.error(e); process.exit(1); });
