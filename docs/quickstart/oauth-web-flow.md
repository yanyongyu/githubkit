# Develop an OAuth APP (GitHub APP) with Web Flow

OAuth web flow allows you to authenticate as a user and act on behalf of the user.

To authenticate as a user, you need to redirect the user to the [GitHub OAuth Authorization Page](https://github.com/login/oauth/authorize) with the `client_id` and `redirect_uri` (See [GitHub Docs - Web application flow](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#web-application-flow) for more information). After the user authorizes your app, GitHub will redirect the user back to your `redirect_uri` with a `code`. You can exchange the `code` for an access token.

Note that the `code` is **one-time use** and only valid for a short period of time. If you want to auth as the user later again, you need to store the user token in a database.

If you are developing a GitHub APP, you may opt-in / opt-out of the **user-to-server token expiration** feature. If you opt-in, the user-to-server token will **expire** after a certain period of time, and you need to use the **refresh token** to generate a new token. In this case, you need to do more work to handle the token refresh. See [GitHub Docs - Refreshing user access tokens](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/refreshing-user-access-tokens) for more information.

## One-Time Usage

To use the `code` once, replace `<code>` with the code you get from the callback:

=== "Sync"

    ```python hl_lines="8"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

    github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

    # redirect user to github oauth page and get the code from callback

    user_github = github.with_auth(github.auth.as_web_user("<code>"))

    # now you can act as the user
    resp = user_github.rest.users.get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # you can get the user name and id now
    username = user.login
    user_id = user.id
    ```

=== "Async"

    ```python hl_lines="8"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

    github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

    # redirect user to github oauth page and get the code from callback

    user_github = github.with_auth(github.auth.as_web_user("<code>"))

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

    ```python hl_lines="8-11 13-15"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

    github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

    # redirect user to github oauth page and get the code from callback

    auth: OAuthTokenAuthStrategy = github.auth.as_web_user("<code>").exchange_token(
        github
    )  # (1)!
    access_token = auth.token

    user_github = github.with_auth(
        OAuthTokenAuthStrategy("<client_id>", "<client_secret>", token=access_token)
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

    ```python hl_lines="8-11 13-15"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

    github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

    # redirect user to github oauth page and get the code from callback

    auth: OAuthTokenAuthStrategy = await github.auth.as_web_user(
        "<code>"
    ).async_exchange_token(github)  # (1)!
    access_token = auth.token

    user_github = github.with_auth(
        OAuthTokenAuthStrategy("<client_id>", "<client_secret>", token=access_token)
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

If you are developing a GitHub APP with user-to-server token expiration, you need to handle the token refresh with the `refresh_token`.

=== "Sync"

    ```python hl_lines="8-11 13-19"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

    github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

    # redirect user to github oauth page and get the code from callback

    auth: OAuthTokenAuthStrategy = github.auth.as_web_user("<code>").exchange_token(
        github
    )  # (1)!
    refresh_token = auth.refresh_token

    auth = OAuthTokenAuthStrategy(
        "<client_id>", "<client_secret>", refresh_token=refresh_token
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

    ```python hl_lines="8-11 13-19"
    from githubkit.versions.latest.models import PublicUser, PrivateUser
    from githubkit import GitHub, OAuthAppAuthStrategy, OAuthTokenAuthStrategy

    github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))

    # redirect user to github oauth page and get the code from callback

    auth: OAuthTokenAuthStrategy = await github.auth.as_web_user(
        "<code>"
    ).async_exchange_token(github)  # (1)!
    refresh_token = auth.refresh_token

    auth = OAuthTokenAuthStrategy(
        "<client_id>", "<client_secret>", refresh_token=refresh_token
    )  # (2)!
    await auth.async_refresh(github)  # (3)!
    refresh_token = auth.refresh_token

    user_github = github.with_auth(auth)

    # now you can act as the user
    resp = await user_github.rest.users.async_get_authenticated()
    user: PublicUser | PrivateUser = resp.parsed_data

    # you can get the user name and id now
    username = user.login
    user_id = user.id
    ```

    1. Exchange the user token manually and store the `refresh_token` in a database.
    2. Restore the user refresh token from database and generate a new token.
    3. Refresh the token manually and store the new one.
