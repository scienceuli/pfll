# zeichenformatierungen.py

import docx

doc = docx.Document('test_02.docx')

liste_der_absaetze = doc.paragraphs
erster_absatz = liste_der_absaetze[0]

for run in erster_absatz.runs:
    print(f"{run.style.name}: {run.text}\n")
