from typing import Any, Dict, List, Union, Optional

from githubkit.compat import GitHubModel, model_before_validator


class SourceLocation(GitHubModel):
    line: int
    column: int


class GraphQLError(GitHubModel):
    type: str  # https://github.com/octokit/graphql.js/pull/314
    message: str
    locations: Optional[List[SourceLocation]] = None
    path: Optional[List[Union[int, str]]] = None
    extensions: Optional[Dict[str, Any]] = None


class GraphQLResponse(GitHubModel):
    data: Optional[Dict[str, Any]] = None
    errors: Optional[List[GraphQLError]] = None
    extensions: Optional[Dict[str, Any]] = None

    @model_before_validator
    @classmethod
    def _validate_data_and_errors(cls, values: Dict[str, Any]):
        if values.get("data") is None and not values.get("errors"):
            raise ValueError("No data or errors found in response")
        return values
