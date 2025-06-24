import requests

import pytest
import csv
from data.get_data import auth_endpoints


@pytest.fixture(scope="session")
def base_url():
    return "https://my-api-examaple.herokuapp.com/api"


def pytest_generate_tests(metafunc):
    print(metafunc.fixturenames)
    if "auth_availability" in metafunc.fixturenames:
        with open("/Users/elenayanushevskaya/Downloads/api-main/data/auth_endpoints.csv") as file:
            reader = csv.reader(file)
            header = next(reader)
            metafunc.parametrize("auth_availability", reader)


def id_val(val):
    return val[0]


@pytest.mark.parametrize("data", auth_endpoints, ids=id_val)
def test_with_generator(data):
    assert data[0] == 'status'
    # assert data[2] == '402'


def test_methods_availability(base_url, auth_availability):
    endpoint, method, expected_status, description = auth_availability
    response = requests.request(method, f"{base_url}/auth/{endpoint}")

    assert response.status_code == int(expected_status), \
        f"Wrong status code on auth {endpoint} url for {method} method"

    assert response.json().get("description") == description
