import json

import requests


def main(event, context):
    url = "https://blockchain.info/latestblock"

    try:
        response = requests.get(url=url)
        data = response.json()
        value = data["hash"]

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
