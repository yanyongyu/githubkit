#!/usr/bin/env bash

echo "Start running"

if env GITHUBKIT_LAZY_DISABLE_FLAG=1 python -c "import githubkit"; then
    echo "✅ Test passed: Successfully imported githubkit"
    exit 0
else
    echo "❌ Test failed: Failed to import githubkit"
    exit 1
fi
