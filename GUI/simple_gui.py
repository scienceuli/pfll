import PySimpleGUI as sg

sg.theme('DarkAmber')   # farbige Gestaltung
# Gestaltung des Fensters
layout = [[sg.Text('Text in Zeile 1')],
          [sg.Text('Eingabe in Zeile 2'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Abbrechen')]]

# Erzeugung des Fensters
window = sg.Window('Fenstertitel', layout)

# Event-Schleife um "events" zu verarbeiten und die "values" der Eingabe weiterzuleiten
while True:
    event, values = window.read()
    if event in (None, 'Abbrechen'):   # wenn der User das Fenster schließt oder Abbrechen anklickt
        break
    print('Deine Eingabe: ', values[0])

window.close()
