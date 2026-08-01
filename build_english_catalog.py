import json

# Load catalog_data.js
with open('e:/catalogo/catalog_data.js', 'r', encoding='utf-8') as f:
    catalog_data_js = f.read()

english_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ARGENTOY x MILONGA CUSTOMS · Official Catalog</title>
<meta name="description" content="Official bootleg fan art custom figures catalog. Select your collectibles and place your order directly via WhatsApp.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:wght@400;500;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#15131c;
    --bg2:#1d1a28;
    --ink:#0a0910;
    --paper:#f6f3ea;
    --txt:#f4f1ff;
    --mut:#a39db8;
    --yellow:#ffd23f;
    --magenta:#ff2e7e;
    --cyan:#2ee6d6;
    --lime:#c6ff3a;
    --wa:#25d366;
    --line:3px solid var(--ink);
    --shadow:6px 6px 0 var(--ink);
    --shadow-sm:4px 4px 0 var(--ink);
    --shadow-lg:10px 10px 0 var(--ink);
    --disp:'Anton',sans-serif;
    --body:'Space Grotesk',sans-serif;
    --mono:'Space Mono',monospace;
  }
  *{box-sizing:border-box;margin:0;padding:0}
  html{scroll-behavior:smooth}
  body{
    font-family:var(--body);
    color:var(--txt);
    background:var(--bg);
    background-image:radial-gradient(rgba(255,255,255,.05) 1.4px,transparent 1.4px);
    background-size:22px 22px;
    min-height:100vh;
    overflow-x:hidden;
    padding-bottom:120px;
    -webkit-tap-highlight-color:transparent;
  }
  body::after{
    content:"";position:fixed;inset:0;pointer-events:none;z-index:9999;opacity:.05;mix-blend-mode:overlay;
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  }
  a{color:inherit}

  .marquee{
    background:var(--magenta);color:var(--ink);border-bottom:var(--line);
    overflow:hidden;white-space:nowrap;font-family:var(--disp);
    letter-spacing:1px;text-transform:uppercase;font-size:13px;
  }
  .marquee__track{display:inline-block;animation:scroll 24s linear infinite;padding:6px 0}
  .marquee__track span{padding:0 18px}
  .marquee__track span::after{content:"✦";padding-left:36px}
  @keyframes scroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}

  header{max-width:1280px;margin:0 auto;padding:18px 20px 6px;}
  .brand-wrap{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;}
  .brand{
    display:inline-block;font-family:var(--disp);font-size:clamp(32px,5.5vw,54px);
    line-height:.86;text-transform:uppercase;letter-spacing:1px;
    color:var(--yellow);
    -webkit-text-stroke:1.5px var(--ink);
    text-shadow:3px 3px 0 var(--magenta);
    transform:rotate(-1.2deg);
  }
  .brand-sub{
    font-family:var(--mono);font-size:12px;color:var(--cyan);
    background:var(--bg2);border:1.5px solid var(--ink);padding:3px 8px;
    box-shadow:2px 2px 0 var(--ink);text-transform:uppercase;letter-spacing:0.5px;
  }
  .tagline{
    margin-top:10px;max-width:680px;font-size:clamp(14px,2vw,16px);
    color:var(--txt);line-height:1.4;
  }

  /* Buscador */
  .searchwrap{max-width:1280px;margin:14px auto 0;padding:0 20px;}
  .search-input{
    width:100%;background:var(--bg2);color:var(--txt);
    border:var(--line);box-shadow:var(--shadow-sm);padding:10px 14px;
    font-family:var(--mono);font-size:13px;outline:none;
    transition:all .15s ease;border-radius:0;
  }
  .search-input:focus{
    border-color:var(--yellow);box-shadow:4px 4px 0 var(--yellow);
  }

  .navwrap{position:sticky;top:0;z-index:50;background:var(--bg);
    border-bottom:var(--line);margin-top:16px;
    background-image:radial-gradient(rgba(255,255,255,.05) 1.4px,transparent 1.4px);background-size:22px 22px;}
  .nav{
    max-width:1280px;margin:0 auto;display:flex;gap:10px;
    padding:12px 20px;overflow-x:auto;scrollbar-width:none;
  }
  .nav::-webkit-scrollbar{display:none}
  .pill{
    flex:0 0 auto;cursor:pointer;font-family:var(--body);font-weight:700;
    font-size:14px;text-transform:uppercase;letter-spacing:.4px;
    background:var(--bg2);color:var(--txt);border:var(--line);
    padding:10px 16px;display:flex;align-items:center;gap:9px;
    box-shadow:var(--shadow-sm);transition:transform .12s ease,box-shadow .12s ease,background .12s;
    transform:rotate(-.5deg);
  }
  .pill:nth-child(even){transform:rotate(.7deg)}
  .pill:hover{transform:translate(-2px,-2px) rotate(0);box-shadow:6px 6px 0 var(--ink)}
  .pill .em{font-size:18px;line-height:1}
  .pill .cnt{font-family:var(--mono);font-size:11px;background:var(--ink);color:var(--yellow);
    padding:1px 6px;border-radius:20px}
  .pill.active{background:var(--yellow);color:var(--ink);box-shadow:var(--shadow-sm)}
  .pill.active .cnt{background:var(--magenta);color:var(--ink)}

  .sec{max-width:1280px;margin:0 auto;padding:22px 20px 0}
  .sec h2{font-family:var(--disp);text-transform:uppercase;font-size:clamp(24px,4.5vw,42px);
    line-height:.95;letter-spacing:.5px}
  .sec h2 .em{margin-right:8px}
  .sec .sub{font-family:var(--mono);font-size:12px;color:var(--mut);margin-top:6px}

  .grid{
    max-width:1280px;margin:0 auto;padding:16px 20px;
    display:grid;gap:14px;
    grid-template-columns:repeat(auto-fill,minmax(145px,1fr));
  }

  /* ===== TARJETAS ===== */
  .card{
    position:relative;background:#fff;border:1.5px solid var(--ac);
    box-shadow:0 3px 12px rgba(0,0,0,.30);
    padding:10px 8px 8px;cursor:pointer;border-radius:0;
    transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease;
    opacity:0;animation:pop .35s ease forwards;
    display:flex;flex-direction:column;justify-content:space-between;
  }
  .card:nth-child(4n+1){--ac:var(--yellow)}
  .card:nth-child(4n+2){--ac:var(--cyan)}
  .card:nth-child(4n+3){--ac:var(--magenta)}
  .card:nth-child(4n+4){--ac:var(--lime)}
  .card:hover{transform:translateY(-4px);box-shadow:0 10px 24px rgba(0,0,0,.42);border-color:var(--ink)}
  .card.sel{border-color:var(--ink);outline:3px solid var(--lime);outline-offset:2px}
  
  .card .ph{
    aspect-ratio:1/1;background:#fff;border:none;overflow:hidden;
    display:flex;align-items:center;justify-content:center;
  }
  .card .ph img{width:100%;height:100%;object-fit:contain;display:block;
    transition:transform .25s ease}
  .card:hover .ph img{transform:scale(1.06)}

  .code{
    position:absolute;top:-9px;left:-6px;z-index:2;
    font-family:var(--mono);font-weight:700;font-size:11px;
    background:var(--ac);color:var(--ink);padding:2px 7px;
    border:1.5px solid var(--ink);box-shadow:0 2px 5px rgba(0,0,0,.28);
    transform:rotate(-3deg);letter-spacing:.5px;
  }
  
  /* Botón + visible */
  .pick{
    position:absolute;top:-10px;right:-10px;z-index:3;
    width:34px;height:34px;border-radius:50%;border:2px solid var(--ink);
    background:var(--lime);color:var(--ink);font-size:22px;font-weight:800;
    display:flex;align-items:center;justify-content:center;cursor:pointer;
    box-shadow:0 2px 6px rgba(0,0,0,.35);line-height:1;transition:transform .12s,background .12s;
    font-family:var(--body);
  }
  .pick:hover{transform:scale(1.18) rotate(90deg)}
  .card.sel .pick{background:var(--magenta);color:#fff;transform:rotate(0)}
  .card.sel .pick:hover{transform:scale(1.18)}

  .card-title{
    font-family:var(--body);
    font-weight:700;
    font-size:11px;
    color:var(--ink);
    margin-top:6px;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
    text-align:center;
    padding:0 2px;
  }

  @keyframes pop{from{opacity:0;transform:translateY(12px) scale(.96)}to{opacity:1;transform:none}}

  /* ===== LIGHTBOX + CARRUSEL ===== */
  .lb{position:fixed;inset:0;z-index:200;display:none;
    align-items:center;justify-content:center;padding:16px;
    background:rgba(8,7,14,.85);backdrop-filter:blur(5px)}
  .lb.open{display:flex;animation:fade .2s ease}
  @keyframes fade{from{opacity:0}to{opacity:1}}
  .lb__box{
    background:var(--paper);border:3px solid var(--ink);box-shadow:var(--shadow-lg);
    max-width:min(540px,94vw);width:100%;padding:14px;position:relative;
    animation:zoom .25s cubic-bezier(.2,1.3,.5,1);
  }
  @keyframes zoom{from{transform:scale(.8);opacity:0}to{transform:scale(1);opacity:1}}
  .lb__img{background:#fff;border:1.5px solid rgba(10,9,16,.15);aspect-ratio:1/1;
    display:flex;align-items:center;justify-content:center;
    position:relative;overflow:hidden}
  .lb__img img{width:100%;height:100%;object-fit:contain}
  .lb__img img.swapL{animation:swapL .22s ease}
  .lb__img img.swapR{animation:swapR .22s ease}
  @keyframes swapL{from{opacity:.25;transform:translateX(-16px)}to{opacity:1;transform:none}}
  @keyframes swapR{from{opacity:.25;transform:translateX(16px)}to{opacity:1;transform:none}}
  
  .lb__nav{position:absolute;top:50%;transform:translateY(-50%);z-index:6;
    width:48px;height:48px;border-radius:50%;border:2px solid var(--ink);
    background:rgba(10,9,16,.75);color:var(--yellow);font-size:26px;line-height:1;
    display:flex;align-items:center;justify-content:center;cursor:pointer;
    backdrop-filter:blur(3px);transition:background .15s,transform .15s,color .15s;
    font-family:var(--body);box-shadow:0 3px 10px rgba(0,0,0,0.4);}
  .lb__nav:hover{background:var(--yellow);color:var(--ink);transform:translateY(-50%) scale(1.1)}
  .lb__nav:active{transform:translateY(-50%) scale(.95)}
  .lb__nav.prev{left:10px}
  .lb__nav.next{right:10px}
  
  .lb__meta{display:flex;flex-direction:column;gap:4px;margin-top:12px}
  .lb__code{font-family:var(--disp);font-size:26px;color:var(--ink);
    text-transform:uppercase;letter-spacing:0.5px;line-height:1.1}
  .lb__count{font-family:var(--mono);font-size:12px;color:#7a7388;}
  .lb__row{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap}
  
  .btn{
    font-family:var(--body);font-weight:700;text-transform:uppercase;letter-spacing:.5px;
    font-size:14px;border:var(--line);box-shadow:var(--shadow-sm);cursor:pointer;
    padding:11px 16px;display:inline-flex;align-items:center;gap:8px;
    transition:transform .12s,box-shadow .12s;background:#fff;color:var(--ink);
  }
  .btn:hover{transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--ink)}
  .btn:active{transform:translate(2px,2px);box-shadow:1px 1px 0 var(--ink)}
  .btn.add{background:var(--lime)}
  .btn.add.is-sel{background:var(--magenta);color:#fff}
  .btn.close{background:var(--ink);color:var(--yellow);margin-left:auto}
  .lb__x{position:absolute;top:-16px;right:-16px;width:40px;height:40px;border-radius:50%;
    background:var(--magenta);color:#fff;border:var(--line);box-shadow:var(--shadow-sm);
    font-size:22px;cursor:pointer;display:flex;align-items:center;justify-content:center}

  /* BARRA FLOTANTE */
  .bar{
    position:fixed;left:0;right:0;bottom:0;z-index:120;
    background:var(--ink);border-top:4px solid var(--yellow);
    transform:translateY(120%);transition:transform .3s cubic-bezier(.2,1,.3,1);
    box-shadow:0 -8px 30px rgba(0,0,0,.5);
  }
  .bar.show{transform:translateY(0)}
  .bar__in{max-width:1280px;margin:0 auto;padding:12px 18px;
    display:flex;align-items:center;gap:12px}
  .bar__count{display:flex;align-items:center;gap:10px;color:var(--txt);font-weight:700}
  .bar__badge{font-family:var(--mono);font-weight:700;background:var(--yellow);color:var(--ink);
    min-width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;
    border:2px solid var(--paper);font-size:14px}
  .bar__badge.bump{animation:bump .3s ease}
  @keyframes bump{0%{transform:scale(1)}40%{transform:scale(1.4)}100%{transform:scale(1)}}
  .bar__txt{font-size:13px;text-transform:uppercase;letter-spacing:.5px}
  .bar__txt small{display:block;font-family:var(--mono);font-size:11px;color:var(--mut);text-transform:none;letter-spacing:0}
  .bar .btn{margin-left:auto}
  .bar .btn.view{background:var(--bg2);color:var(--txt)}
  .bar .btn.wa{background:var(--wa);color:#fff;font-size:15px}

  /* DRAWER */
  .drawer{position:fixed;inset:0;z-index:180;display:none}
  .drawer.open{display:block}
  .drawer__bg{position:absolute;inset:0;background:rgba(8,7,14,.7)}
  .drawer__panel{
    position:absolute;left:0;right:0;bottom:0;max-height:80vh;overflow:auto;
    background:var(--bg2);border-top:4px solid var(--cyan);
    box-shadow:0 -10px 40px rgba(0,0,0,.6);
    transform:translateY(100%);transition:transform .3s cubic-bezier(.2,1,.3,1);
    background-image:radial-gradient(rgba(255,255,255,.04) 1.4px,transparent 1.4px);background-size:22px 22px;
  }
  .drawer.open .drawer__panel{transform:translateY(0)}
  .drawer__head{position:sticky;top:0;background:var(--ink);padding:16px 18px;
    display:flex;align-items:center;gap:10px;border-bottom:var(--line);z-index:2}
  .drawer__head h3{font-family:var(--disp);text-transform:uppercase;font-size:24px;color:var(--yellow);letter-spacing:1px}
  .drawer__head .x{margin-left:auto;background:var(--magenta);color:#fff;border:var(--line);
    width:38px;height:38px;border-radius:50%;font-size:20px;cursor:pointer}
  .drawer__list{padding:14px 18px 120px;display:grid;gap:10px;
    grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}
  .drow{display:flex;align-items:center;gap:12px;background:var(--paper);border:1.5px solid var(--ink);
    box-shadow:var(--shadow-sm);padding:8px}
  .drow img{width:54px;height:54px;object-fit:contain;background:#fff;border:1.5px solid var(--ink)}
  .drow .info{display:flex;flex-direction:column}
  .drow .c{font-family:var(--mono);font-weight:700;color:var(--ink);font-size:13px}
  .drow .n{font-family:var(--body);font-size:11px;color:#555;font-weight:600}
  .drow .rm{margin-left:auto;background:var(--magenta);color:#fff;border:2px solid var(--ink);
    width:30px;height:30px;border-radius:50%;cursor:pointer;font-size:16px;line-height:1}
  .drawer__foot{position:sticky;bottom:0;background:var(--ink);border-top:var(--line);
    padding:14px 18px;display:flex;gap:10px;flex-wrap:wrap}
  .drawer__foot .btn.clear{background:var(--bg2);color:var(--txt)}
  .drawer__foot .btn.wa{background:var(--wa);color:#fff;flex:1;justify-content:center;font-size:15px}
  .empty{color:var(--mut);font-family:var(--mono);padding:30px;text-align:center;grid-column:1/-1}

  .toast{position:fixed;left:50%;bottom:96px;transform:translateX(-50%) translateY(20px);
    z-index:300;background:var(--lime);color:var(--ink);font-weight:700;
    border:var(--line);box-shadow:var(--shadow-sm);padding:10px 16px;
    font-family:var(--mono);font-size:13px;opacity:0;pointer-events:none;
    transition:opacity .2s,transform .2s;text-transform:uppercase}
  .toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
  .toast.rm{background:var(--magenta);color:#fff}

  footer{max-width:1280px;margin:30px auto 0;padding:0 20px 30px;
    font-family:var(--mono);font-size:11px;color:var(--mut);text-align:center}
  @media(max-width:520px){
    .bar__txt small{display:none}
    .bar .btn.view span{display:none}
    .grid{grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:10px}
    .lb__nav{width:42px;height:42px;font-size:22px}
    .lb__nav.prev{left:6px}
    .lb__nav.next{right:6px}
    .lb__code{font-size:22px}
  }
</style>
</head>
<body>

  <div class="marquee" aria-hidden="true">
    <div class="marquee__track">
      <span>HANDMADE BOOTLEG FIGURES</span><span>FAN ART TOYS</span><span>ORDER VIA WHATSAPP</span><span>WORLDWIDE SHIPPING</span><span>HANDMADE BOOTLEG FIGURES</span><span>FAN ART TOYS</span><span>ORDER VIA WHATSAPP</span><span>WORLDWIDE SHIPPING</span>
    </div>
  </div>

  <header>
    <div class="brand-wrap">
      <div class="brand">Milonga Customs</div>
      <span class="brand-sub">by Argentoy</span>
    </div>
    <p class="tagline">Custom fan-art & bootleg collectible figures. Not a toy.</p>
  </header>

  <!-- Buscador por nombre o código -->
  <div class="searchwrap">
    <input type="text" class="search-input" id="searchInput" placeholder="🔍 Search figure or code (e.g. Fort, CRS001)..." autocomplete="off">
  </div>

  <div class="navwrap"><nav class="nav" id="nav"></nav></div>

  <section class="sec">
    <h2 id="secTitle"></h2>
    <div class="sub" id="secSub"></div>
  </section>

  <main class="grid" id="grid"></main>

  <footer>Official Catalog · Milonga Customs by Argentoy · Direct orders via WhatsApp</footer>

  <!-- LIGHTBOX con carrusel -->
  <div class="lb" id="lb" role="dialog" aria-modal="true">
    <div class="lb__box">
      <button class="lb__x" id="lbX" aria-label="Close">×</button>
      <div class="lb__img" id="lbImgWrap">
        <button class="lb__nav prev" id="lbPrev" aria-label="Previous">‹</button>
        <img id="lbImg" alt="">
        <button class="lb__nav next" id="lbNext" aria-label="Next">›</button>
      </div>
      <div class="lb__meta">
        <div class="lb__code" id="lbCode"></div>
        <div class="lb__count" id="lbCount"></div>
      </div>
      <div class="lb__row">
        <button class="btn add" id="lbAdd">＋ Add to order</button>
        <button class="btn close" id="lbClose">Close</button>
      </div>
    </div>
  </div>

  <!-- DRAWER -->
  <div class="drawer" id="drawer">
    <div class="drawer__bg" id="drawerBg"></div>
    <div class="drawer__panel">
      <div class="drawer__head">
        <h3>Your Order</h3>
        <button class="x" id="drawerX" aria-label="Close">×</button>
      </div>
      <div class="drawer__list" id="drawerList"></div>
      <div class="drawer__foot">
        <button class="btn clear" id="clearBtn">Clear all</button>
        <button class="btn wa" id="drawerWa">Order via WhatsApp</button>
      </div>
    </div>
  </div>

  <!-- BARRA FLOTANTE -->
  <div class="bar" id="bar">
    <div class="bar__in">
      <div class="bar__count">
        <span class="bar__badge" id="barBadge">0</span>
        <span class="bar__txt">in your order<small>tap to view</small></span>
      </div>
      <button class="btn view" id="viewBtn">👁 <span>View</span></button>
      <button class="btn wa" id="barWa">Order via WhatsApp</button>
    </div>
  </div>

  <div class="toast" id="toast"></div>

<script>
""" + catalog_data_js + """

/* =========================================================
   ⚙️ CONFIGURACIÓN & TRADUCCIONES
   ========================================================= */
const WHATSAPP_NUMBER = "5491136355086";   // ✅ Updated WhatsApp number

const WA_INTRO = "Hola! 👋 I browsing the catalog and I would like to check price and availability for:";
const WA_OUTRO = "Could you please confirm total price and availability? Thank you!";

// Mapping old category names in dataset to English category names
const CAT_MAP_EN = {
  "Crossovers":                     "Crossovers",
  "Figuras publicas":               "Public Figures",
  "Animacion y Nostalgia Retro":    "Retro & Animation",
  "Musica":                         "Music",
  "Deportes":                       "Sports",
  "Cultura Pop, Memes y Virales":   "Pop Culture & Memes",
  "Cine, TV y Series":              "Movies & TV Series",
  "Anime y Videojuegos":            "Anime & Games"
};

// Update CATALOG_DATA categories to match English names while preserving original folder key
if (typeof CATALOG_DATA !== 'undefined') {
  CATALOG_DATA.forEach(item => {
    if (!item.originalCat) item.originalCat = item.cat;
    if (CAT_MAP_EN[item.cat]) item.cat = CAT_MAP_EN[item.cat];
  });
}

/* =========================================================
   📦 CATÁLOGO
   ========================================================= */
const CATS = [
  {key:"Crossovers",           origKey:"Crossovers",                  em:"🔀", pre:"CRS", from:1, to:26},
  {key:"Public Figures",       origKey:"Figuras publicas",            em:"🎭", pre:"FPU", from:1, to:58},
  {key:"Retro & Animation",    origKey:"Animacion y Nostalgia Retro", em:"📺", pre:"CAT", from:1, to:99},
  {key:"Music",                origKey:"Musica",                      em:"🎸", pre:"MUS", from:1, to:179},
  {key:"Sports",               origKey:"Deportes",                    em:"⚽", pre:"DEP", from:1, to:57},
  {key:"Pop Culture & Memes",  origKey:"Cultura Pop, Memes y Virales",em:"🤡", pre:"CPV", from:1, to:162},
  {key:"Movies & TV Series",   origKey:"Cine, TV y Series",           em:"🎬", pre:"CTS", from:1, to:159},
  {key:"Anime & Games",        origKey:"Anime y Videojuegos",         em:"🎮", pre:"AVG", from:1, to:37},
];

const pad = n => String(n).padStart(3,"0");
CATS.forEach(c=>{
  c.codes = [];
  for(let n=c.from;n<=c.to;n++) c.codes.push(c.pre+pad(n));
});

const ITEM_MAP = {};
if (typeof CATALOG_DATA !== 'undefined') {
  CATALOG_DATA.forEach(item => { ITEM_MAP[item.code] = item; });
}

const thumbOf = (k,code) => encodeURI(`${k}/thumbs/${code}_thumb.webp`);
const fullOf  = (k,code) => encodeURI(`${k}/Full/${code}_full.webp`);
const CAT_OF = {};
CATS.forEach(c=>c.codes.forEach(code=>CAT_OF[code]=c.origKey));

/* =========================================================
   🛒 SELECCIÓN (carrito) con guardado en el navegador
   ========================================================= */
const STORE = "argentoy_pedido_v1";
let selected = loadSel();
let selSet   = new Set(selected);

function loadSel(){ try{ return JSON.parse(localStorage.getItem(STORE))||[]; }catch(e){ return []; } }
function saveSel(){ localStorage.setItem(STORE, JSON.stringify(selected)); selSet=new Set(selected); }
function isSel(code){ return selSet.has(code); }

function toggle(code){
  if(isSel(code)){
    selected = selected.filter(c=>c!==code);
    toast(code+" removed", true);
  }else{
    selected.push(code);
    toast(code+" added ✓", false);
  }
  saveSel();
  syncCard(code);
  updateBar();
  if(lb.classList.contains("open") && lbCode.dataset.code===code) syncLbButton(code);
  if(drawer.classList.contains("open")) renderDrawer();
}

/* =========================================================
   🎨 RENDER
   ========================================================= */
const nav   = document.getElementById("nav");
const grid  = document.getElementById("grid");
const secTitle = document.getElementById("secTitle");
const secSub   = document.getElementById("secSub");
const searchInput = document.getElementById("searchInput");

let activeCat = 5; // Pop Culture & Memes by default
let searchQuery = "";
let currentActiveItems = [];

function renderNav(){
  nav.innerHTML = "";
  CATS.forEach((c,i)=>{
    const b = document.createElement("button");
    b.className = "pill"+(i===activeCat && !searchQuery?" active":"");
    b.innerHTML = `<span class="em">${c.em}</span>${c.key}<span class="cnt">${c.codes.length}</span>`;
    b.onclick = ()=>{ 
      activeCat=i; 
      searchQuery=""; 
      searchInput.value="";
      renderNav(); 
      renderGrid(); 
      window.scrollTo({top:0,behavior:"smooth"}); 
    };
    nav.appendChild(b);
  });
}

function renderGrid(){
  grid.innerHTML = "";
  
  if (searchQuery.trim()) {
    const q = searchQuery.toLowerCase().trim();
    currentActiveItems = CATALOG_DATA.filter(item => {
      const mCode = item.code.toLowerCase().includes(q);
      const mName = item.name && item.name.toLowerCase().includes(q);
      const mCat  = item.cat && item.cat.toLowerCase().includes(q);
      return mCode || mName || mCat;
    });
    secTitle.innerHTML = `<span class="em">🔍</span>Search: "${searchQuery}"`;
    secSub.textContent = `${currentActiveItems.length} figures found`;
  } else {
    const c = CATS[activeCat];
    currentActiveItems = CATALOG_DATA.filter(item => item.cat === c.key);
    secTitle.innerHTML = `<span class="em">${c.em}</span>${c.key}`;
    secSub.textContent = `${currentActiveItems.length} figures · tap to expand`;
  }

  if (currentActiveItems.length === 0) {
    grid.innerHTML = `<div class="empty">No figures found matching your search.</div>`;
    return;
  }

  currentActiveItems.forEach((item, idx)=>{
    const code = item.code;
    const cat = item.originalCat || item.cat;
    const card = document.createElement("div");
    card.className = "card"+(isSel(code)?" sel":"");
    card.dataset.code = code;
    card.style.animationDelay = Math.min(idx,14)*18 + "ms";

    const titleLabel = item.name ? item.name : code;

    card.innerHTML = `
      <span class="code">${code}</span>
      <button class="pick" aria-label="Add ${code}">${isSel(code)?"✓":"+"}</button>
      <div class="ph"><img src="${thumbOf(cat,code)}" alt="${code}" loading="lazy" decoding="async" onerror="this.style.display='none'"></div>
      <div class="card-title" title="${titleLabel}">${titleLabel}</div>`;
    
    card.querySelector(".ph").onclick = ()=>openLb(code);
    card.querySelector(".pick").onclick = (e)=>{ e.stopPropagation(); toggle(code); };
    grid.appendChild(card);
  });
}

searchInput.oninput = (e) => {
  searchQuery = e.target.value;
  renderNav();
  renderGrid();
};

function syncCard(code){
  const card = grid.querySelector(`.card[data-code="${code}"]`);
  if(!card) return;
  const on = isSel(code);
  card.classList.toggle("sel", on);
  card.querySelector(".pick").textContent = on ? "✓" : "+";
}

/* ===== Barra flotante ===== */
const bar = document.getElementById("bar");
const barBadge = document.getElementById("barBadge");
function updateBar(){
  const n = selected.length;
  barBadge.textContent = n;
  bar.classList.toggle("show", n>0);
  barBadge.classList.remove("bump"); void barBadge.offsetWidth; barBadge.classList.add("bump");
}

/* ===== Lightbox + carrusel ===== */
const lb = document.getElementById("lb");
const lbImg = document.getElementById("lbImg");
const lbImgWrap = document.getElementById("lbImgWrap");
const lbCode = document.getElementById("lbCode");
const lbCount = document.getElementById("lbCount");
const lbAdd = document.getElementById("lbAdd");
let lbIndex = 0;

function openLb(code){
  lbIndex = currentActiveItems.findIndex(it => it.code === code);
  if(lbIndex < 0) lbIndex = 0;
  paintLb(false);
  lb.classList.add("open");
}

function paintLb(animate, dir){
  if (!currentActiveItems || currentActiveItems.length === 0) return;
  const item = currentActiveItems[lbIndex];
  const code = item.code;
  const cat = item.originalCat || item.cat;
  
  lbCode.dataset.code = code;
  lbCode.textContent = item.name ? `${item.name} (${code})` : code;
  lbImg.src = fullOf(cat, code);
  lbImg.alt = code;
  lbCount.textContent = (lbIndex + 1) + " / " + currentActiveItems.length;
  syncLbButton(code);
  
  if(animate){
    lbImg.classList.remove("swapL","swapR");
    void lbImg.offsetWidth;
    lbImg.classList.add(dir >= 0 ? "swapR" : "swapL");
  }
}

function lbGo(dir){
  const len = currentActiveItems.length;
  if (len === 0) return;
  lbIndex = (lbIndex + dir + len) % len;
  paintLb(true, dir);
}

function syncLbButton(code){
  const on = isSel(code);
  lbAdd.classList.toggle("is-sel", on);
  lbAdd.innerHTML = on ? "✓ In order — remove" : "＋ Add to order";
}

function closeLb(){ lb.classList.remove("open"); }

lbAdd.onclick = ()=>toggle(lbCode.dataset.code);
document.getElementById("lbX").onclick = closeLb;
document.getElementById("lbClose").onclick = closeLb;
document.getElementById("lbPrev").onclick = (e)=>{ e.stopPropagation(); lbGo(-1); };
document.getElementById("lbNext").onclick = (e)=>{ e.stopPropagation(); lbGo(1); };
lb.onclick = e=>{ if(e.target===lb) closeLb(); };

/* swipe táctil sobre la foto (celu) */
let touchX = null;
lbImgWrap.addEventListener("touchstart", e=>{
  if(e.target.closest(".lb__nav")) return;
  touchX = e.changedTouches[0].clientX;
}, {passive:true});

lbImgWrap.addEventListener("touchend", e=>{
  if(touchX === null) return;
  const dx = e.changedTouches[0].clientX - touchX;
  if(Math.abs(dx) > 45) lbGo(dx < 0 ? 1 : -1);
  touchX = null;
}, {passive:true});

/* ===== Drawer ===== */
const drawer = document.getElementById("drawer");
const drawerList = document.getElementById("drawerList");
function openDrawer(){ renderDrawer(); drawer.classList.add("open"); }
function closeDrawer(){ drawer.classList.remove("open"); }

function renderDrawer(){
  if(selected.length===0){
    drawerList.innerHTML = `<div class="empty">No collectibles selected yet.<br>Close this and tap the ＋ buttons in the catalog.</div>`;
    return;
  }
  drawerList.innerHTML = "";
  selected.forEach(code=>{
    const item = ITEM_MAP[code];
    const k = item ? (item.originalCat || item.cat) : CAT_OF[code];
    
    const row = document.createElement("div");
    row.className = "drow";
    row.innerHTML = `
      <img src="${thumbOf(k,code)}" alt="${code}" onerror="this.style.display='none'">
      <div class="info">
        <span class="c">${code}</span>
        ${item && item.name ? `<span class="n">${item.name}</span>` : ''}
      </div>
      <button class="rm" aria-label="Remove ${code}">×</button>`;
    row.querySelector(".rm").onclick = ()=>toggle(code);
    drawerList.appendChild(row);
  });
}

document.getElementById("viewBtn").onclick = openDrawer;
document.getElementById("drawerX").onclick = closeDrawer;
document.getElementById("drawerBg").onclick = closeDrawer;
document.getElementById("clearBtn").onclick = ()=>{
  if(selected.length && confirm("Clear all items from your order?")){ 
    selected=[]; 
    saveSel(); 
    updateBar(); 
    renderDrawer(); 
    renderGrid(); 
    toast("Order cleared", true); 
  }
};

/* ===== WhatsApp ===== */
function waLink(){
  if(!WHATSAPP_NUMBER){
    alert("WhatsApp number is not configured.");
    return null;
  }
  if(selected.length===0){ toast("Select at least one figure", true); return null; }
  const lista = selected.map(c => {
    const item = ITEM_MAP[c];
    return (item && item.name) ? `• ${c} - ${item.name}` : `• ${c}`;
  }).join("%0A");
  
  const n = selected.length;
  const fig = n === 1 ? "item" : "items";
  const msg = `*Order from catalog* 🧸%0A${encodeURIComponent(WA_INTRO)}%0A${lista}%0A%0ATotal: ${n} ${fig}.%0A${encodeURIComponent(WA_OUTRO)}`;
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${msg}`;
}

function goWa(){ const u=waLink(); if(u) window.open(u,"_blank"); }
document.getElementById("barWa").onclick = goWa;
document.getElementById("drawerWa").onclick = goWa;

/* ===== Toast ===== */
const toastEl = document.getElementById("toast");
let toastT;
function toast(msg, isRemove){
  toastEl.textContent = msg;
  toastEl.classList.toggle("rm", !!isRemove);
  toastEl.classList.add("show");
  clearTimeout(toastT);
  toastT = setTimeout(()=>toastEl.classList.remove("show"), 1400);
}

/* ===== Teclado ===== */
document.addEventListener("keydown", e=>{
  if(e.key==="Escape"){ closeLb(); closeDrawer(); }
  if(lb.classList.contains("open")){
    if(e.key==="ArrowLeft"){ lbGo(-1); e.preventDefault(); }
    if(e.key==="ArrowRight"){ lbGo(1); e.preventDefault(); }
  }
});

/* ===== Arranque ===== */
renderNav();
renderGrid();
updateBar();
</script>
</body>
</html>"""

with open('e:/catalogo/index.html', 'w', encoding='utf-8') as f:
    f.write(english_html)

with open('e:/catalogo/prueba-C.html', 'w', encoding='utf-8') as f:
    f.write(english_html)

print("Catalog successfully updated to English version with all requested requirements!")
