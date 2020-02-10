# daten_verarbeiten.py

import pandas as pd
import openpyxl

# Einlesen der Exceldatei

termine_namen = pd.read_excel("termine_und_namen.xlsx")

termine_namen["Datum"] = pd.to_datetime(termine_namen["Datum"]).dt.strftime("%d.%m.%Y")

termine_namen.to_excel("termine_und_namen_ddmmYYYY.xlsx")

