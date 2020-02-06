# Dictionaries

## In Kürze

### Erzeuge leeres dictionary ###

    data = {}
    # OR
    data = dict()

### Erzeuge dictionary mit initial values ###

    data = {'a':1,'b':2,'c':3}
    # OR
    data = dict(a=1, b=2, c=3)
    # OR
    data = {k: v for k, v in (('a', 1),('b',2),('c',3))}

### Inserting/Updating einen einzelnen Value ###

    data['a']=1  # Updates if 'a' exists, else adds 'a'
    # OR
    data.update({'a':1})
    # OR
    data.update(dict(a=1))
    # OR
    data.update(a=1)

### Inserting/Updating mehrere Values ###

    data.update({'c':3,'d':4})  # Updates 'c' and adds 'd'
    
### Erzeuge  merged dictionary ohne Original zu ändern

    data3 = {}
    data3.update(data)  # Modifies data3, not data
    data3.update(data2)  # Modifies data3, not data2

### Lösche items in dictionary ###

    del data[key]  # Removes specific element in a dictionary
    data.pop(key)  # Removes the key & returns the value
    data.clear()  # Clears entire dictionary
 
### Prüfen, ob Key schon in einem dictionary
    key in data

### Iterate durch Pairs in einem dictionary
    for key in data: # Iterates just through the keys, ignoring the values
    for key, value in d.items(): # Iterates through the pairs
    for key in d.keys(): # Iterates just through key, ignoring the values
    for value in d.values(): # Iterates just through value, ignoring the keys

### Erzeuge ein dictionary von zwei Listen
    data = dict(zip(list_with_keys, list_with_values))

### Nur Python3: Erzeuge merged dictionary ohne Original zu ändern

    data = {**data1, **data2, **data3}

## csv in Dictionary umwandeln
Beispiel:

_schreibweisen.csv_
```
mit Hilfe,mithilfe
aufwändig,aufwendig
```
soll in dictionary umgewandelt werden:
```
{'mit Hilfe': 'mithilfe', 'aufwändig': 'aufwendig'}
```


Aufgabe:

1. Datei öffnen
2. Datei zeilenweise einlesen
3. Zeile aufspalten in Key und Value
4. Key-Value-Paar einem Dictionary hinzufügen

### Methode 1 
```
>>> schreibweisen_dict = {} # leeres dict anlegen
>>> with open('schreibweisen.csv', 'r') as f: # Datei öffnen
...     for line in f: # Datei zeilenweise einlesen
...             alt = line.split(',')[0].strip()
...             neu = line.split(',')[1].strip()
...             schreibweisen_dict[alt] = neu
>>> >>> schreibweisen_dict
{'mit Hilfe': 'mithilfe', 'aufwändig': 'aufwendig'}
```
Jede Zeile wird am Komma gesplittet, daraus entsteht eine Liste mit zwei Elementen (Indizes 0 und 1). Jedes Element wird bereinigt mit `strip()`, d.h. Leerzeichen/Newlines am Anfang/Ende entfernt, und den Variablen `alt` bzw. `neu` zugewiesen.

Anschließend wird `alt` als _Key_ des Dictionarys gesetzt und `neu`  als _Value_.

### Methode 2 
Etwas eleganter und kürzer geht es noch mit dem Modul **csv** aus der Python-Standardbibliothek.
```
>>> schreibweisen_dict = {}
>>> import csv
>>> with open('schreibweisen.csv','r') as f:
...     reader = csv.reader(f)
...     schreibweisen_dict = {rows[0]:rows[1] for rows in reader}
... 
>>> schreibweisen_dict
{'mit Hilfe': 'mithilfe', 'aufwändig': 'aufwendig'}
```
Mit `csv.reader(f)` wird die gesamte Datei auf einmal in die Liste `reader` eingelesen. Jede Zeile wird automatisch am Komma aufgespalten und bereinigt. Mit 
```
schreibweisen_dict = {rows[0]:rows[1] for rows in reader}
```
legt man dann in einem Rutsch das Dictionarys an, indem man über alle Zeilen in `reader` iteriert und jedes Mal ein Key-Value-Paar `row[0]:row[1]` erzeugt.


