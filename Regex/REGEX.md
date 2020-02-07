# Reguläre Ausdrücke

Um die Umlaute in meinem Namen zu finden, könnte ich folgende Anweisung schreiben:
```python
>>> name = "Ulrich Kilian"
>>> for b in name:
...     if b == "a" or b == "e" or b == "i" or b == "o" or b == "u":
...             print(b)
... 
i
i
i
a
```
umständlich ... Einfacher ist es, ein Muster zu definieren, das alle Umlaute abdeckt, und dann nach diesem Muster zu suchen. Solche Muster nennt man _Reguläre Ausdrücke_, kurz _Regex_ für _Regular Expressions_.

Da _Regular Expressions_ ein häufig benutztes Werkzeug sind, hat Python dafür natürlich ein Modul in der Standardbibliothek: **re**.

Der Suchbefehl nach den Umlauten lautet mit einer _Regex_ nur noch:
```python
>>> import re
>>> name = "Ulrich Kilian"
>>> re.findall("[aeiou]",name)
['i', 'i', 'i', 'a']
```
Und was ist mit dem U? 
```python
>>> re.findall("[aeiouAEIOU]",name)
['U', 'i', 'i', 'i', 'a']
```
Oder:
```python
>>> re.findall("[aeiou]",name, re.I)
['U', 'i', 'i', 'i', 'a']
```
Der Flag `re.I` oder `re.IGNORECASE` sorgt dafür, dass Groß- und Kleinschreibung ignoriert wird.

## Raw Strings
Bei "normalen" Strings wird der Backslash interpretiert, wenn man die print-Funktion aufruft:
```python
>>> print("\tHallo")
        Hallo
```
Hier zum Beispiel wurde \t bei der Ausgabe in einen Tab umgewandelt.

Soll der String so behandelt werden, wie er ist (buchstäblich = _literally_), muss man ihn als _Raw String_ kennzeichnen, d.h. ein r voranstellen:
```
>>> print(r"\tHallo")
\tHallo
```
Jetzt wird der \ als Zeichen wie jedes andere auch behandelt. Das ist wichtig, denn gerade bei der Verwendung von _Regex_ sollen due Suchstrings so an **re** übergeben werden, dass sie von dem Modul verstanden werden. Python soll nichts damit anstellen. Im folgenden Beispiel wird bei der ersten Suche nichts gefunden. Erst die Kennzeichnung des Suchausdrucks als _Raw String_ bewirkt, dass `re.search()` nach dem Buchstaben "K" sucht, der am Wortanfang steht - genau das bedeutet \b in der Regex-Syntax.
```python
>>> name = "Ulrich Kilian"
>>> re.search("\bK", name)
>>> re.search(r"\bK", name)
<re.Match object; span=(7, 8), match='K'>
```

## Funktion von re
Das Modul **re** stellt eine Reihe von Funktionen zur Verfügung, mit denen man nach Regex such kann.

* `re.findall()`: gibt Liste aller Treffer zrück
* `re.search()`: gibt ein Trefferobjekt (_match_) zurück, falls eines gefunden wird; bei mehreren Treffern nur das erste
* `re.split()`: Gibt eine Liste zurück, in welcher der String, in dem gesucht wurde, bei jedem _match_ gesplittet wurde
* `re.sub()`: Ersetzt einen oder mehrere _match_ mit einem String



