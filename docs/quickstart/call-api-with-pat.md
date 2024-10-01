# Use Personal Access Token (PAT) to Call GitHub API

First, you need to create a PAT at [GitHub Personal Access Token](https://github.com/settings/personal-access-tokens/new). Then, copy the token and replace `<your_token_here>` in the following code.

## Sync Example

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

## Async Example

```python
from githubkit import GitHub
from githubkit.versions.latest.models import PublicUser, PrivateUser

github = GitHub("<your_token_here>")

# call GitHub rest api
resp = await github.rest.users.async_get_authenticated()
user: PublicUser | PrivateUser = resp.parsed_data

# call GitHub graphql api
data: dict = await github.async_graphql("{ viewer { login } }")
```
