import re

# Update WhatsApp number to 5491136355086 and apply CSS background logic
new_wa_number = "5491136355086"

files_to_update = ['e:/catalogo/prueba-C.html', 'e:/catalogo/index.html']

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update WhatsApp number
    content = re.sub(r'const WHATSAPP_NUMBER = "[^"]*";', f'const WHATSAPP_NUMBER = "{new_wa_number}";', content)

    # Grid image container: transparent background
    content = re.sub(
        r'\.card-image-wrap\s*\{[^}]*\}',
        """.card-image-wrap {
    position: relative;
    width: 100%;
    aspect-ratio: 4/5;
    background: transparent;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }""",
        content
    )

    # Modal image container: crisp clean white background for maximum visibility
    content = re.sub(
        r'\.modal-img-container\s*\{[^}]*\}',
        """.modal-img-container {
    position: relative;
    width: 100%;
    aspect-ratio: 4/5;
    background: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
  }""",
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully updated WhatsApp number to {new_wa_number} and applied transparent grid + white modal background!")
