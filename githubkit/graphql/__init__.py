from typing import TYPE_CHECKING, Any, Dict, Optional, cast

from githubkit.exception import GraphQLFailed

from .models import GraphQLError as GraphQLError
from .models import SourceLocation as SourceLocation
from .models import GraphQLResponse as GraphQLResponse

if TYPE_CHECKING:
    from githubkit.response import Response


def build_graphql_request(
    query: str, variables: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    json: Dict[str, Any] = {"query": query}
    if variables:
        json["variables"] = variables
    return json


def parse_graphql_response(response: "Response[GraphQLResponse]") -> Dict[str, Any]:
    response_data = response.parsed_data
    if response_data.errors:
        raise GraphQLFailed(response_data)
    return cast(Dict[str, Any], response_data.data)
