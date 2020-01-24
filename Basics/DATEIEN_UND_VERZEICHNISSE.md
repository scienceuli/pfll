# Dateien und Verzeichnisse
Wir organisieren unsere Arbeit in Dateien und Verzeichnissen, und wenn Python uns bei dieser Arbeit unterstützen soll, muss der Interpreter Dateien und Verzeichnisse lesen können. Außerdem wollen wir an vielen Stellen unserer Python-Skripts die Ergebnisse von Berechnungen speichern, um später darauf zurückgreifen zu können.

Um zu verstehen, wie Python mit Dateien und Verzeichnissen umgeht, sind einige Bzeichnungen auseinanderzuhalten:

* Jede Datei hat einen _Pfad_ und einen _Dateinamen_.
* Eine Datei hat in der Regel eine _Dateiendung_ (_Extension_), z.B. _.txt_, _.docx_, _.jpg_ usw.
* **Achtung:** Windows-Pfade werden in Python mit einem doppelten Backslash geschrieben (z.B. `'c:\\verzeichnis\\nocheinverzeichnis\\datei.txt'`), weil der einfache Backslash als Befehlszeichen interpretiert wird (z.B. `\n` für _newline_) und deshalb der Backslash im Pfad geschützt werden muss (_escaping_) - und zwar mit einem Backslash:
  ```
  >>> print('\\')
  \
  ```
  Alternative: Bei einem _Raw String_ muss der Backslash nicht geschützt werden:
  ```
  >>> r'C:\verzeichnis'
  'C:\\verzeichnis'
  ```

## Modul os: Dateien und Verzeichnisse
Ein zentrales Modul, das zahlreiche Funktionen für Dateien enthält, ist das Standardmodul **os**. 

### Einige wichtige Funktionen

* Mehrere String lassen sich zu einem Pfad verbinden:
  ```
  >>> os.path.join('verz1', 'verz2', 'verz3', 'datei')
  'verz1/verz2/verz3/datei'
  ```
  _Hinweis_: Python "weiß", auf welchem Betriebssystem es läuft, und wählt automatisch den richtigen Slash(/ aus MacOS und Linux, \\\\ auf Windows).
* `os.getcwd()` gibt das aktuelle Arbeitsverzeichnis zurück:
  ```
  >>> os.getcwd()
  '/Users/scienceuli/Devel/pfll/Basics'
  ```
  Wenn man einen Dateinamen ohne Pfad angibt, geht Python davon aus, dass sich die Datei im aktuellen Arbeitsverzeichnis befindet.
* Relative Pfadangaben (. für aktuelles Verzeichnis, .. für Elternverzeichnis) sind möglich. `os.path.abspath()` gibt den absoluten Pfad zu einem relativen Pfad zurück. mit `os.path.isabs()` kann man testen, ob ein Pfad ein absoluter Pfad ist:
  ```
  >>> os.path.isabs('verzeichnis')
  False
  >>> os.path.isabs('~/verzeichnis')
  False
  >>> os.path.isabs('/~/verzeichnis')
  True
  ```
* `os.path.dirname()` gibt das Verzeichnis eines Pfades zurück:
  ```
  >>> os.path.dirname('verzeichnis1/verzeichnis2/datei.txt')
  'verzeichnis1/verzeichnis2' 
  ```
* `os.path.basename()` gibt nur den Dateinamen zurück:
  ```
  >>> os.path.basename('verzeichnis1/verzeichnis2/datei.txt')
  'datei.txt'
  ```
* `os.path.exists()` prüft, ob ein Verzeichnis auf dem Computer vorhanden ist. Es nimmt sowohl relative als auch absolute Pfadangaben entgegen und gibt _True_ oder _False_ zurück.
  ```
  >>> os.path.exists('/Users/scienceuli/Devel/pfll/Basics')
  True
  >>> os.path.exists('../Basics')
  True
  ```
  Mit `os.path.isdir()` und `os.path.isfile()` kann die Abfrage noch spzifiziert werden.
* `os.path.getsize()` ermittelt die Größe einer Datei in Bytes:
  ```
  >>> os.path.getsize('README.md')
  9541
  ```
* `os.listdir()` (Achtung: ohne Submodul _path_) listet alle Dateien und Ordner in einem Verzeichnis auf:
  ```
  >>> os.listdir('.')
  ['print_input.py', 'README.md', 'DATEIEN_UND_VERZEICHNISSE.md']
  ```
* `os.makedirs()` legt ein Verzeichnis an:
  ```
  >>> os.makedirs('neues_verzeichnis')
  >>> os.listdir('.')
  ['neues_verzeichnis', 'print_input.py', 'README.md',  'DATEIEN_UND_VERZEICHNISSE.md']
  ```
  Falls die Pfadangabe mehrere Verzeichnisse enthält, werden diese Verzeichnis genauso angelegt.

**Übung**: Erzeuge eine typische Dateistruktur für ein Projekt (Verzeichnisse für Manuskripte, Grafiken, Organisation etc.).



### os.rename(): Dateien umbenennen
Eine häufige Aufgabe im Redaktionsalltag besteht darin, Dateien umzubenennen. **os** hält dafür die Methode `os.rename()` bereit:
```
>>> os.listdir('.')
['textdatei3.txt', 'textdatei2.txt', 'textdatei.txt', 'print_input.py', 'README.md', 'DATEIEN_UND_VERZEICHNISSE.md']
>>> os.rename('textdatei2.txt', 'umbenannte_Datei.txt')
>>> os.listdir('.')
['textdatei3.txt', 'textdatei.txt', 'umbenannte_Datei.txt', 'print_input.py', 'README.md', 'DATEIEN_UND_VERZEICHNISSE.md']
```
Nun wird man kein Programm bemühen, um eine einzelne Datei umzubennen. Eher schon, um alle Dateien in einem oder mehreren  Verzeichnissen umzubenennen.

