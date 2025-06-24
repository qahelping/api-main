import requests
from jsonschema import validate


def test_api_json_schema():
    res = requests.get("https://jsonplaceholder.typicode.com/todos/1")

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "userUID": {"type": "number"},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
        },
        "required": ["id", "userId", "title", "completed", 'userUID']
    }

    validate(instance=res.json(), schema=schema)
