#!/usr/bin/env bash

set -e

# config poetry to install env in project
poetry config virtualenvs.in-project true

# setup dev environment
echo "Setting up dev environment"
poetry install --all-extras --with docs && poetry run pre-commit install

# setup pydantic v2 test environment
for env in $(find ./envs/ -maxdepth 1 -mindepth 1 -type d -not -name test); do
  echo "Setting up $env environment"
  (cd $env && poetry install --no-root)
done
