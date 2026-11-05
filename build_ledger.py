#!/usr/bin/env python3
"""Render ledger.html: the lean board with a per-cell drawer (gloss, sources, trail), a sources view and a notes view. Data inline."""
import json, html, pathlib
root=pathlib.Path(__file__).parent
board=json.load(open(root/'data/board.json')); src=json.load(open(root/'data/sources.json'))
trail=json.load(open(root/'data/trail.json')); origin=json.load(open(root/'data/origin.json'))
notes=open(root/'data/notes.html').read()
data=json.dumps({'board':board,'sources':src['sources'],'trail':trail,'origin':origin},ensure_ascii=False).replace('</','<\\/')
page=r'''<title>Lens Ledger</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: a lean 7×4 board of headlines; clicking a cell opens a drawer with the gloss, its sources and its trail.
   Two more views (sources, notes) on the hash. Same tokens as the figure. */
:root{--bg:#f9f9f7;--surface:#fcfcfb;--ink:#0b0b0b;--ink-2:#52514e;--ink-3:#898781;--hair:#e1e0d9;--rule:#c3c2b7;
 --t3:#104281;--t2:#256abf;--t1:#86b6ef;--on-t3:#fff;--on-t2:#fff;--on-t1:#0b0b0b;--focus:#eb6834;
 --font:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d0d0d;--surface:#1a1a19;--ink:#f0efec;--ink-2:#c3c2b7;--ink-3:#898781;--hair:#2c2c2a;--rule:#383835;--t3:#9ec5f4;--t2:#256abf;--t1:#184f95;--on-t3:#0b0b0b;--on-t2:#fff;--on-t1:#f0efec;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0d0d0d;--surface:#1a1a19;--ink:#f0efec;--ink-2:#c3c2b7;--ink-3:#898781;--hair:#2c2c2a;--rule:#383835;--t3:#9ec5f4;--t2:#256abf;--t1:#184f95;--on-t3:#0b0b0b;--on-t2:#fff;--on-t1:#f0efec;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--font);font-size:14px;line-height:1.45;padding-block:16px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.wrap{max-width:1200px;margin:0 auto}
header{display:flex;flex-wrap:wrap;gap:8px 20px;align-items:baseline;justify-content:space-between;padding:0 0 12px;border-bottom:1px solid var(--hair);margin-bottom:14px}
header h1{font-size:19px;font-weight:600;margin:0;letter-spacing:-.01em}
header .v{font-family:var(--mono);font-size:11px;color:var(--ink-3)}
nav{display:flex;gap:4px}
nav a{font-size:13px;color:var(--ink-2);text-decoration:none;padding:5px 10px;border-radius:4px;border:1px solid transparent}
nav a[aria-current="page"]{color:var(--ink);border-color:var(--rule);background:var(--surface)}
nav a:focus-visible,.cell:focus-visible,button:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
.view{display:none}.view.on{display:block}
.sub{color:var(--ink-2);margin:0 0 12px;max-width:88ch;font-size:13.5px}
.scroll{overflow-x:auto}
.mx{display:grid;grid-template-columns:118px repeat(4,minmax(160px,1fr));gap:6px;min-width:820px}
.mx .corner{align-self:end;font-family:var(--mono);font-size:11px;color:var(--ink-3);padding:0 0 6px 2px}
.mx .h{align-self:end;padding:0 4px 6px;border-bottom:1px solid var(--rule);font-weight:600;font-size:14px;line-height:1.25}
.mx .h span{display:block;font-weight:400;font-size:12px;color:var(--ink-2)}
.mx .cs{font-size:11px;line-height:1.35;color:var(--ink-3);padding:2px 4px 0}
.mx .cs b{font-weight:600;color:var(--ink-2);display:block;font-size:10.5px;letter-spacing:.04em;text-transform:uppercase}
.mx .csl{font-size:11px;color:var(--ink-3);padding:2px 6px 0 2px;font-style:italic}
.mx .g{grid-column:1/-1;font-size:12px;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-2);padding:12px 2px 0;font-weight:600}
.mx .g em{font-style:normal;text-transform:none;letter-spacing:0;font-weight:400;margin-left:10px;color:var(--ink-3)}
.mx .r{font-weight:600;font-size:13.5px;line-height:1.25;padding:8px 6px 0 2px}
.mx .r span{display:block;font-weight:400;font-size:12px;color:var(--ink-2);margin-top:2px}
.cell{font:inherit;text-align:left;cursor:pointer;border-radius:5px;padding:8px 10px 7px;min-height:64px;display:flex;flex-direction:column;gap:4px;background:var(--surface);border:1px solid var(--hair);color:var(--ink);width:100%}
.cell b{font-weight:600;font-size:13px;line-height:1.3;text-wrap:balance}
.cell b em{font-style:normal;font-size:11px;vertical-align:1px;margin-right:4px}
.cell u{text-decoration:none;font-family:var(--mono);font-size:10.5px;margin-top:auto;display:flex;justify-content:space-between;gap:8px;color:var(--ink-2);align-items:flex-end}
.cell u s{text-decoration:none;letter-spacing:.08em;white-space:nowrap}
.cell.t3{background:var(--t3);border-color:var(--t3);color:var(--on-t3)}.cell.t3 u{color:var(--on-t3)}
.cell.t2{background:var(--t2);border-color:var(--t2);color:var(--on-t2)}.cell.t2 u{color:var(--on-t2)}
.cell.t1{background:var(--t1);border-color:var(--t1);color:var(--on-t1)}.cell.t1 u{color:var(--on-t1)}
.cell[aria-expanded="true"]{box-shadow:0 0 0 2px var(--focus)}
.cell:hover{filter:brightness(1.06)}
.lg{display:flex;flex-wrap:wrap;gap:6px 16px;align-items:center;font-size:12px;color:var(--ink-2);padding:12px 2px 0}
.lg .sw{display:inline-block;width:13px;height:13px;border-radius:3px;margin-right:6px;vertical-align:-2px;border:1px solid var(--ink-3)}
.lg .k{font-family:var(--mono);font-size:11px;color:var(--ink-3);margin-left:5px;letter-spacing:.08em}
.rule{font-size:12px;color:var(--ink-2);padding:6px 2px 0}
/* drawer */
.drawer{position:fixed;top:0;right:0;bottom:0;width:min(460px,100%);background:var(--surface);border-left:1px solid var(--hair);box-shadow:-8px 0 24px rgba(0,0,0,.12);transform:translateX(100%);transition:transform .18s ease;overflow-y:auto;z-index:20;padding:18px max(18px,env(safe-area-inset-right,0px)) 32px 18px}
.drawer.open{transform:none}
@media (prefers-reduced-motion:reduce){.drawer{transition:none}}
.drawer .eyebrow{font-family:var(--mono);font-size:11px;color:var(--ink-3);display:flex;justify-content:space-between;gap:8px;align-items:center}
.drawer .close{font:inherit;background:none;border:1px solid var(--rule);border-radius:4px;color:var(--ink-2);padding:3px 9px;cursor:pointer}
.drawer h2{font-size:17px;font-weight:600;margin:8px 0 6px;line-height:1.3;text-wrap:balance}
.chip{display:inline-block;font-size:11.5px;padding:2px 8px;border-radius:999px;border:1px solid var(--rule);color:var(--ink-2);margin:0 6px 10px 0}
.chip.t3{background:var(--t3);color:var(--on-t3);border-color:var(--t3)}.chip.t2{background:var(--t2);color:var(--on-t2);border-color:var(--t2)}.chip.t1{background:var(--t1);color:var(--on-t1);border-color:var(--t1)}
.drawer p{margin:0 0 10px}
.drawer h3{font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-3);margin:16px 0 6px;font-weight:600}
.drawer ul{margin:0;padding-left:0;list-style:none}
.drawer li{margin:0 0 8px;font-size:13px;color:var(--ink-2);padding-left:10px;border-left:2px solid var(--hair)}
.drawer li b{color:var(--ink);font-weight:500;font-family:var(--mono);font-size:11.5px}
.drawer li .ver{font-family:var(--mono);font-size:11px;color:var(--ink-3);display:block}
.drawer li .was{color:var(--ink-3)}
.drawer a{color:inherit}
.backdrop{position:fixed;inset:0;background:rgba(0,0,0,.25);z-index:19;display:none}.backdrop.on{display:block}
/* sources view */
.srcs{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:10px 24px;font-size:13px;color:var(--ink-2)}
.srcs .s{padding:8px 0;border-top:1px solid var(--hair)}
.srcs .s b{font-family:var(--mono);font-size:11.5px;color:var(--ink);font-weight:500}
.srcs .s .cites{display:flex;flex-wrap:wrap;gap:4px;margin-top:5px}
.srcs .s .cites button{font:inherit;font-size:11.5px;background:none;border:1px solid var(--rule);border-radius:999px;padding:1px 8px;color:var(--ink-2);cursor:pointer}
.srcs a{color:inherit}
.notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px 32px;font-size:13px;color:var(--ink-2)}
.notes h2{font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-3);margin:0 0 6px;font-weight:600}
.notes p{margin:0 0 8px}.notes ul,.notes ol{margin:0;padding-left:18px}.notes li{margin:0 0 5px}.notes b{color:var(--ink);font-weight:600}
.foot{font-family:var(--mono);font-size:11px;color:var(--ink-3);padding:14px 2px 0;display:flex;flex-wrap:wrap;gap:4px 18px}
</style>
<div class="wrap">
 <header>
  <h1>Seven lenses on four levels of a language model</h1>
  <nav aria-label="Views"><a href="#board" data-view="board">Board</a><a href="#sources" data-view="sources">Sources</a><a href="#notes" data-view="notes">Notes</a></nav>
  <span class="v" id="ver"></span>
 </header>
 <section class="view" id="view-board">
  <p class="sub" id="sub"></p>
  <div class="scroll"><div class="mx" id="mx" role="group" aria-label="Seven lenses by four levels; each cell opens its gloss, sources and trail"></div></div>
  <div class="lg">
   <span><span class="sw" style="background:var(--t3);border-color:var(--t3)"></span>Peer-reviewed study or architectural fact<span class="k">●●●</span></span>
   <span><span class="sw" style="background:var(--t2);border-color:var(--t2)"></span>Preprint, lab paper or documented event<span class="k">●●○</span></span>
   <span><span class="sw" style="background:var(--t1);border-color:var(--t1)"></span>Preliminary, case study or informal<span class="k">●○○</span></span>
   <span><span class="sw"></span>Argued reading<span class="k">○○○</span></span>
   <span>◆ persona-relative</span>
  </div>
  <div class="rule">Click a cell for the full claim, its sources and how it got here. Tier follows the specific result, not the paper; a case study inside a peer-reviewed paper grades as preliminary; peer-reviewed needs a venue listing seen, if only in search results. “·” separates sources that each state their own clause, fill follows the strongest; “+” marks this figure’s authors’ inference, graded at the weakest part; ↔ contested by.</div>
 </section>
 <section class="view" id="view-sources"><p class="sub">Every source on the board, with the cells that cite it. Venue and model statements are what the verifiers could reach, and say at what level.</p><div class="srcs" id="srcs"></div></section>
 <section class="view" id="view-notes">''' + notes + r'''</section>
 <div class="foot" id="foot"></div>
</div>
<div class="backdrop" id="backdrop"></div>
<aside class="drawer" id="drawer" aria-label="Cell detail" aria-hidden="true"></aside>
<script type="application/json" id="data">''' + data + r'''</script>
<script>
(function(){
const D=JSON.parse(document.getElementById('data').textContent);
const B=D.board, cols=B.meta.columns, rows=B.rows, groups=B.groups;
const cells={}; B.cells.forEach(c=>cells[c.row+'/'+c.col]=c);
const srcByTag={}; D.sources.forEach(s=>srcByTag[s.tag]=s);
const G={3:'●●●',2:'●●○',1:'●○○',0:'○○○'};
const TIER={3:'Peer-reviewed study or architectural fact',2:'Preprint, lab paper or documented event',1:'Preliminary, case study or informal',0:'Argued reading'};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const nb=s=>esc(s).replace(/ /g,' ');
function tagHtml(t){return t.split(/( · | ↔ )/).map(p=>(p===' · '||p===' ↔ ')?p:nb(p)).join('');}
function tagSources(t){ // resolve "Name YY", own probe, architecture, product
  const out=[]; t.split(/ · | ↔ | \+ /).forEach(p=>{const m=p.match(/^((?:[A-Z][A-Za-z&]+ )?[A-Z][A-Za-z&]+ \d\d(?:–\d\d)?|own probe|architecture|product)/); if(m&&srcByTag[m[1]]&&!out.includes(m[1])) out.push(m[1]);}); return out;}
const rowLabel={}; rows.forEach(r=>rowLabel[r.key]=r.label); const colLabel={}; cols.forEach(c=>colLabel[c.key]=c.label);
document.getElementById('ver').textContent=B.meta.version+' · '+B.meta.date;
document.getElementById('sub').textContent=B.meta.sub;
document.getElementById('foot').innerHTML=B.meta.foot.map(f=>'<span>'+esc(f)+'</span>').join('');
// board
const mx=document.getElementById('mx'); let h='<div class="corner">lens ↓ / level →</div>';
cols.forEach(c=>h+='<div class="h">'+esc(c.label)+'<span>'+esc(c.sub)+'</span></div>');
h+='<div class="csl">'+esc(B.meta.strip_label)+'</div>'; B.strip.forEach(s=>h+='<div class="cs"><b>'+esc(s.label)+'</b>'+esc(s.text)+'</div>');
groups.forEach(g=>{h+='<div class="g">'+esc(g.label)+'<em>'+esc(g.note)+'</em></div>';
 rows.filter(r=>r.group===g.key).forEach(r=>{h+='<div class="r">'+esc(r.label)+'<span>'+esc(r.sub)+'</span></div>';
  cols.forEach(c=>{const x=cells[r.key+'/'+c.key]; h+='<button class="cell t'+x.tier+'" data-id="'+r.key+'/'+c.key+'" aria-expanded="false" aria-controls="drawer"><b>'+(x.persona?'<em>◆</em>':'')+esc(x.headline)+'</b><u><span>'+tagHtml(x.tags)+'</span><s>'+G[x.tier]+'</s></u></button>';});});});
mx.innerHTML=h;
// drawer
const drawer=document.getElementById('drawer'), backdrop=document.getElementById('backdrop'); let openBtn=null;
function openCell(id,focusBack){const x=cells[id]; if(!x) return; closeDrawer(false);
 let s='<div class="eyebrow"><span>'+esc(rowLabel[x.row])+' × '+esc(colLabel[x.col])+'</span><button class="close" id="dclose">close</button></div>';
 s+='<h2>'+(x.persona?'◆ ':'')+esc(x.headline)+'</h2><span class="chip t'+x.tier+'">'+G[x.tier]+' '+esc(TIER[x.tier])+'</span>'+(x.persona?'<span class="chip">◆ persona-relative</span>':'');
 s+='<p>'+esc(x.gloss)+'</p><p><b style="font-family:var(--mono);font-size:11.5px;font-weight:500">'+tagHtml(x.tags)+'</b></p>';
 const srcs=tagSources(x.tags); if(srcs.length){s+='<h3>Sources</h3><ul>'; srcs.forEach(t=>{s+='<li><b>'+esc(t)+'</b> — '+srcByTag[t].html+'</li>';}); s+='</ul>';}
 const tr=[]; (D.origin[id]||[]).forEach(o=>tr.push({ver:o.version,text:'“'+o.headline+'” — '+o.gloss+(o.tag?' ['+o.tag+']':'')+' · graded: '+o.grade+(o.level!==x.col?' · then in the '+o.level+' column':'')}));
 (D.trail[id]||[]).forEach(t=>tr.push({ver:t.version+' · '+t.date,text:'was “'+t.from.headline+'” at '+G[t.from.tier]+'. '+t.why}));
 if(!tr.length) tr.push({ver:'',text:'Unchanged since the 4 Nov rebuild.'});
 s+='<h3>Trail</h3><ul>'; tr.forEach(t=>{s+='<li>'+(t.ver?'<span class="ver">'+esc(t.ver)+'</span>':'')+esc(t.text)+'</li>';}); s+='</ul>';
 drawer.innerHTML=s; drawer.classList.add('open'); drawer.setAttribute('aria-hidden','false'); backdrop.classList.add('on');
 openBtn=document.querySelector('.cell[data-id="'+id+'"]'); if(openBtn) openBtn.setAttribute('aria-expanded','true');
 document.getElementById('dclose').addEventListener('click',()=>closeDrawer(true)); drawer.scrollTop=0; document.getElementById('dclose').focus();}
function closeDrawer(focusBack){drawer.classList.remove('open'); drawer.setAttribute('aria-hidden','true'); backdrop.classList.remove('on'); if(openBtn){openBtn.setAttribute('aria-expanded','false'); if(focusBack) openBtn.focus();} openBtn=null;}
mx.addEventListener('click',e=>{const b=e.target.closest('.cell'); if(b) openCell(b.dataset.id);});
backdrop.addEventListener('click',()=>closeDrawer(true)); document.addEventListener('keydown',e=>{if(e.key==='Escape'&&drawer.classList.contains('open')) closeDrawer(true);});
// sources view
const cites={}; B.cells.forEach(c=>tagSources(c.tags).forEach(t=>(cites[t]=cites[t]||[]).push(c.row+'/'+c.col)));
let sh=''; D.sources.forEach(s=>{sh+='<div class="s"><b>'+esc(s.tag)+'</b> — '+s.html+'<div class="cites">'+(cites[s.tag]||[]).map(id=>'<button data-id="'+id+'">'+esc(rowLabel[id.split('/')[0]])+' × '+esc(colLabel[id.split('/')[1]])+'</button>').join('')+(cites[s.tag]?'':'<span style="font-size:11.5px;color:var(--ink-3)">named in the header strip or notes only</span>')+'</div></div>';});
document.getElementById('srcs').innerHTML=sh;
document.getElementById('srcs').addEventListener('click',e=>{const b=e.target.closest('button[data-id]'); if(b){show('board'); openCell(b.dataset.id);}});
// views
function show(v){document.querySelectorAll('.view').forEach(x=>x.classList.toggle('on',x.id==='view-'+v)); document.querySelectorAll('nav a').forEach(a=>{if(a.dataset.view===v)a.setAttribute('aria-current','page'); else a.removeAttribute('aria-current');}); closeDrawer(false);}
function route(){const v=(location.hash||'#board').slice(1); show(['board','sources','notes'].includes(v)?v:'board');}
window.addEventListener('hashchange',route); route();
})();
</script>
'''
open(root/'ledger.html','w').write(page); print('ledger built',len(page))
