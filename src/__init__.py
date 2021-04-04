import sentry_sdk
from sentry_sdk.integrations.serverless import serverless_function

import env

from .choose_result import main as choose_result
from .create_draw import main as create_draw
from .fetch_movements import main as fetch_movements
from .random_seed import main as random_seed

sentry_sdk.init(dsn=env.SENTRY_DSN)


choose_result = serverless_function(choose_result)
create_draw = serverless_function(create_draw)
fetch_movements = serverless_function(fetch_movements)
random_seed = serverless_function(random_seed)
