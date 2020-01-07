# Word-Dateien bearbeiten
Mit Python kann man .docx-Dateien lesen und bearbeiten. Es gibt ein eigenes Modul dafür: **docx**. Es wird mit `pip` (oder `pipenv`) installiert:
```
$ pip install python-docx
```
(Hinweis: Es muss `python-docx` installiert werden, in einem Python-Programm wird aber `docx` importiert.)

## Lesen von Word-Dateien
Das folgende Skript importiert das Modul **docx**, öffnet das Dokument _test\_01.docx_ als Objekt `doc` vom Typ `Document`, erzeugt eine Liste der Absätze und gibt die Länge dieser Elemente (also die Anzahl der Listen-Elemente) aus.
Das erste Element (Index 0) dieser Liste ist der erste Absatz. Das Attribut `text` gibt den Text dieses Absatzes zurück.
```
# zaehle_absaetze.py

import docx

doc = docx.Document('test_01.docx')

liste_der_absaetze = doc.paragraphs
anzahl_absaetze = len(liste_der_absaetze)
erster_absatz = liste_der_absaetze[0]
text_erster_absatz = erster_absatz.text


print(f"Das Dokument hat {anzahl_absaetze} Absätze.")
print(f"Der erste Absatz lautet: {text_erster_absatz}")
```
Das bedeutet: Das Paket **docx** stellt ein Objekt `docx.Document()` zur Verfügung, mit dem sich Word-Dateien öffnen lassen. Das Attribut `paragraphs` erstellt dann aus diesem Dokument eine Liste der Absätze. Das Element mit Index 0 in dieser Liste ist der erste Absatz. Seinen Textinhalt liefert das Attribut `text`.

## Formatierungen erkennen
Ein Word-Dokument enthält Absatz- und Zeichenformatierungen. Letztere strukturieren ein Dokument innerhalb eines Absatzes, denn die Absatzteile mit einer durchgehenden Formatierungen bilden einen _Run_. Immer, wenn das Zeichenformat sich ändert, beginnt ein neuer _Run_. 

Das folgende Skript geht die _Runs_ des ersten Absatzes aus dem Dokument _test\_02.docx_ durch und zeigt für jeden _Run_ den Namen des Zeichenformats (`run.style.name`) und den Textinhalt des _Run_ an (`run.text`):
```
# zeichenformatierungen.py

import docx

doc = docx.Document('test_02.docx')

liste_der_absaetze = doc.paragraphs
erster_absatz = liste_der_absaetze[0]

for run in erster_absatz.runs:
    print(f"{run.style.name}: {run.text}\n")
```
Das Attribut `runs` für einen Absatz liefert eine Liste der _Runs_ zurück. Die `for`-Schleife iteriert deshalb über alle _Runs_ innerhalb des Absatzes. 

## Formatierungen ändern
Eine typische "Ungenauigkeit" in Word-Dokument: Zur Fett-Auszeichnung wird sowohl die Zeichenvorlage "Fett" (engl. "Strong") als auch die Zeicheneigenschaft "Fett" (engl. "bold") benutzt. Beide sind optisch nicht zu unterscheiden, strukturell aber verschiedene Dinge. Deshalb bauen wir uns ein Programm, das alle _Runs_ mit der Eigenschaft "bold" in _Runs_ mit dem Zeichenformat "Strong" umwandelt.

Das folgende Skript verarbeitet den ersten Absatz des Dokuments _test\_03.docx_. Er enthält sowohl das Zeichenformat "Strong" als auch die Zeicheneigenschaft "bold". Das Skript iteriert über alle Runs und prüft, ob der jeweilige _Run_ die Eigenschaft "bold" hat (`if run.bold`). Wenn diese Abfrage _True_ zurückgibt (also zutrifft), wird diesem _Run_ das Zeichenformat "Strong" zugewiesen (`run.style = 'Strong'`). Nach Beendigung der Schleife wird das modifizierte Dokument unter anderem Namen abgespeichert.
```
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
```


