# Funktionen
## Built-in Functions
Funkionen haben im Wesentlichen eine Aufgabe: Sie werden mit Input "gefüttert" und liefern einen _Return_ zurück. Einige _Built-in Functions_ haben wir bereits benutzt: `print()` gibt eine Ausgabe am Schirm zurück, `len()` die Länge eines Objekts und `input()` eine Eingabe über das Terminal. Viele weitere Funktionen werden in den Modulen der _Standard Library_ definiert. Das Modul **math** stellt eine Reihe mathematischer Funktionen zur Verfügung, das Modul **random** Funktionen rund um Zufallszahlen usw. So erzeugt beispielsweise die Funktion `randint(a, b)` aus dem Modul **random** eine Zufallszahl zwischen a und b. Um eine Funktion aus einem Modul zu nutzen, muss

1. das Modul importiert werden,
2. die Funktion aus dem Modul an den Modulnamen gehängt werden.

Beispiel:
```python
>>> import random
>>> z = random.randint(1,10)
>>> z
4
```
Die Schreibweise `random.randint()` bedeutet hier also: "Schau im Modul **random** nach der Funktion `randint()`."

Neben den Modulen aus der _Standard Library_ lassen sich noch zahlreiche _Third Party Modules_ installieren, z.B. mit dem `pip`-Kommando im Terminal:
```
$ pip install Flask
```

## Funktionen definieren
Man kann aber nicht nur _built-in functions_ nutzen, sondern selbst Funktionen definieren. Es sind quasi Miniprogramme innerhalb eines Programms, die aus dem Hauptprogramm aufgerufen werden und dann einen bestimmten Code ausführen.

Beispiel:

Man möchte aus einem Bruttobetrag den Nettobetrag ausrechnen. Die Formel dazu ist

> netto = brutto/1.19

für 19% Umsatzsteuer. Wir legen ein Skript an und definieren darin eine Funktion, die genau das tut:
```python
# netto_brutto.py

def brutto2netto(brutto):
    return round(brutto/1.19,2)

print(brutto2netto(119))
print(brutto2netto(217))
print(brutto2netto(830))
```

1. Das Schlüsselwort `def` leitet die Definition der Funktion ein.
2. Dann kommt der selbstgewählte Name.
3. In Klammern werden die _Argumente_ aufgelistet, die an die Funktion übergeben werden.
4. Dann folgt ein Doppelpunkt.
5. Der Code, der innerhalb der Funktion ausgeführt wird, wird eingerückt. Alle Zeilen, die nach der `def...:`-Zeile eingerückt sind, gehören zur Funktion.
6. `return` gibt den Rückgabewert der Funktion an. Das kann eine Zahl, ein String, eine Liste etc. sein.
7. Wenn die Funktion aufgerufen wird, wird das Argument in Klammern übergeben.

Eine Funktion muss aber keine Argumente enthalten und auch kein _return_. Auch die folgende Funktion ist eine gültige Funktion:
```python
def hallo():
    print('Hallo')

hallo()
```
Auch wenn keine Argumente übergeben werden, sind die Klammern zwingend, sowohl in der Definition als auch im Aufruf der Funktion. Ohne Argumente bleiben sie einfach leer. 
