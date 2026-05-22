from typing import Any

from githubkit.compat import GitHubModel, model_before_validator


class SourceLocation(GitHubModel):
    line: int
    column: int


class GraphQLError(GitHubModel):
    # https://github.com/octokit/graphql.js/pull/314
    # https://github.com/yanyongyu/githubkit/issues/159
    type: str | None = None
    message: str
    locations: list[SourceLocation] | None = None
    path: list[int | str] | None = None
    extensions: dict[str, Any] | None = None


class GraphQLResponse(GitHubModel):
    data: dict[str, Any] | None = None
    errors: list[GraphQLError] | None = None
    extensions: dict[str, Any] | None = None

    @model_before_validator
    @classmethod
    def _validate_data_and_errors(cls, values: dict[str, Any]):
        if values.get("data") is None and not values.get("errors"):
            raise ValueError("No data or errors found in response")
        return values
