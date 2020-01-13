# Python Basics
Um die Basiselemente von Python kennenzulernen, nutzen wir die **Python Shell**, die nach der erfolgreichen Installation von Python zur Verfügung steht. Die Python Shell wird gestartet, wenn man in der **Konsole** (Eingabeaufforderung, Terminal) `python` eingibt und die Enter-Taste drückt. Anschließend sieht man eine Eingabezeile, der das Prompt `>>>` vorangestellt ist. Man kann auch die **IDLE** benutzen, die zusammen mit Python installiert wurde. Auch sie enthält eine Python Shell. 

## Ausdrücke in Python
In der Python Shell kann man nun _Befehle_ eingeben, also Anweisungen an Python, irgendetwas zu machen. Die einfachsten Befehle bilden _Ausdrücke_ (_Expressions_), die Werte mit Operatoren verknüpfen und als Resultat einen einzigen Wert zurückgeben. Wir kennen das am besten aus der Mathematik:
```
>>> 1 + 1
2
>>> 7 * 2
14
>>> 10/5
2.0
>>> 7 + (2 * 3)
13
>>> 2 * 4.5
9.0
>>> 6 + 
  File "<stdin>", line 1
    6 + 
       ^
SyntaxError: invalid syntax
```
_Hinweis 1_: Die Leerzeichen sind nicht notwendig, sieht aber übersichtlicher aus und sollte man sich beim Schreiben von Programmen angewöhnen.

_Hinweis 2_: Der Multiplikationsoperator ist der Stern `*`.

_Hinweis 3_: Das Dezimalkomma ist (wie in allen Programmiersprachen) der Punkt.

Immer, wenn Python eine Anweisung nicht versteht, gibt es einen Fehler zurück, z.B. bei dem sinnlosen Ausdruck  `6 +`. 

Man muss in Python zwar keine _Datentypen_ deklarieren, trotzdem gehört jeder Wert in einem Python-Ausdruck zu einem bestimmten Datentyp: 5 ist ein _Integer_, 3.0 ein _Float_. 

Neben diesen Zahlentypen gibt es auch den Zeichentyp _String_. _Strings_ sind also Zeichenketten wie `"Hallo Welt"`. Sie stehen in Anführungszeichen (einfachen oder doppelten). 

Auch _Strings_ kann man mit Operatoren verknüpfen:
```
>>> 'Lektor' + 'Innen'
'LektorInnen`
```
Man spricht in diesem Fall von _Concatenation_: Füge die _Strings_ aneinander. Das Pluszeichen hat also verschiedene Bedeutung für Zahlen und Strings, und deshalb verwundert es nicht, dass die Vermischung zu einem Fehler führt:
```
>>> 3 + 'Hallo'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
**Aber:** Eine Multiplikation _String_ * _Integer_ ist erlaubt und ein nützliches Feature:
```
>>> 'Hallo' + '!'*5
'Hallo!!!!!'
```

