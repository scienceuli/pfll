# seitenzahlen.py

from docx import Document
from lxml import etree
import re

doc = Document('test_05.docx')

# setze die Seitenzahl auf 1
seitenzahl = 1    

indexeintraege_liste = []
indexeintrag = ""
index_flag = 0
for p in doc.paragraphs:
    absatz_stil = p.style.name 
    for run in p.runs:
        # print(run.style.name)
        if '<w:lastRenderedPageBreak/>' in run._element.xml:
            seitenzahl += 1

        if '<w:instrText xml:space="preserve"> XE "</w:instrText>' in run._element.xml:
            print("Indexeintrag gefunden")
            indexeintrag = ""
            
        if run.style.name == "Indexeintrag":
            index_flag = 1
            # print("run gefunden")
            # print(run._element.xml)
            for tags in etree.fromstring(run._element.xml):
                if 'instrText' in tags.tag:
                    # print('instText gefunden')
                    indexeintrag = indexeintrag + tags.text
        else:
            if index_flag == 1:
                print(indexeintrag, seitenzahl, f"(({absatz_stil}))")
                index_flag = 0
        

            

            