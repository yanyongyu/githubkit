#! /usr/bin/env bash

# config poetry to install env in project
poetry config virtualenvs.in-project true

# setup dev environment
poetry install --all-extras && poetry run pre-commit install

# setup pydantic v2 test environment
(cd envs/pydantic-v2 && poetry install --no-root)
