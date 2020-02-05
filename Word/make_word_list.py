# make_word_list.py

import docx
import re

path = 'Typische_Anwendungen.docx'
doc = docx.Document(path)

# Zeichen, die später gelöscht werden
# bad_chars = ['[', ']','(', ')', '{', '}', '<', '>', ',', ';', '.', ':', '„', '“']
bad_chars = "[]()\{\},;:.„“"

word_list_raw = []
word_list = []

for para in doc.paragraphs:
    # die Wortliste wird mit den Wörtern des aktuellen Absatzes erweitert und gleichzeitig gestripped; Trick: list comprehension
    # außerdem werden bad chars gelöscht
    word_list_raw.extend([x.strip().translate({ord(c):'' for c in bad_chars}) for x in para.text.split()])


# print(word_list_raw)

# print(sorted(set(word_list_raw)))

# zeilenweise Ausgabe
with open('word_liste.txt', 'w') as out:
    for word in sorted(set(word_list_raw)):
        # Bereinigen des Wortes: Klammer etc. löschen
        # word = word.translate({ord(c):'' for c in bad_chars})
        print(word)
        out.write(word)
        out.write('\n')
