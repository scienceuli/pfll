# Arbeiten mit Pdfs 

Pdfs sind keine einfachen Textdateien, sondern komplizierte Container aus Text, Bildern, Formulaten, Buttons usw. Man sagt: Pdfs-Dateien sind _Binarys_. Wir können sie deshalb nicht einfach mit 
```
pdfdatei = open("datei.pdf", "r")
```
öffnen und sofort bearbeiten. Es gibt aber mehrere Python-Module, mit denen man z.B. Text aus Pdfs extrahieren, Pdfs beschneiden, Pdfs zusammenfügen usw. kann. 

## Text extrahieren
Im Folgenden wird kurz skizziert, wie man Text aus Pdfs mit den Modulen **PyPDF2** und **PyMuPDD** extrahiert
### PyPDF2
Zu den Pdf-Bibliotheken für Python  zählt u.a. das Modul **PyPDF2**, das zunächst installiert werden muss:
```
$ pip install PyPDF2
```
Anschließend öffnet man die Pdf-Datei mit der `open()`-Methode, muss aber neben _r_ für _read_ noch ein _b_ für _binary_ angeben:
```
>>> import PyPDF2
>>> pdfdatei = open('vfll_broschuere_2018_web.pdf', 'rb')
```  
Mit diesen Daten kann **PyPDF2** noch nicht viel anfangen, es muss zunächst mit der Funktion `PdfFileReader()` ein Pdf-Ojekt erzeugen:
```
pdf = PyPDF2.PdfFileReader(pdfdatei)
```
Das hätte auch in einem Schritt erfolgen können:
```
>>> pdf = PyPDF2.PdfFileReader('vfll_broschuere_2018_web.pdf')
```
Dieses Objekt `pdf` enthält jetzt den Inhalt meines Pdf-Files. Die weiteren Funktionen und Methoden werden ab jetzt darauf angewendet, z.B.

* `numPages` gibt die Anzahl der Seiten aus:
  ```
  >>> pdf.numPages
  77
  ```
* Mit `getPage(n)` hole ich mir die n-te Seite (Zählung beginnt bei 0), z.B.
  ```
  seite = pdf.getPage(0)
  ```
* mit `extractText()` lese ich den Textinhalt einer Seite:
  ```
  >>> print(seite.extractText())
  Gemeinsam für 
  Textqualität
  VFLL e. V. Š der Lektorenverband 
  stellt sich vor
  Verband der
  Freien Lektorinnen
  und Lektoren e. V.
  www.vfll.de 
  ```
  **PyPDF2** kann Text nur seitenweise extrahieren. Möchte man den Text des gesamten Dokuments, muss man einen Loop über alle Seiten ausführen:
  ```
  >>> for seitennummer in range(pdf.numPages):
  ...   print(pdf.getPage(seitennummer).extractText())
  ```


### PyMuPDF
Auch das Modul **PyMuPDF** wird mit `pip` installiert:
```
$ pip install PyMuPDF
```
Es muss aber als `fitz` (dem alten Namen des Moduls) importiert werden:
```
>>> import fitz
```
Das Extrahieren von Text ist ähnlich zur Vorgehensweise unter PyPDF2: Pdf-Datei öffnen, Pdf-Objekt erzeugen, Seite abrufen, Text extrahieren:
```
>>> import fitz
>>> pdf_dokument = "vfll_broschuere_2018_web.pdf"
>>> pdf = fitz.open(pdf_dokument)
>>> print(pdf.pageCount)
77
>>> print(pdf.loadPage(0).getText("text"))
Gemeinsam für 
Textqualität
VFLL e. V. — der Lektorenverband 
stellt sich vor
Verband der
Freien Lektorinnen
und Lektoren e. V.
www.vfll.de
```
Das Ergebnis unterscheidet sich auf den ersten Blick nicht von PyPDF2. Allerdings ist PyMuPDF besser in der Lage, die Seitenstruktur beizubehalten (an eigenen Beispielen ausprobieren).

## Bilder extrahieren
Verschiedene Möglichkeiten, folgt.

## Metadaten auslesen
Mit PyPDF2 lassen sich neben der Seitenzahl noch weitere Metadaten aus einem Pdf auslesen.
```
>>> pdfdatei = open('vfll_broschuere_2018_web.pdf', 'rb')
>>> pdf = PyPDF2.PdfFileReader(pdfdatei)
>>> info = pdf.getDocumentInfo()
>>> print(info)
{'/CreationDate': "D:20180403093455+02'00'", '/Creator': 'Adobe InDesign CC 13.0 (Macintosh)', '/ModDate': "D:20180403093751+02'00'", '/Producer': 'Adobe PDF Library 15.0', '/Trapped': '/False'}
```

## Pdfs bearbeiten und modifizieren
Man kann nicht so einfach Text in eine Pdf-Datei schreiben wie sonst in Python mit der Funktion `write()`. **PyPDF2** arbeitet vor allem mit Seiten:  Seiten entfernen, anders anordnen, hinzugügen usw. Um Pdfs zu erzeugen, stellt PyPDF2 die Klasse `PdfFileWriter()` zur Verfügung, das Gegenstück zu `PdfFileReader()`. 
### Pdfs kombinieren
Um zwei Pdfs aneinander zu hängen, wird jedes Pdf seitenweise in ein `PdfFileWriter()`-Objekt geschrieben, welches am Schluss abgespeichert wird. Der Einfachheit halber nehmen wir im folgenden Beispiel zweimal dieselbe Pdf-Datei.
```
>>> import PyPDF2
>>> pdfdatei1 = open('vfll_broschuere_2018_web.pdf', 'rb')
>>> pdfdatei2 = open('vfll_broschuere_2018_web.pdf', 'rb')
>>> pdf1 = PyPDF2.PdfFileReader(pdfdatei1)
>>> pdf2 = PyPDF2.PdfFileReader(pdfdatei2)
>>> out = PyPDF2.PdfFileWriter()
>>> for seitenzahl in range(pdf1.numPages):
...     seite = pdf1.getPage(seitenzahl)
...     out.addPage(seite)
... 
>>> for seitenzahl in range(pdf2.numPages):
...     seite = pdf2.getPage(seitenzahl)
...     out.addPage(seite)
... 
>>> outdatei = open('vfll_gesamt.pdf','wb')
>>> out.write(outdatei)
>>> outdatei.close()
```
Natürlich hätte man das auch mit Acrobat oder einem anderen Pdf-Programm machen können, aber es geht ja um eine Funktion, die man evtl. in einen Workflow einbetten will, in dem einzelne Pdfs auf ganz verschiedene Weise erzeugt und am Ende zusammengefügt werden.

Für das einfache _Mergen_ hat PyPDF2 sogar eine eigene Klasse `PdfFileMerger()`. Damit lässt sich z.B. ein kleines Script schreiben, das alle Pdf-Dateien mithilfe des Moduls `glob` einsammelt und zusammenfügt:
```
# pdf_merger.py
import glob
from PyPDF2 import PdfFileMerger
def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    file_handles = []
    
    for path in input_paths:
        pdf_merger.append(path)
        
    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)
        
if __name__ == '__main__':
    paths = glob.glob('*.pdf')
    paths.sort()
    merger('pdf_merger.pdf', paths)
```




    


