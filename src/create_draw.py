import json

from api import client
from api.utils import get_response_data


def main(event, context):
    response = client.create_draw()
    data = get_response_data(response)

    return {
        "statusCode": response.status_code,
        "body": json.dumps(data),
    }
