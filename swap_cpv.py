import json

# Read catalog_data.js
with open('e:/catalogo/catalog_data.js', 'r', encoding='utf-8') as f:
    text = f.read().replace('const CATALOG_DATA = ', '').rstrip(';\n')
    data = json.loads(text)

# Find indices of CPV014-CPV022 and CPV154-CPV162
g1_codes = [f"CPV{i:03d}" for i in range(14, 23)]
g2_codes = [f"CPV{i:03d}" for i in range(154, 163)]

g1_indices = [i for i, item in enumerate(data) if item['code'] in g1_codes]
g2_indices = [i for i, item in enumerate(data) if item['code'] in g2_codes]

print(f"Indices g1 (CPV014-022): {g1_indices}")
print(f"Indices g2 (CPV154-162): {g2_indices}")

# Swap items at these indices in the data array
for idx1, idx2 in zip(g1_indices, g2_indices):
    data[idx1], data[idx2] = data[idx2], data[idx1]

# Save updated catalog_data.js
with open('e:/catalogo/catalog_data.js', 'w', encoding='utf-8') as f:
    f.write('const CATALOG_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

print("Swapped position of Brainrot items (CPV014-CPV022) to the end of category!")
