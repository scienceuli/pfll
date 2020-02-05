# Flusssteuerung
In den seltensten Fällen bestehen Computerprogramme nur aus Anweisungen, die stur nacheinander abgearbeitet werden wie bei einem Kochrezept:

1. Man kaufe ...
2. Man nehme ..
3. Man tue ...
4. Man mische ...
5. Man heize vor ...

Vielmehr enthalten fast alle Programme _Verzweigungen_ im Ablauf, die von bestimmten Werten und Resultaten anderer Programmschritte abhängen. Das heißt, ein Programm enthält Konstruktionen, die den **Fluss steuern**, also den weiteren Ablauf des Programms. Im Alltag ist es ja genauso, ständig müssen wir Entscheidungen treffen, die von bestimmten Parametern abhängen:

> _Wenn_ es regnet, _dann_ ziehe ich eine Jacke an.

> _Wenn_ ich genug zu tun habe, _dann_ lehne ich den Auftrag ab.

> _Wenn_ ich Hunger habe, _dann_ esse ich was. 

Damit hätten wir schon die häufigste Flusssteuerung kennengelernt, die **If-Anweisung**. Dazu später mehr.

## Boolesche Werte 
Der Ablauf eines Python-Programms hängt an vielen Stellen davon ab, ob ein bestimmter Zustand vorliegt oder nicht, ob also eine Aussage über diesen Zustand _wahr_ oder _falsch_ ist. In Pytrhon gibt es dafür den Datentyp **Boolean**, der genau zwei Werte haben kann: _True_ oder _False_. Die Schreibweise mit Großbuchstaben am Anfang ist wichtig, also nicht "true" oder "FALSE", sondern _True_ oder _False_:
```
>>> True
True
>>> False
False
>>> a = True
>>> a
True
>>> false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
```
Man beachte die Fehlermeldung in der letzen Zeile. Einer Variablen (_a_ im Beispiel) lässt sich also auch _True_ oder _False_ zuweisen. 

## Vergleichsoperatoren
Sehr oft werden in Python Aussagen mit _True_ oder _False_ bewertet, die etwas vergleichen mit Hilfe von **Vergleichsoperatoren**:
```
>>> 1 == 1
True
>>> 5 > 4
True
>>> 8 == "acht"
False
>>> 5 != 4
True
>>> 2 <= 2
True
>>> 2 >= 2
True
```
Hier tauchen folgende Vergleichsoperatoren auf:

| Operator | Bedeutung |
| ---- | ----|
| == | gleich |
| != | ungleich |
| < | kleiner |
| > | größer |
| >= | größer gleich |
| <= | kleiner gleich |

**Vorsicht**: Der Vergleichsoperator == ist von der Variablenzuweisung  = zu unterscheiden:
```
>>> alter = 17 # Variablenzuweisung
>>> alter == 23 # Vergleichsoperator
False
```

## Boolesche Operatoren
Aussagen, die _True_ oder _False_ sein können, lassen sich mit **Booleschen Operatoren** wie _and_, _or_ usw. verknüpfen und sind dann wiederum _True_ oder _False_:
```
>>> 5 > 4 and 2 > 1
True
```
5 größer 4 _und_ 2 größer 1: diese Aussage ist wahr. 5 größer 4 _und_ 1 größer 2 hingegen nicht:
```
>>> 5 > 4 and 1 > 2
False
```
5 größer 4 _oder_ 1 größer 2 ist hingegen wahr:
```
>>> 5 > 4 or 1 > 2
True
```
Eine Verknüpfung zweier Aussagen mit _or_ ist nur dann _False_, wenn beide Aussagen _False_ sind. Ist mindestens eine Aussage _True_, ist auch die Verknüpfung _True_, unabhängig vom Wahrheitsgehalt der anderen Aussage.

Häufig braucht man auch den Operator _not_:
```
>>> not True
False
>>> not False
True
```

## If- und Else-Anweisungen
Mit einer If-Anweisung prüft Python eine Aussage und führt dann abhängig vom Ausgang der Prüfung eine Anweisung aus:
```
>>> name = 'Ulrich'
>>> if name == 'Ulrich':
...     print('Hallo Ulrich')
... 
Hallo Ulrich
```
Zwei Dingen sind hier wichtig:
* Am Ende der if-Zeile kommt ein Doppelpunkt und eine neue Zeile.
* Die nächste Zeile ist eingerückt (in der Regel rückt man  vier Whitespaces ein). Auch alle weiteren Zeilen, die eingerückt sind, gehören noch zu dem if-Block. Nach dem If-Block geht es ohne Einrückung weiter, d.h. der erste Befehl nach der If-Anweisung _ohne_ Einrückung beendet die If-Anweisung.

Meist führt man If-Anweisungen nicht in der _Python Shell_ aus, sondern baut sie in ein Programm ein. So führt folgendes Skript:
```
# if_beispiel.py

name = "Ulrich"

if name == 'Ulrich':
    print('Hallo Ulrich')
    print('Alles klar?')

print('Fertig.')
```
zu folgender Ausgabe:
```
$ python if_beispiel.py 
Hallo Ulrich
Alles klar?
Fertig.
```
Die beiden print-Anweisungen im If-Block werden nur ausgeführt, wenn `name == 'Ulrich'` den Booleschen Wert _True_ hat. Die letzte nicht eingerückte print-Anweisung ist außerhalb des If-Blocks. Sie wird auf jeden Fall ausgeführt. Ersetze ich im Skript die Zuweisung durch 
```
name = 'Walter'
```
ergibt die Ausführung des Skripts:
```
$ python if_beispiel.py 
Fertig.
```






