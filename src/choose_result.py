from api import client
from api.utils import proxy_view


def main(event, context):
    return proxy_view(func=client.choose_result)
