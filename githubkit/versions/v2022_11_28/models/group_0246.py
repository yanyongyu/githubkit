"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class PorterAuthor(GitHubModel):
    """Porter Author

    Porter Author
    """

    id: int = Field()
    remote_id: str = Field()
    remote_name: str = Field()
    email: str = Field()
    name: str = Field()
    url: str = Field()
    import_url: str = Field()


model_rebuild(PorterAuthor)

__all__ = ("PorterAuthor",)
