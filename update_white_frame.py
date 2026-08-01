import re

files_to_update = ['e:/catalogo/prueba-C.html', 'e:/catalogo/index.html']

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply clean white gallery photo container so photo pixels blend seamlessly
    content = re.sub(
        r'\.card-image-wrap\s*\{[^}]*\}',
        """.card-image-wrap {
    position: relative;
    width: 100%;
    aspect-ratio: 4/5;
    background: #ffffff;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 4px;
  }""",
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated grid card image container background to clean white gallery frame!")
