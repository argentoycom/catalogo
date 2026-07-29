import re

with open('e:/catalogo/prueba-C.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update JS for modal navigation
js_nav_code = """
let activeItems = [];
let currentModalIndex = 0;

const modalPrev = document.getElementById("modalPrev");
const modalNext = document.getElementById("modalNext");

function openModal(code, cat, forcedIndex = -1) {
  if (forcedIndex >= 0) {
    currentModalIndex = forcedIndex;
  } else {
    currentModalIndex = activeItems.findIndex(it => it.code === code);
    if (currentModalIndex < 0) currentModalIndex = 0;
  }

  const item = ITEM_MAP[code] || activeItems[currentModalIndex];
  if (!item) return;

  modalCode.textContent = (item.name) ? `${item.name} (${item.code})` : item.code;
  modalCat.textContent = `Categoría: ${item.cat}`;
  modalImg.src = fullOf(item.cat, item.code);
  modalOverlay.classList.add("open");

  const isSel = selectedCodes.has(item.code);
  modalAddBtn.textContent = isSel ? "Quitar del pedido" : "+ Agregar al pedido";
  modalAddBtn.onclick = () => {
    toggleSelect(item.code);
    openModal(item.code, item.cat, currentModalIndex);
  };
}

function modalGo(delta) {
  if (!activeItems || activeItems.length === 0) return;
  currentModalIndex = (currentModalIndex + delta + activeItems.length) % activeItems.length;
  const item = activeItems[currentModalIndex];
  openModal(item.code, item.cat, currentModalIndex);
}

if (modalPrev) modalPrev.onclick = (e) => { e.stopPropagation(); modalGo(-1); };
if (modalNext) modalNext.onclick = (e) => { e.stopPropagation(); modalGo(1); };

document.addEventListener('keydown', (e) => {
  if (!modalOverlay.classList.contains('open')) return;
  if (e.key === 'ArrowLeft') modalGo(-1);
  if (e.key === 'ArrowRight') modalGo(1);
  if (e.key === 'Escape') modalOverlay.classList.remove('open');
});
"""

# Store currentItems into activeItems in renderGrid
html = html.replace('secSubtitle.textContent = `Se encontraron ${currentItems.length} figuras`;', 
                    'secSubtitle.textContent = `Se encontraron ${currentItems.length} figuras`; activeItems = currentItems;')

html = html.replace('secSubtitle.textContent = `${currentItems.length} figuras de colección disponibles`;', 
                    'secSubtitle.textContent = `${currentItems.length} figuras de colección disponibles`; activeItems = currentItems;')

# Replace openModal function definition with js_nav_code
old_open_modal_pattern = r'function openModal\(code, cat\) \{[\s\S]*?modalOverlay\.classList\.remove\("open"\);\n\};'

html = re.sub(old_open_modal_pattern, js_nav_code.strip() + '\n\nmodalClose.onclick = () => modalOverlay.classList.remove("open");', html)

with open('e:/catalogo/prueba-C.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('e:/catalogo/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Modal arrow navigation script updated in prueba-C.html and index.html!")
