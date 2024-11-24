from typing import Any, Optional, Union

from githubkit.compat import GitHubModel, model_before_validator


class SourceLocation(GitHubModel):
    line: int
    column: int


class GraphQLError(GitHubModel):
    # https://github.com/octokit/graphql.js/pull/314
    # https://github.com/yanyongyu/githubkit/issues/159
    type: Optional[str] = None
    message: str
    locations: Optional[list[SourceLocation]] = None
    path: Optional[list[Union[int, str]]] = None
    extensions: Optional[dict[str, Any]] = None


class GraphQLResponse(GitHubModel):
    data: Optional[dict[str, Any]] = None
    errors: Optional[list[GraphQLError]] = None
    extensions: Optional[dict[str, Any]] = None

    @model_before_validator
    @classmethod
    def _validate_data_and_errors(cls, values: dict[str, Any]):
        if values.get("data") is None and not values.get("errors"):
            raise ValueError("No data or errors found in response")
        return values
