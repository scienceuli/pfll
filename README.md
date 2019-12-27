# Programmieren für Lektorinnen und Lektoren 

* TOC
{:toc}

## Warum programmieren?

Die Situation gehört vermutlich zum Alltag der meisten Lektorinnen und Lektoren: Gerade hat man wieder Stunden damit verbracht, Dateien zu verwalten, Formate zuzuweisen, Daten zu konvertieren, Ordnung in Excel-Chaos zu bekommen usw. Kurz: monotone und langweilige Routineaufgaben, die viel Zeit kosten und von der eigentlichen Arbeit ablenken.

Dabei gibt es doch gerade für solche Aufgaben den Computer! Mit den richtigen Anweisungen - sprich: dem richtigen Programm – erledigt er in Sekunden, wofür wir Stunden brauchen. Natürlich verwenden wir im Büroalltag mächtige (und oft teure) Softwarewerkzeuge, mit deren Hilfe wir schreiben, zeichnen, designen usw. Aber die "kleinen Helferlein" sind es, die uns bei den einfachen, aber zeitraubenden Aufgaben unterstützen. Um nur einige Beispiele zu nennen:
* Dateien verschieben, kopieren, ordnen
* Excel-Arbeitsblätter erstellen, bearbeiten, formatieren
* Word-Dateien durchsuchen, formatieren, erstellen
* Pdfs erzeugen, umwandeln, bearbeiten
* ...

Oft gibt es dafür keine fertigen Programme, weil diese Aufgaben eng mit unseren Projekten und Workflows verzahnt sind. Mit etwas Programmierkenntnis lassen sie sich aber dem Computer beibringen. Dafür muss man kein _IT-Nerd_ mit jahrelanger Programmiererfahrung sein. Schon einige Grundkenntnisse reichen aus, um kleine aber sinnvolle Programme zu erstellen. Und es macht sogar Spaß!

## Warum Python?

Programmieren heißt im Wesentlichen, eine Folge von Anweisungen zu erstellen, die der Computer abarbeitet. Die Anweisungen werden in einer Programmiersprache erstellt, von denen es zahlreiche gibt. Für unsere Zwecke eignet sich Python hervorragend. Warum?
* Python ist Open Source.
* Python ist relativ einfach zu erlernen, auch ohne Vorkenntnisse.
* Die Syntax ist unkompliziert und lehnt sich an die englische Sprache an. Der Befehl  `print("Hallo")` macht zum Beispiel genau das, was man erwartet.
* Mit relativ wenigen Befehlen und Strukturen lässt sich schon viel programmieren.
* Python verfügt von Haus aus über eine umfangreiche Standard-Library. Daneben existieren zahlreiche weitere Libraries, die dafür sorgen, dass Python aus vielen Anwednungsfelderen nicht mehr wegzudenken ist: Data Science, Statistik, KI, Spieleentwicklung usw. Auch für unseren Lektorenalltag gibt es  ciele nützliche Tools.
* Die Python-Community ist riesig. Man findet im Netz unzählige Tutorials, Tipps, Beispielprogramme usw. Es gibt auch viele gute Bücher zu Python. 

## Python installieren

Python wird üblicherweise als _interpretierte Programmiersprache_ verwendet, d.h. die Anweisungen eines Python-Programms (oft _Skript_ genannt) werden dann abgearbeitet, wenn das Programm aufgerufen wird. Dafür muss ein Python-Interpreter (in der Regel auch nur kurz Python genannt) auf dem Computer installiert sein, auf dem das Programm ausgeführt wird.

Python kann kostenlos für Windows, OS X und Linux heruntergeladen werden. Zur Zeit existieren noch zwei Versionen von Python, Python 2 und Python 3. Viele Programme laufen unter beiden Versionen, aber wer mit dem Programmieren beginnt, sollte Python 3 lernen. Deshalb darauf achten: Python 3 herunterladen und installieren.

### Installation auf einem Windows-Rechner

