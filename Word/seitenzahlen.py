# seitenzahlen.py

from docx import Document
import re

doc = Document('test_05.docx')

# setze die Seitenzahl auf 1
seitenzahl = 1    

for p in doc.paragraphs:
    r = re.match('Heading*',p.style.name)
    if r:
        print(p.text, "auf Seite:", seitenzahl)
    for run in p.runs:
        if '<w:lastRenderedPageBreak/>' in run._element.xml:
            seitenzahl += 1
            