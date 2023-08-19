import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def get_resources(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    resp = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

def create_resource():
    new_emp = {
        'eno': 9999,
        'ename': 'shivansu',
        'eaddr': 'Indore',
        'esal': 35000,
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
    print(r.status_code)
    print(r.json())

def update_resource(id):
    new_data = {
        'id': id,
        'eno': 9999,
        'ename': 'shivansu',
        'eaddr': 'Indore',
        'esal': 35000,
    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    print(r.json())

def delete_resource(id):
    data = {'id': id}
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(r.status_code)
    print(r.json())

create_resource()  # Call the create_resource function to test creating a resource
