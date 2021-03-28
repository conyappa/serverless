import json


def fails(status: int = 500, on: tuple = (Exception,)):
    def inner(handler):
        def wrapper(*args, **kwargs):
            try:
                response = handler(*args, **kwargs)

            except on as e:
                body = {
                    "detail": str(e),
                }

                response = {
                    "statusCode": status,
                    "body": json.dumps(body),
                }

            return response

        return wrapper

    return inner
