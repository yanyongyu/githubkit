<!-- markdownlint-disable MD046 -->

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

!!! warning

    This may use about **400M** memory and take a long time.

Please make sure you have activated the virtual environment.

```bash
./scripts/run-codegen.sh
```

### Patch Schema

If you encounter an schema error, you can patch the schema by modifying the `pyproject.toml` file.

In the `[tool.codegen.overrides.schema_overrides]` section, you can modify the schema using json pointer. The value will override the original schema. Specially, if the value is `<unset>`, the original one will be removed.

Please add a comment to explain the reason for the patch if you want to submit a PR.

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
