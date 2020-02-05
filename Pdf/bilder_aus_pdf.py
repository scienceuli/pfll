# bilder_aus_pdf.py

import fitz

# Pdf-Dokument definieren
pdf_dokument = fitz.open("11814_gesamt_20181129.pdf")

def save_image(pix, seite, xref):
# Funktion, die das Bild pix mit  Nr. = xref auf Seite = seite speichert
    pix.writePNG("images/seite%03d_%03d.png" % (seite, xref))


# Schleife über alle Seiten des Dokuments
for seite in range(len(pdf_dokument)):
    # Schleife über alle Bilder
    for image in pdf_dokument.getPageImageList(seite):
        xref = image[0]  # in die Docs schauen, liefert laufende Nummer
        pix = fitz.Pixmap(pdf_dokument, xref) # Bildinhalt
        save_image(pix, seite, xref)
        pix = None # pip zurücksetzen


