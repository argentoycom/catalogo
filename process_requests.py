import json

# 1. Load catalog_data.js
with open('e:/catalogo/catalog_data.js', 'r', encoding='utf-8') as f:
    text = f.read().replace('const CATALOG_DATA = ', '').rstrip(';\n')
    data = json.loads(text)

# 2. Remove specified items: CPV115, CPV117, CPV007
codes_to_remove = {'CPV115', 'CPV117', 'CPV007'}
data = [item for item in data if item['code'] not in codes_to_remove]

# 3. Add new figure: Mick Eyes out (CPV163) if not present
new_item = {
    "code": "CPV163",
    "name": "Mick Eyes out",
    "display": "Mick Eyes out (CPV163)",
    "cat": "Cultura Pop, Memes y Virales",
    "isRisky": False
}
if not any(item['code'] == 'CPV163' for item in data):
    data.append(new_item)

# 4. Reordering helper
def reorder_category(data_list, category_key, priority_codes):
    cat_items = [item for item in data_list if item['cat'] == category_key]
    other_items = [item for item in data_list if item['cat'] != category_key]
    
    cat_map = {item['code']: item for item in cat_items}
    
    priority_items = []
    for code in priority_codes:
        if code in cat_map:
            priority_items.append(cat_map[code])
            del cat_map[code]
            
    remaining_cat_items = list(cat_map.values())
    reordered_cat = priority_items + remaining_cat_items
    
    # Reassemble dataset
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

# Priority arrays
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

data = reorder_category(data, "Animacion y Nostalgia Retro", cat_priority)
data = reorder_category(data, "Cultura Pop, Memes y Virales", cpv_priority)
data = reorder_category(data, "Figuras publicas", fpu_priority)

# Save updated dataset
with open('e:/catalogo/catalog_data.js', 'w', encoding='utf-8') as f:
    f.write('const CATALOG_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

print("catalog_data.js updated cleanly with CPV163!")
