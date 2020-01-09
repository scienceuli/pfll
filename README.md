# Programmieren für Lektorinnen und Lektoren 

* TOC
{:toc}

## Warum programmieren?

Die Situation gehört vermutlich zum Alltag der meisten Lektorinnen und Lektoren: Gerade hat man wieder Stunden damit verbracht, Dateien zu verwalten, Formate zuzuweisen, Daten zu konvertieren, Ordnung in Excel-Chaos zu bekommen usw. Kurz: monotone und langweilige Routineaufgaben, die viel Zeit kosten und von der eigentlichen Arbeit ablenken.

Dabei gibt es doch gerade für solche Aufgaben den Computer! Mit den richtigen Anweisungen - sprich: dem richtigen Programm – erledigt er in Sekunden, wofür wir Stunden brauchen. Natürlich verwenden wir im Büroalltag mächtige (und oft teure) Softwarewerkzeuge, mit deren Hilfe wir schreiben, zeichnen, designen usw. Aber die "kleinen Helferlein" sind es, die uns bei den einfachen, aber zeitraubenden Aufgaben unterstützen. Um nur einige Beispiele zu nennen:
* Eine große Zahl an Dateien muss nach einer Tabelle (alter/neuer Name) oder einem bestimmten Schema umbenannt werden.
* Suche/Ersetze in mehreren Word-Dokumenten (ggf. mit Mustervergleich), ohne diese zu öffnen
* Zitate und Literaturliste in einem Dokument überprüfen (Nummerierung kontinuierlich und eindeutig? Verzeichnis vollständig?)
* Überschriften-Hierearchie in Word-Dateien prüfen (nach Überschrift 1 darf nur Überschrift 2 folgen usw.), Inhaltsverzeichnis anlegen
* Text aus Pdfs lesen, Pdfs zusammenfügen usw.
* Verlinkung von Tabellen und Abbildungen in Word prüfen (wird jedes Element auch im Text aufgerufen?)
* ...

Oft gibt es dafür keine fertigen Programme, weil diese Aufgaben eng mit unseren Projekten und Workflows verzahnt sind. Oder es gibt kommerzielle Lösungen, die aber kosten. Mit etwas Programmierkenntnis lassen sich jedoch solche Workflows jedoch Computer beibringen. Dafür muss man kein _IT-Nerd_ mit jahrelanger Programmiererfahrung sein. Schon einige Grundkenntnisse reichen aus, um kleine aber sinnvolle Programme zu erstellen. Und es macht sogar Spaß!

Und ist man mal auf den Geschmack gekommen, geht man evtl. auch an größere Aufgaben:
* Inhalte aus Webseiten auslesen (_Web Scraping_)
* Datenbanken nutzen
* kleine Webanwendungen basteln
* Bilder bearbeiten
* ...

Auch das ist kein Hexenwerk!

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

