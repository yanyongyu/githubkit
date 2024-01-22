from datetime import timedelta

from .log import logger
from .typing import RetryOption as RetryOption
from .typing import RetryDecisionFunc as RetryDecisionFunc
from .exception import RequestFailed, GitHubException, RateLimitExceeded


class RetryRateLimit:
    __slots__ = ("max_retry",)

    def __init__(self, max_retry: int = 1) -> None:
        self.max_retry = max_retry

    def __call__(self, exc: GitHubException, retry_count: int) -> RetryOption:
        # retry once for rate limit exceeded
        # https://github.com/octokit/octokit.js/blob/450c662e4f29b63a6dbe7592ba5ef53d5fa01d88/src/octokit.ts#L34-L65
        if retry_count < self.max_retry and isinstance(exc, RateLimitExceeded):
            logger.warning(
                f"{exc.__class__.__name__} for request "
                f"{exc.request.method} {exc.request.url}",
                exc_info=exc,
            )
            return RetryOption(True, exc.retry_after)

        return RetryOption(False)


RETRY_RATE_LIMIT = RetryRateLimit()


class RetryServerError:
    __slots__ = ("max_retry",)

    def __init__(self, max_retry: int = 3) -> None:
        self.max_retry = max_retry

    def __call__(self, exc: GitHubException, retry_count: int) -> RetryOption:
        # retry three times for server error
        # https://github.com/octokit/plugin-retry.js/blob/3b9897a58d8b2c37cfba6a8df78e4619d346098a/src/error-request.ts#L11-L14
        if (
            retry_count < self.max_retry
            and isinstance(exc, RequestFailed)
            and exc.response.status_code >= 500
        ):
            logger.warning(
                f"Server error encountered for request "
                f"{exc.request.method} {exc.request.url}",
                exc_info=exc,
            )
            return RetryOption(True, timedelta(seconds=(retry_count + 1) ** 2))

        return RetryOption(False)


RETRY_SERVER_ERROR = RetryServerError()


class RetryChainDecision:
    __slots__ = ("decision_funcs",)

    def __init__(self, *decision_funcs: RetryDecisionFunc) -> None:
        self.decision_funcs = decision_funcs

    def __call__(self, exc: GitHubException, retry_count: int) -> RetryOption:
        for decision_func in self.decision_funcs:
            retry_option = decision_func(exc, retry_count)
            if retry_option.do_retry:
                return retry_option

        return RetryOption(False)


RETRY_DEFAULT = RetryChainDecision(RETRY_RATE_LIMIT, RETRY_SERVER_ERROR)
