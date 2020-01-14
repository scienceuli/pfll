# Arbeiten mit Schnittstellen
## Was sind Schnittstellen?

Möchten wir etwas in der Wikipedia nachschlagen, gehen wir normalerweise auf wikipedia.de und suchen dort das entsprechende Schlagwort. Wikipedia bietet seine Inhalte aber auch in maschinenlesbarer Form über eine **Schnittstelle** an. Im Fachjargon: eine **API**, das steht für _Application Programming Interface_. Eine solche Programmierschnittstelle dient generell dazu, Informationen zwischen einer Anwendung und einzelnen Programmteilen standardisiert auszutauschen. Besondere Bedeutung haben **Web-APIS**, also Schnittstellen zu Web-Anwendungen, um dort Daten abzugreifen, die man dann im eigenen Programm weiterverarbeiten kann. Viele Web-Services bieten APIs an, nicht nur Wikipedia. Auch viele Software-Anwendungen haben APIs, sodass man die Daten aus dem Programm abgreifen und woanders einfügen kann. Kurz gesagt: APIs fungieren als Datenübermittler im Softwarebereich. Inhalte können mit Hilfe von APIs zwischen verschiedenen Webseiten und Programmen ausgetauscht werden.

Um Daten über Schnittstellen auszutauschen, können verschiedene Datenformate benutzt werden. Weit verbreitet sind **REST-APIs**. Hier werden Daten über eine **URL**, d.h. eine Webdadresse _http://...._, abrufbar gemacht. Man sagt auch: diese URL ist der **API-Endpunkt** (_endpoint_). Zurück kommt aber nicht eine Webseite, die ich mir im Browser anschaue, sondern struktierte Daten, etwa **XML** oder **JSON**. JSON-Objekte sind einfach aufgebaute, flexible und gut lesbare Sammlungen von Schlüssel-Wert-Paaren ohne "Schnickschnack", z.B.
```
{"farbe": "Rot"}
```
Hier ist `farbe` der Schlüssel und `Rot` der zugehörige Wert. Ein einfache To-Do-Liste könnte im JSON-Format so aussehen:
```
[
    {"aufgabe": "Steuererklärung", "termin": "Januar"},
    {"aufgabe": "Buch XY lektorieren", "termin": "gestern"},
    {"aufgabe": ...}
    ...
]
```
Man braucht gar keine spezielle Darstellung, um dieses JSON-Ojekt lesen zu können.

Zurück zu Wikipedia: Auch hier werden die Daten als JSON-Objekte angeboten, die sich mit einer bestimmten URL (API-Endpunkt) abrufen lassen. Der API-Endpunkt zum Wikipedia-Artikel über den VfLL (bzw. zu einer Kurzform) ist beispielsweise 
```
https://de.wikipedia.org/api/rest_v1/page/summary/Verband_der_Freien_Lektorinnen_und_Lektoren
```
Einfach mal diesen Endpunkt kopieren und im Browser aufrufen (z.B. im Firefox; dort kann man zwischen den JSON-Rohdaten und einer lesefreundlichen Darstellung wechseln – geht in anderen Browsern mit entsprechenden Plugins sicher auch).

## Wikipedia-API und Python
Wie nicht anders zu erwarten, gibt es auch für Python Erweiterungen (_Packages_), um aus einem Skript heraus die Wikipedia-API anzusprechen. Zum Beispiel `wikipedia`; es wird mit `pip`(oder `pipenv`) installiert:
```
$ pip install wikipedia
```
Einige Beispiele, was man damit machen kann:
* Zu Beginn (egal ob im Script oder der Python Shell) muss `wikipedia` importiert werden: 
  ```
  >>> import wikipedia
  ```
* Standardmäßig sucht die Methode `search()` in der englischen Wikipedia. Um wikipedia.de zu nutzen, muss die Spracheinstellung geändert werden:
    ```
    >>>  wikipedia.set_lang("de")
    ```
* Die Methode `search(suchstring)` findet alle Wikipedia-Artikel, in denen der Suchstring vorkommt, und gibt sie als Liste zurück:
  ```
  >>> wikipedia.search("vfll")
  ['Verband der Freien Lektorinnen und Lektoren', 'Lektorat', 'Deutsche Literaturkonferenz', 'Oliver Grasmück', 'Wissenschaftslektorat', 'Rainer Schöttle', 'Christiane Geldmacher']
  ```
* Die Listenelemente lassen sich wie üblich ansprechen: 
  ```
  >>> wikipedia.search("vfll")[0]
  'Verband der Freien Lektorinnen und Lektoren'
  ```
