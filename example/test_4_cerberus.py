import cerberus
import requests


def test_api_json_schema():
    """Проверка структуры ответа за запрос /todos/1"""
    res = requests.get("https://jsonplaceholder.typicode.com/todos/1")

    schema = {
        "id": {"type": "number"},
        "userUIF": {"type": "number"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    }

    v = cerberus.Validator()
    assert v.validate(res.json(), schema)
