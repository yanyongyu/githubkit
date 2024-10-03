# Configuration

githubkit is highly configurable, you can change the default config by passing config options to `GitHub`:

```python
from githubkit import GitHub

github = GitHub(
    base_url="https://api.github.com/",
    accept_format=None,
    previews=None,
    user_agent="GitHubKit/Python",
    follow_redirects=True,
    timeout=None,
    http_cache=True,
    auto_retry=True,
)
```

Or, you can pass the config object directly (not recommended):

```python
import httpx
from githubkit import GitHub, Config
from githubkit.retry import RETRY_DEFAULT

config = Config(
    base_url="https://api.github.com/",
    accept="application/vnd.github+json",
    user_agent="GitHubKit/Python",
    follow_redirects=True,
    timeout=httpx.Timeout(None),
    http_cache=True,
    auto_retry=RETRY_DEFAULT,
)

github = GitHub(config=config)
```

## Options

### `base_url`

The `base_url` option is used to set the base URL of the GitHub API. If you are using GitHub Enterprise Server, you need to include the `/api/v3/` path in the base URL.

### `accept_format`, `previews`

The `accept_format` and `previews` are used to set the default `Accept` header. By default, githubkit uses `application/vnd.github+json`. You can find more details in [GitHub API docs](https://docs.github.com/en/rest/overview/media-types).

The `accept_format` option could be set to `PARAM+json`, such as `raw+json`.

The `previews` option could be set to a list of preview features, such as `["starfox"]`. You can find the preview feature names in the GitHub API docs. Note that you do not need to include the `-preview` suffix in the preview feature name.

### `user_agent`

The `user_agent` option is used to set the `User-Agent` header. By default, githubkit uses `GitHubKit/Python`.

### `follow_redirects`

The `follow_redirects` option is used to enable or disable the HTTP redirect following feature. By default, githubkit follows the redirects.

### `timeout`

The `timeout` option is used to set the request timeout. You can pass a float, `None` or `httpx.Timeout` to this field. By default, the requests will never timeout. See [Timeout](https://www.python-httpx.org/advanced/timeouts/) for more information.

### `http_cache`

The `http_cache` option enables the http caching feature powered by [Hishel](https://hishel.com/) for HTTPX. GitHub API limits the number of requests that you can make within a specific amount of time. This feature is useful to reduce the number of requests to GitHub API and avoid hitting the rate limit.

### `auto_retry`

The `auto_retry` option enables request retrying when rate limit exceeded and server error encountered. See [Auto Retry](#auto-retry) for more infomation.
