import pytest
import requests

from helpers.logger import logger


@pytest.mark.parametrize("status_code", [
    200,  # OK
    300,  # Multiple Choices
    400,  # Bad Request
    404,  # Not Found
    500  # Internal Server Error
])
def test_logger(status_code):
    url = f'https://httpbin.org/status/{status_code}'
    response = requests.get(url)
    try:
        response.raise_for_status()
        logger.info("OK. URL: %s, Code: %d", url, response.status_code)
        assert True
    except requests.exceptions.HTTPError as err:
        logger.error("Error. %s", str(err))
        assert False
