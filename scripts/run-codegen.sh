#!/usr/bin/env bash

set -e

# cd to the root of the project
cd "$(dirname "$0")/.."

python -m codegen && ruff check --select I --fix --exit-zero . && ruff check --fix --exit-zero . && ruff format .
