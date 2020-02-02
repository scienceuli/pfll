# vfll_scrape_simple.py

'''
analysiert die Webseite www.lektoren.de = Lektorenverzeichnis
es wird nur die erste Seite des Suchergebnisses analysiert
'''

import requests, os, bs4


BASE_URL = 'https://www.lektoren.de'

def get_page(url):
	# url abrufen
	res = requests.get(url)

	# den Text von res an BS4 uebergeben
	soup = bs4.BeautifulSoup(res.text)

	# alle Links auf der Mutterseite
	page_links = soup.select('a')
	return page_links


def get_mitglied_links(page_links):
	# Schleife ueber alle links
	mitglied_url_liste = []
	for link in page_links:
		# falls href exisitiert und '/profil/' enthaelt
		SCHEMES = ('/profil/', '/user/')
		if (link.get('href') != None) and (link.get('href').startswith(SCHEMES)) and ('register' not in link.get('href')):
			# links zu Mitgliederseite
			mitglied_url = BASE_URL + link.get('href')
			# print(mitglied_url)
			mitglied_url_liste.append(mitglied_url)
		
	return mitglied_url_liste

#
# ---- Main Program ----
#  
if __name__ == "__main__":
	search_url = 'https://www.lektoren.de'
	page_links = get_page(search_url)
	links_liste = get_mitglied_links(page_links)

	for link in links_liste:
		print(link)



		