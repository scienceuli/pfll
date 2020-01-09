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


