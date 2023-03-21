<!-- markdownlint-disable MD033 MD041 -->
<div align="center">

[![githubkit](https://socialify.git.ci/yanyongyu/githubkit/image?description=1&descriptionEditable=%E2%9C%A8%20GitHub%20SDK%20for%20Python%20%E2%9C%A8&font=Bitter&language=1&pattern=Circuit%20Board&theme=Light)](https://github.com/yanyongyu/githubkit)

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/yanyongyu/githubkit/master/LICENSE">
    <img src="https://img.shields.io/github/license/yanyongyu/githubkit" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/githubkit">
    <img src="https://img.shields.io/pypi/v/githubkit" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue" alt="python">
  <a href="https://results.pre-commit.ci/latest/github/yanyongyu/githubkit/master">
    <img src="https://results.pre-commit.ci/badge/github/yanyongyu/githubkit/master.svg" alt="pre-commit" />
  </a>
</p>

<div align="center">

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD036 -->

_✨ The modern, all-batteries-included GitHub SDK for Python ✨_

_✨ Support both **sync** and **async** calls, **fully typed** ✨_

_✨ Always up to date, like octokit ✨_

<!-- markdownlint-restore -->

</div>

## Installation

```bash
pip install githubkit
# or, use poetry
poetry add githubkit
# or, use pdm
pdm add githubkit
```

if you want to auth as github app, extra dependencies are required:

```bash
pip install githubkit[auth-app]
# or, use poetry
poetry add githubkit[auth-app]
# or, use pdm
pdm add githubkit[auth-app]
```

if you want to mix sync and async calls in oauth device callback, extra dependencies are required:

```bash
pip install githubkit[auth-oauth-device]
# or, use poetry
poetry add githubkit[auth-oauth-device]
# or, use pdm
pdm add githubkit[auth-oauth-device]
```

## Usage

### Authentication

Initialize a github client with no authentication:

```python
from githubkit import GitHub, UnauthAuthStrategy

github = GitHub()
# or, use UnauthAuthStrategy
github = GitHub(UnauthAuthStrategy())
```

or using PAT (Token):

```python
from githubkit import GitHub, TokenAuthStrategy

github = GitHub("<your_token_here>")
# or, use TokenAuthStrategy
github = GitHub(TokenAuthStrategy("<your_token_here>"))
```

or using GitHub APP authentication:

```python
from githubkit import GitHub, AppAuthStrategy

github = GitHub(
    AppAuthStrategy(
        "<app_id>", "<private_key>", "<optional_client_id>", "<optional_client_secret>"
    )
)
```

or using GitHub APP Installation authentication:

```python
from githubkit import GitHub, AppInstallationAuthStrategy

github = GitHub(
    AppInstallationAuthStrategy(
        "<app_id>", "<private_key>", installation_id, "<optional_client_id>", "<optional_client_secret>",
    )
)
```

or using OAuth APP authentication:

```python
from githubkit import GitHub, OAuthAppAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id_here>", "<client_secret_here>"))
```

or using GitHub APP / OAuth APP web flow authentication:

```python
from githubkit import GitHub, OAuthWebAuthStrategy

github = GitHub(
    OAuthWebAuthStrategy(
        "<client_id_here>", "<client_secret_here>", "<web_flow_exchange_code_here>"
    )
)
```

or using GitHub Action authentication:

```python
from githubkit import GitHub, ActionAuthStrategy

github = GitHub(ActionAuthStrategy())
```

### Calling Rest API

> APIs are fully typed. Typing in the following examples is just for reference only.

Simple sync call:

```python
from githubkit import Response
from githubkit.rest import FullRepository

resp: Response[FullRepository] = github.rest.repos.get(owner="owner", repo="repo")
repo: FullRepository = resp.parsed_data
```

Simple async call:

```python
from githubkit import Response
from githubkit.rest import FullRepository

resp: Response[FullRepository] = await github.rest.repos.async_get(owner="owner", repo="repo")
repo: FullRepository = resp.parsed_data
```

Call API with context (reusing client):

```python
from githubkit import Response
from githubkit.rest import FullRepository

with GitHub("<your_token_here>") as github:
    resp: Response[FullRepository] = github.rest.repos.get(owner="owner", repo="repo")
    repo: FullRepository = resp.parsed_data
```

```python
from githubkit import Response
from githubkit.rest import FullRepository

async with GitHub("<your_token_here>") as github:
    resp: Response[FullRepository] = await github.rest.repos.async_get(owner="owner", repo="repo")
    repo: FullRepository = resp.parsed_data
```

### Pagination

Pagination type checking is also supported:

> Typing is tested with Pylance (Pyright).

```python
from githubkit.rest import Issue

for issue in github.paginate(
    github.rest.issues.list_for_repo, owner="owner", repo="repo", state="open"
):
    issue: Issue
    print(issue.number)
```

```python
from githubkit.rest import Issue

async for issue in github.paginate(
    github.rest.issues.async_list_for_repo, owner="owner", repo="repo", state="open"
):
    issue: Issue
    print(issue.number)
```

complex pagination with custom map function (some api returns data in a nested field):

```python
async for accessible_repo in github.paginate(
    github.rest.apps.async_list_installation_repos_for_authenticated_user,
    map_func=lambda r: r.parsed_data.repositories,
    installation_id=1,
):
    accessible_repo: Repository
    print(accessible_repo.full_name)
```

### Calling GraphQL API

Simple sync call:

```python
data: Dict[str, Any] = github.graphql(query, variables={"foo": "bar"})
```

Simple async call:

```python
data: Dict[str, Any] = github.async_graphql(query, variables={"foo": "bar"})
```

### Webhook Verification

Simple webhook payload verification:

```python
from githubkit.webhooks import verify

valid: bool = verify(secret, request.body, request.headers["X-Hub-Signature-256"])
```

Sign the webhook payload manually:

```python
from githubkit.webhooks import sign

signature: str = sign(secret, payload, method="sha256")
```

### Webhook Parsing

Parse the payload with event name:

```python
from githubkit.webhooks import parse, WebhookEvent

event: WebhookEvent = parse(request.headers["X-GitHub-Event"], request.body)
```

Parse the payload without event name (may cost longer time):

```python
from githubkit.webhooks import parse_without_name, WebhookEvent

event: WebhookEvent = parse_without_name(request.body)
```

Parse dict like payload:

```python
from githubkit.webhooks import parse_obj, parse_obj_without_name, WebhookEvent

event: WebhookEvent = parse_obj(request.headers["X-GitHub-Event"], request.json())
event: WebhookEvent = parse_obj_without_name(request.json())
```

### Switch between AuthStrategy

You can change the auth strategy and get a new client simplely using `with_auth`.

Change from `AppAuthStrategy` to `AppInstallationAuthStrategy`:

```python
from githubkit import GitHub, AppAuthStrategy

github = GitHub(AppAuthStrategy("<app_id>", "<private_key>"))
installation_github = github.with_auth(
    github.auth.as_installation(installation_id)
)
```

Change from `OAuthAppAuthStrategy` to `OAuthWebAuthStrategy`:

```python
from githubkit import GitHub, OAuthAppAuthStrategy

github = GitHub(OAuthAppAuthStrategy("<client_id>", "<client_secret>"))
user_github = github.with_auth(github.auth.as_web_user("<code>"))
```

## Development

Open in Codespaces (Dev Container):

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=master&repo=512138996)

Generate latest models and apis:

```bash
python -m codegen && isort . && black .
```
