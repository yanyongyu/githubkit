#!/usr/bin/env bash

set -e

# cd to the root of the project
cd "$(dirname "$0")/.."

# Run the tests
pytest -n auto --cov-report xml --junitxml=./junit.xml tests
