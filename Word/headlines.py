# headlines.py

import docx
import re # fuer regulaere Ausdruecke

doc = docx.Document('test_04.docx')

liste_der_absaetze = doc.paragraphs

for absatz in liste_der_absaetze:
    print(absatz.style.name)

# definiere regex um Headings zu finden
h = re.compile('(Heading)(\s)(\d+)')

with open('test_04_headlines.txt', 'w') as out:
    for absatz in liste_der_absaetze:
        # Match fuer Überschrift
        m = h.match(absatz.style.name)
        if m:
            anzahl_tabs = int(m.group(3))-1
            out.write("\t"*anzahl_tabs)
            out.write(absatz.style.name + "\n")
