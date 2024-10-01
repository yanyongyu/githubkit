<!-- markdownlint-disable MD033 MD041 -->

# GitHubKit {: .hidden }

<div align="center" markdown="1">

[![githubkit](https://socialify.git.ci/yanyongyu/githubkit/image?description=1&descriptionEditable=%E2%9C%A8%20GitHub%20SDK%20for%20Python%20%E2%9C%A8&font=Bitter&language=1&pattern=Circuit%20Board&theme=Light)](https://github.com/yanyongyu/githubkit)

<p>
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

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD036 -->

_✨ The modern, all-batteries-included GitHub SDK for Python ✨_

_✨ Support both **sync** and **async** calls, **fully typed** ✨_

_✨ Always up to date, like octokit ✨_

<!-- markdownlint-restore -->

</div>

GitHubKit aims to be an easy-to-use, fully typed, and always up-to-date GitHub SDK for Python. It is inspired by [octokit](https://github.com/octokit).

GitHubKit provides several features including:

- 👤 Multiple authentication ways and OAuth flow support
- 🌐 Calling REST API and GraphQL easily
- 🏷️ REST API versioning, including GHEC
- ↻ Built-in pagination support
- 🤓 Optional data validation with [pydantic](https://docs.pydantic.dev/latest/), for both Webhook events and REST API responses
- 🚨 Built-in http cache (powered by [Hishel](https://hishel.com/) for HTTPX) and auto retry
- 📦 Fully typed APIs

## Version Changes

GitHubKit is currently not stable and may have breaking changes in the future. GitHubKit uses the **minor** version number for breaking changes and the **patch** version number for bug fixes or enhancements.

Note that GitHubKit uses [GitHub's official openapi schema](https://github.com/github/rest-api-description) to generate apis and models. This aims to keep the APIs and models up-to-date. You may occasionally encounter **breaking changes** like model names or model field types changing when upgrading githubkit. This is due to **upstream github schema changes** and githubkit can not control this.

!!! warning

    githubkit recommends using a python dependency manager (like poetry / pdm / uv) to lock the version of githubkit to avoid unexpected changes.
