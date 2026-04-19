# Connecting to GitHub Enterprise

Connecting to GitHub Enterprise is similar to using the public GitHub API, but requires two specific configurations. Each is explained below with brief guidance and examples.

## Provide the server API endpoint

When connecting to a GitHub Enterprise Server (GHES or GHEC), you must set the server's REST API endpoint via the `base_url` parameter when creating the client. Use the full API base URL for your instance (for example `https://example.ghe.com/api/v3/`). githubkit will ensure the trailing slash is present.

This tells the client where to send REST and GraphQL requests rather than the public GitHub endpoints.

```python hl_lines="4 7"
from githubkit import GitHub
from githubkit.versions.latest.models import PublicUser, PrivateUser

github = GitHub("<your_token_here>", base_url="https://example.ghe.com/api/v3/")
```

## Switch the REST API schema version

GitHub Enterprise Server may require a different REST API schema/version than the public API. Use the `rest("<schema-version>")` selector on the client to choose the correct REST schema for your server (for example `ghec-2022-11-28`). Picking the right schema ensures endpoint signatures match your server version and provides autocompletion support in your IDE.

The examples below demonstrate how to use both REST API and GraphQL API calls:

=== "Sync"

    ```python hl_lines="2"
    # Call the GitHub REST API with a specific schema version
    resp = github.rest("ghec-2022-11-28").users.get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # Call the GitHub GraphQL API
    data: dict = github.graphql("{ viewer { login } }")
    ```

=== "Async"

    ```python hl_lines="2"
    # Call the GitHub REST API with a specific schema version
    resp = await github.rest("ghec-2022-11-28").users.async_get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # Call the GitHub GraphQL API
    data: dict = await github.async_graphql("{ viewer { login } }")
    ```

For more information, see [REST API Versioning](../usage/rest-api.md#rest-api-versioning).
