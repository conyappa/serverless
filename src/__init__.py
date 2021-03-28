import sentry_sdk
from sentry_sdk.integrations.serverless import serverless_function

import env

from .create_draw import main as create_draw
from .random_seed import main as random_seed

sentry_sdk.init(dsn=env.SENTRY_DSN)


create_draw = serverless_function(create_draw)
random_seed = serverless_function(random_seed)
