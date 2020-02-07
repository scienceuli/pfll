# bilder_extrahieren.py

import zipfile, os

docx = "datei_mit_bild.docx"
image_path = "bilder_aus_datei_mit_bild"

if not image_path:
    os.mkdir(image_path)

with zipfile.ZipFile(docx) as zip:
    print(zip.infolist())
    for file in zip.infolist():
        if file.filename.startswith("word/media"):
            file.filename = os.path.basename(file.filename)
            zip.extract(file, image_path)
