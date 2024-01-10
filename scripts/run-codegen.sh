#! /usr/bin/env bash

# cd to the root of the project
cd "$(dirname "$0")/.."

python -m codegen && isort . && black .
