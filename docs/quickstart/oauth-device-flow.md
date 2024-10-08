# Develop an OAuth APP (GitHub APP) with device flow

OAuth device flow also allows you to authenticate as a user and act on behalf of the user. It is suitable for headless application like CLI tools.

To authenticate as a user, you need to display a `user_code` to the user and ask the user to visit the [GitHub OAuth Device Verification Page](https://github.com/login/device) to enter the code. After the user authorizes your app, the client application will get the user token.

Note that the `user_code` is **one-time use** and only valid for a short period of time. If you want to auth as the user later again, you need to store the user token in a database.

Like OAuth web flow, you can opt-in / opt-out of the **user-to-server token expiration** feature.

## One-Time Usage

If you just want to temporarily act as the user, you can simply call the API directly with the `OAuthDeviceAuthStrategy` and a callback function.

=== "Sync"

    ```python hl_lines="4-8"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

    # sync/async func for displaying user code to user
    def callback(data: dict):
        print(data["user_code"])

    user_github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

    # now you can act as the user
    resp = user_github.rest.users.get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # you can get the user name and id now
    username = user.login
    user_id = user.id
    ```

=== "Async"

    ```python hl_lines="4-8"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

    # sync/async func for displaying user code to user
    def callback(data: dict):
        print(data["user_code"])

    user_github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

    # now you can act as the user
    resp = await user_github.rest.users.async_get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # you can get the user name and id now
    username = user.login
    user_id = user.id
    ```

## Store token without expiration

If you are developing an OAuth APP or a GitHub APP without user-to-server token expiration, you just need to exchange the `code` for an access token.

=== "Sync"

    ```python hl_lines="10-11 13-15"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

    # sync/async func for displaying user code to user
    def callback(data: dict):
        print(data["user_code"])

    github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

    auth: OAuthTokenAuthStrategy = github.auth.exchange_token(github)  # (1)!
    access_token = auth.token

    user_github = github.with_auth(
        OAuthTokenAuthStrategy("<client_id>", token=access_token)
    )  # (2)!

    # now you can act as the user
    resp = user_github.rest.users.get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # you can get the user name and id now
    username = user.login
    user_id = user.id
    ```

    1. Exchange the user token manually and store the `access_token` in a database.
    2. Restore the user token from database.

=== "Async"

    ```python hl_lines="10-13 15-17"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

    # sync/async func for displaying user code to user
    async def callback(data: dict):
        print(data["user_code"])

    github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

    auth: OAuthTokenAuthStrategy = await github.auth.async_exchange_token(
        github
    )  # (1)!
    access_token = auth.token

    user_github = github.with_auth(
        OAuthTokenAuthStrategy("<client_id>", token=access_token)
    )  # (2)!

    # now you can act as the user
    resp = await user_github.rest.users.async_get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # you can get the user name and id now
    username = user.login
    user_id = user.id
    ```

    1. Exchange the user token manually and store the `access_token` in a database.
    2. Restore the user token from database.

## Store token with expiration

=== "Sync"

    ```python hl_lines="10-11 13-19"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

    # sync/async func for displaying user code to user
    def callback(data: dict):
        print(data["user_code"])

    github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

    auth: OAuthTokenAuthStrategy = github.auth.exchange_token(github)  # (1)!
    refresh_token = auth.refresh_token

    auth = OAuthTokenAuthStrategy(
        "<client_id>", refresh_token=refresh_token
    )  # (2)!
    auth.refresh(github)  # (3)!
    refresh_token = auth.refresh_token

    user_github = github.with_auth(auth)

    # now you can act as the user
    resp = user_github.rest.users.get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # you can get the user name and id now
    username = user.login
    user_id = user.id
    ```

    1. Exchange the user token manually and store the `refresh_token` in a database.
    2. Restore the user refresh token from database and generate a new token.
    3. Refresh the token manually and store the new one.

=== "Async"

    ```python hl_lines="10-13 14-21"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

    # sync/async func for displaying user code to user
    async def callback(data: dict):
        print(data["user_code"])

    github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

    auth: OAuthTokenAuthStrategy = await github.auth.async_exchange_token(
        github
    )  # (1)!
    refresh_token = auth.refresh_token

    auth = OAuthTokenAuthStrategy(
        "<client_id>", refresh_token=refresh_token
    )  # (2)!
    await auth.async_refresh(github)  # (3)!
    refresh_token = auth.refresh_token

    user_github = github.with_auth(auth)

    # now you can act as the user
    resp = user_github.rest.users.get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # you can get the user name and id now
    username = user.login
    user_id = user.id
    ```

    1. Exchange the user token manually and store the `refresh_token` in a database.
    2. Restore the user refresh token from database and generate a new token.
    3. Refresh the token manually and store the new one.
