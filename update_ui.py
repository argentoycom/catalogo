import re

with open('e:/catalogo/prueba-C.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for Header, Nav Pills, Image Background, and Modal Nav Buttons
css_replacements = [
    # Reduce Header Title Size
    (r'\.title-brand\s*\{[^}]*\}', 
     """.title-brand {
    font-family: var(--font-display);
    font-size: clamp(28px, 5vw, 52px);
    line-height: 0.95;
    letter-spacing: 1px;
    text-transform: uppercase;
    background: linear-gradient(135deg, #ffffff 30%, #a5b4fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }"""),
  
    # Reduce Header Padding
    (r'header\s*\{[^}]*\}', 
     """header {
    max-width: 1280px;
    margin: 0 auto;
    padding: 20px 20px 10px;
  }"""),
  
    # Make Nav Pills larger and more prominent
    (r'\.pill-btn\s*\{[^}]*\}', 
     """.pill-btn {
    flex: 0 0 auto;
    background: var(--bg-card);
    border: 1.5px solid rgba(255, 255, 255, 0.15);
    color: var(--text-main);
    font-family: var(--font-sans);
    font-weight: 700;
    font-size: 15px;
    padding: 10px 20px;
    border-radius: 12px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: all 0.2s ease;
  }"""),

    # Neutral soft light gray background for figure images instead of stark white/black
    (r'\.card-image-wrap\s*\{[^}]*\}', 
     """.card-image-wrap {
    position: relative;
    width: 100%;
    aspect-ratio: 4/5;
    background: #e2e4e9;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }"""),

    (r'\.modal-img-container\s*\{[^}]*\}', 
     """.modal-img-container {
    position: relative;
    width: 100%;
    aspect-ratio: 4/5;
    background: #d8dae2;
    display: flex;
    align-items: center;
    justify-content: center;
  }""")
]

for pattern, repl in css_replacements:
    html = re.sub(pattern, repl, html)

# Add Modal Nav Arrow CSS if not present
modal_arrow_css = """
  /* Modal Navigation Arrows */
  .modal-nav-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: rgba(15, 16, 21, 0.75);
    backdrop-filter: blur(4px);
    color: #fff;
    border: 1.5px solid rgba(255, 255, 255, 0.3);
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 15;
    transition: all 0.2s ease;
    user-select: none;
  }

  .modal-nav-btn:hover {
    background: var(--accent-yellow);
    color: #000;
    border-color: var(--accent-yellow);
    transform: translateY(-50%) scale(1.1);
  }

  .modal-nav-btn.prev { left: 12px; }
  .modal-nav-btn.next { right: 12px; }
"""

if '.modal-nav-btn' not in html:
    html = html.replace('</style>', modal_arrow_css + '\n</style>')

# Add Modal HTML Left/Right Navigation Buttons
modal_arrows_html = """
      <button class="modal-close" id="modalClose">✕</button>
      <button class="modal-nav-btn prev" id="modalPrev" title="Anterior (flecha izquierda)">◀</button>
      <button class="modal-nav-btn next" id="modalNext" title="Siguiente (flecha derecha)">▶</button>
"""

html = re.sub(r'<button class="modal-close" id="modalClose">✕</button>', modal_arrows_html.strip(), html)

# Replace thumbOf with fullOf in renderGrid so grid images use Full 1200x1200px quality!
html = html.replace('src="${thumbOf(cat, code)}"', 'src="${fullOf(cat, code)}"')

with open('e:/catalogo/prueba-C.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated CSS, image resolution, and Modal arrow elements in prueba-C.html!")
