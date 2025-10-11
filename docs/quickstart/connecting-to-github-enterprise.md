# Connecting to GitHub Enterprise

Connecting to the GitHub Enterprise is similar to the public GitHub API, but requires two specific configurations:

- To connect to **GitHub Enterprise Server**, you must provide the server's API endpoint in the `base_url` parameter.
- You need to switch the REST API schema version when using client.

The example below highlights these two changes.

=== "Sync"

    ```python hl_lines="4, 7"
    from githubkit import GitHub
    from githubkit.versions.latest.models import PublicUser, PrivateUser

    github = GitHub("<your_token_here>", base_url="https://example.ghe.com/api/v3/")

    # call GitHub rest api
    resp = github.rest("ghec-2022-11-28").users.get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # call GitHub graphql api
    data: dict = github.graphql("{ viewer { login } }")
    ```

=== "Async"

    ```python hl_lines="4, 7"
    from githubkit import GitHub
    from githubkit.versions.latest.models import PublicUser, PrivateUser

    github = GitHub("<your_token_here>", base_url="https://example.ghe.com/api/v3/")

    # call GitHub rest api
    resp = await github.rest("ghec-2022-11-28").users.async_get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # call GitHub graphql api
    data: dict = await github.async_graphql("{ viewer { login } }")
    ```
