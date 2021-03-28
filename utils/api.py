import requests
from requests import RequestException

import env


def get_response_data(response):
    if not response.ok:
        raise RequestException(
            f"Request to '{response.url}' failed"
            f"with status code {response.status_code}."
        )

    return response.json()


client = {
    "create_draw": lambda: requests.get(f"{env.API_BASE_URL}/draws"),
}
