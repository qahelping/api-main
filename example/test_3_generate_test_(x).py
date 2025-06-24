# https://docs.pytest.org/en/stable/parametrize.html#parametrize-basics
# Should pass --input as param to pytest

def pytest_addoption(parser):
    parser.addoption(
        "--input",
        action="append",
        default=[],
        help="list of inputs to pass to test functions",
    )


# pytest -q --input="hello" --input="world" test_3_generate_test.py -v
# pytest -q --input="hello_12!" test_3_generate_test.py -v
# pytest -q --input="hello world" test_3_generate_test.py -v
# python -m pytest test_3_generate_test.py -v --input="HELLO" --input="WORLD"
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--input",
        action="append",
        default=[],
        help="list of inputs to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "input" in metafunc.fixturenames:
        metafunc.parametrize("input", metafunc.config.getoption("input"))


def test_valid_string(input):
    assert input.isalpha(), f"'{input}' contains not only letters"


def test_upper_string(input):
    assert input.isupper(), f"'{input}' is not upper case string"


@pytest.mark.parametrize("limited_param", [1, 2, 3])
def test_compute(limited_param, input):
    assert limited_param < 4
    assert input.isalpha()
