import json

# Load CATALOG_DATA text
with open('e:/catalogo/catalog_data.js', encoding='utf-8') as f:
    js_data = f.read()

# Load prueba-C.html
with open('e:/catalogo/prueba-C.html', encoding='utf-8') as f:
    html = f.read()

# Replace <script src="catalog_data.js"></script> with inline js_data
target_script_tag = '<script src="catalog_data.js"></script>'
if target_script_tag in html:
    html = html.replace(target_script_tag, '')

# Inject js_data right inside <script>
script_marker = '<script>'
html = html.replace(script_marker, script_marker + '\n' + js_data + '\n', 1)

# Ensure codes population exists
codes_pop_code = """
const pad = n => String(n).padStart(3,"0");
CATS.forEach(c => {
  c.codes = [];
  for(let n=c.from; n<=c.to; n++) c.codes.push(c.pre + pad(n));
});
"""

if 'const pad =' not in html:
    html = html.replace('const ITEM_MAP = {};', codes_pop_code + '\nconst ITEM_MAP = {};')

with open('e:/catalogo/prueba-C.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("prueba-C.html fixed and fully self-contained!")
