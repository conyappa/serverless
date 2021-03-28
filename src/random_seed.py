import json

import requests

import env
from api import get_response_data


def latest_bitcoin_block_hash():
    url = env.LATEST_BITCOIN_BLOCK_URL
    response = requests.get(url)

    data = get_response_data(response)
    return data["hash"]


def main(event, context):
    body = {
        "value": latest_bitcoin_block_hash(),
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body),
    }
