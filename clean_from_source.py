import pandas as pd
import json
import re

# Read Excel file
excel_path = 'e:/catalogo/Nombres de personajes/catalogo.xlsx'
df = pd.read_excel(excel_path)

# Category mapping to English
CAT_MAP_EN = {
  "Cultura Pop, Memes y Virales":   "Pop Culture & Memes",
  "Cine, TV y Series":              "Movies & TV Series",
  "Musica":                         "Music",
  "Animacion y Nostalgia Retro":    "Retro & Animation",
  "Figuras publicas":               "Famous People",
  "Deportes":                       "Sports",
  "Crossovers":                     "Crossovers",
  "Anime y Videojuegos":            "Anime & Games"
}

risky_terms = [
    "e.t", "e.t.", " et ", "alf", "he-man", "heman", "duke nuken", "duke nukem",
    "frankenstein", "jason", "chucky", "scream", "el exorcista", "exorcista", "exorcist",
    "hannibal", "rocky", "nirvana", "david bowie", "michael jackson", "led zepelin", "led zeppelin",
    "gorillaz", "homelander", "toy story", "pokémon", "pokemon", "pikachu", "pokeball",
    "dragon ball", "dragonball", "goku", "chayajin", "sayayin", "vegeta", "yamcha",
    "the last of us", "final fantasy", "cloud", "michael myers", "jason voorhees",
    "grand theft auto", "gta", "stranger things", "demogorgon", "dustin", "eddie munson",
    "eleven", "max mayfield", "will byers", "the office", "kevin malone", "dwight", "michael scott",
    "godzila", "godzilla", "calvin candie", "marvel", "x-men", "xmen", "rogue", "magneto",
    "spider-man", "spiderman", "spider noir", "venom", "star wars", "darth vader", "vader",
    "kenobi", "chewbacca", "alfbacca", "batman", "joker", "superman", "watchmen",
    "dr. manhattan", "dr manhattan", "rorschach", "the simpsons", "simpsons", "homero", "bart", "burns",
    "disney", "pixar", " alien ", "alien ", "alien", "mars attacks", "hasbro", "power rangers",
    "power ranger", "nintendo", "star fox", "capcom", "resident evil", "biohazard", "dino crisis",
    "metal gear", "crash bandicoot", "hollow knight", "silksong", "lego", "hot wheels",
    "pink floyd", "the beatles", "beatles", "ramones", "slipknot"
]

def contains_risky_term(title):
    if not title or pd.isna(title):
        return False
    t_lower = " " + str(title).lower() + " "
    for term in risky_terms:
        if len(term.strip()) <= 3:
            pattern = r'\b' + re.escape(term.strip()) + r'\b'
            if re.search(pattern, t_lower):
                return True
        else:
            if term.strip() in t_lower:
                return True
    return False

# Build catalog items
items = []
codes_to_remove = {'CPV115', 'CPV117', 'CPV007'}

for idx, row in df.iterrows():
    code = str(row['Codigo']).strip()
    if code in codes_to_remove:
        continue
        
    raw_name = str(row['Nombre']).strip() if pd.notna(row['Nombre']) else ""
    orig_cat = str(row['Categoria']).strip() if pd.notna(row['Categoria']) else ""
    cat_en = CAT_MAP_EN.get(orig_cat, orig_cat)

    is_risky = contains_risky_term(raw_name)

    if is_risky:
        final_name = ""
        display = code
    else:
        # Perform replacements on Messi & Maradona
        clean_name = re.sub(r'(?i)messi', 'Lio', raw_name)
        clean_name = re.sub(r'(?i)maradona', 'Diego', clean_name)
        final_name = clean_name
        display = f"{clean_name} ({code})" if clean_name else code

    items.append({
        "code": code,
        "name": final_name,
        "display": display,
        "cat": cat_en,
        "originalCat": orig_cat,
        "isRisky": is_risky
    })

# Add CPV163 Mick Eyes out
if not any(it['code'] == 'CPV163' for it in items):
    items.append({
        "code": "CPV163",
        "name": "Mick Eyes out",
        "display": "Mick Eyes out (CPV163)",
        "cat": "Pop Culture & Memes",
        "originalCat": "Cultura Pop, Memes y Virales",
        "isRisky": False
    })

# Priority reordering helper
def reorder_category(data_list, category_key, priority_codes):
    cat_items = [item for item in data_list if item['cat'] == category_key]
    cat_map = {item['code']: item for item in cat_items}
    
    priority_items = []
    for code in priority_codes:
        if code in cat_map:
            priority_items.append(cat_map[code])
            del cat_map[code]
            
    remaining = list(cat_map.values())
    reordered_cat = priority_items + remaining
    
    new_data = []
    cat_inserted = False
    for item in data_list:
        if item['cat'] == category_key:
            if not cat_inserted:
                new_data.extend(reordered_cat)
                cat_inserted = True
        else:
            new_data.append(item)
    if not cat_inserted:
        new_data.extend(reordered_cat)
    return new_data

cat_priority = [
    "CAT065", "CAT074", "CAT076", "CAT077", "CAT082", "CAT099", "CAT096", "CAT079", 
    "CAT080", "CAT063", "CAT036", "CAT030", "CAT029", "CAT028", "CAT013", "CAT014", 
    "CAT015", "CAT001"
]

cpv_priority = [
    "CPV001", "CPV002", "CPV086", "CPV093", "CPV095", "CPV012", "CPV083", "CPV077", 
    "CPV138", "CPV008", "CPV099", "CPV013", "CPV051", "CPV122", "CPV123", "CPV053", 
    "CPV103", "CPV126", "CPV084", "CPV154", "CPV132", "CPV155", "CPV028", "CPV030", 
    "CPV031", "CPV032", "CPV034", "CPV037", "CPV046", "CPV047", "CPV044", "CPV048", 
    "CPV050", "CPV060", "CPV079", "CPV104"
]

fpu_priority = [
    "FPU031", "FPU042", "FPU043", "FPU004", "FPU010", "FPU011", "FPU015", "FPU016", 
    "FPU018", "FPU026", "FPU025", "FPU022", "FPU034", "FPU035", "FPU038", "FPU050", 
    "FPU051", "FPU056", "FPU047", "FPU053", "FPU057", "FPU058"
]

items = reorder_category(items, "Retro & Animation", cat_priority)
items = reorder_category(items, "Pop Culture & Memes", cpv_priority)
items = reorder_category(items, "Famous People", fpu_priority)

# Save to catalog_data.js
with open('e:/catalogo/catalog_data.js', 'w', encoding='utf-8') as f:
    f.write('const CATALOG_DATA = ' + json.dumps(items, ensure_ascii=False, indent=2) + ';\n')

cleared_total = sum(1 for it in items if it['name'] == "")
lio_total = sum(1 for it in items if 'Lio' in it['name'])
diego_total = sum(1 for it in items if 'Diego' in it['name'])

print(f"Master Catalog Processed Successfully!")
print(f"Total Figures in Dataset: {len(items)}")
print(f"Cleared Risky Titles (Code Only): {cleared_total}")
print(f"Figures with Lio: {lio_total}")
print(f"Figures with Diego: {diego_total}")
