# Installation

```bash
pip install githubkit
# or, use poetry
poetry add githubkit
# or, use pdm
pdm add githubkit
# or, use uv
uv add githubkit
```

if you want to auth as github app, extra dependencies are required:

```bash
pip install githubkit[auth-app]
# or, use poetry
poetry add githubkit[auth-app]
# or, use pdm
pdm add githubkit[auth-app]
# or, use uv
uv add githubkit[auth-app]
```

if you want to mix sync and async calls in oauth device callback, extra dependencies are required:

```bash
pip install githubkit[auth-oauth-device]
# or, use poetry
poetry add githubkit[auth-oauth-device]
# or, use pdm
pdm add githubkit[auth-oauth-device]
# or, use uv
uv add githubkit[auth-oauth-device]
```

githubkit supports **both pydantic v1 and v2**, but pydantic v2 is recommended. If you have encountered any problems with pydantic v1/v2, please file an issue.

> [!WARNING]
> githubkit uses [GitHub's official openapi schema](https://github.com/github/rest-api-description) to generate apis and models.
> You may occasionally encounter **breaking changes** like model names or model field types changing when upgrading githubkit.
> This is due to **upstream schema changes** and githubkit can not control this.
>
> githubkit recommends using a python dependency manager (like poetry / pdm / uv) to lock the version of githubkit to avoid unexpected changes.
