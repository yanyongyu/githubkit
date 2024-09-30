---
hide:
  - navigation
---

# Quick Start

Here is some common use cases to help you get started quickly. The following examples are written in sync style, you can also use async style by using functions with `async_` prefix. For more detailed usage, please refer to the [Usage](#usage) section.

> APIs are fully typed. Type hints in the following examples are just for reference only.

## Use personal access token (PAT) to call GitHub API

```python
from githubkit import GitHub
from githubkit.versions.latest.models import PublicUser, PrivateUser

github = GitHub("<your_token_here>")

# call GitHub rest api
resp = github.rest.users.get_authenticated()
user: PublicUser | PrivateUser = resp.parsed_data

# call GitHub graphql api
data: dict = github.graphql("{ viewer { login } }")
```

## Develop an OAuth APP (GitHub APP) with web flow

OAuth web flow allows you to authenticate as a user and act on behalf of the user.

Note that if you are developing a GitHub APP, you may opt-in / opt-out of the user-to-server token expiration feature. If you opt-in, the user-to-server token will expire after a certain period of time, and you need to use the refresh token to generate a new token. In this case, you need to do more work to handle the token refresh. See [GitHub Docs - Refreshing user access tokens](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/refreshing-user-access-tokens) for more information.

If you are developing an OAuth APP or a GitHub APP without user-to-server token expiration:

```python
from githubkit.versions.latest.models import PublicUser, PrivateUser
from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

# redirect user to github oauth page and get the code from callback

# one time usage
user_github = github.with_auth(github.auth.as_web_user("<code>"))

# or, store the user token in a database for later use
auth: OAuthTokenAuthStrategy = github.auth.as_web_user("<code>").exchange_token(github)
# store the user token to database
access_token = auth.token

# restore the user token from database

user_github = github.with_auth(
    OAuthTokenAuthStrategy(
        "<client_id>", "<client_secret>", token=access_token
    )
)

# now you can act as the user
resp = user_github.rest.users.get_authenticated()
user: PublicUser | PrivateUser = resp.parsed_data

# you can get the user name and id now
username = user.login
user_id = user.id
```

If you are developing a GitHub APP with user-to-server token expiration:

```python
from githubkit.versions.latest.models import PublicUser, PrivateUser
from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

# redirect user to github oauth page and get the code from callback

# one time usage
user_github = github.with_auth(github.auth.as_web_user("<code>"))

# or, store the user refresh token in a database for later use
auth: OAuthTokenAuthStrategy = github.auth.as_web_user("<code>").exchange_token(github)
refresh_token = auth.refresh_token

# restore the user refresh token from database

# you can use the refresh_token to generate a new token
auth = OAuthTokenAuthStrategy(
    "<client_id>", "<client_secret>", refresh_token=refresh_token
)
# refresh the token manually if you want to store the new refresh token
# otherwise, the token will be refreshed automatically when you make a request
auth.refresh(github)
refresh_token = auth.refresh_token

user_github = github.with_auth(auth)

# now you can act as the user
resp = user_github.rest.users.get_authenticated()
user: PublicUser | PrivateUser = resp.parsed_data

# you can get the user name and id now
username = user.login
user_id = user.id
```

## Develop an OAuth APP (GitHub APP) with device flow

```python
from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

# sync/async func for displaying user code to user
def callback(data: dict):
    print(data["user_code"])

user_github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

# if you want to store the user token in a database
auth: OAuthTokenAuthStrategy = user_github.auth.exchange_token(user_github)
access_token = auth.token
refresh_token = auth.refresh_token
# restore the user token from database
user_github = user_github.with_auth(
    OAuthTokenAuthStrategy(
        "<client_id>", None, refresh_token=refresh_token
    )
)
```

## Develop a GitHub APP

Authenticating as a installation by repository name:

```python
from githubkit import GitHub, AppAuthStrategy
from githubkit.versions.latest.models import Issue, Installation

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

Authenticating as a installation by username:

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
