from pydantic import BaseModel, ConfigDict


class GitHubModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)


class ExtraGitHubModel(GitHubModel):
    model_config = ConfigDict(extra="allow")


def model_rebuild(model: BaseModel):
    model.model_rebuild()
