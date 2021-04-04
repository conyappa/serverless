import requests
from requests import RequestException, Response

import env

DEFAULT_HEADERS = {
    "Internal-Key": env.INTERNAL_KEY,
}


def get_response_data(response: Response):
    if response.ok:
        return response.json()

    raise RequestException(f"Request to '{response.url}' failed" f" with status code {response.status_code}.")


def api_request(method: str, path: str = "", headers: dict = {}):
    url = f"{env.API_BASE_URL}{path}"
    headers = {**DEFAULT_HEADERS, **headers}

    return requests.request(method=method, url=url, headers=headers)
