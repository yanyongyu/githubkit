# Configuration

githubkit is highly configurable. You can customize its behavior by passing keyword arguments directly to the `GitHub` constructor:

```python
from githubkit import GitHub

github = GitHub(
    base_url="https://api.github.com/",
    accept_format=None,
    previews=None,
    user_agent="GitHubKit/Python",
    follow_redirects=True,
    timeout=None,
    ssl_verify=True,
    trust_env=True,
    proxy=None,
    transport=None,
    async_transport=None,
    event_hooks=None,
    async_event_hooks=None,
    cache_strategy=None,
    http_cache=True,
    throttler=None,
    auto_retry=True,
    rest_api_validate_body=True,
)
```

Alternatively, you can build a `Config` object and pass it via the `config` parameter. This is useful when you want to share the same configuration across multiple `GitHub` instances:

```python
import httpx
from githubkit import GitHub, Config
from githubkit.retry import RETRY_DEFAULT
from githubkit.cache import DEFAULT_CACHE_STRATEGY

config = Config(
    base_url="https://api.github.com/",
    accept="application/vnd.github+json",
    user_agent="GitHubKit/Python",
    follow_redirects=True,
    timeout=httpx.Timeout(None),
    ssl_verify=True,
    trust_env=True,
    proxy=None,
    transport=None,
    async_transport=None,
    event_hooks=None,
    async_event_hooks=None,
    cache_strategy=DEFAULT_CACHE_STRATEGY,
    http_cache=True,
    throttler=None,
    auto_retry=RETRY_DEFAULT,
    rest_api_validate_body=True,
)

github = GitHub(config=config)
```

!!! note

    When using the `config` parameter, you **cannot** pass individual keyword arguments at the same time — they are mutually exclusive.

## Options

### `base_url`

The base URL for all API requests. Defaults to `https://api.github.com/`.

If you are using **GitHub Enterprise Server**, you must include the `/api/v3/` path suffix:

```python
github = GitHub(base_url="https://github.example.com/api/v3/")
```

!!! note

    githubkit automatically appends a trailing slash (`/`) if one is missing.

### `accept_format`, `previews`

These options control the `Accept` header sent with every request. By default, githubkit uses `application/vnd.github+json`.

- **`accept_format`** — a media type suffix such as `"raw+json"` or `"html+json"`. The leading dot is optional; githubkit adds it automatically. See [GitHub API Media Types](https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types) for available formats.
- **`previews`** — a list of API preview feature names, e.g., `["starfox"]`. Do **not** include the `-preview` suffix — githubkit adds it for you.

```python
# Request raw markdown content as JSON
github = GitHub(accept_format="raw+json")

# Enable an API preview feature
github = GitHub(previews=["starfox"])
```

### `user_agent`

Sets the `User-Agent` header. Defaults to `"GitHubKit/Python"`.

### `follow_redirects`

Whether to automatically follow HTTP redirects (3xx responses). Enabled by default.

### `timeout`

