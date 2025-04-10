"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict


class CvssSeveritiesType(TypedDict):
    """CvssSeverities"""

    cvss_v3: NotRequired[Union[CvssSeveritiesPropCvssV3Type, None]]
    cvss_v4: NotRequired[Union[CvssSeveritiesPropCvssV4Type, None]]


class CvssSeveritiesPropCvssV3Type(TypedDict):
    """CvssSeveritiesPropCvssV3"""

    vector_string: Union[str, None]
    score: Union[float, None]


class CvssSeveritiesPropCvssV4Type(TypedDict):
    """CvssSeveritiesPropCvssV4"""

    vector_string: Union[str, None]
    score: Union[float, None]


__all__ = (
    "CvssSeveritiesPropCvssV3Type",
    "CvssSeveritiesPropCvssV4Type",
    "CvssSeveritiesType",
)
