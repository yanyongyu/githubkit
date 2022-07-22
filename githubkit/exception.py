from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .response import Response


class GitHubException(Exception):
    ...


class RequestFailed(GitHubException):
    def __init__(self, response: "Response"):
        self.response = response

    def __repr__(self) -> str:
        return (
            f"<RequestFailed: {self.response.raw_request.method} "
            f"{self.response.raw_request.url}, status_code: {self.response.status_code}>"
        )
