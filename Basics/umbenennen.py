# umbenennen.py

'''
liest Dateien aus einem Verzeichnis ein und führt 
eine Umbennung mit replace() durch
'''

import os

pfad = 'Dateien_zum_umbenennen'

datei_liste = os.listdir(pfad)

print('Dateien zum umbenennen:')
print(datei_liste)

for datei in datei_liste:
    os.rename(os.path.join(pfad, datei), os.path.join(pfad, datei.replace('-', '_')))

umbenannt_liste = os.listdir(pfad)
print('Umbenannte Dateien:')
print(umbenannt_liste)