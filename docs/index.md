<!-- markdownlint-disable MD033 MD041 -->

# githubkit {: .hidden }

<div align="center" markdown>

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

githubkit aims to be an easy-to-use, fully typed, and always up-to-date GitHub SDK for Python. It is inspired by [octokit](https://github.com/octokit).

githubkit provides several features including:

- :material-multicast: Support both sync and async calls
- :material-account-key: Multiple authentication ways and OAuth flow support
- :material-api: Calling REST API and GraphQL easily
- :material-tag-multiple: REST API versioning, including GHEC
- :material-page-next: Built-in pagination support
- :material-database-check: Optional data validation with [pydantic](https://docs.pydantic.dev/latest/), for both Webhook events and REST API responses
- :material-cached: Built-in http cache (powered by [Hishel](https://hishel.com/) for HTTPX) and auto retry
- :material-lightning-bolt: Lazy loading of APIs and models
- :material-check-circle: Fully typed APIs

## Version Changes

githubkit is currently not stable and may have breaking changes in the future. githubkit uses the **minor** version number for breaking changes and the **patch** version number for bug fixes or enhancements.

Note that githubkit uses [GitHub's official openapi schema](https://github.com/github/rest-api-description) to generate apis and models. This aims to keep the APIs and models up-to-date. You may occasionally encounter **breaking changes** like model names or model field types changing when upgrading githubkit. This is due to **upstream github schema changes** and githubkit can not control this.

!!! warning

    githubkit recommends using a python dependency manager (like poetry / pdm / uv) to lock the version of githubkit to avoid unexpected changes.

## Reporting Issues

If you encounter any issues or have some questions, please report them on the [GitHub issue tracker](https://github.com/yanyongyu/githubkit/issues).

If you encounter any schema errors, please provide the reproducible code and the raw response data when reporting the issue. Optionally, you can also report the schema error to upstream [GitHub's official openapi schema](https://github.com/github/rest-api-description) repository.
