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
Übersichtlicher ist es, die Regex zunächst zu kompilieren und diner Variablen zuzuweisen. Mit dieser Variable können dann verschiedene Funktionen aufgerufen werden (s.u.):
```
>>> regex = re.compile(r'\bK')
>>> regex.search(name)
<re.Match object; span=(7, 8), match='K'>
```
Ein String mit dem gefundenen Text (_Match_) bekommt man mit der Methode `group()`:
```python
>>> mo = regex.search(name)
>>> mo.group()
'K'
```

## Regex Search

Die Abfolge zusammengefasst:
1. Importiere das Regex-Module mit `import re`.
2. Erzeuge ein Regex-Objekt mit der Funktion `re.compile()`. Nicht vergessen: _Raw String_ benutzen.
3. Der String, in dem gesucht werden soll, wird an die Methode `search()` übergeben. Diese wird an das Regex-Objekt gebunden. Zurück kommt ein _Match_-Objekt.
4. Um den gefundenen Text zu bekommen, wird die Methode `group()` aufgerufen. Sie gehört zum _Match_ Objekt. 


## Funktion von re
Das Modul **re** stellt eine Reihe von Funktionen zur Verfügung, mit denen man nach Regex such kann.

* `re.compile()`
* `re.findall()`: gibt Liste aller Treffer zrück
* `re.search()`: gibt ein Trefferobjekt (_match_) zurück, falls eines gefunden wird; bei mehreren Treffern nur das erste
* `re.split()`: Gibt eine Liste zurück, in welcher der String, in dem gesucht wurde, bei jedem _match_ gesplittet wurde
* `re.sub()`: Ersetzt einen oder mehrere _match_ mit einem String


## Beispiele
### Suche nach einer Telefonnummer:
```python
>>> message = "Hallo, meine Telefonnummer ist 0123-4567890."
>>> tel_regex = re.compile(r'\d\d\d-\d\d\d\d\d\d\d')
>>> mo = tel_regex.search(message)
>>> print(f'Mobilnummer gefunden: {mo.group()}')
Mobilnummer gefunden: 123-4567890
```
### Mit Klammern gruppieren:
```python
>>> tel_regex = re.compile(r'(\d\d\d)-(\d\d\d\d\d\d\d)')
>>> mo = tel_regex.search(message)
>>> print(f'Mobilnummer gefunden mit Vorwahl  {mo.group(1)}')
Mobilnummer gefunden mit Vorwahl  123
```
`groups()` liefert alle _groups_ als Tupel zurück:
```python
>>> mo.groups()
('123', '4567890')
```
### Multiple Suche mit der _Pipe_ = "entweder oder":
```python
>>> text = "Ulrich besuchte Walter zushause."
>>> name_regex = re.compile(r'Ulrich|Walter')
>>> mo = name_regex.search(text)
>>> print(f'Wer besucht? {mo1.group()}')
Wer besucht? Ulrich
>>> text = "Walter besucht Ulrich zuhause."
>>> mo = name_regex.search(text)
>>> print(f'Wer besucht? {mo.group()}')
Wer besucht? Walter
```
_Hinweise_: 

1. Die Suche wird nach dem ersten Treffer ("Ulrich" oder "Walter") abgebrochen.
   Will man alle Treffer, muss man die Methode `findall()` verwenden:
   ```python
   >>> mo = name_regex.findall(text)
   >>> print(mo)
   ['Walter', 'Ulrich']
   ```
2. Leerzeichen spielen eine Rolle: `re.compile(r'Ulrich|Walter')` ist eine andere Regex als `re.compile(r'Ulrich | Walter')`.

### Suche nach Literaturangaben
In einem Text sind Literaturverweise in der Form _(Meier 2018)_ angegeben, wobei auch mehrere Namen vorkommen können wie _(Müller und Schmidt 2017)_ oder _(Müller et al. 2010)_. Das Muster ist also:

> Klammer plus irgendwelche Zeichen plus ein Leerzeichen plus vierstellige Zahl

Um nach solchen Literaturangaben zu suchen, könnte man folgende Regex definieren:
```python
>>> lit_regex = re.compile(r'\(.+?\s\d{4}\)')
>>> text = "Wie bereits in (Meier 2018) und (Müller und Schmidt 2017) gezeigt wurde, sind die Aussagen von (Müller et al. 2010) Quatsch."
>>> mo = lit_regex.findall(text)
>>> mo
['(Meier 2018)', '(Müller und Schmidt 2017)', '(Müller et al. 2010)']
```
Hier werden mehrere Eigenschaften regulärer Ausdrücke deutlich:

* Da runde Klammern in regulären Ausdrücken dazu dienen, Gruppen zu bilden (s.u.), muss man der Klammer, wenn sie als "echtes" Zeichen gesucht werden soll, einen Backslash \ voranstellen.
* Ein Punkt  . steht für ein beliebiges Zeichen, das Pluszeichen  + bedeutet "ein oder mehrere Vorkommen". Das Fragezeichen signalisiert, dass die Suche nicht "gefräßig" (_greedy_) sein soll, d.h. es wird der minimal mögliche Match zu .+ gesucht.
* \s steht für ein Whitespace.
* Eine Zahl in geschweiften Klammern gibt die Anzahl an, in der das davor stehende Musterzeichen (hier \d) auftreten soll.

