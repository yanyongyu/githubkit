"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class UserEmailsDeleteBodyOneof0(GitHubModel):
    """UserEmailsDeleteBodyOneof0

    Deletes one or more email addresses from your GitHub account. Must contain at
    least one email address. **Note:** Alternatively, you can pass a single email
    address or an `array` of emails addresses directly, but we recommend that you
    pass an object using the `emails` key.

    Examples:
        {'emails': ['octocat@github.com', 'mona@github.com']}
    """

    emails: List[str] = Field(
        description="Email addresses associated with the GitHub user account."
    )


model_rebuild(UserEmailsDeleteBodyOneof0)

__all__ = ("UserEmailsDeleteBodyOneof0",)
