import requests
from pprint import pprint

url = "http://localhost:8000/api/entries"
param = {"author": 2}
res = requests.get(url, params=param)
pprint(res.text)
