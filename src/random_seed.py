import json

import requests
from requests import RequestException

import env
from utils.api import get_response_data
from utils.decorators import fails


def latest_bitcoin_block_hash():
    url = env.LATEST_BITCOIN_BLOCK_URL
    response = requests.get(url)

    data = get_response_data(response)
    return data["hash"]


@fails(on=(RequestException,))
def main(event, context):
    body = {
        "value": latest_bitcoin_block_hash(),
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body),
    }
