import os

html_string = ''

for datei in os.listdir('./images'):
    html_string = html_string + f"<p><img src='./images/{datei}'></p>"

with open("index.html", "w") as html_datei:
    html_datei.write(html_string)
