import requests
import json

URL = "http://maps.googleapis.com/maps/api/geocode/json"
location = "delhi technological university"

PARAMS = {'address':location}

r = requests.get(url=URL, params = PARAMS)

data = json.loads(r.text)

print(data)