Das folgende Skript geht die Dateien in einem Verzeichnis durch und ersetzt mittels der Methode `replace(alter String, neuer String)` den Bindestrich durch einen Underscore.
```
# umbenennen.py

'''
liest Dateien aus einem Verzeichnis ein und führt 
eine Umbennung mit replace() durch
'''

import os

pfad = 'Dateien_zum_umbenennen'

datei_liste = os.listdir(pfad)

print('Dateien zum umbenennen:')
print(datei_liste)

for datei in datei_liste:
    os.rename(os.path.join(pfad, datei), os.path.join(pfad, datei.replace('-', '_')))

umbenannt_liste = os.listdir(pfad)
print('Umbenannte Dateien:')
print(umbenannt_liste)
```
Ausführen des Skripts:
```
$ python umbenennen.py 
Dateien zum umbenennen:
['datei-9', 'datei-7', 'datei-6', 'datei-1', 'datei-8', 'datei-27', 'datei-18', 'datei-20', 'datei-16', 'datei-29', 'datei-11', 'datei-10', 'datei-17', 'datei-28', 'datei-21', 'datei-26', 'datei-19', 'datei-4', 'datei-3', 'datei-2', 'datei-5', 'datei-23', 'datei-24', 'datei-12', 'datei-15', 'datei-14', 'datei-13', 'datei-25', 'datei-22', 'datei-30']
Umbenannte Dateien:
['datei_30', 'datei_6', 'datei_1', 'datei_8', 'datei_9', 'datei_7', 'datei_13', 'datei_14', 'datei_22', 'datei_25', 'datei_24', 'datei_23', 'datei_15', 'datei_12', 'datei_2', 'datei_5', 'datei_4', 'datei_3', 'datei_17', 'datei_28', 'datei_10', 'datei_26', 'datei_19', 'datei_21', 'datei_20', 'datei_27', 'datei_18', 'datei_11', 'datei_16', 'datei_29']
``` 




## Dateien öffnen
Zwei Dateitypen müssen unterschieden werden: Text-Dateien und Binary-Dateien. Erstere enthalten nur Text, Letztere sind alles andere. Mit beiden Dateitypen kann Python umgehen.

### Textdateien öffnen, lesen und beschreiben
Mit `open()` werden in Python Dateien geöffnet. Zusätzlich wird die Methode angegeben, was mit der Datei passieren soll:

* Wird sie gelesen (_read_)? Dann `open('textdatei.txt', 'r')`.
* Wird eine neue Datei angelegt, in die geschrieben (_write_) werden soll? Dann `open('textdatei.txt', 'w')`.
* Oder soll in eine bereits vorhandene Datei geschrieben werden (_append_)? Dann `open('textdatei.txt', 'a')`.

Die Funktion `open()` öffnet die Datei nur und legt die Methode fest, der eigentliche Lese- oder Schreibvorgang folgt dann. Die geöffnete Datei weist man in der Regel einer Variablen zu, die auf die geöffnete Datei zeigt:
```
f = open('datei.txt', 'r')
```
Beispiel:

Die Datei _textdatei.txt_ hat zweu Zeilen:
```
Dies ist die erste Zeile.
Dies ist die zweite Zeile.
```
Die Methode `read()` liest die Datei in _einen_ String ein:
```
>>> f = open('datei.txt', 'r')
>>> content = f.read()
'Dies ist die erste Zeile.\nDies ist die zweite Zeile.\n'
```
Beachte: Der String `content` enthält auch den Zeilenumbruch `\n` - _textdatei.txt_ ist ja eine zweizeilige Datei.

Wenn man die Datei nicht wieder ordentlich schließt, wird zwar keine Fehlermeldung ausgegeben, trotzdem sollte man das immer machen:
```
>>> f.close()
```
Verwendet man statt `read()` die Methode `readlines()`, wird die Datei zeilenweise in eine Liste eingelesen:
```
>>> f = open('textdatei.txt', 'r')
>>> content = f.readlines()
>>> content
['Dies ist die erste Zeile.\n', 'Dies ist die zweite Zeile.\n']
>>> f.close()
```
Man beachte, dass der Newline-Befehl `\n` trotzdem noch da ist.

Mit der Methode `write()` schreibt man in eine Datei:
```
>>> f = open('textdatei2.txt', 'w')
>>> f.write('Dies ist eine neue Datei!')
25
>>> f.close()
```
Die Zahl, die von `write()` zurückgegeben wird, gibt die Zahl der Zeichen an. Sollen zwei Zeilen, die man in eine Datei schreibt, dort auch zwei Zeilen sein, muss man `\n` mit ausgeben:
```
>>> f = open('textdatei3.txt', 'w')
>>> f.write('Dies ist die erste Zeile der neuen Datei!\n')
42
>>> f.write('Dies ist die zweite Zeile der neuen Datei!\n')
42
>>> f.close()
```
_Hinweis:_ Wenn nichts anderes angegeben ist, legt `open()` die Datei immer im aktuellen Arbeitsverzeichnis an.

_Hinweis:_ Da man evtl. vor hat, der Datei später noch weitere Zeilen hinzuzufügen, sollte man immer am Ende einer Zeile `\n` mit ausgeben.