Auf https://python.org/downloads/ findet man Python für alle Betriebssysteme, sowohl für alte 32-bit- als auch für 64-bit-Rechner (alles, was nach 2007 gekauft wurde, sollte ein 64-bit-Rechner sein). Für Windows also den Python-3-Installer (64-bit) downloaden, ausführen und den Installationsanweisungen folgen. Die Default-Einstellungen können übernommen werden. Man sollte darauf achten, dass die Option _Add Python 3.X to your PATH_ angeklickt ist.

### Installation auf einem Mac

Unter OS X ist Python in der Regel schon installiert. Man kann das herausfinden, indem man ein **Terminal** öffnet und dort den Befehl `python --version` eingibt, gefolgt von der **Enter**-Taste. Dieser Befehl gibt die installierte Python-Version aus: 

```
$ python --version
python 2.7.17
```

Das Dollar-Zeichen (Prompt) markiert die Eingabeaufforderung im **Terminal**. Alles, was _danach_ folgt, wird vom User eingegeben, inklusive des abschließenden **Enter**-Befehls. Das Dollar-Zeichen wird also nicht mit eingegeben. Zeilen _ohne_ Dollar-Zeichen am Anfang gevben das an, was der Rechner im __Terminal__ zurückgibt.

Die auf einem Mac vorinstallierte Python-Version ist also Python 2, wir wollen aber mit Python 3 arbeiten. Python 3 muss also erst noch installiert werden. (Wenn tatsächlich schon Python 3 installiert ist, kann man das Folgende überspringen). Das kann auf mehreren Wegen erfolgen.

#### Installation von der Python-Webseite

Man kann von https://python.org/downloads/ den zur eigenen OSX-Version passenden Python-3-Installer (.dmg) herunterladen und ausführen. Python 3 steht anschließend zur Verfügung und befindet sich im Programm-Verzeichnis. 

#### Installation mit HomeBrew
**Empfehlenswert** ist jedoch die Installation mittels **HomeBrew**, einem weit verbreiteten _Paketmanager_, mit dem man zusätzliche Software installieren kann. Das erfordert ein klein wenig mehr Aufwand, ist aber "sauberer", was Installationspfade, Updates und Uninstalls angeht. Um **HomeBrew** zu installieren, wird wiederum **XCode** benötigt, Apples Entwicklungsumgebung. Die Installation erfordert aber nur eine Zeile im **Terminal**:
```
$ xcode-select --install
```
**XCode** ist ein großes Programm, es kann also einen Moment dauern, bis es heruntergeladen und installiert ist.

Die Befehlszeile, um __HomeBrew__ zu installieren, lautet:
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Einfach ins **Terminal** kopieren und **Enter** eingeben. Ob die Installation geklappt hat, kann man mit folgendem Befehl prüfen:
```
$ brew doctor
Your system ist ready to brew.
```

Abschließend kommt die eigentliche Installation von Python 3. Dazu gibt man folgenden Befehl im **Terminal** ein:
```
$ brew install python3
```
Nach Abschluss der Installation bestätigt folgender Befehl, dass Python 3 nun vorhanden ist:
```
$ python3 --version
Python 3.7.5
```
(oder eine aktuellere Version 3.7.X).

### Installation auf einem Linux-Rechner
Bei den meisten Linux-Distributionen ist Python vorinstalliert. Um die installierte Version zu prüfen, gibt man im **Terminal** `python3 --version` ein:
```
$ python3 --version
Python 3.7.5
```
(oder eine andere Python-3-Version).

Falls mehrere Python-Versionen installiert sind, liefert `apt list --installed | grep python` eine Übersicht.

Die Installation/Aktualisierung von Python 3 mithilfe des Kommandos `apt-get` ist problemlos. Zunächst wird der Index des apt-get-Repositories auf dem eigenen Rechner aktualisiert:
```
$ sudo apt-get update
```
Falls noch keine Python-3-Version installiert ist, wird die neueste Version installiert mit:
```
$ sudo apt-get install python3
```
Falls eine vorhandene Python-3-Version nur aktualisiert werden muss, liefert
```
$ sudo apt-get upgrade python3
```

 