Auf [Python.org](https://python.org/downloads/) findet man Python für alle Betriebssysteme, sowohl für alte 32-bit- als auch für 64-bit-Rechner (alles, was nach 2007 gekauft wurde, sollte ein 64-bit-Rechner sein). Für Windows also den Python-3-Installer (64-bit) downloaden, ausführen und den Installationsanweisungen folgen. Die Default-Einstellungen können übernommen werden. Man sollte darauf achten, dass die Option _Add Python 3.X to your PATH_ angeklickt ist.

### Installation auf einem Mac

Unter OS X ist Python in der Regel schon installiert. Man kann das herausfinden, indem man ein **Terminal** öffnet und dort den Befehl `python --version` eingibt, gefolgt von der **Enter**-Taste. Dieser Befehl gibt die installierte Python-Version aus: 

```
$ python --version
python 2.7.17
```

Das Dollar-Zeichen (Prompt) markiert die Eingabeaufforderung im **Terminal**. Alles, was _danach_ folgt, wird vom User eingegeben, inklusive des abschließenden **Enter**-Befehls. Das Dollar-Zeichen wird also nicht mit eingegeben. Zeilen _ohne_ Dollar-Zeichen am Anfang gevben das an, was der Rechner im __Terminal__ zurückgibt.

Die auf einem Mac vorinstallierte Python-Version ist also Python 2, wir wollen aber mit Python 3 arbeiten. Python 3 muss also erst noch installiert werden. (Wenn tatsächlich schon Python 3 installiert ist, kann man das Folgende überspringen). Das kann auf mehreren Wegen erfolgen.

#### Installation von der Python-Webseite

Man kann von [Python.org](https://python.org/downloads/) den zur eigenen OSX-Version passenden Python-3-Installer (.dmg) herunterladen und ausführen. Python 3 steht anschließend zur Verfügung und befindet sich im Programm-Verzeichnis. 

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
die Aktualisierung.

### Editoren
Python-Programme können in jedem Text-Editor geschieben werden (Achtung: Word etc. sind _keine_ Text-Editoren). Es gibt aber einige Editoren, die besonders für das Programmieren geeignet sind, weil Sie die Programmiererin bei vielen Dingen unterstützen (z.B. Syntax, farbliche Gestaltung, Programme ausführen usw.). Man spricht auch von **Entwicklungsumgebungen**

* [Visual Studio Code](https://code.visualstudio.com) ist ein sehr beliebter und leistungsfähiger Open-Source-Editor, der überwiegend von MS-Mitarbeitern entwickelt wird (aber so gut wie nichts mit dem ähnlick klingenden Produkt "Visual Studio" zu tun hat). Es gibt zahlreiche Erweiterungen, die das Leben erleichern.
* [Sublime Text](https://www.sublimetext.com) bewegt sich auf ähnlichem Niveau. Es ist frei downloadbar, allerdings wird man aufgefordert, eine Lizenz zu erwerben.
* [Thonny](https://bitbucket.org/plas/thonny/downloads/) für Windows, MacOS und Linux ist eine Entwicklungsumgebung, die besonders für Einsteigerinnen geeignet ist. Die Benutzeroberfläche von Thonny ist einfach und übersichtlich gestaltet, quasi selbsterklärend. Für kleine Projekte und zum Lernen bestens geeignet, für große Projekte eher nicht.
* [Mu](https://codewith.mu/en/download) ist ebenfalls für alle Betriebssysteme downloadbar und richtet sich wie Thonny eher an Neulinge.

## Python ausführen
Es gibt mehrere Möglichkeiten, Python-Code auszuführen:
* interaktiv in einer **Python Shell**
* im **Terminal** (MacOS, Linux) bzw. in der **Eingabeaufforderung** (Windows)
* in einer **IDE** (integrated development environment, integrierte Entwicklungsumgebung) oder einem **Editor**
* aus einem **Dateimanager**

### Terminal und Eingabeaufforderung
Die übliche Weise, mit dem Python-Interpreter zu interagieren, passiert in einer **Konsole**, in der man entsprechende Kommandos eingibt.
Das Hauptwerkzeug, mit Python zu arbeiten, ist also nicht die Maus, sondern die Tastatur.

Die Standardkonsole unter **Mac OS** ist das **Terminal**, das man unter den Dienstprogrammen auf dem Mac findet. Es besteht im Wesentlichen aus einem Fenster mit einer Eingabeaufforderung (Prompt). Auch unter **Linux** heißt die Konsole **Terminal**. Der Funktionsumfang der Terminals unter OS X und Linux ist sehr ähnlich.

Die **Windows**-Konsole wird **Eingabeaufforderung** bzw. **cmd** genannt. Sie läasst sich z.B. im Startmenü aufrufen. Die Windows-Konsole ist nicht so mächtig wie die Linux- und OS X-Versionen. Mit Python lässt sich aber trotzdem auch unter Windows arbeiten.  

### Python Shell
Wurde Python 3 erfolgreich installiert, kann im **Terminal** (MacOS, Linux) bzw. der **Eingabeaufforderung** (Windows) eine interaktive **Python Shell** gestartet werden:
```
$ python3
Python 3.6.6 (default, Aug 19 2019, 07:56:19) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.10.44.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
Der Standard-Prompt für den interaktiven Modus ist \>>>. In der **Python Shell** kann nun beliebiger Python-Code eingegeben und sofort ausgeführt werden. Wird die **Python Shell** beendet, ist der eingegebene Code "weg" – er wird nicht gespeichert.
```
>>> print('Hello World!')
Hello World!
>>> 2 + 3
5
```
Um den interaktiven Modus wieder zu verlassen, nutzt man entweder den Befehl `quit()` bzw. `exit()` oder gibt **Ctrl+Z** (Windows) bzw. **Ctrl+D** (MacOS, Linux) ein.

### Python-Skripte
Ein Python-Skript ist eine Text-Datei mit der Endung **.py**, die in einem beliebigen Text-Editor erstellt werden kann (siehe Punkt [Editoren](#editoren)). Sie enthält Python-Code, der dann ausgeführt wird, wenn das Skript aus dem **Terminal** oder der **Eingabeaufforderung** heraus aufgerufen wird. Das Skript **hello.py**, das 'Hello World!' ausgeben soll, enthält beispielsweise folgende Zeilen:
```
#!/usr/bin/env python3
 
print('Hello World!')
```
Die erste Zeile, die mit dem _shebang_ **#!** startet, ist nicht unbedingt notwendig und aus Python-Sicht ein Kommentar. Sie wird dann benötigt, wenn das Skript _direkt_ ausgeführt wird im **Terminal**:
```
$ hello.py
Hello World!
```
Sie wird _nicht_ benötigt, wenn das Skript zusammen mit dem Python-Interpreter ausgeführt wird:
```
$ python3 hello.py
Hello World!
```
Sinn und Zweck der _Shebang_-Zeile ist es, das Skript in verschiedenen Umgebungen (z.B. auf verschiedenen Rechnern) lauffähig zu machen. Sie besagt sinngemäß: "Nimm aus meiner Umgebung (also meinen Pfaden, Installationen etc.) auf meinem Rechner den Python-3-Interpreter, den du dort findest." Man könnte als _Shebang_-Zeile auch den _absoluten Pfad_ zur Python-3-Installation auf dem jeweiligen Rechner angeben.

### Pakete installieren mit pip
**pip** ist der _Package Installer_ für Python. **pip** wird verwendet, um zusätzliche Python-Pakete zu installieren, die in der Standardbibliothek nicht enthalten sind. Das sind in erster Linie Pakete, die im [Python Package Index](https://pypi.org) gelistet sind. **pip** ist bereits auf dem Computer installiert, wenn Python vorhanden ist. Aber **Achtung**: Zumindest unter MacOS/Linux ist **pip** per default der Paketmanager für Python 2 und identisch zu **pip2**. Der entsprechende Paketmanager **pip3** wird installiert, wenn Python 3 installiert wird. Eine Übersicht, was installiert ist, liefern die Versionsabfragen zu **pip** und **pip3**:
```
$ pip --version 
pip 19.0.3 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)

$ pip3 --version
pip 19.1.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```
**pip** gehört also hier zu Python 2, **pip3** zu Python 3.

Ein Upgrade von **pip** mit 
```
$ python3 -m pip install --upgrade pip
Collecting pip
  Using cached https://files.pythonhosted.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl
Installing collected packages: pip
  Found existing installation: pip 19.1.1
    Uninstalling pip-19.1.1:
      Successfully uninstalled pip-19.1.1
Successfully installed pip-19.3.1
```
sorgt dafür, dass nun **pip2** der Paketmanager für Python 2  und **pip** bzw. **pip3** der Paketmanager für Python 3 ist:
```
$ pip2 -V 
pip 19.0.3 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)
$ pip -V
pip 19.3.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
$ pip3 -V
pip 19.3.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```
D.h., egal ob nun **pip** oder **pip3** aufgerufen wird: es handelt sich jeweils um denselben Paketmanager für Python 3.

Um ein  Paket mit **pip** zu installieren, wird im **Terminal** einfach `pip install` zusammen mit dem Paketnamen aufgerufen:
```
pip install IrgendeinPaket
```


### Virtuelle Umgebungen
**Virtuelle Umgebungen** sind ein sehr praktisches Werkzeug, wenn man programmiert. Warum? Manchmal möchte man für ein bestimmtes Projekt eine andere Python-Version benutzen, aber nichts an der Version ändern, die  auf dem Rechner bereits installiert ist. Oder man möchte in einem Projekt bestimmte Python-Module installieren, die man in einem anderen Projekt nicht haben möchte. Mithilfe von virtuellen Projekten ist es möglich, mehrere Python-Versionen *nebeneinander* zu nutzen, ohne dass sie sich gegenseitig beeinflussen. Jedes Projekt hat dann seine eigene virtuelle Umgebung und ist von den anderen Projekten klar isoliert.

Eine virtuelle Umgebung unter Python 3 wird erzeugt, wenn `python3` zusammen mit dem Modul **venv** aufgerufen wird:
```
$python3 -m venv /pfad/zur/neuen/virtuellen/Ummgebung
```

_Beispiel_: Wir legen ein neues Projekt _neues\_Projekt_ an und wechseln in das neue Verzeichnis:
```
$ mkdir neues_projekt
$ cd neues_projekt
```
Innerhalb des neuen Verzeichnisses wird nun eine virtuelle Umgebung _env_ angelegt (Namen frei wählbar):
```
$ python3 -m venv env
```
Dieser Befehl legt ein neues Unterverzeichnis _env_ an, in dem eine ausführbare Python-3-Version liegt und in den auch alle zuätzlichen Intsallationen per **pip** geschrieben werden.

Die neue virtuelle muss nun noch aktiviert werden:
```
$ source env/bin/activate
(env) $
```
Der Prompt im **Terminal** wechsel von $ zu (env) $ und signalisiert damit, dass man sich nun innerhalb der virtuellen Umgebung _env_ befindet.

Die virtuelle Umgebung lässt sich deaktivieren mit:
```
(env) $ deactivate
```

### pip plus virtualenv = pipenv
Inzwischen verwenden viele Programmierer zur Einrichtung virtueller Umgebungen und zur Installationen von Python-Paketen nicht mehr **virtualenv** bzw. **pip**, sondern das Tool **pipenv**. Es kombiniert beide Methoden und hat eine Reihe von Vorteilen gegenüber den "alten" Werkzeugen **virtualenv** und **pip**.

#### Installation
Die Installation von **pipenv** ist einfach:
```
$ pip install pipenv
```
Um eine virtuelle Umgebung einzurichten _und_ ein zusätzliches Python-Paket (z.B. _requests_) zu installieren, reicht nun _ein_ Befehl: Man geht ins Arbeitsverzeichnis eines Projekts (oder erstellt ein neues Projektverzeichnis und wechsel dorthin) und führt dort `pipenv install requests` aus:
```
$ mkdir mein_projekt
$ cd mein_projekt
$ pipenv install requests
Creating a virtualenv for this project…
Pipfile: /Users/scienceuli/Devel/pfll/Pipfile
Using /Users/scienceuli/.pyenv/versions/3.7.4/bin/python3.7 (3.7.4) to create virtualenv…
⠹ Creating virtual environment...
...
✔ Successfully created virtual environment! 
Virtualenv location: /Users/scienceuli/.local/share/virtualenvs/pfll-YbjUxZUl
Creating a Pipfile for this project…
Installing requests…
Adding requests to Pipfile's [packages]…
✔ Installation Succeeded 
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success! 
Updated Pipfile.lock (444a6d)!
Installing dependencies from Pipfile.lock (444a6d)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 5/5 — 00:00:01
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```
Mit diesem Befehl wird also 
1. eine virtuelle Umgebung mit Python 3.7.4 erzeugt,
2. ein sogenanntes _Pipfile_ angelegt, das die virtuelle Umgebung beschreibt (wo gespeichert, was installiert, welche Versionen, ...),
3. das Paket _requests_ installiert,
4. ein _Pipfile.lock_ angelegt, das  automatisch erzeugt wird und detaillierte Informationen zu installierten Paketen (_packages_) und Abhänggigkeiten (_dependencies_) enthält. Mithilfe des _Pipfile.lock_ lässt sich die virtuelle Umgebung an einem anderen Ort _exakt_ reproduzieren.

#### Aktivierung und Deaktivierung
Die mit `pipenv install` erzeugte virtuelle Umgebung wird mit 
```
$ pipenv shell
```
aktiviert. Der Prompt ändert sich daraufhin und zeigt die virtuelle Umgebung (sie hat defaultmäßig den gleichen Namen wie das Projektverzeichnis) an:
```
(mein_projekt) $
```
Ruft man in der virtuellen Umgebung `which python` auf, sieht man, dass jetzt die Python-Installation der virtuellen Umgebung benutzt wird:
```
(mein_projekt) $ which python
/Users/scienceuli/.local/share/virtualenvs/mein_projekt-YbjUxZUl/bin/python
```
Mit
```
$ exit
exit
```
verlässt man die virtuelle Umgebung wieder.

Mithilfe des Befehls `pipenv run python` kann man Python aus der virtuellen Umgebung starten (oder ein Skript), _ohne_ sie vorher durch `pipenv shell` aktiviert zu haben:
```
$ pipenv run python
```
bzw.
```
$ pipenv run python skript.py
```
Voraussetzung: Man ist im Projekt-Verzeichnis, in dem sich das _Pipfile_ befindet.

#### Wichtige pipenv-Kommandos

```
$ pipenv install package --dev
```
_package_ wird nur in der Entwicklungsumgebung installiert

```
$ pipenv uninstall package
```
deinstalliert das Paket _package_

```
$ pipenv --python 3.6
```
reinstalliert die virtuelle Umgebung mit einer anderen Python-Version (hier: 3.6 statt 3.7). **Achtung:** Auch _Pipfile_ muss geändert werden

```
$ pipenv --rm
```
virtuelle Umgebung wird entfernt 

```
$ pipenv --venv
```
Pfad zur virtuellen Umgebung

```
$ pipenv check
```
prüft die installiert Pakete und Abhängigkeiten

```
$ pipenv graph
```
zeigt eine Grafik der Abhängigkeiten

```
.env
```
In dieser Datei werden Umgebungsvariablen wie z.B. _SECRET\_KEY_ abgelegt, die beim Starten von Python in der virtuellen Umgebung geladen werden.
```
$ pipenv run python
Loading .env environment variables...
...
```




## Workflows automatisieren mit Python
* Basics ((folgt))
* Arbeiten mit Dateien und Verzeichnissen ((folgt))
* [Arbeiten mit Word-Dateien](Word/README.md)
* Arbeiten mit Pdfs ((folgt))
* Arbeiten mit Excel ((folgt))
* [GUI](GUI/SimpleGUI.md)
* Arbeiten mit Schnittstellen ((folgt))
* Mit wenigen Klicks zum eigenen Blog ((folgt))
* Web-Anwendungen ((folgt))
* ...


