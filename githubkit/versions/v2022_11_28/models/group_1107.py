"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class TeamsTeamIdProjectsProjectIdPutBody(GitHubModel):
    """TeamsTeamIdProjectsProjectIdPutBody"""

    permission: Missing[Literal["read", "write", "admin"]] = Field(
        default=UNSET,
        description="The permission to grant to the team for this project. Default: the team's `permission` attribute will be used to determine what permission to grant the team on this project. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling this endpoint. For more information, see \"[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\"",
    )


model_rebuild(TeamsTeamIdProjectsProjectIdPutBody)

__all__ = ("TeamsTeamIdProjectsProjectIdPutBody",)