* Die Methode `summary()` gibt die Zusammenfassung eines Wikipedia-Artikels zurück; mit dem zusätzlichen Argument `sentences` kann die Anzahl der zurückgegebenen Sätze eingeschränkt werden:
  ```
  vfll = wikipedia.search("vfll")[0]
  >>> vfll
  'Verband der Freien Lektorinnen und Lektoren'
  >>> wikipedia.summary(vfll, sentences=2)
  'Der Verband der Freien Lektorinnen und Lektoren (VFLL) ist Interessenvertretung und Netzwerk der freiberuflich arbeitenden  Lektoren in Deutschland. Er wurde im Jahr 2000 gegründet und hat 2019 etwa 950 Mitglieder, wobei der Nachweis einer freien Tätigkeit in mindestens einem Bereich wie Lektorat, Korrektorat oder Redaktion Voraussetzung für die Mitgliedschaft ist.'
  ```
  `summary()` gibt aber einen Fehler zurück, falls der Wikipedia-Artikel nicht existiert oder nicht eindeutig ist.

Weitere Informationen zum Package `wikipedia` findet man auf [PyPi.org](https://pypi.org/project/wikipedia/).

## Weitere APIs mit requests
Eine REST API ist also kurz gesagt eine Webadresse (Endpoint), über die man standardisiert Daten beziehen (oder anbieten) kann. Für die Kommunikation werden dabei sogenannte **HTTTP requests** benutzt. Sie können folgende Aktionen enthalten:
* **GET:** Daten beziehen von einer API
* **POST:** Neue Daten an eine API schicken
* **PUT:** existierende Daten ändern
* **DELETE:** existierende Daten löschen

Das Standardpaket, um in Python 3 mit APIs zu arbeiten, ist **requests**. Es wird mit `pip` installiert
```
$ pip install requests
```
und stellt die oben genannten Aktionen (_request_) get, put usw. zur Verfügung. Ein solcher _request_ liefert immer eine Antwort (_response_) zurück, u.a. ob der _request_ erfolgreich war. Beispiel:
```
>>> import requests
>>> response = requests.get('https://www.vfll.de')
>>> print(response)
<Response [200]>
```
Der Rückgabe-Code 200 bedeutet: der _request_ war efolgreich, d.h. die angefragte Webseite existiert.  

### Dino Ipsum API
Eine nützliche Auflistung von APIs stellt die Webseite [RapidAPI](https://rapidapi.com) zur Verfügung, z.B. die **Dino Ipsum API**, die Platzhaltertext liefert. Die zugehörige Dokumentation auf RapidAPI listet die Parameter auf, die zusammen mit dem _request_ übergeben werden müssen, und generiert ein zugehöriges _Code Snippet_, das man direkt im eigenen Programm benutzen kann:
```
# dino_api.py

import requests

url = "https://alexnormand-dino-ipsum.p.rapidapi.com/"

querystring = {"format":"text","words":"30","paragraphs":"1"}

headers = {
    'x-rapidapi-host': "alexnormand-dino-ipsum.p.rapidapi.com",
    'x-rapidapi-key': "c3bd903d62mshe194ab08181a0a9p1b5c2fjsn0168bb4f01ea"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
```
Die Ausführung des Skripts liefert zum Beispiel
```
$ python dino.py
Strenusaurus Strenusaurus Sphenosuchus Wuerhosaurus Deinocheirus Zalmoxes Oviraptor Othnielia Rahonavis Ojoraptorsaurus Coloradia Sphenosaurus Iguanodon Haplocanthosaurus Dynamosaurus Brasileosaurus Blasisaurus Ekrixinatosaurus Muttaburrasaurus Leptoceratops Walgettosuchus Appalachiosaurus Edmontonia Dolichosuchus Gyposaurus Philovenator Sonidosaurus Dilophosaurus Vitakrisaurus Denversaurus.
```
Das Skripts definiert zunächst ein _dictionary_ namens `querystring`, das die Parameter enthält. Das _dictionary_ `headers` enthält die Angaben zum Server (Webadresse), der die API anbietet. Diese Angaben entnimmt man der Dokumentation der API. Schließlich wird per `requests.request` eine Anfrage an die API zusammengestellt, die die Aktion (GET), die API-Adresse (headers) und die Parameter (params) enthält.

`response.text` enthält dann die Antwort der API.

### Openthesaurus
Die Webseite [OpenThesaurus](https://www.openthesaurus.de/about/api) stellt eine Synonym-API zur Verfügung, die XML- oder JSON-Daten zurückgibt. Die API ist auf der Webseite dokumentiert. Das folgende Skript übergibt die Variable `term` als Parameter an den Endpunkt und wählt als Format `application/json`:
```
# synonyme.py

import requests

term = "programmieren"

response = requests.get("http://www.openthesaurus.de/synonyme/search",
                                params={"q": term, "format": "application/json"})

print(response.text)
```
`response.text` ist hier also ein JSON-Objekt
```
{"metaData":{"apiVersion":"0.2","warning":"ACHTUNG: Bitte vor ernsthafter Nutzung feedback@openthesaurus.de kontaktieren, um bei API-\u00c4nderungen informiert zu werden","copyright":"Copyright (C) 2019 Daniel Naber (www.danielnaber.de)","license":"Creative Commons Attribution-ShareAlike 4.0 or GNU LESSER GENERAL PUBLIC LICENSE Version 2.1","source":"https://www.openthesaurus.de","date":"Tue Jan 14 09:05:53 CET 2020"},"synsets":[{"id":888,"categories":["Computer"],"terms":[{"term":"coden"},{"term":"entwickeln"},{"term":"implementieren"},{"term":"programmieren"},{"term":"hacken","level":"umgangssprachlich"},{"term":"proggen","level":"umgangssprachlich"}]}]}
```
Das müssen wir noch etwas aufbereiten, und zwar mithilfe des Python-Pakets **json**, das zur Standardbibliothek von Python gehört und deshalb nicht extra installiert werden muss. Aber immer daran denken: Es muss zu Beginn eines Skripts importiert werden: `import json`. Dieses Paket stellt u.a. die Methode `loads()` zur Verfügung, mit der man einen String im JSON-Format in Python-Elemente umwandelt, in diesem Fall in eine Liste, die Dictionarys enthält. Schreibt man in der letzten Zeile des Skripts also
```
print(json.loads(response.text))
```
sieht die Anwort ähnlich aus, enthält aber nur noch Python-Elemente:
```
{'metaData': {'apiVersion': '0.2', 'warning': 'ACHTUNG: Bitte vor ernsthafter Nutzung feedback@openthesaurus.de kontaktieren, um bei API-Änderungen informiert zu werden', 'copyright': 'Copyright (C) 2019 Daniel Naber (www.danielnaber.de)', 'license': 'Creative Commons Attribution-ShareAlike 4.0 or GNU LESSER GENERAL PUBLIC LICENSE Version 2.1', 'source': 'https://www.openthesaurus.de', 'date': 'Tue Jan 14 09:07:58 CET 2020'}, 'synsets': [{'id': 888, 'categories': ['Computer'], 'terms': [{'term': 'coden'}, {'term': 'entwickeln'}, {'term': 'implementieren'}, {'term': 'programmieren'}, {'term': 'hacken', 'level': 'umgangssprachlich'}, {'term': 'proggen', 'level': 'umgangssprachlich'}]}]}
```
Dieses Dictionary enthält zum Key _synsets_ eine Liste [...], in der an erster Stelle (also Index 0) ein Dictionary steht, das zum Key _terms_ eine Liste von Dictionarys mit Synonymen anbietet. Der folgende Code liefert diese Liste:
```
response_dict = json.loads(response.text)

synonym_dict_liste = response_dict["synsets"][0]["terms"]

print(synonym_dict_liste)
```
Ergebnis:
```
[{'term': 'coden'}, {'term': 'entwickeln'}, {'term': 'implementieren'}, {'term': 'programmieren'}, {'term': 'hacken', 'level': 'umgangssprachlich'}, {'term': 'proggen', 'level': 'umgangssprachlich'}]
```
Der folgende Code iteriert über diese Liste und gibt für jeden Listeneintrag (also jedes Synonym-Dictionary) den Wert zum Key `'term'` aus:
```
for syn_dict in synonym_dict_liste:
    print(syn_dict["term"])
```
Hier noch mal das ganze Skript:
```
# synonyme.py

import requests, json

term = "programmieren"

response = requests.get("http://www.openthesaurus.de/synonyme/search",
                                params={"q": term, "format": "application/json"})

response_dict = json.loads(response.text)

synonym_dict_liste = response_dict["synsets"][0]["terms"]

print(f"Synonyme von Openthesaurus zu {term}:")

for syn_dict in synonym_dict_liste:
    print(syn_dict["term"])
```
mit der Ausgabe
```
Synonyme von Openthesaurus zu programmieren:
coden
entwickeln
implementieren
programmieren
hacken
proggen
```

