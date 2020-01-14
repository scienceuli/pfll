# wetter.py

import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"callback":"test","id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q":"Stuttgart"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "c3bd903d62mshe194ab08181a0a9p1b5c2fjsn0168bb4f01ea"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)