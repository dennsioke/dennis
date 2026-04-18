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
      echo "Usage: $0 [--output_path <path>] <base|new>" >&2
      exit 1
      ;;
  esac
done

MODE="${MODE:-new}"

REPORTER_ARGS=("--reporter=verbose")
if [ -n "$OUTPUT_PATH" ]; then
  REPORTER_ARGS+=("--reporter=junit" "--outputFile.junit=$OUTPUT_PATH")
fi

if [ "$MODE" = "base" ]; then
  node_modules/.bin/vitest run --config vitest.base.config.ts "${REPORTER_ARGS[@]}"
elif [ "$MODE" = "new" ]; then
  node_modules/.bin/vitest run --config vitest.cancel.config.ts "${REPORTER_ARGS[@]}"
else
  echo "Usage: $0 [--output_path <path>] <base|new>" >&2
  exit 1
fi
