"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class GoogleCloudConfig(GitHubModel):
    """GoogleCloudConfig

    Google Cloud Config for audit log streaming configuration.
    """

    bucket: str = Field(description="Google Cloud Bucket Name")
    key_id: str = Field(
        description="Key ID obtained from the audit log stream key endpoint used to encrypt secrets."
    )
    encrypted_json_credentials: str = Field()


model_rebuild(GoogleCloudConfig)

__all__ = ("GoogleCloudConfig",)
