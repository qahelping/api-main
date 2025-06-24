import pytest
import requests

from data.codes import STATUS_CODE


def test_text():
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=5')
    assert response.status_code == 200
    assert 'url' in response.text
    assert 'height' in response.text
    assert 'width' in response.text
    assert 'url' in response.text
    assert 'https://cdn2.thecatapi.com/images/' in response.text


def test_json():
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=5')
    response_json = response.json()
    assert response.status_code == 200
    assert response_json[0]['id']
    assert response_json[0]['height']
    assert response_json[0]['width']
    assert 'https://cdn2.thecatapi.com/images/' in response_json[0]['url']


def test_raise_for_status_200():
    url = "https://httpbin.org/status/200"
    r = requests.get(url)

    try:
        r.raise_for_status()
        print("Запрос успешен.")
        assert True
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка HTTP: {err}")
        assert False


def test_raise_for_status_500():
    url = "https://httpbin.org/status/500"
    r = requests.get(url)

    try:
        r.raise_for_status()
        print("Запрос успешен.")
        assert False
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка HTTP: {err}")
        assert True


@pytest.mark.parametrize("status_code, codes", STATUS_CODE)
def test_status_codes(status_code, codes):
    response = requests.get(f'https://httpbin.org/status/{status_code}')

    assert response.status_code == codes, f"Expected {codes}, but got {response.status_code}"
