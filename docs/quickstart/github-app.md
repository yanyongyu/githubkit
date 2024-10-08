# Develop a GitHub APP

## Authenticating as an installation by repository name

=== "Sync"

    ```python
    from githubkit import GitHub, AppAuthStrategy
    from githubkit.versions.latest.models import Installation, IssueComment

    github = GitHub(
        AppAuthStrategy("your_app_id", "your_private_key", "client_id", "client_secret")
    )

    resp = github.rest.apps.get_repo_installation("owner", "repo")
    repo_installation: Installation = resp.parsed_data

    installation_github = github.with_auth(
        github.auth.as_installation(repo_installation.id)
    )

    # create a comment on an issue
    resp = installation_github.rest.issues.create_comment("owner", "repo", 1, body="Hello")
    issue: IssueComment = resp.parsed_data
    ```

=== "Async"

    ```python
    from githubkit import GitHub, AppAuthStrategy
    from githubkit.versions.latest.models import Installation, IssueComment

    github = GitHub(
        AppAuthStrategy("your_app_id", "your_private_key", "client_id", "client_secret")
    )

    resp = await github.rest.apps.async_get_repo_installation("owner", "repo")
    repo_installation: Installation = resp.parsed_data

    installation_github = github.with_auth(
        github.auth.as_installation(repo_installation.id)
    )

    # create a comment on an issue
    resp = await installation_github.rest.issues.async_create_comment(
        "owner", "repo", 1, body="Hello"
    )
    issue: IssueComment = resp.parsed_data
    ```

## Authenticating as an installation by username

=== "Sync"

    ```python
    from githubkit import GitHub, AppAuthStrategy
    from githubkit.versions.latest.models import Installation, IssueComment

    github = GitHub(
        AppAuthStrategy("your_app_id", "your_private_key", "client_id", "client_secret")
    )

    resp = github.rest.apps.get_user_installation("username")
    user_installation: Installation = resp.parsed_data

    installation_github = github.with_auth(
        github.auth.as_installation(user_installation.id)
    )

    # create a comment on an issue
    resp = installation_github.rest.issues.create_comment("owner", "repo", 1, body="Hello")
    issue: IssueComment = resp.parsed_data
    ```

=== "Async"

    ```python
    from githubkit import GitHub, AppAuthStrategy
    from githubkit.versions.latest.models import Installation, IssueComment

    github = GitHub(
        AppAuthStrategy("your_app_id", "your_private_key", "client_id", "client_secret")
    )

    resp = await github.rest.apps.async_get_user_installation("username")
    user_installation: Installation = resp.parsed_data

    installation_github = github.with_auth(
        github.auth.as_installation(user_installation.id)
    )

    # create a comment on an issue
    resp = await installation_github.rest.issues.async_create_comment(
        "owner", "repo", 1, body="Hello"
    )
    issue: IssueComment = resp.parsed_data
    ```
