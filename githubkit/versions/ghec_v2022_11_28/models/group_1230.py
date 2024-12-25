"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class UserSocialAccountsDeleteBody(GitHubModel):
    """UserSocialAccountsDeleteBody

    Examples:
        {'account_urls': ['https://www.linkedin.com/company/github/',
    'https://twitter.com/github']}
    """

    account_urls: list[str] = Field(
        description="Full URLs for the social media profiles to delete."
    )


model_rebuild(UserSocialAccountsDeleteBody)

__all__ = ("UserSocialAccountsDeleteBody",)