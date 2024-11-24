from datetime import timedelta
from typing import TYPE_CHECKING, Generic, TypeVar

import httpx

if TYPE_CHECKING:
    from .graphql import GraphQLResponse
    from .response import Response


E = TypeVar("E", bound=Exception)


class GitHubException(Exception): ...


class CacheUnsupportedError(GitHubException):
    """Unsupported Cache Usage Error"""


class AuthCredentialError(GitHubException):
    """Auth Credential Error"""


class AuthExpiredError(GitHubException):
    """Auth Expired Error"""


class RequestError(GitHubException, Generic[E]):
    """Simple API request failed with unknown error"""

    def __init__(self, exc: E) -> None:
        self.exc = exc

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(origin_exc={self.exc!r})"


class RequestTimeout(RequestError[httpx.TimeoutException]):
    """Simple API request timeout"""

    @property
    def request(self) -> httpx.Request:
        return self.exc.request

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(method={self.request.method}, "
            f"url={self.request.url})"
        )


class RequestFailed(RequestError[httpx.HTTPStatusError]):
    """Simple API request failed with error status code"""

    def __init__(self, response: "Response"):
        super().__init__(
            httpx.HTTPStatusError(
                "Request failed",
                request=response.raw_request,
                response=response.raw_response,
            )
        )
        self.request = response.raw_request
        self.response = response

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(method={self.request.method}, "
            f"url={self.request.url}, status_code={self.response._status_reason})"
        )


class RateLimitExceeded(RequestFailed):
    """API request failed with rate limit exceeded"""

    def __init__(self, response: "Response", retry_after: timedelta):
        super().__init__(response)
        self.retry_after = retry_after

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(method={self.request.method}, "
            f"url={self.request.url}, status_code={self.response._status_reason}, "
            f"retry_after={self.retry_after})"
        )


class PrimaryRateLimitExceeded(RateLimitExceeded):
    """API request failed with primary rate limit exceeded"""


class SecondaryRateLimitExceeded(RateLimitExceeded):
    """API request failed with secondary rate limit exceeded"""


class GraphQLError(GitHubException):
    """Simple GraphQL request error"""


class GraphQLFailed(GraphQLError):
    """GraphQL request with errors in response"""

    def __init__(self, response: "GraphQLResponse"):
        self.response = response

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.response.errors!r})"


class GraphQLPaginationError(GraphQLError):
    """GraphQL paginate response error"""

    def __init__(self, response: "GraphQLResponse"):
        self.response = response

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.response})"


class GraphQLMissingPageInfo(GraphQLPaginationError):
    """GraphQL paginate response missing PageInfo object"""


class GraphQLMissingCursorChange(GraphQLPaginationError):
    """GraphQL paginate response missing cursor change"""


class WebhookTypeNotFound(GitHubException):
    """Webhook event type not found"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"
