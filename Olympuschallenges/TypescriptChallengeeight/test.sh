#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-new}"

if [ "$MODE" = "base" ]; then
  npx vitest run --exclude 'tests/prefix-items-tuples.test.ts'
elif [ "$MODE" = "new" ]; then
  npx vitest run tests/prefix-items-tuples.test.ts
else
  echo "Usage: $0 [base|new]" >&2
  exit 1
fi
