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
    ssl_verify=True,
    cache_strategy=None,
    http_cache=True,
    throttler=None,
    auto_retry=True,
    rest_api_validate_body=True,
)
```

Or, you can pass the config object directly (not recommended):

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
    cache_strategy=DEFAULT_CACHE_STRATEGY,
    http_cache=True,
    throttler=None,
    auto_retry=RETRY_DEFAULT,
    rest_api_validate_body=True,
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

### `ssl_verify`

The `ssl_verify` option is used to customize the SSL certificate verification. By default, githubkit enables the SSL certificate verification. If you want to disable the SSL certificate verification, you can set this option to `False`. Or you can provide a custom ssl context to this option. See [SSL](https://www.python-httpx.org/advanced/ssl/) for more information.

### `trust_env`

If `trust_env` is set to `True`, githubkit (httpx) will look for the environment variables to configure the proxy and SSL certificate verification. By default, this option is set to `True`. If you want to disable this feature, you can set this option to `False`.

### `proxy`

If you want to set a proxy for client programmatically, you can pass a proxy URL to the `proxy` option. See [httpx's proxies documentation](https://www.python-httpx.org/advanced/proxies/) for more information.

### `transport`, `async_transport`

These two options let you provide a custom [HTTPX transport](https://www.python-httpx.org/advanced/transports/) for the underlying HTTP client.

They accept instances of the following types:

- `httpx.BaseTransport` (sync transport) — pass via the `transport` option.
- `httpx.AsyncBaseTransport` (async transport) — pass via the `async_transport` option.

When provided, githubkit will forward the transport to create the client. This is useful for:

- providing a custom network implementation;
- injecting test-only transports (for example `httpx.MockTransport`) to stub responses in unit tests;
- using alternative transports provided by HTTPX or third parties.

Note that if you pass `None` to the option, the default transport will be created by HTTPX.

### `cache_strategy`

The `cache_strategy` option defines how to cache the tokens or http responses. You can provide a githubkit built-in cache strategy or a custom one that implements the `BaseCacheStrategy` interface. By default, githubkit uses the `MemCacheStrategy` to cache the data in memory.

Available built-in cache strategies:

- `MemCacheStrategy`: Cache the data in memory.

      Normally, you do not need to specifically use this cache strategy. It is used by default.

      ```python
      from githubkit.cache import DEFAULT_CACHE_STRATEGY, MemCacheStrategy

      # Use the default cache strategy
      github = GitHub(cache_strategy=DEFAULT_CACHE_STRATEGY)
      # Or you can initialize another MemCacheStrategy instance
      # this will create a new cache instance and not share the cache with the global one
      github = GitHub(cache_strategy=MemCacheStrategy())
      ```

- `RedisCacheStrategy`: Cache the data in Redis (Sync only).

      To cache the data in Redis (Sync only), you need to provide a redis client to the `RedisCacheStrategy`. For example:

      ```python
      from redis import Redis

      github = GitHub(
          cache_strategy=RedisCacheStrategy(
              client=Redis(host="localhost", port=6379), prefix="githubkit:"
          )
      )
      ```

      The `prefix` option is used to set the key prefix in Redis. You should add a `:` at the end of the prefix if you want to use namespace like key format. Both `githubkit` and `hishel` will use the prefix to store the cache data.

      Note that using this sync only cache strategy will cause the `GitHub` instance to be sync only.

- `AsyncRedisCacheStrategy`: Cache the data in Redis (Async only).

      To cache the data in Redis (Async only), you need to provide an async redis client to the `AsyncRedisCacheStrategy`. For example:

      ```python
      from redis.asyncio import Redis

      github = GitHub(
          cache_strategy=AsyncRedisCacheStrategy(
              client=Redis(host="localhost", port=6379), prefix="githubkit:"
          )
      )
      ```

      The `prefix` option is used to set the key prefix in Redis. You should add a `:` at the end of the prefix if you want to use namespace like key format. Both `githubkit` and `hishel` will use the prefix to store the cache data.

      Note that using this async only cache strategy will cause the `GitHub` instance to be async only.

### `http_cache`

The `http_cache` option enables the http caching feature powered by [Hishel](https://hishel.com/) for HTTPX. GitHub API limits the number of requests that you can make within a specific amount of time. This feature is useful to reduce the number of requests to GitHub API and avoid hitting the rate limit.

### `throttler`

The `throttler` option is used to control the request concurrency to avoid hitting the rate limit. You can provide a githubkit built-in throttler or a custom one that implements the `BaseThrottler` interface. By default, githubkit uses the `LocalThrottler` to control the request concurrency.

Available built-in throttlers:

- `LocalThrottler`: Control the request concurrency in the local process / event loop.

      ```python
      from githubkit.throttling import LocalThrottler

      github = GitHub(throttler=LocalThrottler(100))
      ```

### `auto_retry`

The `auto_retry` option enables request retrying when rate limit exceeded and server error encountered. See [Auto Retry](./auto-retry.md) for more infomation.

### `rest_api_validate_body`

The `rest_api_validate_body` option is used to enable or disable the rest API request body validation. By default, githubkit validates the input data against the GitHub API schema. If you do not want to validate the input data, you can set this option to `False`.
