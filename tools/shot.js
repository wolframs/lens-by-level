// usage: node shot.js <html> <outprefix> [scale]
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [,, html, out, scaleArg] = process.argv;
  const scale = Number(scaleArg || 1);
  const body = fs.readFileSync(html, 'utf8');
  const page = (theme) => `<!doctype html><html${theme?` data-theme="${theme}"`:''}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style></head><body>${body}</body></html>`;
  const browser = await chromium.launch();
  for (const [theme, w] of [['light',1240],['dark',1240],['light',400]]) {
    const ctx = await browser.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: scale, colorScheme: theme });
    const p = await ctx.newPage();
    const errs = [];
    p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
    p.on('pageerror', e => errs.push(String(e)));
    await p.setContent(page(theme === 'dark' ? 'dark' : null), { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    await p.screenshot({ path: `${out}-${theme}-${w}.png`, fullPage: true });
    const fig = await p.$('.fig');
    if (fig && w > 400) await fig.screenshot({ path: `${out}-fig-${theme}.png` });
    console.log(theme, w, 'scrollWidth', sw, 'errors', errs);
    await ctx.close();
  }
  await browser.close();
})();
