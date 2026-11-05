const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const body=fs.readFileSync(process.argv[2],'utf8'); const out=process.argv[3];
 const wrap=(t)=>`<!doctype html><html${t?` data-theme="${t}"`:''}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>:root{color-scheme:light}body{margin:0;font:14px system-ui}img{max-width:100%}</style></head><body>${body}</body></html>`;
 const br=await chromium.launch();
 for(const [theme,w] of [['light',1240],['dark',1240],['light',400]]){const ctx=await br.newContext({viewport:{width:w,height:900},deviceScaleFactor:1,colorScheme:theme}); const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(String(e))); p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
  await p.setContent(wrap(theme==='dark'?'dark':null),{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready);
  await p.screenshot({path:`${out}-${theme}-${w}.png`,fullPage:true});
  await p.click('.cell[data-id="dynamics/runstance"]'); await p.waitForTimeout(300);
  await p.screenshot({path:`${out}-${theme}-${w}-drawer.png`,fullPage:false});
  const drawerText=await p.$eval('#drawer',d=>d.innerText.slice(0,200)); await p.keyboard.press('Escape');
  await p.evaluate(()=>{location.hash='#sources'}); await p.waitForTimeout(200); await p.screenshot({path:`${out}-${theme}-${w}-sources.png`,fullPage:false});
  console.log(theme,w,'scrollW',await p.evaluate(()=>document.documentElement.scrollWidth),'errors',errs,'drawer:',drawerText.replace(/\n/g,' | ').slice(0,120)); await ctx.close();}
 await br.close();})();
