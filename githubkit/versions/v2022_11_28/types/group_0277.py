"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class RepositoryRuleViolationErrorType(TypedDict):
    """RepositoryRuleViolationError

    Repository rule violation was detected
    """

    message: NotRequired[str]
    documentation_url: NotRequired[str]
    status: NotRequired[str]
    metadata: NotRequired[RepositoryRuleViolationErrorPropMetadataType]


class RepositoryRuleViolationErrorPropMetadataType(TypedDict):
    """RepositoryRuleViolationErrorPropMetadata"""

    secret_scanning: NotRequired[
        RepositoryRuleViolationErrorPropMetadataPropSecretScanningType
    ]


class RepositoryRuleViolationErrorPropMetadataPropSecretScanningType(TypedDict):
    """RepositoryRuleViolationErrorPropMetadataPropSecretScanning"""

    bypass_placeholders: NotRequired[
        list[
            RepositoryRuleViolationErrorPropMetadataPropSecretScanningPropBypassPlaceholdersItemsType
        ]
    ]


class RepositoryRuleViolationErrorPropMetadataPropSecretScanningPropBypassPlaceholdersItemsType(
    TypedDict
):
    """RepositoryRuleViolationErrorPropMetadataPropSecretScanningPropBypassPlaceholders
    Items
    """

    placeholder_id: NotRequired[str]
    token_type: NotRequired[str]


__all__ = (
    "RepositoryRuleViolationErrorPropMetadataPropSecretScanningPropBypassPlaceholdersItemsType",
    "RepositoryRuleViolationErrorPropMetadataPropSecretScanningType",
    "RepositoryRuleViolationErrorPropMetadataType",
    "RepositoryRuleViolationErrorType",
)
