import os
from pathlib import Path

############
# ENV VARS #
############

INTERNAL_KEY = os.environ.get("INTERNAL_KEY")
API_BASE_URL = os.environ.get("API_BASE_URL")

LATEST_BITCOIN_BLOCK_URL = os.environ.get("LATEST_BITCOIN_BLOCK_URL")


###################
# LOCAL OVERWRITE #
###################

LOCAL_STEM = "local"
LOCAL_PATH = Path(f"src/env/{LOCAL_STEM}.py")

if LOCAL_PATH.exists():
    from .local import *  # noqa: F401,F403
