# Develop a GitHub APP

A GitHub App acts on behalf of an installation, which is an instance of your app installed on a user or organization account. To perform actions, you must first authenticate as the app itself, then switch to a new client authenticated as a specific installation.

The first step is to initialize the client using your app's credentials with the `AppAuthStrategy`. This initial client can only access app-level APIs.

```python
from githubkit import GitHub, AppAuthStrategy

# 1. Authenticate as the GitHub App
# This client is used to get information about your app's installations.
app_github = GitHub(
    AppAuthStrategy(
        app_id="your_app_id",
        private_key="your_private_key",
        client_id="your_client_id",
        client_secret="your_client_secret",
    )
)
```

Once the app client is created, you can use it to query the installation info and switch to a new client authenticated as an installation.

## Acting on Behalf of an Installation

If your app needs to act on a specific repository, you can find its installation ID by repo name or org name.

=== "Sync"

    ```python
    from githubkit import GitHub, AppAuthStrategy
    from githubkit.versions.latest.models import Installation, IssueComment

    app_github = GitHub(
        AppAuthStrategy(
            app_id="your_app_id",
            private_key="your_private_key",
            client_id="your_client_id",
            client_secret="your_client_secret",
        )
    )

    # 2. Find the installation ID for a specific repository
    resp = app_github.rest.apps.get_repo_installation("owner", "repo")
    repo_installation: Installation = resp.parsed_data

    # 3. Create a new client authenticated as that installation
    installation_github = app_github.with_auth(
        app_github.auth.as_installation(repo_installation.id)
    )

    # 4. Use the installation client to perform actions
    resp = installation_github.rest.issues.create_comment("owner", "repo", 1, body="Hello")
    issue: IssueComment = resp.parsed_data
    ```

=== "Async"

    ```python
    from githubkit import GitHub, AppAuthStrategy
    from githubkit.versions.latest.models import Installation, IssueComment

    app_github = GitHub(
        AppAuthStrategy(
            app_id="your_app_id",
            private_key="your_private_key",
            client_id="your_client_id",
            client_secret="your_client_secret",
        )
    )

    # 2. Find the installation ID for a specific repository
    resp = await app_github.rest.apps.async_get_repo_installation("owner", "repo")
    repo_installation: Installation = resp.parsed_data

    # 3. Create a new client authenticated as that installation
    installation_github = app_github.with_auth(
        app_github.auth.as_installation(repo_installation.id)
    )

    # 4. Use the installation client to perform actions
    resp = await installation_github.rest.issues.async_create_comment(
        "owner", "repo", 1, body="Hello"
    )
    issue: IssueComment = resp.parsed_data
    ```

## Acting on Behalf of a User

API requests made by an app on behalf of a user will be attributed to that user. To make an API request on behalf of a user, the user must authorize your app.

=== "Sync"

    ```python
    from githubkit import GitHub, AppAuthStrategy
    from githubkit.versions.latest.models import Installation, IssueComment

    app_github = GitHub(
        AppAuthStrategy(
            app_id="your_app_id",
            private_key="your_private_key",
            client_id="your_client_id",
            client_secret="your_client_secret",
        )
    )

    # 2. Find the installation ID for a specific user
    resp = app_github.rest.apps.get_user_installation("username")
    user_installation: Installation = resp.parsed_data

    # 3. Create a new client authenticated as that user
    user_github = app_github.with_auth(
        app_github.auth.as_installation(user_installation.id)
    )

    # 4. Use the user client to perform actions on a repository
    resp = user_github.rest.issues.create_comment("owner", "repo", 1, body="Hello")
    issue: IssueComment = resp.parsed_data
    ```

=== "Async"

    ```python
    from githubkit import GitHub, AppAuthStrategy
    from githubkit.versions.latest.models import Installation, IssueComment

    app_github = GitHub(
        AppAuthStrategy(
            app_id="your_app_id",
            private_key="your_private_key",
            client_id="your_client_id",
            client_secret="your_client_secret",
        )
    )

    # 2. Find the installation ID for a specific user
    resp = await app_github.rest.apps.async_get_user_installation("username")
    user_installation: Installation = resp.parsed_data

    # 3. Create a new client authenticated as that user
    user_github = app_github.with_auth(
        app_github.auth.as_installation(user_installation.id)
    )

    # 4. Use the user client to perform actions on a repository
    resp = await user_github.rest.issues.async_create_comment(
        "owner", "repo", 1, body="Hello"
    )
    issue: IssueComment = resp.parsed_data
    ```
