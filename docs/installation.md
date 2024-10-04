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

## Extra Dependencies

If you want to auth as github app, you should install `auth-app` extra dependencies:

=== "poetry"

    ```bash
    poetry add githubkit[auth-app]
    ```

=== "pdm"

    ```bash
    pdm add githubkit[auth-app]
    ```

=== "uv"

    ```bash
    uv add githubkit[auth-app]
    ```

=== "pip"

    ```bash
    pip install githubkit[auth-app]
    ```

If you want to mix sync and async calls in oauth device callback, you should install `auth-oauth-device` extra dependencies:

=== "poetry"

    ```bash
    poetry add githubkit[auth-oauth-device]
    ```

=== "pdm"

    ```bash
    pdm add githubkit[auth-oauth-device]
    ```

=== "uv"

    ```bash
    uv add githubkit[auth-oauth-device]
    ```

=== "pip"

    ```bash
    pip install githubkit[auth-oauth-device]
    ```

## Full Installation

You can install fully featured githubkit with `all` extra dependencies:

=== "poetry"

    ```bash
    poetry add githubkit[all]
    ```

=== "pdm"

    ```bash
    pdm add githubkit[all]
    ```

=== "uv"

    ```bash
    uv add githubkit[all]
    ```

=== "pip"

    ```bash
    pip install githubkit[all]
    ```
