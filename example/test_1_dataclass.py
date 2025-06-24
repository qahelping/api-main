from dataclasses import dataclass

user = {'name': 'User',
        'age': 15}


@dataclass
class User:
    name: str = 'User'
    age: int = 15


dc_user = User()


def test_dict():
    assert user['name'] == 'User'


def test_dc():
    assert dc_user.name == 'User'