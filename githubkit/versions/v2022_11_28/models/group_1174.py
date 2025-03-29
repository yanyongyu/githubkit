"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild


class UserEmailsPostBodyOneof0(GitHubModel):
    """UserEmailsPostBodyOneof0

    Examples:
        {'emails': ['octocat@github.com', 'mona@github.com']}
    """

    emails: list[str] = Field(
        min_length=1 if PYDANTIC_V2 else None,
        description="Adds one or more email addresses to your GitHub account. Must contain at least one email address. **Note:** Alternatively, you can pass a single email address or an `array` of emails addresses directly, but we recommend that you pass an object using the `emails` key.",
    )


model_rebuild(UserEmailsPostBodyOneof0)

__all__ = ("UserEmailsPostBodyOneof0",)
