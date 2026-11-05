// Render each card in share/thread.html to share/post-N.png at 1600×900; card 3 embeds a dimmed board from ledger.html.
const { chromium } = require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{
 const root=path.resolve(__dirname,'..'); const br=await chromium.launch();
 // 1) build the emphasis board image from ledger.html
 const led=fs.readFileSync(path.join(root,'ledger.html'),'utf8');
 let ctx=await br.newContext({viewport:{width:1240,height:1300},deviceScaleFactor:2}); let p=await ctx.newPage();
 await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>body{margin:0}</style></head><body>${led}</body></html>`,{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready);
 await p.addStyleTag({content:`.cell{opacity:.16} .cell[data-id="behaviour/token"],.cell[data-id="relational/model"]{opacity:1;box-shadow:0 0 0 4px #eb6834} .mx .cs,.mx .csl,.mx .h span{opacity:.5} header,.sub,.lg,.rule,.foot{display:none!important} .wrap{padding-top:12px}`});
 await p.evaluate(()=>{const mk=(id,txt,dx,dy)=>{const c=document.querySelector('.cell[data-id="'+id+'"]');const r=c.getBoundingClientRect();const d=document.createElement('div');d.textContent=txt;Object.assign(d.style,{position:'absolute',left:(r.left+window.scrollX+dx)+'px',top:(r.top+window.scrollY+dy)+'px',background:'#eb6834',color:'#fff',font:'600 17px IBM Plex Sans,system-ui,sans-serif',padding:'6px 12px',borderRadius:'6px',whiteSpace:'nowrap',zIndex:5});document.body.appendChild(d);};
  mk('behaviour/token','“it’s just predicting the next token”',-150,-40); mk('relational/model','“my 4o had a personality”',0,-40);});
 const mx=await p.$('.mx'); await mx.screenshot({path:path.join(root,'share','_emph.png')}); await ctx.close();
 // 2) render the cards
 let html=fs.readFileSync(path.join(root,'share','thread.html'),'utf8');
 const img='data:image/png;base64,'+fs.readFileSync(path.join(root,'share','_emph.png')).toString('base64');
 html=html.replace(/<div id="emph"[^>]*><\/div>/,`<div style="flex:1"><img src="${img}" style="max-height:500px;max-width:100%;border:1px solid #e1e0d9;border-radius:8px;display:block" alt="board with two cells highlighted"></div>`);
 const lean='data:image/png;base64,'+fs.readFileSync(path.join(root,'lens-board-lean.png')).toString('base64');
 html=html.replace("src='../lens-board-lean.png'",`src="${lean}"`);
 ctx=await br.newContext({viewport:{width:1700,height:1000},deviceScaleFactor:1}); p=await ctx.newPage();
 await p.setContent(html,{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready);
 for(let i=1;i<=6;i++){const el=await p.$('#c'+i); await el.screenshot({path:path.join(root,'share',`post-${i}.png`)});}
 await br.close(); fs.unlinkSync(path.join(root,'share','_emph.png')); console.log('rendered 6 cards');
})();
