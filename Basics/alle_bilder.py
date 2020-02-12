# alle_bilder.py

import os
import glob
import fnmatch
import pathlib

path = "/Users/scienceuli/Projekte/DBBay/Bayern8/Verlag_an"

# Variante 1: klassisch
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.eps'):
            print(file)


# Variante 2: fnmatch
for root, dirs, files in os.walk(path):
    for file in fnmatch.filter(files, '*.eps'):
        # print(file)
        pass

# Variante 3: pathlib.Path (ab Python 3.5)
for file in pathlib.Path(path).rglob('*.eps'):
    # print(os.path.basename(file))
    pass
