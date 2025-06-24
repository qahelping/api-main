import pytest
import requests


def test_params():
    param = {'limit': '1'}
    response = requests.get('https://api.thecatapi.com/v1/images/search', params=param)
    assert response.status_code == 200


def test_query_params():
    limit = '5'
    response = requests.get(f'https://api.thecatapi.com/v1/images/search?limit={limit}')
    assert response.status_code == 200


@pytest.fixture()
def status_code(request):
    return request.param


@pytest.mark.parametrize("status_code", [
    200,  # OK
    300,  # Multiple Choices
    400,  # Bad Request
    404,  # Not Found
    500  # Internal Server Error
], indirect=True)
def test_status_codes(status_code):
    response = requests.get(f'https://httpbin.org/status/{status_code}')

    assert response.status_code == status_code, f"Expected {status_code}, but got {response.status_code}"


@pytest.fixture
def data(request):
    # action
    return request.param * 2


@pytest.mark.parametrize("data", [1, 2, 3], indirect=True)
def test_indirect(data):
    assert data in [2, 4, 6]