The request timeout. Accepts a `float` (seconds), an `httpx.Timeout` object for fine-grained control, or `None` for no timeout (default). See [HTTPX Timeouts](https://www.python-httpx.org/advanced/timeouts/) for details.

```python
import httpx

# Simple: 10 second timeout for all operations
github = GitHub(timeout=10.0)

# Fine-grained: different timeouts for connect vs. read
github = GitHub(timeout=httpx.Timeout(5.0, read=30.0))
```

### `ssl_verify`

Controls SSL certificate verification. Defaults to `True`.

- `True` — verify SSL certificates using the default CA bundle.
- `False` — **disable** SSL verification (not recommended for production).
- `ssl.SSLContext` — provide a custom SSL context for advanced use cases.

See [HTTPX SSL](https://www.python-httpx.org/advanced/ssl/) for details.

### `trust_env`

When `True` (default), githubkit (via HTTPX) reads environment variables such as `HTTP_PROXY`, `HTTPS_PROXY`, and `SSL_CERT_FILE` to configure proxies and SSL. Set to `False` to ignore these variables.

### `proxy`

Sets a proxy URL for all requests. Accepts a string, `httpx.URL`, or `httpx.Proxy` object.

```python
github = GitHub(proxy="http://proxy.example.com:8080")
```

See [HTTPX Proxies](https://www.python-httpx.org/advanced/proxies/) for more details.

!!! note

    If `trust_env` is `True` and no `proxy` is set, githubkit respects the `HTTP_PROXY` / `HTTPS_PROXY` / `ALL_PROXY` environment variables.

### `transport`, `async_transport`

Provide custom [HTTPX transports](https://www.python-httpx.org/advanced/transports/) to replace the default networking layer. This is useful for:

- **Unit testing** — inject `httpx.MockTransport` to stub API responses without making real HTTP calls.
- **Custom networking** — use alternative transport implementations (e.g., HTTP/3, Unix sockets).

| Option            | Type                       | Used for       |
| ----------------- | -------------------------- | -------------- |
| `transport`       | `httpx.BaseTransport`      | Sync requests  |
| `async_transport` | `httpx.AsyncBaseTransport` | Async requests |

```python
import httpx

def mock_handler(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"login": "octocat"})

github = GitHub(transport=httpx.MockTransport(mock_handler))
```

!!! warning

    When a custom transport is provided, proxy-related environment variables (`HTTP_PROXY`, etc.) have no effect. Set `transport` / `async_transport` to `None` (default) to use HTTPX's built-in transport.

### `event_hooks`, `async_event_hooks`

Register [HTTPX event hooks](https://www.python-httpx.org/advanced/event-hooks/) that run on every request and/or response. This is useful for logging, injecting headers, collecting metrics, or raising on error status codes — without modifying your business logic.

| Option              | Hook signatures                             | Used for       |
| ------------------- | ------------------------------------------- | -------------- |
| `event_hooks`       | `def hook(request)` / `def hook(response)`  | Sync requests  |
| `async_event_hooks` | `async def hook(request)` / `async def hook(response)` | Async requests |

Both options accept a dictionary mapping event names (`"request"`, `"response"`) to a list of callables. Each callable receives an `httpx.Request` or `httpx.Response` object respectively.

=== "Sync"

    ```python
    import httpx
    from githubkit import GitHub

    def log_request(request: httpx.Request) -> None:
        print(f"-> {request.method} {request.url}")

    def log_response(response: httpx.Response) -> None:
        print(f"<- {response.status_code}")

    github = GitHub(
        event_hooks={
            "request": [log_request],
            "response": [log_response],
        },
    )
    ```

=== "Async"

    ```python
    import httpx
    from githubkit import GitHub

    async def log_request(request: httpx.Request) -> None:
        print(f"-> {request.method} {request.url}")

    async def log_response(response: httpx.Response) -> None:
        print(f"<- {response.status_code}")

    github = GitHub(
        async_event_hooks={
            "request": [log_request],
            "response": [log_response],
        },
    )
    ```

!!! note

    Response hooks are called **before** the response body is read. If you need to access the body inside a hook, call `response.read()` (sync) or `await response.aread()` (async).

### `cache_strategy`

Controls how githubkit caches **tokens** (e.g., GitHub App installation tokens) and **HTTP responses**. The default is `MemCacheStrategy`, which stores data in process memory.

You can provide any built-in strategy or implement a custom one by subclassing `BaseCacheStrategy`.

#### Built-in Cache Strategies

**`MemCacheStrategy`** — In-memory cache (default)

No extra setup is needed. Each `MemCacheStrategy` instance maintains its own cache; the default instance is shared globally.

```python
from githubkit import GitHub
from githubkit.cache import DEFAULT_CACHE_STRATEGY, MemCacheStrategy

# Use the global default (shared across all GitHub instances)
github = GitHub(cache_strategy=DEFAULT_CACHE_STRATEGY)

# Or create an isolated cache instance
github = GitHub(cache_strategy=MemCacheStrategy())
```

**`RedisCacheStrategy`** — Redis cache (sync only)

Stores tokens and HTTP responses in Redis. Requires the `redis` package.

```python
from redis import Redis
from githubkit import GitHub
from githubkit.cache import RedisCacheStrategy

github = GitHub(
    cache_strategy=RedisCacheStrategy(
        client=Redis(host="localhost", port=6379),
        prefix="githubkit:",
    )
)
```

!!! warning

    Using `RedisCacheStrategy` restricts the `GitHub` instance to **sync-only** operations.

**`AsyncRedisCacheStrategy`** — Redis cache (async only)

The async counterpart of `RedisCacheStrategy`. Requires the `redis` package with async support (`redis.asyncio`).

```python
from redis.asyncio import Redis
from githubkit import GitHub
from githubkit.cache import AsyncRedisCacheStrategy

github = GitHub(
    cache_strategy=AsyncRedisCacheStrategy(
        client=Redis(host="localhost", port=6379),
        prefix="githubkit:",
    )
)
```

!!! warning

    Using `AsyncRedisCacheStrategy` restricts the `GitHub` instance to **async-only** operations.

!!! tip

    The `prefix` parameter adds a key namespace in Redis. Include a trailing colon (`:`) for readable key names (e.g., `"githubkit:"`). Both githubkit and [Hishel](https://hishel.com/) use this prefix.

### `http_cache`

Enables HTTP response caching powered by [Hishel](https://hishel.com/). When enabled, githubkit respects standard HTTP caching headers (`ETag`, `Last-Modified`, `Cache-Control`) returned by the GitHub API. This reduces redundant API calls and helps you stay within [rate limits](https://docs.github.com/en/rest/rate-limit).

Enabled by default (`True`). Set to `False` to disable.

### `throttler`

Controls request concurrency to prevent hitting GitHub's rate limits. By default, githubkit uses `LocalThrottler`, which limits concurrent requests within the current process or event loop.

```python
from githubkit import GitHub
from githubkit.throttling import LocalThrottler

# Allow at most 100 concurrent requests
github = GitHub(throttler=LocalThrottler(100))
```

You can implement a custom throttler by subclassing `BaseThrottler`.

### `auto_retry`

Enables automatic retrying of requests when a **rate limit is exceeded** (HTTP 403/429) or a **server error** (HTTP 5xx) is encountered. Enabled by default (`True`).

- `True` — use the built-in retry strategy.
- `False` — disable auto-retry.
- `RetryDecisionFunc` — provide a custom callable for fine-grained control.

See [Auto Retry](../auto-retry.md) for more information.

### `rest_api_validate_body`

When `True` (default), githubkit validates REST API request bodies against the GitHub API schema **before** sending the request. This catches invalid payloads early with clear error messages.

Set to `False` to skip validation, which can be useful if you need to send payloads that don't strictly match the schema (e.g., undocumented fields).
