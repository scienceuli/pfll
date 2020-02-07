# bilder_extrahieren_V2.py
"""
extrahiert die Bilder aus einer Docx-Zipdatei mithilfe
einer Iteration über die namelist()
"""

import zipfile, os, shutil

docx = "datei_mit_bild.docx"
image_path = "bilder_aus_datei_mit_bild"

# Verzeichnis anlegen, in das die Bilde kommen
# falls es noch nicht existiert

try:
    os.mkdir(image_path)
except FileExistsError:
    print("Verzeichnis existiert bereits")

with zipfile.ZipFile(docx) as zip:
    print(zip.namelist())
    for file in zip.namelist():
        if file.startswith("word/media"):
            filename = os.path.basename(file)
            source = zip.open(file)
            target = open(os.path.join(image_path, filename), "wb")
            with source, target:
                shutil.copyfileobj(source, target)
