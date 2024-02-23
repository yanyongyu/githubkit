"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoCheckSuitesPreferencesPatchBodyType(TypedDict):
    """ReposOwnerRepoCheckSuitesPreferencesPatchBody"""

    auto_trigger_checks: NotRequired[
        List[
            ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType
        ]
    ]


class ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType(
    TypedDict
):
    """ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItems"""

    app_id: int
    setting: bool


__all__ = (
    "ReposOwnerRepoCheckSuitesPreferencesPatchBodyType",
    "ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType",
)
