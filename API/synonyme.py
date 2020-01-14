# synonyme.py

import requests, json

term = "programmieren"

response = requests.get("http://www.openthesaurus.de/synonyme/search",
                                params={"q": term, "format": "application/json"})

response_dict = json.loads(response.text)

synonym_dict_liste = response_dict["synsets"][0]["terms"]

print(f"Synonyme von Openthesaurus zu {term}:")

for syn_dict in synonym_dict_liste:
    print(syn_dict["term"])