# bilder_aendern.py
"""
konvertiert die Bilder aus einer Docx-Zipdatei 
mithilfe PIL
hier: konvertieren in  s/w: RGB -> L
"""

import zipfile, os, shutil
from PIL import Image
import io

docx = "datei_mit_bild.docx"
docx_conv = "datei_mit_bild_conv.docx"

with zipfile.ZipFile(docx) as zipin:
    with zipfile.ZipFile(docx_conv, "w") as zipout:
        print(zipin.infolist())
        for file in zipin.infolist():
            # content einlesen
            content = zipin.read(file)
            if file.filename.startswith("word/media"):
                # Byte Streasm des Bildes einlesen
                img = Image.open(io.BytesIO(content))
                # Format der Bilddatei bestimmen
                fmt = file.filename.split(".")[-1]
                # konvertieren des Bildes
                img = img.convert("L")
                # Objekt erzeugen für Byte Stream -> out
                outb = io.BytesIO()
                img.save(outb, fmt)
                content = outb.getvalue()
                file.file_size = len(content)
                file.CRC = zipfile.crc32(content)
            
            zipout.writestr(file, content)

