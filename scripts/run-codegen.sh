#!/usr/bin/env bash

set -e

# cd to the root of the project
cd "$(dirname "$0")/.."

python -m codegen && ruff check --select I --fix --exit-zero . && ruff check --fix --exit-zero . && ruff format . && ruff check --fix .

NEW_VERSION=$(date +"%y.%-m.%-d")
for package_dir in packages/*/; do
  package=$(basename "$package_dir")
  if [ -f "$package_dir/pyproject.toml" ]; then
    OLD_VERSION=$(uv version --package "$package" --short)
    sed -i "s/$OLD_VERSION/$NEW_VERSION/g" "$package_dir/pyproject.toml"
  fi
done

uv sync --all-extras --all-packages
