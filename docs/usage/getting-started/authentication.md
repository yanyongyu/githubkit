# Authentication

githubkit supports a variety of authentication strategies for the GitHub API. The following table summarizes all available strategies:

| Strategy                                                                 | Use Case                       |
| ------------------------------------------------------------------------ | ------------------------------ |
| [`UnauthAuthStrategy`](#without-authentication)                          | Public endpoints, quick tests  |
| [`TokenAuthStrategy`](#token-authentication)                             | Personal Access Tokens (PAT)   |
| [`AppAuthStrategy`](#github-app-authentication)                          | GitHub App (JWT)               |
| [`AppInstallationAuthStrategy`](#github-app-installation-authentication) | GitHub App installation        |
| [`OAuthAppAuthStrategy`](#oauth-app-authentication)                      | OAuth App (client credentials) |
| [`OAuthTokenAuthStrategy`](#oauth-user-token-authentication)             | Stored user access tokens      |
| [`OAuthWebAuthStrategy`](#oauth-web-flow-authentication)                 | OAuth web flow code exchange   |
| [`OAuthDeviceAuthStrategy`](#oauth-device-flow-authentication)           | OAuth device flow (CLI, IoT)   |
| [`ActionAuthStrategy`](#github-action-authentication)                    | GitHub Actions workflows       |

All strategies are importable from the top-level `githubkit` package.

## Without Authentication

Access public GitHub API endpoints without credentials. Useful for quick tests, but subject to much lower [rate limits](https://docs.github.com/en/rest/rate-limit).

```python
from githubkit import GitHub, UnauthAuthStrategy

# Simply omit the auth parameter
github = GitHub()

# Or explicitly use UnauthAuthStrategy
github = GitHub(UnauthAuthStrategy())
```

## Token Authentication

The simplest way to authenticate — pass a [Personal Access Token (PAT)](https://github.com/settings/personal-access-tokens/new) as a string. This works for both classic tokens and fine-grained PATs.

```python
from githubkit import GitHub, TokenAuthStrategy

# Shorthand: pass a token string directly
github = GitHub("<your_token_here>")

# Explicit: use TokenAuthStrategy
github = GitHub(TokenAuthStrategy("<your_token_here>"))
```

!!! tip

    Store tokens in environment variables or a secrets manager — never hard-code them in source files.

## GitHub App Authentication

Authenticate **as a GitHub App** using a JSON Web Token (JWT) signed with the app's private key. This gives you access to app-level API endpoints (e.g., listing installations). See [GitHub Docs — Authenticating as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app) for background.

You can identify the app by **app ID** or **client ID** (GitHub supports both). The client ID and client secret are only required if you plan to use OAuth features (e.g., exchanging user tokens).

```python
from githubkit import GitHub, AppAuthStrategy

# Using app ID (client ID and secret are optional)
github = GitHub(
    AppAuthStrategy(
        "<app_id>", "<private_key>", "<optional_client_id>", "<optional_client_secret>"
    )
)

# Using client ID instead of app ID
github = GitHub(
    AppAuthStrategy(
        None, "<private_key>", "<client_id>", "<optional_client_secret>"
    )
)
```

## GitHub App Installation Authentication

Authenticate **as a specific installation** of your GitHub App. This grants access to the repositories and permissions that the organization or user has approved for that installation. API requests are attributed to the app.

See [GitHub Docs — Authenticating as an installation](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation) for details.

```python
from githubkit import GitHub, AppInstallationAuthStrategy

# Using app ID
github = GitHub(
    AppInstallationAuthStrategy(
        "<app_id>", "<private_key>", installation_id, "<optional_client_id>", "<optional_client_secret>",
    )
)

# Using client ID instead of app ID
github = GitHub(
    AppInstallationAuthStrategy(
        None, "<private_key>", installation_id, "<client_id>", "<optional_client_secret>",
    )
)
```

!!! tip

    You can also derive an installation client from a `GitHub` App instance using `with_auth` — see [Switching Auth Strategies](#switching-auth-strategies) below.

## OAuth App Authentication

Authenticate as an **OAuth App** using client credentials. This strategy uses [Basic authentication](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app) with the client ID and secret, which is required for certain endpoints (e.g., managing OAuth tokens).

```python
from githubkit import GitHub, OAuthAppAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))
```

## OAuth User Token Authentication

Act **on behalf of a user** using a previously obtained OAuth access token. This is the strategy to use when you have stored a user's token in your database and want to make API calls as that user.

### Without token expiration

For OAuth Apps or GitHub Apps **without** user-to-server token expiration enabled:

```python
from githubkit import GitHub, OAuthTokenAuthStrategy

github = GitHub(
    OAuthTokenAuthStrategy(
        "<client_id>", "<client_secret>", token="<access_token>"
    )
)
```

### With token expiration (refresh tokens)

For GitHub Apps **with** user-to-server token expiration enabled, provide the refresh token so githubkit can automatically renew expired access tokens. If you also supply the access token, you **must** include its expiration time:

```python
from datetime import datetime

from githubkit import GitHub, OAuthTokenAuthStrategy

github = GitHub(
    OAuthTokenAuthStrategy(
        "<client_id>",
        "<client_secret>",
        token="<access_token>",  # optional if refresh_token is set
        expire_time=datetime(),  # required when token is provided
        refresh_token="<refresh_token>",  # optional if token is set
        refresh_token_expire_time=datetime(),  # optional
    )
)
```

### Manually refreshing the token

You can force a token refresh at any time:

```python
# sync
github.auth.refresh(github)
# async
await github.auth.async_refresh(github)
```

This updates the `token` and `refresh_token` attributes **in place** on the auth strategy object. After refreshing, persist the new values from `github.auth` to your database.

## OAuth Web Flow Authentication

Exchange an OAuth **authorization code** (from the web application flow) for a user access token. See [GitHub Docs — Using the web application flow](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app#using-the-web-application-flow-to-generate-a-user-access-token).

```python
from githubkit import GitHub, OAuthWebAuthStrategy

github = GitHub(
    OAuthWebAuthStrategy("<client_id>", "<client_secret>", "<code>")
)
```

!!! warning

    This strategy is **one-time use** — the authorization code can only be exchanged once. After obtaining the token, persist it and switch to `OAuthTokenAuthStrategy` for subsequent requests.

To exchange the code and retrieve the resulting token:

```python
from githubkit import GitHub, OAuthWebAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(
    OAuthWebAuthStrategy("<client_id>", "<client_secret>", "<code>")
)

# sync
auth: OAuthTokenAuthStrategy = github.auth.exchange_token(github)
# async
auth: OAuthTokenAuthStrategy = await github.auth.async_exchange_token(github)

# Persist these values to your database
access_token = auth.token
refresh_token = auth.refresh_token
```

See [Switching Auth Strategies](#switching-auth-strategies) for a complete example of web flow integration with `OAuthAppAuthStrategy`.

## OAuth Device Flow Authentication

Authenticate a user on **input-constrained devices** (CLI tools, IoT, smart TVs) without a web browser. githubkit handles the polling loop automatically. See [GitHub Docs — Using the device flow](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app#using-the-device-flow-to-generate-a-user-access-token).

You must provide a **callback function** that displays the user code. githubkit calls this function when a code is generated, then polls the server until the user completes authentication or the code expires.

```python
from githubkit import GitHub, OAuthDeviceAuthStrategy

def callback(data: dict):
    """Display the user code and verification URL to the user."""
    print(f"Open {data['verification_uri']} and enter code: {data['user_code']}")

github = GitHub(
    OAuthDeviceAuthStrategy("<client_id>", callback)
)
```

The callback receives the full device authorization response as a dict. Key fields can be found in the [GitHub Docs — Using the device flow](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app#using-the-device-flow-to-generate-a-user-access-token).

!!! warning

    This strategy is also **one-time use**. Exchange and persist the token for future requests:

```python
from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

# sync
auth: OAuthTokenAuthStrategy = github.auth.exchange_token(github)
# async
auth: OAuthTokenAuthStrategy = await github.auth.async_exchange_token(github)

# Persist these values
access_token = auth.token
refresh_token = auth.refresh_token
```

## GitHub Action Authentication

Authenticate automatically inside **GitHub Actions** workflows using the `GITHUB_TOKEN` provided by the runner.

```python
from githubkit import GitHub, ActionAuthStrategy

github = GitHub(ActionAuthStrategy())
```

Make sure the token is available to your step — pass it as an **input** or **environment variable**:

```yaml
- name: Run my script
  with:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

# Or as an environment variable
- name: Run my script
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Switching Auth Strategies

The `with_auth` method creates a **new `GitHub` instance** with a different auth strategy while **sharing the same configuration** (base URL, timeout, cache, etc.). This is essential for OAuth flows where you start as an app and then act as a user.

### GitHub App → Installation

```python
from githubkit import GitHub, AppAuthStrategy

github = GitHub(AppAuthStrategy("<app_id>", "<private_key>"))

# Create a new client authenticated as a specific installation
installation_github = github.with_auth(
    github.auth.as_installation(installation_id)
)
```

### GitHub App → OAuth App

Requires `client_id` and `client_secret` to be set on the `AppAuthStrategy`:

```python
from githubkit import GitHub, AppAuthStrategy

github = GitHub(
    AppAuthStrategy(
        "<app_id>", "<private_key>", "<client_id>", "<client_secret>"
    )
)

oauth_github = github.with_auth(github.auth.as_oauth_app())
```

### OAuth App → User (Web Flow)

Exchange a web flow code for a user token and make requests as the user:

```python
from githubkit import GitHub, OAuthAppAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

# Create a client that acts as the user
user_github = github.with_auth(github.auth.as_web_user("<code>"))

# Make a request as the user
resp = user_github.rest.users.get_authenticated()
user = resp.parsed_data

# Retrieve the tokens for persistence
user_token = user_github.auth.token
user_token_expire_time = user_github.auth.expire_time
refresh_token = user_github.auth.refresh_token
refresh_token_expire_time = user_github.auth.refresh_token_expire_time
```

You can also exchange the code for a token **without making a request first**:

```python
from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

# sync
auth: OAuthTokenAuthStrategy = github.auth.as_web_user("<code>").exchange_token(github)
# async
auth: OAuthTokenAuthStrategy = await github.auth.as_web_user("<code>").async_exchange_token(github)

# Persist the tokens
user_token = auth.token
user_token_expire_time = auth.expire_time
refresh_token = auth.refresh_token
refresh_token_expire_time = auth.refresh_token_expire_time

# Create a new client with the exchanged token
user_github = github.with_auth(auth)
```

### Device Flow → Token

```python
from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

def callback(data: dict):
    print(data["user_code"])

user_github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

# Option 1: Make a request first (triggers the device flow automatically)
resp = user_github.rest.users.get_authenticated()
user = resp.parsed_data

# Retrieve the tokens for persistence
user_token = user_github.auth.token
user_token_expire_time = user_github.auth.expire_time
refresh_token = user_github.auth.refresh_token
refresh_token_expire_time = user_github.auth.refresh_token_expire_time

# you can also exchange the token directly without making a request
auth: OAuthTokenAuthStrategy = github.auth.exchange_token(github)
# or asynchronously
auth: OAuthTokenAuthStrategy = await github.auth.async_exchange_token(github)

user_token = auth.token
user_token_expire_time = auth.expire_time
refresh_token = auth.refresh_token
refresh_token_expire_time = auth.refresh_token_expire_time

# Create a reusable client with the token
token_github = user_github.with_auth(auth)
```
