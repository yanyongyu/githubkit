"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import Literal

VERSIONS = {
    "2022-11-28": "v2022_11_28",
}
LATEST_VERSION = "2022-11-28"
VERSION_TYPE = Literal["2022-11-28"]

from .rest import RestVersionSwitcher as RestVersionSwitcher
from .webhooks import WebhooksVersionSwitcher as WebhooksVersionSwitcher
