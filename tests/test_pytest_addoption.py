import pytest
import requests


def test_environment(env):
    assert env in ["dev", "staging", "prod"], f"Unknown environment: {env}"


def test_domen(domen):
    response = requests.post(f'https://httpbin.{domen}/post', data={'key': 'value'})
    assert response.status_code == 200


@pytest.mark.parametrize("code", [200, 300, 400, 404, 500, 502])
def test_url_status(code, request_method):
    target = 'https://httpbin.org/' + f"/status/{code}"
    response = request_method(url=target)
    assert response.status_code == code
