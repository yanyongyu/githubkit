# Installation

!!! tip

    githubkit supports **both pydantic v1 and v2**, but pydantic v2 is recommended. If you have encountered any problems with pydantic v1/v2, please file an issue.

## Basic Installation

=== "poetry"

    ```bash
    poetry add githubkit
    ```

=== "pdm"

    ```bash
    pdm add githubkit
    ```

=== "uv"

    ```bash
    uv add githubkit
    ```

=== "pip"

    ```bash
    pip install githubkit
    ```

## GitHub Schema Versions Installation

githubkit provides versioned REST API definitions and models through the `githubkit-schemas` ecosystem.

By default, installing `githubkit` (or `githubkit-schemas`) gives you the latest stable schema version.

!!! note "Calendar versioning"

    `githubkit-schemas` and its versioned packages follow [Calendar Versioning (CalVer)](https://calver.org/) in the format `YY.MM.PATCH` (e.g. `26.5.12`). Releases are issued whenever GitHub updates its API schemas, so the package version reflects when the schema was published rather than a semantic API stability guarantee.

### Pin Schema Versions

By default, `githubkit-schemas` always points to the latest stable schema, so a fresh install may pull in a newer schema than expected. Explicitly pinning the package ensures every environment uses the same schema version:

=== "poetry"

    ```bash
    poetry add 'githubkit-schemas==26.5.12'
    ```

=== "pdm"

    ```bash
    pdm add 'githubkit-schemas==26.5.12'
    ```

=== "uv"

    ```bash
    uv add 'githubkit-schemas==26.5.12'
    ```

=== "pip"

    ```bash
    pip install 'githubkit-schemas==26.5.12'
    ```

### Install Extra Schema Versions

If you need an additional schema module, install the corresponding extra on `githubkit-schemas`.

- `githubkit-schemas` tracks the latest stable schema.
- `githubkit-schemas-<version>` is a concrete, version-specific package.
- `githubkit-schemas[<version>]` is a convenience extra that installs the matching `githubkit-schemas-<version>` package.

For example, to pin schema version `2022-11-28`:

=== "poetry"

    ```bash
    poetry add 'githubkit-schemas[2022-11-28]'
    ```

=== "pdm"

    ```bash
    pdm add 'githubkit-schemas[2022-11-28]'
    ```

=== "uv"

    ```bash
    uv add 'githubkit-schemas[2022-11-28]'
    ```

=== "pip"

    ```bash
    pip install 'githubkit-schemas[2022-11-28]'
    ```

For GitHub Enterprise Cloud/Server compatibility schemas, use versions like `ghec-2022-11-28` in the same format.

After installation, select the schema in code with `github.rest("<schema-version>")`. See [REST API Versioning](usage/rest-api.md#rest-api-versioning).

## Extra Dependencies

If you want to auth as github app, you should install `auth-app` extra dependencies:

=== "poetry"

    ```bash
    poetry add 'githubkit[auth-app]'
    ```

=== "pdm"

    ```bash
    pdm add 'githubkit[auth-app]'
    ```

=== "uv"

    ```bash
    uv add 'githubkit[auth-app]'
    ```

=== "pip"

    ```bash
    pip install 'githubkit[auth-app]'
    ```

## Full Installation

You can install fully featured githubkit with `all` extra dependencies:

=== "poetry"

    ```bash
    poetry add 'githubkit[all]'
    ```

=== "pdm"

    ```bash
    pdm add 'githubkit[all]'
    ```

=== "uv"

    ```bash
    uv add 'githubkit[all]'
    ```

=== "pip"

    ```bash
    pip install 'githubkit[all]'
    ```
