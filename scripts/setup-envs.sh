#!/usr/bin/env bash

set -e

# setup dev environment
echo "Setting up dev environment"
uv sync --all-extras && uv run pre-commit install
