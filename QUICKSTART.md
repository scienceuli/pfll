# Quickstart: Programmieren mit Python

## Wo ist das Terminal?
Um zu programmieren, braucht man fast immer das _Command-Line Interface_ (CLI), auch _Command-Line_, _Terminal_, _Eingabeaufforderung_ etc. genannt, je nach Betriebssystem.

* **Mac OS:** Programm _Terminal_, im Finder unter _Programme > Dienstprogramme_.
* **Linux:** _Terminal_, nicht zu übersehen ...
* **Windows 10:** _Start_ anklicken und "PowerShell" eingeben. Der _Command Prompt_ (die _Eingabeaufforderung_) ginge auch, aber _PowerShell_ ist mehr Linux-like. Ist die _PowerShell_ gestartet, blinkt der Cursor am Ende der Zeile
  ```
  PS C:\WINDOWS\system32> 
  ```


In Tutorials, Computerbüchern etc. wird das _Prompt_  des CLI in der Regel mit einem Dollar-Zeichen $ symbolisiert, unabhängig davon, mit welchem Betriebssystem man arbeitet und wie das CLI konfiguruert ist. Arbeitet man mit der _PowerShell_ unter Windows 10, dann steht `$` für die o.g. Zeile.

Hat man noch nie das CLI benutzt, lohnt es sich, zu Beginn `help` zu starten:
```
$ help
```
Das $ steht, wie gesagt, für den Prompt der Eingabeaufforderung. Es wird nicht mit eingegeben, sondern nur "help" und Enter-Taste (Return-Taste). 

## Python installieren

* **Mac OS:** Python 2 ist vorhanden, Python 3 nicht. Erst _HomeBrew_ installieren:
  ```
  $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
  ```
  Dann Python 3:
  ```
  $ brew install python3
  ```

* **Linux:** Python 2 ist in der Regel vorhanden, Python 3 nicht. Installation:
  ```
  $ sudo apt install python3
  ```
* **Windows 10:** Von [python.org](https://www.python.org/downloads/) herunterladen und per Doppelklick auf die Datei die Installation beginnen. Im aufgehenden Fenster einfach "Install now" wählen (nicht "Customize installation"). **Wichtig:** Zwei Check-Boxes:  1. "Für alle Nutzer" (o.ä.) **nicht auswählen**, 2. "dem Pfad hinzufügen" (o.ä.) **auswählen**, das erleichtert später den Aufruf der einzelnen Python-Tools.

## Installation testen
Im CLI `python3`(Linux, Mac OS) bzw. `python` (Windows 10) ausführen. Es sollte die _Python Shell_ gestartet werden:
```
$ python
...
>>>
```
Kennzeichen der _Python Shell_ ist das dreifache Größer-als-Zeichen >>>.

Verlassen kann man die _Python Shell_ durch Eingabe des Befehls `quit()`:
```
>>> quit()
```
Die beiden runden Klammern sind wichtig.





