import json

with open('e:/catalogo/catalog_data.js', 'r', encoding='utf-8') as f:
    catalog_data_js = f.read()

final_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ARGENTOY x MILONGA CUSTOMS · Official Catalog</title>
<meta name="description" content="Official bootleg fan art custom figures catalog. Select your collectibles and place your order directly via WhatsApp.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Oswald:wght@500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg-dark: #0e0f14;
    --bg-card: #161820;
    --bg-card-hover: #1e212b;
    --border-card: rgba(255, 255, 255, 0.08);
    --border-card-hover: rgba(250, 204, 21, 0.4);
    --text-main: #f1f3f9;
    --text-muted: #8b90a0;
    --accent-yellow: #ffd23f;
    --accent-magenta: #ff2e7e;
    --accent-pink: #ff2e7e;
    --accent-lime: #c6ff3a;
    --wa-color: #25d366;
    
    --font-heading: 'Oswald', sans-serif;
    --font-body: 'Inter', sans-serif;
    --font-mono: 'Space Mono', monospace;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }

  body {
    font-family: var(--font-body);
    background-color: var(--bg-dark);
    color: var(--text-main);
    min-height: 100vh;
    padding-bottom: 120px;
    -webkit-tap-highlight-color: transparent;
    overflow-x: hidden;
  }

  /* Marquesina Superior */
  .marquee {
    background: var(--accent-magenta);
    color: #0a0910;
    font-weight: 800;
    border-bottom: 3px solid #0a0910;
    overflow: hidden;
    white-space: nowrap;
    font-family: var(--font-heading);
    letter-spacing: 1px;
    text-transform: uppercase;
    font-size: 14px;
  }

  .marquee__track {
    display: inline-block;
    animation: scroll 26s linear infinite;
    padding: 7px 0;
  }

  .marquee__track span { padding: 0 18px; }
  .marquee__track span::after { content: "✦"; padding-left: 36px; opacity: 0.7; }

  @keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
  }

  /* Header */
  header {
    max-width: 1280px;
    margin: 0 auto;
    padding: 24px 20px 12px;
  }

  .brand-wrap {
    display: flex;
    align-items: baseline;
    gap: 10px;
    flex-wrap: wrap;
  }

  .brand {
    font-family: var(--font-heading);
    font-size: clamp(32px, 6vw, 54px);
    line-height: 1;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-main);
    font-weight: 700;
  }

  .brand span {
    color: var(--accent-yellow);
  }

  .brand-sub {
    font-family: var(--font-mono);
    font-size: 12px;
    color: var(--text-muted);
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }

  .tagline {
    margin-top: 8px;
    max-width: 680px;
    font-size: clamp(13px, 2vw, 15px);
    color: var(--accent-yellow);
    line-height: 1.4;
    font-weight: 600;
    letter-spacing: 0.2px;
  }

  /* Buscador */
  .searchwrap {
    max-width: 1280px;
    margin: 16px auto 0;
    padding: 0 20px;
  }

  .search-input {
    width: 100%;
    background: var(--bg-card);
    color: var(--text-main);
    border: 1px solid var(--border-card);
    padding: 12px 16px;
    border-radius: 10px;
    font-family: var(--font-body);
    font-size: 14px;
    outline: none;
    transition: all 0.2s ease;
  }

  .search-input:focus {
    border-color: var(--accent-yellow);
    box-shadow: 0 0 0 3px rgba(250, 204, 21, 0.15);
  }

  /* Nav Categorías en Mobile & Desktop */
  .navwrap {
    position: sticky;
    top: 0;
    z-index: 50;
    background: rgba(14, 15, 20, 0.95);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border-card);
    margin-top: 16px;
  }

  .navwrap::after {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    width: 40px;
    background: linear-gradient(to right, transparent, rgba(14, 15, 20, 0.92));
    pointer-events: none;
  }

  .nav {
    max-width: 1280px;
    margin: 0 auto;
    display: flex;
    gap: 10px;
    padding: 12px 20px;
    overflow-x: auto;
    scrollbar-width: none;
    scroll-behavior: smooth;
  }

  .nav::-webkit-scrollbar { display: none; }

  /* Botones inactivos con mayor contraste y borde visible */
  .pill {
    flex: 0 0 auto;
    cursor: pointer;
    font-family: var(--font-body);
    font-weight: 700;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    background: #282338;
    color: var(--text-main);
    border: 1.5px solid #ffd23f;
    padding: 10px 16px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    gap: 9px;
    transition: all 0.2s ease;
  }

  .pill:hover {
    background: var(--bg-card-hover);
    border-color: #ffe066;
    transform: translateY(-2px);
  }

  .pill.active {
    background: var(--accent-yellow);
    color: #000;
    border-color: var(--accent-yellow);
    font-weight: 800;
  }

  .pill .cnt {
    font-family: var(--font-mono);
    font-size: 11px;
    background: rgba(0, 0, 0, 0.35);
    color: var(--accent-yellow);
    padding: 1px 7px;
    border-radius: 6px;
  }

  .pill.active .cnt {
    background: #000;
    color: var(--accent-yellow);
  }

  /* Sección Principal */
  .sec {
    max-width: 1280px;
    margin: 0 auto;
    padding: 24px 20px 0;
  }

  .sec h2 {
    font-family: var(--font-heading);
    text-transform: uppercase;
    font-size: clamp(26px, 4.5vw, 40px);
    line-height: 1;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .sec .sub {
    font-family: var(--font-mono);
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 6px;
  }

  /* Grilla de Tarjetas */
  .grid {
    max-width: 1280px;
    margin: 0 auto;
    padding: 18px 20px;
    display: grid;
    gap: 16px;
    grid-template-columns: repeat(auto-fill, minmax(145px, 1fr));
  }

  /* Card Item */
  .card {
    position: relative;
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: 12px;
    padding: 8px;
    cursor: pointer;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  }

  .card:hover {
    transform: translateY(-4px);
    border-color: var(--border-card-hover);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.5);
  }

  .card.sel {
    border-color: var(--accent-yellow);
    box-shadow: 0 0 0 2px var(--accent-yellow);
  }

  /* Discreto cartelito de código arriba a la izquierda */
  .code {
    position: absolute;
    top: 8px;
    left: 8px;
    z-index: 3;
    font-family: var(--font-mono);
    font-weight: 700;
    font-size: 10px;
    background: rgba(14, 15, 20, 0.85);
    backdrop-filter: blur(4px);
    color: var(--text-muted);
    padding: 2px 6px;
    border-radius: 4px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    letter-spacing: 0.5px;
  }

  /* Contenedor de foto con MARCA DE AGUA */
  .card .ph {
    position: relative;
    aspect-ratio: 1/1;
    background: #ffffff;
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .card .ph img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    transition: transform 0.25s ease;
  }

  .card:hover .ph img { transform: scale(1.05); }

  /* Marca de agua visual en tarjetas (.ph::after) */
  .card .ph::after {
    content: "ARGENTOY GLOBAL";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-30deg);
    opacity: 0.20;
    font-family: var(--font-mono);
    font-size: 13px;
    font-weight: 700;
    color: #ffffff;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
    pointer-events: none;
    white-space: nowrap;
    letter-spacing: 2px;
    z-index: 2;
  }

  /* Botón + Flotante en la esquina inferior derecha */
  .pick {
    position: absolute;
    bottom: 8px;
    right: 8px;
    z-index: 3;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    border: none;
    background: var(--accent-yellow);
    color: #000;
    font-size: 20px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    line-height: 1;
    transition: transform 0.15s ease, background 0.15s ease;
    font-family: var(--font-body);
  }

  .pick:hover { transform: scale(1.15); }
  .card.sel .pick { background: var(--wa-color); color: #fff; }

  .card-title {
    font-family: var(--font-body);
    font-weight: 600;
    font-size: 11px;
    color: var(--text-main);
    margin-top: 8px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: left;
    padding-right: 36px;
  }

  /* Lightbox / Modal */
  .lb {
    position: fixed;
    inset: 0;
    z-index: 200;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 16px;
    background: rgba(0, 0, 0, 0.85);
    backdrop-filter: blur(8px);
  }

  .lb.open { display: flex; animation: fade 0.2s ease; }
  @keyframes fade { from { opacity: 0; } to { opacity: 1; } }

  .lb__box {
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: 16px;
    max-width: min(500px, 94vw);
    width: 100%;
    padding: 16px;
    position: relative;
    box-shadow: 0 25px 50px rgba(0,0,0,0.8);
  }

  /* Contenedor de foto ampliada con MARCA DE AGUA */
  .lb__img {
    position: relative;
    background: #ffffff;
    border-radius: 12px;
    aspect-ratio: 1/1;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  .lb__img img { width: 100%; height: 100%; object-fit: contain; }

  /* Marca de agua visual en visor Lightbox (.lb__img::after) */
  .lb__img::after {
    content: "ARGENTOY GLOBAL";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-30deg);
    opacity: 0.20;
    font-family: var(--font-mono);
    font-size: 22px;
    font-weight: 700;
    color: #ffffff;
    text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8);
    pointer-events: none;
    white-space: nowrap;
    letter-spacing: 3px;
    z-index: 5;
  }

  .lb__nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 6;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: 1px solid rgba(255, 255, 255, 0.2);
    background: rgba(14, 15, 20, 0.8);
    color: var(--text-main);
    font-size: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    backdrop-filter: blur(4px);
    transition: all 0.15s ease;
  }

  .lb__nav:hover { background: var(--accent-yellow); color: #000; }
  .lb__nav.prev { left: 10px; }
  .lb__nav.next { right: 10px; }

  .lb__meta { margin-top: 14px; }
  .lb__code { font-family: var(--font-heading); font-size: 22px; color: var(--accent-yellow); letter-spacing: 0.5px; }
  .lb__count { font-family: var(--font-mono); font-size: 11px; color: var(--text-muted); margin-top: 2px; }

  .lb__row { display: flex; gap: 10px; margin-top: 14px; }

  .btn {
    font-family: var(--font-body);
    font-weight: 700;
    font-size: 13px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    padding: 12px 18px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    transition: all 0.15s ease;
  }

  .btn.add { background: var(--accent-yellow); color: #000; flex: 1; }
  .btn.add.is-sel { background: var(--wa-color); color: #fff; }
  .btn.close { background: rgba(255, 255, 255, 0.08); color: var(--text-main); }
  
  .lb__x {
    position: absolute;
    top: 12px;
    right: 12px;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: rgba(0, 0, 0, 0.6);
    color: #fff;
    border: 1px solid rgba(255, 255, 255, 0.2);
    font-size: 18px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
  }

  /* Barra Flotante WhatsApp Siempre Visible */
  .bar {
    position: fixed;
    left: 50%;
    transform: translateX(-50%);
    bottom: 20px;
    z-index: 120;
    width: calc(100% - 32px);
    max-width: 540px;
    background: rgba(22, 24, 32, 0.95);
    backdrop-filter: blur(16px);
    border: 1px solid var(--border-card);
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.6);
    border-radius: 16px;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .bar__count { display: flex; align-items: center; gap: 10px; color: var(--text-main); font-weight: 600; }
  .bar__badge { font-family: var(--font-mono); font-weight: 700; background: var(--accent-yellow); color: #000; min-width: 28px; height: 28px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 13px; }
  .bar__txt { font-size: 12px; }
  .bar__txt small { display: block; font-family: var(--font-mono); font-size: 10px; color: var(--text-muted); }
  .bar .actions { display: flex; gap: 8px; }
  .bar .btn.view { background: rgba(255, 255, 255, 0.08); color: var(--text-main); }
  .bar .btn.wa { background: var(--wa-color); color: #fff; font-weight: 700; }

  /* Drawer */
  .drawer { position: fixed; inset: 0; z-index: 180; display: none; }
  .drawer.open { display: block; }
  .drawer__bg { position: absolute; inset: 0; background: rgba(0,0,0,0.7); }
  .drawer__panel { position: absolute; left: 0; right: 0; bottom: 0; max-height: 80vh; overflow: auto; background: var(--bg-card); border-top: 1px solid var(--border-card); border-radius: 20px 20px 0 0; padding-bottom: 20px; }
  .drawer__head { position: sticky; top: 0; background: var(--bg-card); padding: 16px 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border-card); z-index: 2; }
  .drawer__head h3 { font-family: var(--font-heading); font-size: 22px; color: var(--accent-yellow); text-transform: uppercase; }
  .drawer__head .x { background: rgba(255, 255, 255, 0.08); color: #fff; border: none; width: 32px; height: 32px; border-radius: 50%; font-size: 18px; cursor: pointer; }
  .drawer__list { padding: 16px 20px 100px; display: grid; gap: 10px; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); }
  .drow { display: flex; align-items: center; gap: 12px; background: rgba(255,255,255,0.03); border: 1px solid var(--border-card); border-radius: 10px; padding: 8px; }
  .drow img { width: 48px; height: 48px; object-fit: contain; background: #fff; border-radius: 6px; }
  .drow .info { display: flex; flex-direction: column; }
  .drow .c { font-family: var(--font-mono); font-weight: 700; color: var(--accent-yellow); font-size: 12px; }
  .drow .n { font-size: 11px; color: var(--text-muted); font-weight: 500; }
  .drow .rm { margin-left: auto; background: rgba(255,46,126,0.15); color: var(--accent-pink); border: none; width: 28px; height: 28px; border-radius: 50%; cursor: pointer; font-size: 14px; }
  .drawer__foot { position: sticky; bottom: 0; background: var(--bg-card); border-top: 1px solid var(--border-card); padding: 14px 20px; display: flex; gap: 10px; }

  .empty { color: var(--text-muted); font-family: var(--font-mono); padding: 30px; text-align: center; grid-column: 1/-1; }
  .toast { position: fixed; left: 50%; bottom: 90px; transform: translateX(-50%) translateY(20px); z-index: 300; background: var(--accent-yellow); color: #000; font-weight: 700; border-radius: 8px; padding: 10px 18px; font-family: var(--font-mono); font-size: 12px; opacity: 0; pointer-events: none; transition: all 0.2s ease; text-transform: uppercase; }
  .toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
  .toast.rm { background: var(--accent-pink); color: #fff; }

  footer { max-width: 1280px; margin: 30px auto 0; padding: 0 20px 30px; font-family: var(--font-mono); font-size: 11px; color: var(--text-muted); text-align: center; }
</style>
</head>
<body>

  <!-- Marquesina Superior -->
  <div class="marquee" aria-hidden="true">
    <div class="marquee__track">
      <span>HANDMADE BOOTLEG TOYS</span><span>WORLDWIDE SHIPPING</span><span>BULK DISCOUNTS</span><span>CHECK STOCK VIA WHATSAPP</span><span>100% ARTISANAL</span><span>HANDMADE BOOTLEG TOYS</span><span>WORLDWIDE SHIPPING</span><span>BULK DISCOUNTS</span><span>CHECK STOCK VIA WHATSAPP</span><span>100% ARTISANAL</span>
    </div>
  </div>

  <header>
    <div class="brand-wrap">
      <h1 class="brand">100% <span>MILONGA</span></h1>
      <span class="brand-sub">by Argentoy International</span>
    </div>
    <p class="tagline">Adult collectibles. Not toys. TAP＋ TO CHECK STOCK via WhatsApp</p>
  </header>

  <!-- Buscador estricto por nombre -->
  <div class="searchwrap">
    <input type="text" class="search-input" id="searchInput" placeholder="🔍 Search..." autocomplete="off">
  </div>

  <div class="navwrap"><nav class="nav" id="nav"></nav></div>

  <section class="sec">
    <h2 id="secTitle"></h2>
    <div class="sub" id="secSub"></div>
  </section>

  <main class="grid" id="grid"></main>

  <footer>Official Catalog · Milonga Customs by Argentoy · Direct orders via WhatsApp</footer>

  <!-- LIGHTBOX -->
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
        <button class="btn add" id="lbAdd">＋ Check Stock & Price</button>
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
        <button class="btn close" id="clearBtn">Clear all</button>
        <button class="btn wa" id="drawerWa">Order via WhatsApp</button>
      </div>
    </div>
  </div>

  <!-- BARRA FLOTANTE SIEMPRE VISIBLE DE WHATSAPP -->
  <div class="bar" id="bar">
    <div class="bar__count">
      <span class="bar__badge" id="barBadge">0</span>
      <span class="bar__txt">in your order<small>tap to view</small></span>
    </div>
    <div class="actions">
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
const WHATSAPP_NUMBER = "5491136355086";

const WA_INTRO = "Hola! 👋";
const WA_OUTRO = "Hola! 👋";

// Mapping dataset categories to English names
const CAT_MAP_EN = {
  "Cultura Pop, Memes y Virales":   "Pop Culture & Memes",
  "Cine, TV y Series":              "Movies & TV Series",
  "Musica":                         "Music",
  "Animacion y Nostalgia Retro":    "Retro & Animation",
  "Figuras publicas":               "Famous People",
  "Deportes":                       "Sports",
  "Crossovers":                     "Crossovers",
  "Anime y Videojuegos":            "Anime & Games"
};

// Update CATALOG_DATA categories to match English names
if (typeof CATALOG_DATA !== 'undefined') {
  CATALOG_DATA.forEach(item => {
    if (!item.originalCat) item.originalCat = item.cat;
    if (CAT_MAP_EN[item.cat]) item.cat = CAT_MAP_EN[item.cat];
  });
}

/* =========================================================
   📦 CATÁLOGO - ORDEN DE CATEGORÍAS (Requerimiento 1)
   ========================================================= */
const CATS = [
  {key:"Pop Culture & Memes",  origKey:"Cultura Pop, Memes y Virales",em:"🤡", pre:"CPV", from:1, to:163},
  {key:"Movies & TV Series",   origKey:"Cine, TV y Series",           em:"🎬", pre:"CTS", from:1, to:159},
  {key:"Music",                origKey:"Musica",                      em:"🎸", pre:"MUS", from:1, to:179},
  {key:"Retro & Animation",    origKey:"Animacion y Nostalgia Retro", em:"📺", pre:"CAT", from:1, to:99},
  {key:"Famous People",        origKey:"Figuras publicas",            em:"🎭", pre:"FPU", from:1, to:58},
  {key:"Sports",               origKey:"Deportes",                    em:"⚽", pre:"DEP", from:1, to:57},
  {key:"Crossovers",           origKey:"Crossovers",                  em:"🔀", pre:"CRS", from:1, to:26},
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

let activeCat = 0; // Pop Culture & Memes por defecto en la posición 0
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
    // Búsqueda por nombre de figura
    currentActiveItems = CATALOG_DATA.filter(item => {
      return item.name && item.name.toLowerCase().includes(q);
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

    const titleLabel = item.name ? item.name : code;

    card.innerHTML = `
      <span class="code">${code}</span>
      <div class="ph"><img src="${thumbOf(cat,code)}" alt="${code}" loading="lazy" decoding="async" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'100\\' height=\\'100\\'%3E%3Crect width=\\'100%25\\' height=\'100%25\\' fill=\\'%23161820\\'%2/>%3C/svg%3E'"></div>
      <div class="card-title" title="${titleLabel}">${titleLabel}</div>
      <button class="pick" aria-label="Add ${code}">${isSel(code)?"✓":"+"}</button>`;
    
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
  bar.classList.add("show");
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
  lbAdd.innerHTML = on ? "✓ Selected — Remove" : "＋ Check Stock & Price";
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
  const itemTxt = n === 1 ? "item" : "items";
  const msg = `${encodeURIComponent(WA_INTRO)}%0A${lista}%0A%0ATotal: ${n} ${itemTxt}.%0A${encodeURIComponent(WA_OUTRO)}`;
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
    f.write(final_html)

with open('e:/catalogo/prueba-C.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Catalog successfully updated with watermark, category reordering, marquee styles, mobile nav enhancements, and lightbox button text!")
