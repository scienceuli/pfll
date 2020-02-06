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
```python
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
```python
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

| Operator | Bedeutung      |
| -------- | -------------- |
| ==       | gleich         |
| !=       | ungleich       |
| <        | kleiner        |
| >        | größer         |
| >=       | größer gleich  |
| <=       | kleiner gleich |

**Vorsicht**: Der Vergleichsoperator == ist von der Variablenzuweisung  = zu unterscheiden:
```python
>>> alter = 17 # Variablenzuweisung
>>> alter == 23 # Vergleichsoperator
False
```

## Boolesche Operatoren
Aussagen, die _True_ oder _False_ sein können, lassen sich mit **Booleschen Operatoren** wie _and_, _or_ usw. verknüpfen und sind dann wiederum _True_ oder _False_:
```python
>>> 5 > 4 and 2 > 1
True
```
5 größer 4 _und_ 2 größer 1: diese Aussage ist wahr. 5 größer 4 _und_ 1 größer 2 hingegen nicht:
```python
>>> 5 > 4 and 1 > 2
False
```
5 größer 4 _oder_ 1 größer 2 ist hingegen wahr:
```python
>>> 5 > 4 or 1 > 2
True
```
Eine Verknüpfung zweier Aussagen mit _or_ ist nur dann _False_, wenn beide Aussagen _False_ sind. Ist mindestens eine Aussage _True_, ist auch die Verknüpfung _True_, unabhängig vom Wahrheitsgehalt der anderen Aussage.

Häufig braucht man auch den Operator _not_:
```python
>>> not True
False
>>> not False
True
```

## If- und Else-Anweisungen
### If-Anweiseung
Mit einer If-Anweisung prüft Python eine Aussage und führt dann abhängig vom Ausgang der Prüfung eine Anweisung aus:
```python
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
```python
# if_beispiel.py

name = "Ulrich"

if name == 'Ulrich':
    print('Hallo Ulrich')
    print('Alles klar?')

print('Fertig.')
```
zu folgender Ausgabe:
```python
$ python if_beispiel.py 
Hallo Ulrich
Alles klar?
Fertig.
```
Die beiden print-Anweisungen im If-Block werden nur ausgeführt, wenn `name == 'Ulrich'` den Booleschen Wert _True_ hat. Die letzte nicht eingerückte print-Anweisung ist außerhalb des If-Blocks. Sie wird auf jeden Fall ausgeführt. Ersetze ich im Skript die Zuweisung durch 
```python
name = 'Walter'
```
ergibt die Ausführung des Skripts:
```python
$ python if_beispiel.py 
Fertig.
```

### Else- und Elif-Anweisung
Was passiert, wenn die Bedingung für die If-Anweisung _False_ ergibt? Das kann durch eine **Else-Anweisung** gesteuert werden:
### else Statements

```python
name = 'Bob'
if name == 'Alice':
    print('Hallo, Alice.')
else:
    print('Hallo, Fremder.')
```
Es können aber auch weitere Bedingungen formuliert werden mithilfe von beliebig vielen **Elif-Anweisungen** (elif = else if):
```python
name = 'Bob'
age = 30
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
```


## Loops
Viele Anweisungen in Programmen sind in Schleifen eingebettet, d.h. sie werden mehrmals hintereinander ausgeführt. Möchte man z.B. die Zahlen von 1 bis 10 ausgeben, könnte man 10 Print-Befehle hintereinander packen:
```python
print(1)
print(2)
print(3)
...
```
Die Schwierigkeit dieser Vorgehensweise wird spätestens dann deutlich, wenn man die Zahlen von 1 bis 100 ausgeben möchte.

Einfach ist es, eine Variable zu definieren, die alle Werte von 1 bis 10 durchläuft und bei jedem Durchgang mit dem aktuellen Wert ausgegeben wird:
```python
>>> for i in range(1,11):
...     print(i)
... 
1
2
3
4
5
6
7
8
9
10
```
`range(1,11)` stellt den Zahlenbereich von 1 bis 10 dar, d.h. die erste Zahl in `range()` wird mitgezählt, die letzte jedoch nicht mehr! Das muss man immer im Hinterkopf haben.
Gibt man nur eine Zahl ein, beginnt die Zählung bei 0 und geht bis Zahl minus eins.


