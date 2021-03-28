import requests
from requests import RequestException

import env


DEFAULT_HEADERS = {
    "Internal-Key": env.INTERNAL_KEY,
}


def get_response_data(response):
    if not response.ok:
        raise RequestException(
            f"Request to '{response.url}' failed"
            f" with status code {response.status_code}."
        )

    return response.json()


def api_request(method, path="", headers={}):
    url = f"{env.API_BASE_URL}{path}"
    headers = {**DEFAULT_HEADERS, **headers}

    return requests.request(method=method, url=url, headers=headers)


client = {
    "create_draw": lambda: api_request(method="POST", path="/draws"),
}
