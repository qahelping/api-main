from helpers.get_data import get_data_from_csv

import pytest
from pydantic import BaseModel

from helpers.get_data import get_data_from_json


def id_val(val):
    return val[0]


auth_endpoints = get_data_from_csv("../files/auth_endpoints.csv")


@pytest.mark.parametrize("data", auth_endpoints, ids=id_val)
def test_with_generator(data):
    assert data[0] == 'login'


data = get_data_from_json("../files/file.json")


class Player(BaseModel):
    name: str
    rank: int
    gold: str
    dead: bool


@pytest.mark.parametrize("data", data)
def test_json(data):
    print(data)
    assert data['name'] in ('Dominator', 'TheKiller', 'Vasya666', 'Cheater')


@pytest.mark.parametrize("data", data)
def test_json_2(data):
    obj = {
        "name": "Dominator",
        "rank": 1,
        "gold": "100000",
        "dead": False
    },
    player = Player.model_validate_json(obj)
