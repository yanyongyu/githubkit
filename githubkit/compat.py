from pydantic import BaseModel, ConfigDict


class GitHubModel(BaseModel):
    ...


class ExtraGitHubModel(GitHubModel):
    model_config = ConfigDict(extra="allow")
