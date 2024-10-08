<!-- markdownlint-disable MD041 -->
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

<p align="center">
  <a href="https://yanyongyu.github.io/githubkit/"><b>Documentation</b></a> |
  <a href="https://github.com/yanyongyu/githubkit/issues"><b>Report Bug</b></a> |
  <a href="https://docs.github.com/"><b>GitHub Docs</b></a>
</p>

githubkit aims to be an easy-to-use, fully typed, and always up-to-date GitHub SDK for Python. It is inspired by [octokit](https://github.com/octokit).

githubkit provides several features including:

- Support both sync and async calls
- Multiple authentication ways and OAuth flow support
- Calling REST API and GraphQL easily
- REST API versioning, including GHEC
- Built-in pagination support
- Optional data validation with [Pydantic](https://docs.pydantic.dev/latest/), for both webhook events and REST API responses
- Built-in http cache (powered by [Hishel](https://hishel.com/) for HTTPX) and auto retry
- Lazy loading of APIs and models
- Fully typed APIs

## Getting Started

For more, see the [documentation](https://yanyongyu.github.io/githubkit).

### Installation

Install githubkit with the package manager of your choice:

```bash
pip install githubkit
# or, use poetry
poetry add githubkit
# or, use pdm
pdm add githubkit
# or, use uv
uv add githubkit
```

### Usage

Create a [Personal Access Token (PAT)](https://github.com/settings/personal-access-tokens/new) and use it to create a `GitHub` instance:

```python
from githubkit import GitHub

github = GitHub("<your_token_here>")
```

Then, enjoy githubkit now!

```python
from githubkit import Response
from githubkit.versions.latest.models import FullRepository

resp: Response[FullRepository] = github.rest.repos.get("owner", "repo")
repo: FullRepository = resp.parsed_data
print(repo.full_name)
```

## Development

See the [development](https://yanyongyu.github.io/githubkit/contributing/) in the contributing guide.

## Contributors

Thanks to the following people who have contributed to this project:

<a href="https://github.com/yanyongyu/githubkit/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yanyongyu/githubkit&max=1000" alt="contributors" />
</a>
