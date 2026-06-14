# Reusing Client

githubkit manages an underlying [HTTPX](https://www.python-httpx.org/) client for making HTTP requests. You can use a **context manager** to ensure the HTTP client is properly created, reused, and closed when you're done.

<!-- https://github.com/yanyongyu/githubkit/issues/285 -->

!!! warning

    We strongly recommend **using the context manager** for any workload that makes multiple API calls or long running processes. Repeatedly creating new HTTP clients may lead to **memory leaks**.

## Using the Context Manager

Wrapping your `GitHub` instance in a `with` (sync) or `async with` (async) block creates a single HTTP client that is shared across all requests made inside that block, and automatically closed on exit:

=== "Sync"

    ```python hl_lines="4"
    from githubkit import GitHub, Response
    from githubkit_schemas.latest.models import FullRepository

    with GitHub("<your_token_here>") as github:
        resp: Response[FullRepository] = github.rest.repos.get(owner="owner", repo="repo")
        repo: FullRepository = resp.parsed_data
    ```

=== "Async"

    ```python hl_lines="4"
    from githubkit import GitHub, Response
    from githubkit_schemas.latest.models import FullRepository

    async with GitHub("<your_token_here>") as github:
        resp: Response[FullRepository] = await github.rest.repos.async_get(owner="owner", repo="repo")
        repo: FullRepository = resp.parsed_data
    ```

!!! note

    A context manager cannot be entered twice. Attempting to nest `with github:` inside another `with github:` on the same instance will raise a `RuntimeError`.

## Without the Context Manager

You can also use `GitHub` without a context manager. In this case, githubkit creates a new HTTP client per request, which is convenient for one-off calls but less efficient for multiple requests:

```python
from githubkit import GitHub

github = GitHub("<your_token_here>")
resp = github.rest.repos.get(owner="owner", repo="repo")
```
