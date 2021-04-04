from .utils import api_request

choose_result = lambda: api_request(method="PATCH", path="/draws/ongoing")
create_draw = lambda: api_request(method="POST", path="/draws")
