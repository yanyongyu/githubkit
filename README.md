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

## Usage

### Initialization

Initialize a github client using PAT (Token):

```python
from githubkit import GitHub, TokenAuthStrategy

github = GitHub("<your_token_here>")
# or, use TokenAuthStrategy
github = GitHub(TokenAuthStrategy("<your_token_here>"))
```

or using basic authentication:

```python
from githubkit import GitHub, BasicAuthStrategy

github = GitHub(BasicAuthStrategy("<client_id_here>", "<client_secret_here>"))
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

# with GitHub("<your_token_here>") as github:
with github:
    resp: Response[FullRepository] = github.rest.repos.get(owner="owner", repo="repo")
    repo: FullRepository = resp.parsed_data
```

```python
from githubkit import Response
from githubkit.rest import FullRepository

# async with GitHub("<your_token_here>") as github:
async with github:
    resp: Response[FullRepository] = await github.rest.repos.async_get(owner="owner", repo="repo")
    repo: FullRepository = resp.parsed_data
```

### Pagination

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
