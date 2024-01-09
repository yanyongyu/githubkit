#! /usr/bin/env bash

# cd to the root of the project
cd "$(dirname "$0")/.."

# Run the tests
pytest -n auto --cov-report xml tests