## Variablen
**Variablen** sind sehr wichtige Objekte in Python. Dabei weist man einer frei wählbaren Bezeichnung einen bestimmten Wert zu:
```
>>> a = 5
>>> spam = "Hallo"
```
Python-Programmiererinnen müssen Variablen nicht deklarieren, also erst sagen "a ist eine Integer-Zahl und a bekommt den Wert 5", aber durch die Zuweisung `a = 5`  wird `a` zu einer Integer-Variable und durch `spam = "Hallo"` wird `spam` zu einer String-Variablen. Folgende Konstruktion führt deshalb wieder zu einem Fehler:
```
>>> a + spam
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
während
```
>>> spam = "Guten "
>>> egg = "Appetit"
>>> spam + egg
'Guten Appetit'
```
funktioniert. (_Hinweis_: spam, egg etc. werden in Python-Tutorials gerne als Variablennamen benutzt, zum Hintergrund: mal auf Youtube nach Monty Python und diesen Begriffen suchen.)

Variablen können jederzeit überschrieben werden, der alte Wert ist dann vergessen:
```
>>> a = 3
>>> a
3
>>> a = 5
>>> a
5
```
Befehle der Form `a = 3` liefern nichts zurück, sondern sind _Statements_. Im Python-Alltag unterscheidet man die Ausdrücke _Expression_ und _Statement_ in der Regel aber nicht, sondern spricht einfach von _Code_.

## Programme schreiben und ausführen
Die Python-Shell führt die Code-Zeilen, den man in ihr schreibt, unmittelbar aus. Die andere Möglichkeit, Code zu schreiben, besteht darin, in einem Text-Editor Programme zu schreiben, die anschließend von oben nach unten abgearbeitet werden. Als Editoren eignen sich vor allem spezielle **Entwicklungsumgebungen**, die das Programmieren durch Zusatzfunktionen erleichtern. Es gibt sehr mächtige Editoren, aber auch sehr einfach gehaltene, die für den Einstieg vollkommen ausreichen, z.B.:
* die mit Python installierte **IDLE**
* [Thonny](https://bitbucket.org/plas/thonny/downloads/)
* [Mu](https://codewith.mu/en/download)

Das folgende einfache Programm _print\_input.py_ verwendet die Funktionen `print()` und und `input()`:
```
# print_input.py
# Programm mit print und input

print('Wie heißt du?')

name = input()  # Eingabe des Namens

