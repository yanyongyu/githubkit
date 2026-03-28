# Reusing Client

You can make multiple requests with the same client instance in one context:

=== "Sync"

    ```python hl_lines="4"
    from githubkit import GitHub, Response
    from githubkit.versions.latest.models import FullRepository

    with GitHub("<your_token_here>") as github:
        resp: Response[FullRepository] = github.rest.repos.get(owner="owner", repo="repo")
        repo: FullRepository = resp.parsed_data
    ```

=== "Async"

    ```python hl_lines="4"
    from githubkit import GitHub, Response
    from githubkit.versions.latest.models import FullRepository

    async with GitHub("<your_token_here>") as github:
        resp: Response[FullRepository] = await github.rest.repos.async_get(owner="owner", repo="repo")
        repo: FullRepository = resp.parsed_data
    ```

!!! warning

    Repeatedly creating new client instances may lead to memory leaks. We recommend reusing the same client instance within a single context to avoid this issue.
