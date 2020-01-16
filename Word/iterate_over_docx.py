# iterate_over_docx.py

from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table, _Row
from docx.text.paragraph import Paragraph
import docx, re
from lxml import etree

path = 'Typische_Anwendungen_seitenumbruch-codes.docx'
doc = docx.Document(path)

def iter_block_items(parent):
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    elif isinstance(parent, _Row):
        parent_elm = parent._tr
    else:
        raise ValueError("something's not right")
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

register_liste = []
seitenzahl = 1

def checkIndex(xml, seite, stil):
    '''
    prüft, ob der XML-String eines Runs einen XE-Eintrag enthält
    falls ja: in register_liste eintragen
    '''
    indexeintrag = re.search('(XE ")(.*)(")', xml)
    if indexeintrag:
        register_liste.append(indexeintrag.group(2) + "\t" + str(seite) + "((" + stil + "))")

def checkPage(string, seitenzahl):
    '''
    prüft ob der run.text-String <END> enthält
    falls ja: seitenzahl um 1 erhöhen
    neue Seitenzahl zurückgeben
    ''' 
    if '<END>' in string:
        seitenzahl += 1
    return seitenzahl



for block in iter_block_items(doc):
    # read Paragraph
    if isinstance(block, Paragraph):
        print(block.text)
        absatz_stil = block.style.name
        for run in block.runs:
            seitenzahl = checkPage(run.text, seitenzahl)
            checkIndex(run._element.xml, seitenzahl, absatz_stil)
        
    # read table
    elif isinstance(block, Table):
        for row in block.rows:
            row_data = []
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    absatz_stil = paragraph.style.name
                    row_data.append(paragraph.text)
                    for run in paragraph.runs:
                        seitenzahl = checkPage(run.text, seitenzahl)
                        checkIndex(run._element.xml, seitenzahl, absatz_stil)
            print('\t'.join(row_data))
            #if '<END>' in '\t'.join(row_data):
            #    seitenzahl += 1

print(f"Seitenzahl: {seitenzahl}")
with open("register.txt", "w") as file:
    for listitem in register_liste:
        file.write('%s\n' % listitem)