print('Hallo, ' + name)
```

* `print(string)` gibt einen String aus, also irgendetwas, was in Anführungszeichen steht, oder eine Variable, der zuvor ein String zugewiesen wurde, z.B. `frage = 'Wie heißt du?'` und `print(frage)`. Man sagt: Die Funktion `print` wurde mit dem _Argument_ `frage` aufgerufen. 
* `input()` wartet auf eine Eingabe von der Konsole, in der das Programm ausgeführt wurde. Dieser Funktion muss kein Argument übergeben werden, die Klammer bleibt leer, _muss_ aber immer geschrieben werden.
* Das, was der User nun eingegeben hat, wird der Variablen `name` zugewiesen. `input()` gibt immer einen String zurück, selbst wenn ich eine Zahl eingebe. Das können wir in der Shell schnell überprüfen: 
    ```
    >>> name = input()
    Uli
    >>> name
    'Uli'
    >>> zahl = input()
    11
    >>> zahl
    '11'
    ```
  Aus der Eingabe 11 mach `input()` den String `'11'`.
* Ein \# macht alles, was danach steht, zu einem Kommentar. Kommentare sind sehr wichtig in Programmen, damit man sich nach einem halben Jahr noch daran erinnert, was man sich damals gedacht hat ...
* Ein Python-Programm kann beliebig viele Leerzeilen enthalten. Sie dienen der Strukturierung und Lesbarkeit des Programms.

Das Programm speichert man unter einem beliebigen Dateinamen mit der Endung _.py_ ab (auch hier sind aussagekräftige Dateinamen vorzuziehen). Anschließend kann man es aus dem Terminal heraus ausführen:
```
$ python print_input.py 
Wie heißt du?
Uli
Hallo, Uli
```



## Listen
### Listen anlegen und darauf zugreifen
**Listen** sind sehr nützliche Konstuktionen. Man hat ja auch im Lektorinnenalltag ständig damit zu tun: Listen von Begiffen, von Namen, von Projekten, von ...

Listen werden in Python mit eckigen Klammern notiert, wobei die Listenelemente mit Kommas abgetrennt werden:
```
namen_liste = ['Ulrich', 'Walter', 'Sabine']
```
Diese Liste (von mir `namen_liste` genannt) enthält drei Strings als Elemente. Ihre Länge ist also 3:
```
>>> namen_liste = ['Ulrich', 'Walter', 'Sabine']
>>> len(namen_liste)
3
```
Die Funktion `len()` kann man auch auf Strings anwenden. Dann gibt sie die Länge des Strings zurück:
```
>>> name = 'Ulrich'
>>> len(name)
6
```
Die Elemnte einer Liste werden von Python durchnummeriert, beginnend bei 0:
```
>>> namen_liste[0]
'Ulrich'
>>> namen_liste[1]
'Walter'
>>> namen_liste[2]
'Sabine'
```
Der `print()`-Befehl angewandt auf die Liste gibt die gesamte Liste aus, inklusive Klammern:
```
>>> print(namen_liste)
['Ulrich', 'Walter', 'Sabine']
```
Manchmal durchaus nützlich: Der Index -1 gibt immer das letzte Element einer Liste aus, der Index -2 das vorletzte usw.:
```
>>> namen_liste[-1]
'Sabine'
>>> namen_liste[-2]
'Walter'
>>> namen_liste[-3]
'Ulrich'
```
Listen lassen sich ändern,
```
>>> namen_liste[0] = 'Ursula'
>>> namen_liste
['Ursula', 'Walter', 'Sabine']
```
und mithilfe von `append()` verlängern.
```
>>> namen_liste.append('Ulrich')
>>> namen_liste
['Ursula', 'Walter', 'Sabine', 'Ulrich']
```
Möchte man an einer bestimmten Stelle, z.B. der mit Index 1, ein Element einfügen, nutzt man
```
>>> namen_liste.insert(1, 'Monika') 
>>> namen_liste
['Ursula', 'Monika', 'Walter', 'Sabine', 'Ulrich']
```

### Listen sortieren
Sehr oft möchte man Listen sortieren. Dabei gibt es zwei Möglichkeiten:
* dauerhaft sortieren mit `sort()` (bzw. `sort(reverse=True)` für die andere Richtung, d.h. die Liste wird geändert:
  ```
  >>> namen_liste.sort()
  >>> namen_liste
  ['Monika', 'Sabine', 'Ulrich', 'Ursula', 'Walter']
  >>> namen_liste.sort(reverse=True)
  >>> namen_liste
  ['Walter', 'Ursula', 'Ulrich', 'Sabine', 'Monika']
  ```
* einmalig sortieren, ohne die ursprüngliche Liste zu ändern, mit der Funktion `sorted()`:
  ```
  >>> sorted(namen_liste)
  ['Monika', 'Sabine', 'Ulrich', 'Ursula', 'Walter']
  >>> namen_liste
  ['Walter', 'Ursula', 'Ulrich', 'Sabine', 'Monika']
  ```

## Dictionaries

Auch der Datentyp _Dictionaries_ stellt eine listenähnliche Datensammlung dar, allerdings werden jetzt die Dictionary-Elemente nicht einfach durchnummeriert, sondern bestehen aus **Schlüssel-Wert-Paaren** wie `"name": "Ulrich"`. Hierbei ist `"name"` der Schlüssel und `"Ulrich"` der zugehörige Wert. Der Wert kann auch eine Zahl sein: `"alter": 26`. Die Schlüssel-Wert-Paare werden durch geschweifte Klammern zu einem _Dictionary_ zusammengefasst:
```
person = {"name": "Ulrich", "alter": 42, "ort": "Frickingen"}
```
Ein _Dictionary_ kann man sich also wie einen Steckbrief für ein Objekt vorstellen.   

Die Werte eines _Dictionaries_ lassen sich über den Schlüssel abrufen:
```
>>> person = {"name": "Ulrich", "alter": 26, "ort": "Frickingen"}
>>> print(person["name"] + " ist " + str(person["alter"]) + " Jahre alt.")
Ulrich ist 42 Jahre alt.
```
Man beachte hier: Das Pluszeichen kann nur Strings mit Strings verknüpfen. Deshalb muss die Integer-Zahl `person["alter"]` erst mithilfe der Funktion `str(person["alter"])` in einen String umgewandelt werden.












