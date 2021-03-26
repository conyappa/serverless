import json

import requests
from requests import RequestException

from .utils import fail_as


def latest_bitcoin_block_hash():
    url = "https://blockchain.info/latestblock"
    response = requests.get(url=url)

    if response.ok:
        raise RequestException(f"Request to '{url}' failed with status code {response.status_code}.")  # noqa: E501

    data = response.json()
    return data["hash"]


@fail_as(status=503, on=(RequestException,))
def main(event, context):
    body = {"value": latest_bitcoin_block_hash()}

    return {
        "statusCode": 200,
        "body": json.dumps(body),
    }
