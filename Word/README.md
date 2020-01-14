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

## Überschriften prüfen
Mithilfe eines Python-Skripts kann man auch schnell die Formate innerhalb eines Word-Dokuments prüfen, z.B. die Logik ihrer Verwendung.

Beispiel: Das Dokument _test\_04.docx_ enthält einige Überschriften (_Heading 1_, _Heading 2_ usw. ). Das folgende Skript legt zunächst wieder eine Liste der Absätze an und iteriert dann über alle Absätze. Dabei wird der Name des jeweiligen Absatzstils ausgegeben.

Jetzt sollen uns aber nur die Absatzstile _Heading 1_, _Heading 2_ usw. interessieren. Um diese aus allen Absatzstillen herauszufischen, definieren wir einen sog. _Regulären Ausdruck_ (_Regular Expression_), mit dem wir die Absatzstile vergleichen. Für die Arbeit mit regulären Ausdrücken hält Python die Standardbibliothek **re** bereit. Diese müssen wir zwar nicht installieren, aber zu Beginn mit `import re` importieren.

Der reguläre Ausdruck, der auf alle Überschriftenstile passt, lautet
```
h = re.compile('(Heading)(\s)(\d+)')
```
Also ein String, der sich aus `'Heading'`, einem Leerzeichen `\s` und einer oder mehreren Ziffern `\d+` zusammensetzt. Das `\d` steht dabei für eine Ziffer (_digit_) und das Pluszeichen steht  für "eine oder mehrere". Die runden Klammern gruppieren den regulären Ausdruck, das vereinfacht den Verweis auf Teile des gesuchten Ausdrucks (s.u.).

Wenn unser Skript auf eine Überschrift stößt, soll es diese Überschrift in eine Textdatei, die wir anlegen bzw. öffnen, schreiben. Wir suchen also einen _Match_ zwischen unserem regulären Ausdruck und dem Absatzstil, über den gerade iteriert wird:
```
m = h.match(absatz.style.name)
``` 
Die Variable `m` ist also jetzt keine Zahl oder String, sondern ein Wahrheitswert: Passt der Match, dann _True_, passt er nicht, dann _False_. Wir interessieren uns nur für _True_:
```
if m:
    out.write(absatz.style.name)
```
Um die Ausgabe noch ein wenig schöner zu machen, fügen wir  noch einen Zeilenumbruch `\n` nach jeder Zeile ein. Außerdem wenden wir noch einen kleinen Trick an: Liegt ein _Match_ vor, dann enthält das dritte runde Klammerpaar des regulären Ausdrucks die Nummer des Überschriftenstils. Also: Bei "Heading 2" schlägt der Match an (passt zum regulären Ausdruck), d.h. das dritte Klammerpaar im regulären Ausdruck passt in diesem Fall auf "2". Auf diese "2" können wir durch die Funktion `group(3)` zugreifen, da sie den Inhalt des dritten Klammerpaars im regulären Ausdruck zurückgibt.

Mit dieser Zahl möchten wir anschließend rechnen, d.h. wir wandeln sie per `int()` in eine Integerzahl um. Wir sagen nämlich: Füge vor jeder Zeile so viele Tabs ein, wie es der Überschriftenhiearchie entspricht. Bzw. genauer: ziehe noch 1 ab, da vor einer Überschrift mit Stil _Heading 1_ kein Tab, stehen soll, vor einer mit _Heading 2_ ein Tab usw.

Das gesamt Skript siehe also wie folgt aus:
```
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
```
Es schreibt folgende Zeilen in die Datei _test\_04\_headlines.txt_:
```
Heading 1
	Heading 2
			Heading 4
	Heading 2
		Heading 3
		Heading 3
```
Kopiert man diese Zeilen z.B. nach Excel, werden die Überschriften aufgrund der Tabs auf verschiedene Spalten verteilt. Man sieht dann schnell, dass hier ein Fehler in der Überschriftenlogik vorliegt: Nach einer _Heading 2_ kommt direkt eine _Heading 4_.

Mögliche Erweiterung: Tritt dieser Fall auf (eine Überschriftenebene fehlt), soll eine Meldung ausgegeben werden. 

## Word und Seitenzahlen
Kann man mithilfe von **python-docx** die Seitenzahlen aus einem Word-Dokument ziehen? Die kurze Antwort: Nein, da Word die Seitenzahlen während des Render-Vorgangs erzeugt, wenn es den Text für die Darstellung am Monitor bzw. den Druck aufbereitet. _Aber_: Word schreibt in die XML-Daten an den Stellen, an denen beim letzten Render-Vorgang ein Page Break eingefügt wurde, das Element `<w:lastRenderedPageBreak>`. Und jetzt das coole: das Objekt `run._element.xml` gibt zu einem _Run_ das zugehörige  Element zurück. Wenn man also über alle _Runs_ eines Absatzes iteriert und auf das XML-Element `<w:lastRenderedPageBreak>` stößt, setzt man die Seitenzahl um 1 herauf.

Das folgende Skript iteriert über alle Absätze eines Dokuments und vergleicht den Absatzstil mit dem Regulären Ausdruck `'Heading*'`. Findet es eine Überschrift, gibt sie den Text der Überschrift und die zugehörige Seitenzahl. Diese wiederum ändert sich um 1, wenn ein _Run_ das XML-Element  `<w:lastRenderedPageBreak>`  enthält:
```
seitenzahl += 1
```
Diese Zeile ist die Kurzform von `seitenzahl = seitenzahl + 1`.

```
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
```
Die Ausgabe:
```
Überschrift 1 auf Seite: 1
Überschrift 2 auf Seite: 1
Überschrift 5 auf Seite: 1
Überschrift 3 auf Seite: 1
Überschrift 4 auf Seite: 1
Überschrift 6 auf Seite: 1
Überschrift 7 auf Seite: 1
Überschrift 8 auf Seite: 2
Überschrift 9 auf Seite: 2
Überschrift 10 auf Seite: 2
Überschrift 11 auf Seite: 2
```





