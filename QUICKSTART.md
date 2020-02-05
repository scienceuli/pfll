# Quickstart: Programmieren mit Python

## Wo ist das Terminal?
Um zu programmieren, braucht man zwingend das _Command-Line Interface_ (CLI), auch _Command-Line_, _Terminal_, _Eingabeaufforderung_ etc. genannt, je nach Betriebssystem.

* **Mac OS:** Programm _Terminal_, im Finder unter _Programme > Dienstprogramme_.
* **Linux:** _Terminal_, nicht zu übersehen ...
* **Windows 10:** _Start_ anklicken und "PowerShell" eingeben. Der _Command Prompt_ geht auch, aber _PowerShell_ ist mehr Linux-like.

Hat man noch nie das CLI benutzt, lohnt es sich, zu Beginn `help` zu starten:
```
$ help
```
Das $ steht für den Prompt der Eingabeaufforderung, es wird nicht mit eingegeben, sondern nur "help" und Enter-Taste (Return-Taste). 

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
  sudo apt install python3
  ```
* **Windows 10:** Von [python.org](https://www.python.org/downloads/) herunterladen und Installer ausführen. **Wichtig:** Zwei Check-Boxes:  1. "Für alle Nutzer" (o.ä.) **nicht auswählen**, 2. "dem Pfad hinzufügen" (o.ä.) **auswählen**.

## Installation testen
Im CLI `python3`(Linux, Mac OS) bzw. `python` (Windows 10) ausführen. Es sollte die _Python Shell_ gestartet werden:
```
$ python
...
>>>
```




