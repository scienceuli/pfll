# word_to_string.py

import docx

def getText(file):
    d = docx.Document(file) # Lese das Dokument ein
    gesamterText = [] # eine leere Liste, in die absatzweise der Textinhalt eines Dokuments kommt
    for para in d.paragraphs: # iteriere über alle Absätze 
        gesamterText.append(para.text) # erweitere die Liste mit Text des Absatzes

    return '\n'.join(gesamterText) # vereinige alle Elemente der Liste zu einem String mit Returns dazwischen

print(getText('test_01.docx'))
