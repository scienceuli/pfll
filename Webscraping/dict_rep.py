# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 00:57:10 2018

@author: Maame Yaa Osei and Ariel Arman Woode
"""

import re
from specialTree import *

# Opening .txt file to read from
# file = input("Paste directory of markdown file here: ")
file = "./md_files/md_file000.md"
readFile = open(file)

# Initialising variables
myDict = {}
rawLine_str = ""
rawLine_list = []
cleanLine = []
tree = Tree()


replace_list = [
    "{.field-group-format-toggler}",
    "::: {.term-tree-list}\n",
    "::: {.term}\n",
    "::: {.info .description}",
    "{.term-name}",
    "[ ]{.label .fa .fa-phone .fa-fw} [ ",
    r"[Impressum/Datenschutz](/impressum) \|",
    "[VFLL-Website](http://www.vfll.de)",
    "{arbeitsbereiche .field-label}",
    "{dienstleistungen .field-label}",
    '{.postal-code autocomplete="postal-code"',
    'x-autocompletetype="postal-code"}',
    "{.locality",
    'autocomplete="locality" x-autocompletetype="locality"}',
    '{.country autocomplete="country"',
    'x-autocompletetype="country"}',
    "{.field-telefon",
    "{.field-mobil",
    ".inline}",
    " {.label .fa .fa-mobile .fa-fw}",
    "{.label .fa .fa-envelope .fa-fw}",
    "[",
    "]",
]

# Reading data from input file
for line in readFile:
    if not line.strip().startswith(":::"):
        rawLine_str += line.replace("\t", "")
        for r in replace_list:
            rawLine_str = rawLine_str.replace(r, "")
        rawLine_list = rawLine_str.split("\n")


cleanLine = [i for i in rawLine_list if i is not ""]


# Making headings unique to use as keys in feeder dictionary `myDict`
currKey = None
count = 0
for line in cleanLine:
    if re.match("#+.+", line):
        currKey = line + "_" + str(count)
        myDict[currKey] = []
        count += 1
    else:
        myDict[currKey].append(line)


# Inserting key, value pairs of headings and lines into parser-tree.
for k, v in myDict.items():
    tree.insert((k, v))
tree.clean()
print(tree)
print("Kindly check directory and open the file 'myjson.json' for output")