Eine Gruppierung könnte man hier nutzen, um nach dem Matching auf den/die Autoren und die Jahreszahl zugreifen können:
```python
>>> lit_regex = re.compile(r'(\((.+?)\s(\d{4})\))')
>>> mo = lit_regex.findall(text)
>>> mo
[('(Meier 2018)', 'Meier', '2018'), ('(Müller und Schmidt 2017)', 'Müller und Schmidt', '2017'), ('(Müller et al. 2010)', 'Müller et al.', '2010')]
```
`findall()` listet jetzt nicht nur den gesamten Litearturverweis auf (äußere Klammer im Regex), sondern auch die Untergruppen `(.+?)` (die Autoren) und `(\d{4})` (die Jahreszahl). Pro Match werden alle drei Gruppen als Tupel zurückgegeben. Diese Struktur könnte man nutzen, um eine Liste aus Autoren und Jahreszahlen anzulegen:
```python
>>> for tuple in mo:
...     print(f'Autor:\t{tuple[1]}\tJahr:\t{tuple[2]}')
... 
Autor:  Meier   Jahr:   2018
Autor:  Müller und Schmidt      Jahr:   2017
Autor:  Müller et al.   Jahr:   2010
```
Mit der _Python Extension_ `(?P<name>...)`  kann man Gruppen sogar benennen. Das ist hilfreich, wenn die Regex aus vielen Gruppen besteht, auf die man bei einem _Match_ zugreifen möchte:
```python
>>> lit_regex = re.compile(r'(?P<zitat>\((?P<autor>.+?)\s(?P<jahr>\d{4})\))')
>>> mo = lit_regex.search(text)
>>> mo.group()
'(Meier 2018)'
>>> mo.group('jahr')
'2018'
>>> mo.groupdict()
{'zitat': '(Meier 2018)', 'autor': 'Meier', 'jahr': '2018'}
```
Werden die Regex länger, kann man _Triple Quotes_ und die Option _re.VERBOSE_ nutzen, um den Regex mehrzeilig zu schreiben und Kpmmentare anzubringen:
```python 
lit_regex = re.compile(r"""(?P<zitat>\()        # ganzes Zitat
                           (?P<autor>.+?)       # Autor
                           \s
                           (?P<jahr>\d{4})      # Jahr
                           \))""", re.VERBOSE)
```
Das funktioniert nicht mit `findall()`. Aber mithilfe von `finditer()` kann man zunächste eine Liste von _Matchings_ erzeugen, über die man dann iterieren kann:
```python
>>> mo_iteration = lit_regex.finditer(text)
>>> for mo in mo_iteration:
...     print(mo.group('jahr'))
... 
2018
2017
2010
```
### Suche nach doppelten Wörtern
Die benannten Gruppen in Regex lassen sich nutzen, um mit _backreferences_ zu arbeiten, d.h.: Die Suche findet einen _Match_ und sucht dann nach dem Text des _Match_ weiter. Damit lassen sich z.B. doppelte Wörter aufspüren  
```python
>>> text = "Anschließend fuhren wir noch noch in die Stadt."
>>> doppelt_regex = re.compile(r'\b(?P<wort>\w+)\s+(?P=wort)\b')
>>> doppelt_regex.search(text).group()
'noch noch'
```

### Falsch geschriebene Wörter finden
Die automatische Textanalyse ist ein aktuelles Forschungsgebiet. Wer sich dafür interessiert, sollte man nach _Textmining_, _NLTK_ etc. recherchieren.

Hier nur ein einfaches Beispiel, wie man einen Text nach Wörtern untersucht, die wir in einer Liste falscher Schreibweisen gesammelt haben:
```python
>>> falsch_liste = ['nähmlich', 'wiederspiegeln', 'Kalrsruhe']
```
Damit wollen wir jetzt die Wörter in einem Text vergleichen. Die _Regex_ für ein einzelnes Wort ist recht einfach:
```python
>>> wort_regex = re.compile(r'\w+')
```
Damit zerlegen wir jetzt einen kleinen Text in Wörter:
```python
>>> text = 'Dann fuhren wir nähmlich nach Kalrsruhe und überlegten uns, was wir zu Abend essen.'
>>> wort_liste = wort_regex.findall(text)
>>> wort_liste
['Dann', 'fuhren', 'wir', 'nähmlich', 'nach', 'Kalrsruhe', 'und', 'überlegten', 'uns', 'was', 'wir', 'zu', 'Abend', 'essen']
```
Jetzt vergleichen wir alle Wörter des Textes mit der Falsch-Liste:
```
>>> for wort in wort_liste:
...     if wort in falsch_liste:
...             print(f'falsches Wort gefunden: {wort}')
... 
falsches Wort gefunden: nähmlich
falsches Wort gefunden: Kalrsruhe
```
Ein sehr einfaches Beispiel, aber es zeigt eine Möglichkeit, was sich eventuell machen lässt.

Möglichwerweise interessant: [Website der HS Hannover](http://textmining.wp.hs-hannover.de/Korrektur.html)

## Review of Regex Symbols

| Symbol                   | Matches                                                      |
| ------------------------ | ------------------------------------------------------------ |
| `?`                      | zero or one of the preceding group.                          |
| `*`                      | zero or more of the preceding group.                         |
| `+`                      | one or more of the preceding group.                          |
| `{n}`                    | exactly n of the preceding group.                            |
| `{n,}`                   | n or more of the preceding group.                            |
| `{,m}`                   | 0 to m of the preceding group.                               |
| `{n,m}`                  | at least n and at most m of the preceding p.                 |
| `{n,m}?` or `*?` or `+?` | performs a nongreedy match of the preceding p.               |
| `^spam`                  | means the string must begin with spam.                       |
| `spam$`                  | means the string must end with spam.                         |
| `.`                      | any character, except newline characters.                    |
| `\d`, `\w`, and `\s`     | a digit, word, or space character, ectively.                 |
| `\D`, `\W`, and `\S`     | anything except a digit, word, or space acter, respectively. |
| `[abc]`                  | any character between the brackets (such as a, b, ).         |
| `[^abc]`                 | any character that isn’t between the brackets.               |












