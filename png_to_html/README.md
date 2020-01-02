# Bilddateien als html ausgeben

_Aufgabe_: Bilddateien in einem Ordner durchgehen und Dateinamen in ein html-img-Element einfügen

Um mit einem Python-Skript Informationen zu Dateien und Verzeichnissen auf dem  Computer abzurufen, muss das Skript mit dem Betriebssystem  "kommunizieren". Python stellt dafür das Modul **os** zur Verfügung. Es gehört zur Standardbibliothek von Python und muss daher nicht extra installiert werden. 

**os** enthält Dutzende von Funktionen, um mit dem Betriebssystem zu interagieren. Um diese zu nutzen, muss das Modul **os** am Beginn des Skripts importiert werden:
```
import os
```
Viele der Funktionen sind so benannt, dass sie fast selbsterklärend sind.
So listet die Funktion `os.listdir(Verzeichnis)` die Dateien in dem Verzeichnis auf, das man beim Funktionsaufruf angibt. Lässt man die Klammer leer, nimmt `os.listdir()` das Verzeichnis, in dem sich das Python-Skript befindet.

**Hinweis 1:** Benutzt man eine Funktion aus einem Modul, so muss beim Funktionsaufruf immer das Modul vorangestellt werden: `os.listdir()` statt `listdir()`

**Hinweis 2:** Ein Funtionsaufruf muss *immer* ein Klammerpaar enthalten. Das kann leer sein (dann wird nichts übergeben), aber man darf nicht die Klammern weglassen.

Das Skript muss nun folgendes leisten:
1. Gehe das  Verzeichnis *./images* (ein Unterverzeichnis zum aktuellen Verziechnis) durch.
2. Merke dir dabei jeweils den Dateinamen und füge ihn an einer bestimmten Stelle in ein html-Element ein. Da wir eine html-Datei produzieren möchten, die Links auf Bilder enthält, ist das img-Tag das richtige html-Element.
3. Speichere am Schluss eine html-Datei ab, in der nun alle Dateien durch img-Tags verlinkt sind.

Das Durchgehen eines Verzeichnis liefert eine Schleife über die Dateien, die `os.listdir()` findet:
```
for datei in os.listdir('./images'):
    ...
```
Für jede Datei im Verzeichnis *./images*, die gelistet wird, nehmen wir den Dateinamen und schreiben ihn in einen String, der das img-Element aus html enthält. Wir benutzen dazu ein schönes Konstrukt, das Python seit der Version 3.6 bereithält: den **f-String**. Mit einem f-String lässt sich der Inhalt einer Variablen in einen String einbetten. In unserem Beispiel ist das die Schleifen-Variable `datei`, die den Dateinamen enthält:
```
for datei in os.listdir('./images'):
    html_string = html_string + f"<p><img src='.images/{datei}'></p>"
```
Der Variablenname für die Schleife ist frei wählbar. Wir definieren hier ja diese Variable: Wir geben ihr einen Namen (`datei`) und weisen ihr einen Inhalt zu (das, was `os-listdir()` zurückliefert).

Die Schleife macht nun Folgendes: Sie geht das Verzeichnis *./images/* durch. Bei jeder Runde fügt der in der Schleife ausgeführte Befehl den Dateinamen, der in `datei` abgespeichert ist, in einen f-String ein. Diesen String hängt das Skript dann an den bereits vorhandenen String `html_string` an. Dieser wird also immer länger. Damit beim ersten Schleifendurchgang keine Fehlermeldung auftritt, muss `html_string` bereits exisiteren, bevor die Schleife durchlaufen wird. Also legen wir `html_string` zunächst als leeren String an:
```
html_string = ''
```

Nach Beendigung der Schleife muss der html-String noch in eine html-Datei geschrieben werden. Der folgende Code legt eine schreibbare Datei *index.html* an und schreibt den html-String dort hinein:
```
with open("index.html", "w") as html_datei:
    html_datei.write(html_string)
```
Hier ist `html_datei` eine frei benennbare Variable für die gerade geöffnete Datei.

Hier noch mal das gesamt Sktipt:
```
import os

html = ''

for datei in os.listdir('./images'):
    html_string = html_string + f"<p><img src='./images/{datei}'></p>"

with open("index.html", "w") as html_datei:
    html_datei.write(html)
```


