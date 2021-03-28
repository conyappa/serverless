from requests import RequestException

from utils.api import client
from utils.decorators import fail_as


@fail_as(status=503, on=(RequestException,))
def main(event, context):
    pass
