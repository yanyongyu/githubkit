"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0046 import DatadogConfig
from .group_0045 import SplunkConfig, AmazonS3OidcConfig
from .group_0044 import (
    AzureHubConfig,
    AzureBlobConfig,
    GoogleCloudConfig,
    AmazonS3AccessKeysConfig,
)


class EnterprisesEnterpriseAuditLogStreamsPostBody(GitHubModel):
    """EnterprisesEnterpriseAuditLogStreamsPostBody"""

    enabled: bool = Field(description="This setting pauses or resumes a stream.")
    stream_type: Literal[
        "Azure Blob Storage",
        "Azure Event Hubs",
        "Amazon S3",
        "Splunk",
        "HTTPS Event Collector",
        "Google Cloud Storage",
        "Datadog",
    ] = Field(
        description="The audit log streaming provider. The name is case sensitive."
    )
    vendor_specific: Union[
        AzureBlobConfig,
        AzureHubConfig,
        AmazonS3OidcConfig,
        AmazonS3AccessKeysConfig,
        SplunkConfig,
        GoogleCloudConfig,
        DatadogConfig,
    ] = Field()


model_rebuild(EnterprisesEnterpriseAuditLogStreamsPostBody)

__all__ = ("EnterprisesEnterpriseAuditLogStreamsPostBody",)
