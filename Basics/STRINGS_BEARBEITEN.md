# Strings bearbeiten
Lektorinnen arbeiten mit Text, also Zeichenketten, also _Strings_. Deshalb sind auch für sie Methoden interessant, mit denen sich _Strings_ bearbeiten lassen. 

## String-Typologie
Kurz gesagt, sind _Strings_ alles, was in Anführungszeichen steht:
```
>>> "Hallo"
'Hallo'
```
Um ein (einzelnes) Anführungszeichen selbst als Zeichen innerhalb eines Strings zu nutzen, muss es mit einem Backslash geschützt (_escape_) werden: 
```
>>> "Viele schreiben Hallos als Hallo\'s"
"Viele schreiben Hallos als Hallo's"
```
Auch andere Zeichen können durch einen Backslash geschützt werden und bekommen so eine spezielle Bedeutung, z.B. Newline und Tab:
```
>>> print("Hallo!\nHallo\tUlrich")
Hallo!
Hallo   Ulrich
```
_Raw Strings_ interpretieren hingegen Zeichen wie den Backslash nicht als Escape-Zeichen, sondern als normales Zeichen; in der Ausgabe wird deshalb wiederum der Backslah geschützt:
```
>>> r"Viele schreiben Hallos als Hallo\'s"
"Viele schreiben Hallos als Hallo\\'s"
```
Für sehr lange Strings kann man _Triple Quotes_ einsetzen. Dabei können während der Eingabe Returns eingegeben werden:
```
>>> print("""Ein langer String mit einem Absatz
... und einem Tab
... und noch einem Absatz.""")
Ein langer String mit einem Absatz
und einem Tab
und noch einem Absatz.
```
Belegen wir eine Variable mit einem Triple-Quote-String, enthält sie die eingegebenen Newlines als Escape Character:
```
>> string_lang = """Ein langer String mit einem Absatz
... ... und einem Tab
... ... und noch einem Absatz."""
>>> string_lang
'Ein langer String mit einem Absatz\n... und einem Tab\n... und noch einem Absatz.'
```

## Teile von Strings (String Slices)
Strings kann man sich als Liste vorstellen, z.B. `"Hallo!"` als Liste von sechs Zeichen. Man kann deshalb auf Teile eines Strings zugreifen wie auf Elemente einer Liste:
```
>>> spam = "Hallo!"
>>> spam[0]
'H'
>>> spam[1:2]
'a'
>>> spam[-1]
'!'
```
Oder prüfen, ob ein String bestimmte Zeichen enthält:
```
>>> 'al' in spam
True
>>> 'x' in spam
False
```

## String-Methoden
Strings lassen sich mit verschiedenen Methoden modifizieren. 

Um verschiedene Strings miteinander vergleichen zu können, ist es oft sinnvoll, Groß- und Kleinschreibung zu ignorieren, also sie in Groß- oder Kleinbuchstaben umzuwandeln:

* `spam.upper()` liefert Großbuchstaben:
  ```
  >>> spam.upper()
  'HALLO!'
  ```
* `spam.lower()` liefert Kleinbuchstaben:
  ```
  >>> spam.lower()
  'hallo!'
  ```

