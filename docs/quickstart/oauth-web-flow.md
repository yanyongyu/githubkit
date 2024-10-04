# Develop an OAuth APP (GitHub APP) with Web Flow

OAuth web flow allows you to authenticate as a user and act on behalf of the user.

Note that if you are developing a GitHub APP, you may opt-in / opt-out of the user-to-server token expiration feature. If you opt-in, the user-to-server token will expire after a certain period of time, and you need to use the refresh token to generate a new token. In this case, you need to do more work to handle the token refresh. See [GitHub Docs - Refreshing user access tokens](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/refreshing-user-access-tokens) for more information.

## Sync Example

If you are developing an OAuth APP or a GitHub APP without user-to-server token expiration:

```python
from githubkit.versions.latest.models import PublicUser, PrivateUser
from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

# redirect user to github oauth page and get the code from callback

user_github = github.with_auth(github.auth.as_web_user("<code>"))  # (1)!

# === or ===
auth: OAuthTokenAuthStrategy = github.auth.as_web_user("<code>").exchange_token(
    github
)  # (2)!
access_token = auth.token

user_github = github.with_auth(
    OAuthTokenAuthStrategy("<client_id>", "<client_secret>", token=access_token)
)  # (3)!

# now you can act as the user
resp = user_github.rest.users.get_authenticated()
user: PublicUser | PrivateUser = resp.parsed_data

# you can get the user name and id now
username = user.login
user_id = user.id
```

1. If you just want to use the user token once, simply switch to OAuth Web Auth Strategy.
2. exchange the user token manually and store it in a database.
3. restore the user token from database

If you are developing a GitHub APP with user-to-server token expiration:

```python
from githubkit.versions.latest.models import PublicUser, PrivateUser
from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

# redirect user to github oauth page and get the code from callback

user_github = github.with_auth(github.auth.as_web_user("<code>"))  # (1)!

# === or ===
auth: OAuthTokenAuthStrategy = github.auth.as_web_user("<code>").exchange_token(
    github
)  # (2)!
refresh_token = auth.refresh_token

auth = OAuthTokenAuthStrategy(
    "<client_id>", "<client_secret>", refresh_token=refresh_token
)  # (3)!
auth.refresh(github)  # (4)!
refresh_token = auth.refresh_token

user_github = github.with_auth(auth)

# now you can act as the user
resp = user_github.rest.users.get_authenticated()
user: PublicUser | PrivateUser = resp.parsed_data

# you can get the user name and id now
username = user.login
user_id = user.id
```

1. If you just want to use the user token once, simply switch to OAuth Web Auth Strategy.
2. exchange the user token manually and store it in a database.
3. restore the user refresh token from database and generate a new token.
4. refresh the token manually and store the new one. otherwise, the token will be refreshed automatically when you make a request.

## Async Example

If you are developing an OAuth APP or a GitHub APP without user-to-server token expiration:

```python
from githubkit.versions.latest.models import PublicUser, PrivateUser
from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

# redirect user to github oauth page and get the code from callback

user_github = github.with_auth(github.auth.as_web_user("<code>"))  # (1)!

# === or ===
auth: OAuthTokenAuthStrategy = await github.auth.as_web_user(
    "<code>"
).async_exchange_token(github)  # (2)!
access_token = auth.token

user_github = github.with_auth(
    OAuthTokenAuthStrategy("<client_id>", "<client_secret>", token=access_token)
)  # (3)!

# now you can act as the user
resp = await user_github.rest.users.async_get_authenticated()
user: PublicUser | PrivateUser = resp.parsed_data

# you can get the user name and id now
username = user.login
user_id = user.id
```

1. If you just want to use the user token once, simply switch to OAuth Web Auth Strategy.
2. exchange the user token manually and store it in a database.
3. restore the user token from database

If you are developing a GitHub APP with user-to-server token expiration:

```python
from githubkit.versions.latest.models import PublicUser, PrivateUser
from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

# redirect user to github oauth page and get the code from callback

user_github = github.with_auth(github.auth.as_web_user("<code>"))  # (1)!

# === or ===
auth: OAuthTokenAuthStrategy = await github.auth.as_web_user(
    "<code>"
).async_exchange_token(github)  # (2)!
refresh_token = auth.refresh_token

auth = OAuthTokenAuthStrategy(
    "<client_id>", "<client_secret>", refresh_token=refresh_token
)  # (3)!
await auth.async_refresh(github)  # (4)!
refresh_token = auth.refresh_token

user_github = github.with_auth(auth)

# now you can act as the user
resp = await user_github.rest.users.async_get_authenticated()
user: PublicUser | PrivateUser = resp.parsed_data

# you can get the user name and id now
username = user.login
user_id = user.id
```

1. If you just want to use the user token once, simply switch to OAuth Web Auth Strategy.
2. exchange the user token manually and store it in a database.
3. restore the user refresh token from database and generate a new token.
4. refresh the token manually and store the new one. otherwise, the token will be refreshed automatically when you make a request.
