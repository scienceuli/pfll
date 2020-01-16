# seitenzahlen.py

from docx import Document
from lxml import etree
import re

doc = Document('Typische_Anwendungen_seitenumbruch-codes.docx')

# setze die Seitenzahl auf 1
seitenzahl = 1    

indexeintraege_liste = []
indexeintrag = ""
index_flag = 0

register = open("register.txt", "w")
for p in doc.paragraphs:
    absatz_stil = p.style.name
    for run in p.runs:
        # print(run._element.xml)
        if '<END>' in run.text:
            seitenzahl += 1

        # print(run._element.xml)

        indexeintrag = re.search('(XE ")(.*)(")', run._element.xml)
        if indexeintrag:
            print("Indexeintrag gefunden", indexeintrag.group(2))
            register.write(indexeintrag.group(2))
            register.write("\t")
            register.write(str(seitenzahl))
            register.write(f" (({absatz_stil}))")
            register.write("\n")
            

register.close()
        

            

            