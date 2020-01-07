# bold_versus_fett.py

import docx

doc = docx.Document('test_03.docx')

liste_der_absaetze = doc.paragraphs
erster_absatz = liste_der_absaetze[0]

for run in erster_absatz.runs:
    if run.bold:
        print(run.text)
        run.style = "Strong"

doc.save("test_03_restyled.docx")
