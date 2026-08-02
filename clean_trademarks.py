import json
import re

# Load catalog_data.js
with open('e:/catalogo/catalog_data.js', 'r', encoding='utf-8') as f:
    text = f.read().replace('const CATALOG_DATA = ', '').rstrip(';\n')
    data = json.loads(text)

# Risky terms list (normalized lower case)
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
    if not title:
        return False
    t_lower = " " + title.lower() + " "
    for term in risky_terms:
        if len(term.strip()) <= 3:
            pattern = r'\b' + re.escape(term.strip()) + r'\b'
            if re.search(pattern, t_lower):
                return True
        else:
            if term.strip() in t_lower:
                return True
    return False

modified_count = 0
cleared_count = 0

for item in data:
    name = item.get('name', '')
    display = item.get('display', '')
    original_title = name if name else display

    # Check risk
    if contains_risky_term(original_title):
        item['name'] = ""
        item['display'] = item['code']
        item['isRisky'] = True
        cleared_count += 1
    else:
        # Perform replacements on Messi and Maradona
        if name:
            new_name = re.sub(r'(?i)messi', 'Lio', name)
            new_name = re.sub(r'(?i)maradona', 'Diego', new_name)
            if new_name != name:
                modified_count += 1
                item['name'] = new_name
                item['display'] = f"{new_name} ({item['code']})"

print(f"Processing Complete!")
print(f"Titles cleared due to trademark risk: {cleared_count}")
print(f"Titles updated with Lio / Diego replacements: {modified_count}")

# Save back to catalog_data.js
with open('e:/catalogo/catalog_data.js', 'w', encoding='utf-8') as f:
    f.write('const CATALOG_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

