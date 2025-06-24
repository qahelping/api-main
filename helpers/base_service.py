import json
import requests

from helpers.logger import logger

class BaseService():

    def delete(self, url, headers):
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None


    def post(self, url, body):
        try:
            headers = {'accept': "application/json", 'Content-Type': 'application/json'}
            response = requests.post(url, data=json.dumps(body), headers=headers)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None


    def put(self, url, body, headers):
        try:
            response = requests.put(url, data=json.dumps(body), headers=headers)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None


    def get(self, url, params=None, headers=None):
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None
