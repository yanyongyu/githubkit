"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, model_rebuild


class AppManifestsCodeConversionsPostResponse201Allof1(ExtraGitHubModel):
    """AppManifestsCodeConversionsPostResponse201Allof1"""

    client_id: str = Field()
    client_secret: str = Field()
    webhook_secret: Union[str, None] = Field()
    pem: str = Field()


model_rebuild(AppManifestsCodeConversionsPostResponse201Allof1)

__all__ = ("AppManifestsCodeConversionsPostResponse201Allof1",)