Beispiel: 
```
>>> antwort = input("ja/nein: ")
ja/nein: Ja
>>> antwort.lower() == "ja"
True
```
Die Antwort "Ja" wird als wahr bewertet, weil sie in Kleinbuchstaben dem Vergleichsstring "ja" entspricht. Groß- und Kleinschreibung werden übrigens geprüft mit `islower()` und `isupper()`:
```
>>> "Hallo".islower()
False
>>> "hallo".islower()
True
```
Es gibt noch weitere Prüfmethoden, die aufgrund ihrer Beschreibung selbsterklärend sind: `isalpha()`, `isalnum()`, `isdecimal()`, `isspace()`, `istitle()`:
```
>>> "5".isalpha()
False
>>> "5a".isalnum()
True
>>> "Dies Ist Ein Titel".istitle()
True
```
Von besonderer Bedeutung sind häufig auch Anfang und Ende eines Strings:
```
>>> spam = "Hallo"
>>> if spam.startswith("H"):
...     print("ok")
... 
ok
>>> "Ulrich".endswith("ch")
True
```
Um die Elemente einer Liste zu einem String zu verbinden, gibt es die Methode `join()`:
```
>>> ','.join(["Uli", "Walter", "Sabine"])
'Uli,Walter,Sabine'
```
`.join()` wird dabei an das/die Zechen angehängt, mit denen die Listenelemente verknüpft werden soll; in der Klammer steht die Liste. Als Verknüpfungszeichen gehen auch Newline, Tab usw.:
```
>>> print('\n'.join(["Uli", "Walter", "Sabine"]))
Uli
Walter
Sabine
```
Das Gegenstück zu `join()` ist `split()`. Es macht aus einem String eine Liste:
```
>>> "Hund,Katze,Maus".split(',')
['Hund', 'Katze', 'Maus']
>>> "Ich heiße Ulrich".split()
['Ich', 'heiße', 'Ulrich']
>>> "Ich heiße Ulrich".split( )
['Ich', 'heiße', 'Ulrich']
```
Defaultmäßig benutzt `split()` also den Whitespace zum Trennen, d.h. `split()` und `split( )` führen zum gleichen Ergebnis. Der Split-Character verschnwindet beim Splitten:
```
>>> "Ich wohne in Frickingen".split('i')
['Ich wohne ', 'n Fr', 'ck', 'ngen']
```
`rjust(n)` und `ljust()` geben rechts- und linksbündige Strings aus, wobei in der Klammer die Gesamtlänge des Strings angegeben wird:
```
>>> "Ulrich".rjust(10)
'    Ulrich'
```
In einem optionalen zweiten Parameter kann ein ein Füllzeichen angegeben werden:
```
>>> "172".rjust(12,".")
'.........172'
```
`center()` gibt es natürlich auch ...

Wichtige Methoden sind auch `strip()`, `lstrip()`, `rstrip()`, mit denen man Randzeichen eines Strings entfernt: 
```
>>> ' Ulrich '.strip()
'Ulrich'
>>> ' Ulrich '.lstrip()
'Ulrich '
>>> ' Ulrich '.rstrip()
' Ulrich'
```
`strip()` lässt sich auch mit beliebigen andere Zeichen verwenden:
```
>>> 'Ulrich'.strip('Uh')
'lric'
```
Mit der Methode `replace()` lassen sich Teile eines Strings ersetzen:
```
>>> 'Ulrich'.replace('ri', 'bru')
'Ulbruch'
```

## Kopieren in und von der Zwischenablage
Mithilfe des Moduls **pyperclip** können Strings aus Python heraus in die Zwischenablage kopiert werden bzw. der aktuelle Inhalt der Zwischenablage in einen String geschrieben werden. Das Modul muss zunächst installiert werden:
```
$ pip install pyperclip
```
`pyperclip.copy()` kopiert Text in die Zwischenablage, `pyperclip.paste()` fügt aus der Zwischenablage ein:
```
>>> import pyperclip
>>> pyperclip.copy("Das kopiere ich in die Zwischenablage")
>>> pyperclip.paste()
'Das kopiere ich in die Zwischenablage'
```

## Strings formatieren
String lassen sich mit dem Pluszeichen aneinander hängen. Beispiel:
```
>>> note = 'Hallo ' + name + ', kannst du am ' + tag + ' um ' + zeit + ' zu einem ' + veranstaltung + ' kommen? Auf der Tagesordnung stehen ' + agenda + '.'
>>> note
'Hallo Walter, kannst du am Dienstag um 15 Uhr zu einem Meeting kommen? Auf der Tagesordnung stehen agile Methoden.'
```
Das Zusammenbasteln des Strings _note_ auf diese Weise ist aber unübersichtlich und frickelig. 

Übersichtlicher ist ein formatierter String mit Platzhaltern:
```
>>> note = 'Hallo %s, kannst du am %s um %s zu einem %s kommen? Auf der Tagesordnung stehen %s.' % (name, tag, zeit, veranstaltung, agenda) 
>>> note
'Hallo Walter, kannst du am Dienstag um 15 Uhr zu einem Meeting kommen? Auf der Tagesordnung stehen agile Methoden.'
```
Nach dem String wird mit einem Tupel `(...)` angegeben, was für den Platzhalter `%s` eingesetzt werden soll.

Seite Python 3.? stehem F-Strings `f'...'` zur Verfügung, die noch _pythonischer_ sind:
```
>>> note = f'Hallo {name}, kannst du am {tag} um {zeit} zu einem {veranstaltung} kommen? Auf der Tagesordnung stehen {agenda}.' 
>>> note
'Hallo Walter, kannst du am Dienstag um 15 Uhr zu einem Meeting kommen? Auf der Tagesordnung stehen agile Methoden.'
```
Hier werden die einzusetzenden Variablen in geschweiften Klammern direkt im String platziert.







