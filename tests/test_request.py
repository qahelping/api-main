import requests


def test_get():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.status_code == 200
    assert 'message' in response.text


def test_post():
    response = requests.post('https://httpbin.org/post', data={'key': 'value'})
    assert response.status_code == 200


def test_put():
    response = requests.put('https://httpbin.org/put', data={'key': 'value'})
    assert response.status_code == 200


def test_delete():
    response = requests.delete('https://httpbin.org/delete')
    assert response.status_code == 200


def test_head():
    response = requests.head('https://httpbin.org/head')
    assert response.status_code == 404


def test_options():
    response = requests.options('https://httpbin.org/options')
    assert response.status_code == 404
