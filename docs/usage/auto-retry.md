# Auto Retry

By default, githubkit will retry the request when specific exception encountered. When rate limit exceeded, githubkit will retry **once** after GitHub suggested waiting time. When server error encountered (http status >= 500), githubkit will retry **max three times**.

## Disable Auto Retry

You can disable this feature by set the `auto_retry` option to `False`:

```python
github = GitHub(
    ...
    auto_retry=False
)
```

## Customize Retry Decision

You can also customize the retry decision by passing a callable. The callable should accept two arguments: the exception raised `exc` and the current retry count `retry_count`. The callable should return a `RetryOption` object. `RetryOption` is a named tuple with two fields: `do_retry` and `retry_after`. If `do_retry` is `True`, the request will be retried after `retry_after` time. Otherwise, the exception will be raised.

```python hl_lines="6-9 13"
from datetime import timedelta

from githubkit.retry import RetryOption
from githubkit.exception import GitHubException

def retry_decision_func(exc: GitHubException, retry_count: int) -> RetryOption:
    if retry_count < 1:
        return RetryOption(True, timedelta(seconds=60))
    return RetryOption(False)

github = GitHub(
    ...
    auto_retry=retry_decision_func
)
```

## Builtin Retry Decision

githubkit also provides some builtin retry decision function.

### Rate Limit Exceeded

```python
from githubkit.retry import RETRY_RATE_LIMIT, RetryRateLimit

github = GitHub(
  ...
  auto_retry=RETRY_RATE_LIMIT  # (1)!
)

github = GitHub(
  ...
  auto_retry=RetryRateLimit(max_retry=1)  # (2)!
)
```

1. Retry once when rate limit exceeded.
2. Retry when rate limit exceeded with custom max retry count.

### Server Error

```python
from githubkit.retry import RETRY_SERVER_ERROR, RetryServerError

github = GitHub(
   ...
   auto_retry=RETRY_SERVER_ERROR  # (1)!
)
github = GitHub(
   ...
   auto_retry=RetryServerError(max_retry=1)  # (2)!
)
```

1. Retry three times when server error encountered.
2. Retry when server error encountered with custom max retry count.

### Chain Retry Decision Functions

You can chain multiple retry decision functions by using `RetryChainDecision`. The request will be retried if **any** of the decision functions return `True`. For example:

```python
from githubkit.retry import RETRY_RATE_LIMIT, RETRY_SERVER_ERROR, RetryChainDecision

github = GitHub(
   ...
   auto_retry=RetryChainDecision(RETRY_RATE_LIMIT, RETRY_SERVER_ERROR)
)
```
