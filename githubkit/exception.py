from typing import TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from .response import Response
    from .graphql import GraphQLResponse


class GitHubException(Exception):
    ...


class AuthCredentialError(GitHubException):
    """Auth Credential Error"""


class AuthExpiredError(GitHubException):
    """Auth Expired Error"""


class RequestError(GitHubException):
    """Simple API request failed with unknown error"""


class RequestTimeout(GitHubException):
    """Simple API request timeout"""

    def __init__(self, request: httpx.Request):
        self.request = request

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(method={self.request.method}, "
            f"url={self.request.url})"
        )


class RequestFailed(GitHubException):
    """Simple API request failed with error status code"""

    def __init__(self, response: "Response"):
        self.request = response.raw_request
        self.response = response

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(method={self.request.method}, "
            f"url={self.request.url}, status_code={self.response.status_code})"
        )


class GraphQLFailed(GitHubException):
    """GraphQL request with errors in response"""

    def __init__(self, response: "GraphQLResponse"):
        self.response = response

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.response.errors!r})"


class WebhookTypeNotFound(GitHubException):
    """Webhook event type not found"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"
