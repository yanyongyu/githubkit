# Contributing

We welcome contributions to the project. Thank you in advance for your contribution to githubkit!

## Development Environment

Open in Codespaces (Dev Container):

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=master&repo=512138996)

Local development environment setup:

Make sure you have installed [Poetry](https://python-poetry.org/).

```bash
poetry install --all-extras --with docs && poetry run pre-commit install
```

Test environment setup (optional):

```bash
for env in $(find ./envs/ -maxdepth 1 -mindepth 1 -type d -not -name test); do
  echo "Setting up $env environment"
  (cd $env && poetry install --no-root)
done
```

## GitHub Schema Update

Generate latest models and apis from GitHub's OpenAPI schema:

<!-- markdownlint-disable MD046 -->

!!! warning

    This may use about **400M** memory and take a long time.

<!-- markdownlint-enable MD046 -->

Please make sure you have activated the virtual environment.

```bash
./scripts/run-codegen.sh
```

## Testing

Run tests in dev env:

```bash
./scripts/run-tests.sh
```

Run tests in specific test env, for example:

```bash
cd ./envs/pydantic-v2/
poetry run bash ../../scripts/run-tests.sh
```
