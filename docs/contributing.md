# Contributing

We welcome contributions to the project. Thank you in advance for your contribution to githubkit!

## Development Environment

Open in Codespaces (Dev Container):

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=master&repo=512138996)

Local development environment setup:

Make sure you have installed [uv](https://docs.astral.sh/uv/).

```bash
uv sync --all-extras && uv run pre-commit install
```

## GitHub Schema Update

Generate latest models and apis from GitHub's OpenAPI schema:

!!! warning

    This may use about **400M** memory and take a long time.

Please make sure you have activated the virtual environment.

```bash
uv run bash ./scripts/run-codegen.sh
```

### Patch Schema

If you encounter an schema error, you can patch the schema by modifying the `pyproject.toml` file.

In the `[tool.codegen.overrides.schema_overrides]` section, you can modify the schema using json pointer. The value will override the original schema.

Specially, if the json pointer points to a dictionary, you can use special value `<unset>` to remove the key from the dictionary. If the json pointer points to a array, you can use a list value to replace the original array. Or you can use a dict with key `<add>` and `<remove>` to add or remove items from the array.

Please add a comment to explain the reason for the patch if you want to submit a PR.

## Testing

Run tests with pytest:

```bash
env GITHUB_TOKEN='<your token here>' uv run pytest -n auto tests
```

If you want to switch between pydantic v1 and v2, you can use the following command:

```bash
# Pydantic v1
uv sync --all-extras --group pydantic-v1
# Pydantic v2
uv sync --all-extras --group pydantic-v2
```
