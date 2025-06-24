import json

import pytest
import requests


def test_post():
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}

    response = requests.post(url, data=json.dumps(payload))
    response_json = response.json()
    assert response.status_code == 404
    assert response_json['message'] == 'Not Found'


def test_api_post():
    body = {
        "id": 1,
        "petId": 1,
        "quantity": 0,
        "shipDate": "2024-02-17T09:42:10.119Z",
        "status": "placed",
        "complete": 'true'
    }
    headers = {'accept': "application/json", 'Content-Type': 'application/json'}
    response = requests.post('https://petstore.swagger.io/v2/store/order', data=json.dumps(body), headers=headers)
    response_json = response.json()
    assert response.status_code == requests.codes.ok
    assert response_json['id'] == body['id']
    assert response_json['status'] == body['status']
