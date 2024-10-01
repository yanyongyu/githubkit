# Develop an OAuth APP (GitHub APP) with device flow

## Sync Example

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

## Async Example

```python
from githubkit import GitHub, OAuthDeviceAuthStrategy, OAuthTokenAuthStrategy

# sync/async func for displaying user code to user
async def callback(data: dict):
    print(data["user_code"])

user_github = GitHub(OAuthDeviceAuthStrategy("<client_id>", callback))

# if you want to store the user token in a database
auth: OAuthTokenAuthStrategy = await user_github.auth.async_exchange_token(user_github)
access_token = auth.token
refresh_token = auth.refresh_token
# restore the user token from database
user_github = user_github.with_auth(
    OAuthTokenAuthStrategy(
        "<client_id>", None, refresh_token=refresh_token
    )
)
```
