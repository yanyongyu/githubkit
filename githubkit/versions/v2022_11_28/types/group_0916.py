"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgSecurityProductEnablementPostBodyType(TypedDict):
    """OrgsOrgSecurityProductEnablementPostBody"""

    query_suite: NotRequired[Literal["default", "extended"]]


__all__ = ("OrgsOrgSecurityProductEnablementPostBodyType",)
