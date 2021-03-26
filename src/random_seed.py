import json
import os

import requests


def latest_bitcoin_block_hash():
    url = os.environ.get("LATEST_BITCOIN_BLOCK_URL")
    response = requests.get(url=url)

    data = response.json()
    return data["hash"]


def main(event, context):
    try:
        value = latest_bitcoin_block_hash()

    except Exception:
        response = {
            "statusCode": 503,
        }

    else:
        body = {
            "value": value,
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body),
        }

    return response
