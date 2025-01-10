# Authentication

githubkit supports multiple authentication strategies to access the GitHub API. You can also switch between them easily when doing auth flow.

## Without Authentication

If you want to access GitHub API without authentication or make a temporary test, you can use `UnauthAuthStrategy`:

```python
from githubkit import GitHub, UnauthAuthStrategy

# simply omit the auth parameter
github = GitHub()
# or, use UnauthAuthStrategy
github = GitHub(UnauthAuthStrategy())
```

## Token Authentication

You can authenticate to GitHub using a [Personal Access Token (PAT)](https://github.com/settings/personal-access-tokens/new). Replace `<your_token_here>` with your token:

```python
from githubkit import GitHub, TokenAuthStrategy

# simply pass the token as a string
github = GitHub("<your_token_here>")
# or, use TokenAuthStrategy
github = GitHub(TokenAuthStrategy("<your_token_here>"))
```

## GitHub APP Authentication

If you are developing a GitHub App, you can authenticate using the GitHub App's private key and app ID. See [GitHub Docs - Authenticating as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app) for more information.

If you do not want to use OAuth features, you can omit the client ID and client secret. Replace `<app_id>`, `<private_key>`, `<optional_client_id>`, and `<optional_client_secret>` with your app's credentials:

```python
from githubkit import GitHub, AppAuthStrategy

github = GitHub(
    AppAuthStrategy(
        "<app_id>", "<private_key>", "<optional_client_id>", "<optional_client_secret>"
    )
)
```

GitHub currently supports authentication using a GitHub App's private key and client ID. So, you could provide either the app ID or the client ID.

```python
from githubkit import GitHub, AppAuthStrategy

github = GitHub(
    AppAuthStrategy(
        None, "<private_key>", "<client_id>", "<optional_client_secret>"
    )
)
```

## GitHub APP Installation Authentication

GitHub Ap installation allows the app to access resources owned by that installation, as long as the app was granted the necessary repository access and permissions. API requests made by an app installation are attributed to the app. For more information, see [GitHub Docs - Authenticating as an installation](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation).

```python
from githubkit import GitHub, AppInstallationAuthStrategy

github = GitHub(
    AppInstallationAuthStrategy(
        "<app_id>", "<private_key>", installation_id, "<optional_client_id>", "<optional_client_secret>",
    )
)
```

App installation authentication also supports using the client ID instead of the app ID:

```python
from githubkit import GitHub, AppInstallationAuthStrategy

github = GitHub(
    AppInstallationAuthStrategy(
        None, "<private_key>", installation_id, "<client_id>", "<optional_client_secret>",
    )
)
```

## OAuth APP Authentication

If you are developing an OAuth App, you can authenticate using the client ID and client secret. See [GitHub Docs - Authenticating with an OAuth App](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app) for more information.

```python
from githubkit import GitHub, OAuthAppAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))
```

## OAuth User Token Authentication

OAuth App (GitHub App) allows you to act on behalf of a user after the user authorized your app. You can authenticate using the user token. This auth strategy is usefull when you stored the user token in a database.

If you are developing an OAuth App or a GitHub App without user-to-server token expiration, you can authenticate using the user token directly:

```python
from githubkit import GitHub, OAuthTokenAuthStrategy

github = GitHub(
    OAuthTokenAuthStrategy(
        "<client_id>", "<client_secret>", token="<access_token>"
    )
)
```

If you are developing a GitHub App with user-to-server token expiration, you need to provide the refresh token to keep the token up-to-date. In this case, you can omit the access token, but if you provide the access token, the access token expiration time is required:

```python
from datetime import datetime

from githubkit import GitHub, OAuthTokenAuthStrategy

github = GitHub(
    OAuthTokenAuthStrategy(
        "<client_id>",
        "<client_secret>",
        token="<access_token>",  # optional
        expire_time=datetime(),  # optional
        refresh_token="<refresh_token>",
        refresh_token_expire_time=datetime(),  # optional
    )
)
```

If you want to refresh the access token immediately, you can normally call the `refresh` method:

```python
# sync
auth = github.auth.refresh(github)
# async
auth = await github.auth.async_refresh(github)
```

This will update the access token and refresh token inplace. You can now store the new refresh token in `github.auth` to your database.

## OAuth Web Flow Authentication

GitHub OAuth web flow allows you to exchange the user access token with the web flow code. githubkit has built-in support for OAuth web flow token exchanging. See [GitHub Docs - Using the web application flow](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app#using-the-web-application-flow-to-generate-a-user-access-token) for more information.

```python
from githubkit import GitHub, OAuthWebAuthStrategy

github = GitHub(
    OAuthWebAuthStrategy(
        "<client_id_here>", "<client_secret_here>", "<web_flow_exchange_code_here>"
    )
)
```

Note that this auth strategy is only for one-time use. You need to store the user access token and refresh token in your database for future use:

```python
from githubkit import GitHub, OAuthWebAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(
    OAuthWebAuthStrategy(
        "<client_id_here>", "<client_secret_here>", "<web_flow_exchange_code_here>"
    )
)

# sync
auth: OAuthTokenAuthStrategy = github.auth.exchange_token(github)
# async
auth: OAuthTokenAuthStrategy = await github.auth.async_exchange_token(github)

access_token = auth.token
refresh_token = auth.refresh_token
```

See [Switch between AuthStrategy](#switch-between-authstrategy) for more detail about oauth flow.

## OAuth Device Flow Authentication

OAuth device flow allows you to authenticate as a user without a web browser (e.g., cli tools, desktop apps). githubkit has built-in support for OAuth device flow. See [GitHub Docs - Using the device flow](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app#using-the-device-flow-to-generate-a-user-access-token) for more information.

Before you start the device flow, you need to create a callback function to display the user code to the user. The callback function will be called when the user code is generated, and githubkit will poll the server until the user successfully authenticated or code expired.

```python
from githubkit import GitHub, OAuthDeviceAuthStrategy

# sync/async func for displaying user code to user
# the data dict is the generation response from the github server.
# see the link above for more fields in the response.
def callback(data: dict):
    print(data["user_code"])

github = GitHub(
    OAuthDeviceAuthStrategy(
        "<client_id_here>", callback
    )
)
```

Note that this auth strategy is only for one-time use too. You need to store the user access token and refresh token in your database for future use:

```python
from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(
    OAuthDeviceAuthStrategy(
        "<client_id_here>", callback
    )
)

# sync
auth: OAuthTokenAuthStrategy = github.auth.exchange_token(github)
# async
auth: OAuthTokenAuthStrategy = await github.auth.async_exchange_token(github)

access_token = auth.token
refresh_token = auth.refresh_token
```

## GitHub Action Authentication

githubkit provides a built-in auth strategy for GitHub Actions. You can use the `ActionAuthStrategy` to automatically authenticate to the GitHub API.

```python
from githubkit import GitHub, ActionAuthStrategy

github = GitHub(ActionAuthStrategy())
```

and add input or env to the action step:

```yaml
- name: Some step use githubkit
  with:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

- name: Some step use githubkit
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Switch between AuthStrategy

You can change the auth strategy and get a new client simplely using `with_auth`.

Switch from GitHub App to a specific installation:

```python
from githubkit import GitHub, AppAuthStrategy

github = GitHub(AppAuthStrategy("<app_id>", "<private_key>"))
installation_github = github.with_auth(
    github.auth.as_installation(installation_id)
)
```

Switch from GitHub App to an OAuth App:

```python
from githubkit import GitHub, AppAuthStrategy, OAuthAppAuthStrategy

github = GitHub(
    AppAuthStrategy(
        "<app_id>", "<private_key>", "<client_id>", "<client_secret>"
    )
)

oauth_github = github.with_auth(github.auth.as_oauth_app())
```

Switch from OAuth App to a web user authorization (OAuth Web Flow):

```python
from githubkit import GitHub, OAuthAppAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))
user_github = github.with_auth(github.auth.as_web_user("<code>"))

# now you can act as the user
resp = user_github.rest.users.get_authenticated()
user = resp.parsed_data

# you can get the user token after you maked a request as user
user_token = user_github.auth.token
user_token_expire_time = user_github.auth.expire_time
refresh_token = user_github.auth.refresh_token
refresh_token_expire_time = user_github.auth.refresh_token_expire_time
```

you can also get the user token directly without making a request (Switch from `OAuthWebAuthStrategy` to `OAuthTokenAuthStrategy`):

```python
from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

auth: OAuthTokenAuthStrategy = github.auth.as_web_user("<code>").exchange_token(github)
# or asynchronously
auth: OAuthTokenAuthStrategy = await github.auth.as_web_user("<code>").async_exchange_token(github)

user_token = auth.token
user_token_expire_time = auth.expire_time
refresh_token = auth.refresh_token
refresh_token_expire_time = auth.refresh_token_expire_time

user_github = github.with_auth(auth)
```

Switch from `OAuthDeviceAuthStrategy` to `OAuthTokenAuthStrategy`:

```python
from githubkit import GitHub, OAuthDeviceAuthStrategy

def callback(data: dict):
    print(data["user_code"])

user_github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

# now you can act as the user
resp = user_github.rest.users.get_authenticated()
user = resp.parsed_data

# you can get the user token after you maked a request as user
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

user_github = github.with_auth(auth)
```
