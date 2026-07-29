import os
import shutil
import openpyxl
import json

# Paths
BASE_DIR = r"e:\catalogo"
EXCEL_PATH = os.path.join(BASE_DIR, "Nombres de personajes", "catalogo.xlsx")
NEW_FOLDER_NAME = "Nombres Filtrados (Seguro Schedule A)"
NEW_DIR = os.path.join(BASE_DIR, NEW_FOLDER_NAME)

# Palabras clave de alto y medio riesgo (Marqueras / Trademarks masivos agresivos)
RISKY_KEYWORDS = [
    # Bandas y Música
    'beatles', 'rolling stones', 'slipknot', 'iron maiden', 'guns n', 'guns and roses', 
    'green day', 'pink floyd', 'pink freud', 'metallica', 'nirvana', 'kurt cobain', 
    'freddie mercury', 'queen', 'kiss',
    
    # Videojuegos & Ent
    'nintendo', 'star fox', 'mario', 'gta', 'grand theft auto', 'resident evil', 
    'capcom', 'mortal kombat', 'warner', 'pokemon', 'pikachu', 'zelda', 'sonic',
    
    # Cine, TV & Streaming
    'disney', 'marvel', 'star wars', 'darth vader', 'vader', 'spider', 'woody', 
    'stranger things', 'netflix', 'the office', 'the boys', 'batman', 'superman', 
    'simpson', 'toy story', 'shrek', 'turtles', 'tmnt',
    
    # Corporativos
    'lego', 'mattel', 'monster energy', 'monster', 'mcdonald', 'ronald mcdonald', 
    'coca cola', 'pepsi', 'nike', 'adidas',
    
    # Anime & Manga
    'dragon ball', 'evangelion', 'toriyama', 'naruto', 'one piece', 'saint seiya',
    
    # Terror Clásico
    'pennywise', 'jason', 'voorhees', 'freddy krueger', 'freddy'
]

def is_figure_risky(name):
    if not name:
        return False
    n = str(name).lower()
    for kw in RISKY_KEYWORDS:
        if kw in n:
            return True
    return False

def main():
    wb = openpyxl.load_workbook(EXCEL_PATH)
    sheet = wb.active
    rows = list(sheet.iter_rows(values_only=True))[1:]

    os.makedirs(NEW_DIR, exist_ok=True)
    
    catalog_dataset = []
    risky_count = 0
    safe_count = 0

    print(f"Cargadas {len(rows)} filas del Excel.")

    for row in rows:
        if not row or not row[0]:
            continue
        
        code = str(row[0]).strip()
        name = str(row[1]).strip() if row[1] else ""
        cat = str(row[2]).strip() if row[2] else ""
        
        risky = is_figure_risky(name)
        
        if risky:
            risky_count += 1
            display_title = code  # Solo codigo para evitar Schedule A
            sanitized_name = f"{code}"
        else:
            safe_count += 1
            display_title = f"{name} ({code})"
            # Limpiar nombre para nombre de archivo de sistema
            clean_name = "".join(c for c in name if c.isalnum() or c in (" ", "-", "_", "(", ")")).strip()
            sanitized_name = f"{code} - {clean_name}"

        item = {
            "code": code,
            "name": name if not risky else "",
            "display": display_title,
            "cat": cat,
            "isRisky": risky
        }
        catalog_dataset.append(item)

        # Copiar imagenes a la nueva carpeta sin borrar nada
        cat_dir = os.path.join(NEW_DIR, cat)
        cat_thumbs = os.path.join(cat_dir, "thumbs")
        cat_full = os.path.join(cat_dir, "full")
        os.makedirs(cat_thumbs, exist_ok=True)
        os.makedirs(cat_full, exist_ok=True)

        # Orígenes de imagen
        src_thumb = os.path.join(BASE_DIR, cat, "thumbs", f"{code}_thumb.webp")
        src_full = os.path.join(BASE_DIR, cat, "Full", f"{code}_full.webp")

        dst_thumb = os.path.join(cat_thumbs, f"{sanitized_name}_thumb.webp")
        dst_full = os.path.join(cat_full, f"{sanitized_name}_full.webp")

        if os.path.exists(src_thumb):
            shutil.copy2(src_thumb, dst_thumb)
        if os.path.exists(src_full):
            shutil.copy2(src_full, dst_full)

    # Guardar JSON con el mapeo seguro
    json_path = os.path.join(NEW_DIR, "catalog_mapping.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(catalog_dataset, f, ensure_ascii=False, indent=2)

    # Guardar catalog_data.js para usar directamente en la web
    js_path = os.path.join(BASE_DIR, "catalog_data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("const CATALOG_DATA = " + json.dumps(catalog_dataset, ensure_ascii=False, indent=2) + ";\n")

    print(f"[OK] Proceso completado exitosamente!")
    print(f"Carpeta creada: {NEW_DIR}")
    print(f"Totales: {len(catalog_dataset)} figuras.")
    print(f"Riesgo Marca (Solo codigo): {risky_count}")
    print(f"Seguras (Nombre + Codigo): {safe_count}")

if __name__ == "__main__":
    main()
