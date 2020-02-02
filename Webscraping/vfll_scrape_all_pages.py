# vfll_scrape_all_pages.py
'''
analysiert die Webseite www.lektoren.de = Lektorenverzeichnis
Die Seite zeigt das Ergebnis der Suchanfrage https://www.lektoren.de/search-results?find=*
aufgeteilt auf mehrere Seiten
Aufgabe: iteriere über n für https://www.lektoren.de/search-results?find=*&page=n
'''

import requests, os, bs4


# base url der Mutterseite
base_url = 'https://www.lektoren.de'

def get_page(pagenum):
    '''
    Funktion gibt alle links auf Seite n des Search Results zurück
    '''
    search_url = f'https://www.lektoren.de/search-results?find=*&page={pagenum}'
    # url abrufen
    res = requests.get(search_url)

    # den Text von res an BS4 uebergeben
    soup = bs4.BeautifulSoup(res.text)

    # alle Links auf der Mutterseite
    page_links = soup.select('a')
    return page_links


def get_mitglied_links(page_links):
    '''
    Funktion filtert aus allen Links einer Seite die 
    relevanten Links auf VfLL-Mitglieder heraus.
    Falls keine Links mehr gefunden werden, wird page_exists auf False gesetzt
    Zurückgeben wird die Liste der Mitlieder-Links auf einer Seite 
    und der Boolean page_exists
    '''
    page_exists = True
    # Schleife ueber alle links
    mitglied_url_liste = []
    for link in page_links:
        # falls href exisitiert und '/profil/' enthaelt
        SCHEMES = ('/profil/', '/user/')
        if (link.get('href') != None) and (link.get('href').startswith(SCHEMES)) and ('register' not in link.get('href')):
            # links zu Mitgliederseite
            mitglied_url = base_url + link.get('href')
            # print(mitglied_url)
            mitglied_url_liste.append(mitglied_url)
    if not mitglied_url_liste:
        page_exists = False
        
    return mitglied_url_liste, page_exists


if __name__ == "__main__":
    '''
    solage page_exists == True, wird aufsteigend über die Seiten iteriert
    und die Liste aller Mitglieder-Links um die Link-Liste der aktuellen
    Seite erweitert
    '''
    all_links_liste = []
    page = 0
    while True:
        page_links = get_page(page)
        link_liste, page_exists = get_mitglied_links(page_links)
        if page_exists == False:
            break
        else:
            all_links_liste.extend(link_liste)
            page += 1

    out = open("vfll_links.txt", "w") 
    for link in all_links_liste:
        out.write(link)
        out.write("\n")

    out.close()


        