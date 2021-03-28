from requests import RequestException
import json

from utils.api import get_response_data, client
from utils.decorators import fails


@fails(on=(RequestException,))
def main(event, context):
    response = client["create_draw"]()
    data = get_response_data(response)

    return {
        "statusCode": response.status_code,
        "body": json.dumps(data),
    }
