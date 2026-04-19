# Using Personal Access Token (PAT) to Call GitHub API

## Prerequisites

Many REST API endpoints require authentication or return additional information if you are authenticated.
To authenticate your request, you will need to provide an authentication token with the required scopes or permissions.
You can create a PAT at [GitHub Personal Access Token](https://github.com/settings/personal-access-tokens/new).

## Making API Calls

Once you have your token, you can initialize the `GitHub` client and start making requests. The example below shows how to fetch the authenticated user's info using both the REST and GraphQL APIs.

=== "Sync"

    ```python
    from githubkit import GitHub
    from githubkit.versions.latest.models import PublicUser, PrivateUser

    # Initialize the client with your Personal Access Token
    github = GitHub("<your_token_here>")

    # Call GitHub rest api
    resp = github.rest.users.get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # Call GitHub graphql api
    data: dict = github.graphql("{ viewer { login } }")
    ```

=== "Async"

    ```python
    from githubkit import GitHub
    from githubkit.versions.latest.models import PublicUser, PrivateUser

    # Initialize the client with your Personal Access Token
    github = GitHub("<your_token_here>")

    # Call GitHub rest api
    resp = await github.rest.users.async_get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # Call GitHub graphql api
    data: dict = await github.async_graphql("{ viewer { login } }")
    ```
