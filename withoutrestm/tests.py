import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
n = input('Enter required id:')
r = requests.get(BASE_URL + ENDPOINT + n + '/')
data = r.json()
print(data)
