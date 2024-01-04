"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class Enterprise(GitHubModel):
    """Enterprise

    An enterprise on GitHub.
    """

    description: Missing[Union[str, None]] = Field(
        default=UNSET, description="A short description of the enterprise."
    )
    html_url: str = Field()
    website_url: Missing[Union[str, None]] = Field(
        default=UNSET, description="The enterprise's website URL."
    )
    id: int = Field(description="Unique identifier of the enterprise")
    node_id: str = Field()
    name: str = Field(description="The name of the enterprise.")
    slug: str = Field(description="The slug url identifier for the enterprise.")
    created_at: Union[datetime, None] = Field()
    updated_at: Union[datetime, None] = Field()
    avatar_url: str = Field()


model_rebuild(Enterprise)

__all__ = ("Enterprise",)
