# vfll_scrape_simple.py

"""
analysiert die Webseite www.lektoren.de = Lektorenverzeichnis
es wird nur die erste Seite des Suchergebnisses analysiert
"""

import requests, os, bs4


BASE_URL = "https://www.lektoren.de"


def get_page(url):
    # url abrufen
    res = requests.get(url)

    # den Text von res an BS4 uebergeben
    soup = bs4.BeautifulSoup(res.text)
    return soup


def get_links(soup):
    # alle Links auf einer Seite = soup
    page_links = soup.select("a")
    return page_links


def collect_in_page(page_content):
    print(page_content)
    # die Rubriken wie Kurzprofil, Referenzen:
    CLASSES = [
        "field-full-name",
        "field-firma",
        "field-group-format-title",
        "field-label",
        "group-adess.field-group.div",
    ]

    page_dict = {}

    section_list = page_content.find_all(class_=CLASSES)
    for s in section_list:
        print(s)

    for section in section_list:
        tag_text_string = ""
        # if isinstance(section, bs4.Tag):
        #    print(
        #        "Abteilung: "
        #        + section.get("class")[0]
        #        + " = "
        #        + section.get_text()
        #        + "\n"
        #    )
        for tag in section.next_siblings:
            if isinstance(tag, bs4.Tag) and tag.get("class")[0] in CLASSES:
                # print("next: " + tag.get("class")[0] + "\n")
                # print(tag_text_string)
                break
            if isinstance(tag, bs4.NavigableString):
                continue
            if isinstance(tag, bs4.Tag) and not tag.get_text().strip().startswith(
                "<!--"
            ):
                # print("Klasse: " + tag.get("class")[0])
                tag_text_string = tag_text_string + tag.get_text().strip()

        # print(tag_text_string)


def get_mitglied_links(page_links):
    # Schleife ueber alle links
    mitglied_url_liste = []
    for link in page_links:
        # falls href exisitiert und '/profil/' enthaelt
        SCHEMES = ("/profil/", "/user/")
        if (
            (link.get("href") != None)
            and (link.get("href").startswith(SCHEMES))
            and ("register" not in link.get("href"))
        ):
            # links zu Mitgliederseite
            mitglied_url = BASE_URL + link.get("href")
            # print(mitglied_url)
            mitglied_url_liste.append(mitglied_url)

    return mitglied_url_liste


#
# ---- Main Program ----
#
if __name__ == "__main__":
    search_url = "https://www.lektoren.de"
    page = get_page(search_url)

    page_links = get_links(page)
    links_liste = get_mitglied_links(page_links)

    # loop über alle mitglieder_links
    for link in links_liste:
        page = get_page(link)
        collect_in_page(page)

    # for link in links_liste:
    #    print(link)

