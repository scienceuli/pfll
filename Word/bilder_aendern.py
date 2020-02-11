# bilder_extrahieren_V2.py
"""
extrahiert die Bilder aus einer Docx-Zipdatei mithilfe
einer Iteration über die namelist()
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
            content = zipin.read(file)
            if file.filename.startswith("word/media"):
                img = Image.open(io.BytesIO(content))
                fmt = file.filename.split(".")[-1]
                img = img.convert("L")
                outb = io.BytesIO()
                img.save(outb, fmt)
                content = outb.getvalue()
                file.file_size = len(content)
                file.CRC = zipfile.crc32(content)
            #    filename = os.path.basename(file)
            #    source = zipin.open(file)
            #    img = Image.open(source)
            #    img_L = img.convert("L")
            #    img_L.save(source)
            #    zipout.writestr(docx_conv)
            zipout.writestr(file, content)

