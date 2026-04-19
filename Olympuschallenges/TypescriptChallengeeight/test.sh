#!/usr/bin/env bash
set -euo pipefail

OUTPUT_PATH=""
MODE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --output_path)
      OUTPUT_PATH="$2"
      shift 2
      ;;
    base|new)
      MODE="$1"
      shift
      ;;
    *)
      echo "Usage: $0 --output_path <path> [base|new]" >&2
      exit 1
      ;;
  esac
done

if [ -z "$MODE" ]; then
  echo "Usage: $0 --output_path <path> [base|new]" >&2
  exit 1
fi

REPORTER_ARGS=()
if [ -n "$OUTPUT_PATH" ]; then
  REPORTER_ARGS=(--reporter=junit --outputFile="$OUTPUT_PATH")
fi

if [ "$MODE" = "base" ]; then
  npx vitest run --exclude 'tests/prefix-items-tuples.test.ts' "${REPORTER_ARGS[@]}"
elif [ "$MODE" = "new" ]; then
  npx vitest run tests/prefix-items-tuples.test.ts "${REPORTER_ARGS[@]}"
fi
