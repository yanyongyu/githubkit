<!-- markdownlint-disable MD033 MD041 -->
<div align="center">

[![githubkit](https://socialify.git.ci/yanyongyu/githubkit/image?description=1&descriptionEditable=%E2%9C%A8%20GitHub%20SDK%20for%20Python%20%E2%9C%A8&font=Bitter&language=1&pattern=Circuit%20Board&theme=Light)](https://github.com/yanyongyu/githubkit)

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/yanyongyu/githubkit/master/LICENSE">
    <img src="https://img.shields.io/github/license/yanyongyu/githubkit" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/githubkit">
    <img src="https://img.shields.io/pypi/v/githubkit?logo=python&logoColor=edb641" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue?logo=python&logoColor=edb641" alt="python">
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&logoColor=edb641" alt="black">
  </a>
  <a href="https://github.com/Microsoft/pyright">
    <img src="https://img.shields.io/badge/types-pyright-797952.svg?logo=python&logoColor=edb641" alt="pyright">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json" alt="ruff">
  </a>
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

githubkit supports **both pydantic v1 and v2**, but pydantic v2 is recommended. If you have encountered any problems with pydantic v1/v2, please file an issue.

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

and add env or input to the step:

```yaml
- name: Some step use githubkit
  with:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

- name: Some step use githubkit
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Config

githubkit is highly configurable, you can change the default config by passing config options to `GitHub`:

```python
from githubkit import GitHub

github = GitHub(
    base_url="https://api.github.com/",
    accept_format="full+json",
    previews=["starfox"],
    user_agent="GitHubKit/Python",
    follow_redirects=True,
    timeout=None,
    http_cache=True,
    auto_retry=True,
)
```

The `accept_format` and `previews` are used to set the default `Accept` header, you can find more details in [GitHub API docs](https://docs.github.com/en/rest/overview/media-types).

The `http_cache` option enables the http caching feature powered by [Hishel](https://hishel.com/) for HTTPX. GitHub API limits the number of requests that you can make within a specific amount of time. This feature is useful to reduce the number of requests to GitHub API and avoid hitting the rate limit.

The `auto_retry` option enables request retrying when rate limit exceeded and server error encountered. See [Auto Retry](#auto-retry) for more infomation.

### Calling Rest API

> APIs are fully typed. Typing in the following examples is just for reference only.

Simple sync call:

```python
from githubkit import Response
from githubkit.versions.latest.models import FullRepository

resp: Response[FullRepository] = github.rest.repos.get(owner="owner", repo="repo")
repo: FullRepository = resp.parsed_data
```

Simple async call:

```python
from githubkit import Response
from githubkit.versions.latest.models import FullRepository

resp: Response[FullRepository] = await github.rest.repos.async_get(owner="owner", repo="repo")
repo: FullRepository = resp.parsed_data
```

Call API with context (reusing client):

```python
from githubkit import Response
from githubkit.versions.latest.models import FullRepository

with GitHub("<your_token_here>") as github:
    resp: Response[FullRepository] = github.rest.repos.get(owner="owner", repo="repo")
    repo: FullRepository = resp.parsed_data
```

```python
from githubkit import Response
from githubkit.versions.latest.models import FullRepository

async with GitHub("<your_token_here>") as github:
    resp: Response[FullRepository] = await github.rest.repos.async_get(owner="owner", repo="repo")
    repo: FullRepository = resp.parsed_data
```

### Data Validation

As shown above, the response data is parsed and validated by accessing the `response.parsed_data` property. This ensures that the data type returned by the API is as expected and your code is safe to use it (with static type checking). But sometimes you may want to get the raw data returned by the API, such as when the schema is not correct. You can use the `response.text` property or `response.json()` method to get the raw data:

```python
from typing import Any, Dict
from githubkit import Response

resp: Response[FullRepository] = github.rest.repos.get(owner="owner", repo="repo")
repo: Dict[str, Any] = resp.json()
```

### Rest API Versioning

> APIs are fully typed. Different versions of APIs are typed separately.

githubkit supports all versions of GitHub API, you can switch between versions as follows:

```python
github.rest("2022-11-28").repos.get(owner="owner", repo="repo")
```

The models of versions can be imported from `githubkit.versions.<version>.models`, for example:

```python
from githubkit.versions.v2022_11_28.models import FullRepository
```

Specially, the `latest` version is always linked to the latest version of GitHub API:

```python
from githubkit.versions.latest.models import FullRepository
```

> [!NOTE]
> For backward compatibility, the `githubkit.rest` module is linked to the models of `latest` version by default.
>
> ```python
> from githubkit.rest import FullRepository
> ```

You can also get the latest version name of GitHub API and all versions mapping of GitHub API:

```python
from githubkit.versions import LATEST_VERSION, VERSIONS
```

Current supported versions are: (you can find it in the section `[[tool.codegen.descriptions]]` of the `pyproject.toml` file)

- 2022-11-28 (latest)
- ghec-2022-11-28

### Pagination

Pagination type checking is also supported:

> Typing is tested with Pylance (Pyright).

```python
from githubkit.versions.latest.models import Issue

for issue in github.paginate(
    github.rest.issues.list_for_repo, owner="owner", repo="repo", state="open"
):
    issue: Issue
    print(issue.number)
```

```python
from githubkit.versions.latest.models import Issue

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
data: Dict[str, Any] = await github.async_graphql(query, variables={"foo": "bar"})
```

### Auto Retry

By default, githubkit will retry the request when specific exception encountered. When rate limit exceeded, githubkit will retry once after GitHub suggested waiting time. When server error encountered (http status >= 500), githubkit will retry max three times.

You can disable this feature by set the `auto_retry` config to `False`:

```python
github = GitHub(
    ...
    auto_retry=False
)
```

You can also customize the retry decision function by passing a callable:

```python
from datetime import timedelta

from githubkit.retry import RetryOption
from githubkit.exception import GitHubException

def retry_decision_func(exc: GitHubException, retry_count: int) -> RetryOption:
    if retry_count < 1:
        return RetryOption(True, timedelta(seconds=60))
    return RetryOption(False)

github = GitHub(
    ...
    auto_retry=retry_decision_func
)
```

githubkit also provides some builtin retry decision function:

1. Retry when rate limit exceeded:

   ```python
   from githubkit.retry import RETRY_RATE_LIMIT, RetryRateLimit

   # default
   github = GitHub(
      ...
      auto_retry=RETRY_RATE_LIMIT
   )
   # or, custom max retry count
   github = GitHub(
      ...
      auto_retry=RetryRateLimit(max_retry=1)
   )
   ```

2. Retry when server error encountered:

   ```python
   from githubkit.retry import RETRY_SERVER_ERROR, RetryServerError

   # default
   github = GitHub(
      ...
      auto_retry=RETRY_SERVER_ERROR
   )
   # or, custom max retry count
   github = GitHub(
      ...
      auto_retry=RetryServerError(max_retry=1)
   )
   ```

3. Chain retry decision functions:

   ```python
   from githubkit.retry import RETRY_RATE_LIMIT, RETRY_SERVER_ERROR, RetryChainDecision

   github = GitHub(
      ...
      auto_retry=RetryChainDecision(RETRY_RATE_LIMIT, RETRY_SERVER_ERROR)
   )
   ```

### Webhook Verification

> `githubkit.webhooks` module contains some shortcut functions to help you verify and parse webhook payload.

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

> `githubkit.webhooks` module contains some shortcut functions to help you verify and parse webhook payload.

Parse the payload with event name:

```python
from githubkit.webhooks import parse

event = parse(request.headers["X-GitHub-Event"], request.body)
```

(**NOT RECOMMENDED**) Parse the payload without event name (may cost longer time and more memory):

```python
from githubkit.webhooks import parse_without_name

event = parse_without_name(request.body)
```

> [!WARNING]
> The `parse_without_name` function will try to parse the payload with all supported event names.  
> The behavior of this function is not the same between pydantic v1 and v2.  
> When using pydantic v1, the function will return the first valid event model (known as `left-to-right` mode).  
> When using pydantic v2, the function will return the highest scored valid event model (known as `smart` mode).  
> See: [Union Modes](https://docs.pydantic.dev/latest/concepts/unions/#union-modes).

Parse dict like payload:

```python
from githubkit.webhooks import parse_obj, parse_obj_without_name

event = parse_obj(request.headers["X-GitHub-Event"], request.json())
event = parse_obj_without_name(request.json())  # NOT RECOMMENDED
```

The `parse` and `parse_obj` function supports type overload, if you provide static value for the `event_name` parameter, the return type will be inferred automatically.

Webhook also supports versioning, you can switch between versions as follows:

```python
from githubkit import GitHub

event = GitHub.webhooks("2022-11-28").parse(request.headers["X-GitHub-Event"], request.body)
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

> [!WARNING]
> This may use about **400M** memory and take a long time.

```bash
./scripts/run-codegen.sh
```

Run tests in dev env:

```bash
./scripts/run-tests.sh
```

Run tests in test envs, for example:

```bash
cd ./envs/pydantic-v2/
poetry run bash ../../scripts/run-tests.sh
```

## Contributors

Thanks to the following people who have contributed to this project:

<a href="https://github.com/yanyongyu/githubkit/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yanyongyu/githubkit&max=1000" alt="contributors" />
</a>
