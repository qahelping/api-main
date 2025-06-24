from asyncio import Event

import pytest
from pydantic import BaseModel

from helpers.get_data import get_data_from_json

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
    obj =   {
      "name": "Dominator",
      "rank": 1,
      "gold": "100000",
      "dead": False
    },
    player = Player.model_validate_json(obj)

