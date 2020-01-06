---
title: SimpleGUI
permalink: /GUI/simplegui/
---

# Python und Graphical User Interface (GUI)
Python-Skripte werden im Terminal gestartet und bekommen ggf. nötigen Imput auch über das Terminal. Mit Python lassen sich aber auch **grafische Benutzeroberflächen** gestalten (**GUI**) gestalten. Verschiedene Module stehen dabei zur Verfügung, um GUIs zu konstruieren. Ein besonders einfach zu handhabendes Werkzeug ist **PySimpleGUI**. Es erlaubt, ohne großen Aufwand einer Anwendung eine grafische Oberfläche hinzuzufügen.

## Installation
**PySimpleGUI** wird mithilfe des Paketmanagers **pip** bzw. **pip3** installiert:
```
$ pip install pysimplegui
```
oder
```
pip3 install pysimplegui
```

## Einfaches Beispiel
Das folgende einfache Skript *simple_gui.py* zeigt die grundätzliche Nutzung von **PySimpleGUI**:
```
import PySimpleGUI as sg

sg.theme('DarkAmber')   # farbige Gestaltung
# Gestaltung des Fensters
layout = [  [sg.Text('Text in Zeile 1')],
            [sg.Text('Eingabe in Zeile 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Abbrechen')] ]

# Erzeugung des Fensters
window = sg.Window('Fenstertitel', layout)

# Event-Schleife um "events" zu verarbeiten und die "values" der Eingabe weiterzuleiten
while True:
    event, values = window.read()
    if event in (None, 'Abbrechen'):   # wenn der User das Fenster schließt oder Abbrechen anklickt
        break
    print('Deine Eingabe: ', values[0])

window.close()
```
Der Aufruft dieses Skripts
```
$ python3 simple_gui.py
```
erzeugt dieses Fenster:
![Einfaches PySimpleGUI-Fenster mit Eingabemöglichkeit](GUI/simple_window.png "Einfaches GUI")



