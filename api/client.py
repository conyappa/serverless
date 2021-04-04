from .utils import api_request

choose_result = lambda: api_request(method="POST", path="/draws/ongoing/choose")
create_draw = lambda: api_request(method="POST", path="/draws")
