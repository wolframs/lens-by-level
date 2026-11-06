// Render share/post-N.png and share/lead.png (1600×900). Usage: node share/shoot.js [theme] [card ...].
// With a theme, the board images are recoloured to match. Card names (1…6, lead) render only those:
// the posted images stay as they went out, so `node share/shoot.js midnight lead` touches the lead alone.
const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
const theme=process.argv[2]||''; const only=process.argv.slice(3);
const LEDGER_VARS={midnight:{css:`:root{--bg:#0e1320!important;--surface:#141b2b!important;--ink:#eef2f8!important;--ink-2:#b4bdcc!important;--ink-3:#7e889b!important;--hair:#212a3b!important;--rule:#36425c!important;--t3:#aed6ff!important;--t2:#5b97da!important;--t1:#2b5689!important;--on-t3:#0b1220!important;--on-t2:#0b1220!important;--on-t1:#eef2f8!important;--focus:#ffb54d!important;--font:"Hanken Grotesk",system-ui,sans-serif!important;--mono:"JetBrains Mono",ui-monospace,monospace!important;color-scheme:dark}`,
  fonts:'https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap',acc:'#ffb54d',onAcc:'#1a1205',bg:'#0e1320',hair:'#212a3b'}};
(async()=>{
 const root=path.resolve(__dirname,'..'); const br=await chromium.launch(); const T=LEDGER_VARS[theme];
 const acc=T?T.acc:'#eb6834', onAcc=T?T.onAcc:'#fff', hair=T?T.hair:'#e1e0d9';
 const led=fs.readFileSync(path.join(root,'ledger.html'),'utf8');
 async function ledgerPage(){const ctx=await br.newContext({viewport:{width:1240,height:1300},deviceScaleFactor:2}); const p=await ctx.newPage();
  await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0}</style></head><body>${led}</body></html>`,{waitUntil:'networkidle'});
  if(T){await p.addStyleTag({url:T.fonts}); await p.addStyleTag({content:T.css});} await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(200); return [ctx,p];}
 // lean board
 let [ctx,p]=await ledgerPage();
 await p.addStyleTag({content:`nav,.foot,.rule,.sub,#ver{display:none!important}`});
 const lean=path.join(root,'share','_lean.png'); await (await p.$('.wrap')).screenshot({path:lean}); await ctx.close();
 // emphasis board
 [ctx,p]=await ledgerPage();
 await p.addStyleTag({content:`.cell{opacity:.16} .cell[data-id="behaviour/token"],.cell[data-id="relational/model"]{opacity:1;box-shadow:0 0 0 4px ${acc}} .mx .cs,.mx .csl,.mx .h span{opacity:.5} header,.sub,.lg,.rule,.foot{display:none!important} .wrap{padding-top:12px}`});
 await p.evaluate(([acc,onAcc])=>{const mk=(id,txt,dx,dy)=>{const c=document.querySelector('.cell[data-id="'+id+'"]');const r=c.getBoundingClientRect();const d=document.createElement('div');d.textContent=txt;Object.assign(d.style,{position:'absolute',left:(r.left+window.scrollX+dx)+'px',top:(r.top+window.scrollY+dy)+'px',background:acc,color:onAcc,font:'600 17px system-ui,sans-serif',padding:'6px 12px',borderRadius:'6px',whiteSpace:'nowrap',zIndex:5});document.body.appendChild(d);};
  mk('behaviour/token','“it’s just predicting the next token”',-150,-40); mk('relational/model','“my 4o had a personality”',0,-40);},[acc,onAcc]);
 const emph=path.join(root,'share','_emph.png'); await (await p.$('.mx')).screenshot({path:emph}); await ctx.close();
 // cards
 const src=theme?path.join(root,'share','themes',theme,'thread.html'):path.join(root,'share','thread.html');
 let html=fs.readFileSync(src,'utf8'); const b64=f=>'data:image/png;base64,'+fs.readFileSync(f).toString('base64');
 html=html.replaceAll(/<div id="emph"[^>]*><\/div>/g,`<div style="flex:1"><img src="${b64(emph)}" style="max-height:500px;max-width:100%;border:1px solid ${hair};border-radius:8px;display:block" alt="board with two cells highlighted"></div>`);
 html=html.replace(/src='\.\.\/lens-board-lean\.png' style='[^']*'/,`src="${b64(lean)}" style="max-height:788px;max-width:100%;display:block;margin:0 auto;border-radius:8px"`);
 ctx=await br.newContext({viewport:{width:1700,height:1000}}); p=await ctx.newPage();
 await p.setContent(html,{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready);
 const names=only.length?only:['1','2','3','4','5','6','lead'];
 for(const n of names){const el=await p.$('#c'+n); await el.screenshot({path:path.join(root,'share',n==='lead'?'lead.png':`post-${n}.png`)});}
 await br.close(); fs.unlinkSync(emph); fs.unlinkSync(lean); console.log('rendered', names.join(' '), theme||'(base)');
})();
