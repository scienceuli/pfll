# bilder_extrahieren.py

"""
extrahiert die Bilder aus einer Docx-Zipdatei mithilfe
einer Iteration über die infolist()
"""

import zipfile, os

docx = "datei_mit_bild.docx"
image_path = "bilder_aus_datei_mit_bild"

# Verzeichnis anlegen, in das die Bilde kommen
# falls es noch nicht existiert

try:
    os.mkdir(image_path)
except FileExistsError:
    print("Verzeichnis existiert bereits")

with zipfile.ZipFile(docx) as zip:
    print(zip.infolist())
    for file in zip.infolist():
        if file.filename.startswith("word/media"):
            file.filename = os.path.basename(file.filename)
            zip.extract(file, image_path)
