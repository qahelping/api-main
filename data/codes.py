import requests

STATUS_CODE = [
    (200, requests.codes.ok),  # OK
    (300, requests.codes.multiple_choices),  # Multiple Choices
    (400, requests.codes.bad_request),  # Bad Request
    (404, requests.codes.not_found),  # Not Found
    (500, requests.codes.internal_server_error),  # Internal Server Error
    (511, requests.codes.network_authentication),  # Network Authentication Required
]