#!/usr/bin/env bash

set -e

# cd to the root of the project
cd "$(dirname "$0")/.."

python -m codegen && isort . && ruff check --fix --exit-zero . && ruff format .
