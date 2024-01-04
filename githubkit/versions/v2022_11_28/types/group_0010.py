"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired


class ValidationErrorType(TypedDict):
    """Validation Error

    Validation Error
    """

    message: str
    documentation_url: str
    errors: NotRequired[List[ValidationErrorPropErrorsItemsType]]


class ValidationErrorPropErrorsItemsType(TypedDict):
    """ValidationErrorPropErrorsItems"""

    resource: NotRequired[str]
    field: NotRequired[str]
    message: NotRequired[str]
    code: str
    index: NotRequired[int]
    value: NotRequired[Union[str, None, int, None, List[str], None]]


__all__ = (
    "ValidationErrorType",
    "ValidationErrorPropErrorsItemsType",
)
