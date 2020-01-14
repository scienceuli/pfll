# dino_api.py

import requests

url = "https://alexnormand-dino-ipsum.p.rapidapi.com/"

querystring = {"format":"text","words":"30","paragraphs":"1"}

headers = {
    'x-rapidapi-host': "alexnormand-dino-ipsum.p.rapidapi.com",
    'x-rapidapi-key': "c3bd903d62mshe194ab08181a0a9p1b5c2fjsn0168bb4f01ea"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


