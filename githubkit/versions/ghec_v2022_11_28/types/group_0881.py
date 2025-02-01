"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import TypedDict

from .group_0049 import (
    AmazonS3AccessKeysConfigType,
    AzureBlobConfigType,
    AzureHubConfigType,
    GoogleCloudConfigType,
)
from .group_0050 import AmazonS3OidcConfigType, SplunkConfigType
from .group_0051 import DatadogConfigType


class EnterprisesEnterpriseAuditLogStreamsPostBodyType(TypedDict):
    """EnterprisesEnterpriseAuditLogStreamsPostBody"""

    enabled: bool
    stream_type: Literal[
        "Azure Blob Storage",
        "Azure Event Hubs",
        "Amazon S3",
        "Splunk",
        "HTTPS Event Collector",
        "Google Cloud Storage",
        "Datadog",
    ]
    vendor_specific: Union[
        AzureBlobConfigType,
        AzureHubConfigType,
        AmazonS3OidcConfigType,
        AmazonS3AccessKeysConfigType,
        SplunkConfigType,
        GoogleCloudConfigType,
        DatadogConfigType,
    ]


__all__ = ("EnterprisesEnterpriseAuditLogStreamsPostBodyType",)
