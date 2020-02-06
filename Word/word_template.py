# word_template.py

import docx
import datetime

# Absender und Adressat
absender = "Ulrich"
adressat = "Walter"

# Datum und Ort
now = datetime.datetime.now()
datum = now.strftime("%d.%m.%Y")
ort = "Frickingen"

# Dictionary mit Muster und Variablen
template_dict = {
    "{Adressat}": adressat,
    "{Absender}": absender,
    "{Datum}": datum,
    "{Ort}": ort,
}

# Einlesen des Templates
doc = docx.Document("template.docx")

# Iteration über alle Absätze
for para in doc.paragraphs:
    for key in template_dict:  # Iteration über Dictionary
        para.text = str.replace(para.text, key, template_dict[key])

# Abspeichern unter neuem Namen
doc.save("rechnung.docx")

