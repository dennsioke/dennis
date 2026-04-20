#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

OUTPUT_PATH=""
MODE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --output_path) OUTPUT_PATH="$2"; shift 2 ;;
    base|new) MODE="$1"; shift ;;
    *) echo "Usage: $0 [--output_path <path>] <base|new>" >&2; exit 1 ;;
  esac
done

MODE="${MODE:-new}"

export NODE_ENV=tsoa_test

(cd packages/runtime && yarn build)
(cd packages/cli && yarn build)

cd tests

npx ts-node --require=tsconfig-paths/register ./prepare.ts

REPORTER_ARGS=(--reporter=spec)
if [ -n "$OUTPUT_PATH" ]; then
  REPORTER_ARGS=(--reporter=xunit --reporter-option output="$OUTPUT_PATH")
fi

if [ "$MODE" = "base" ]; then
  npx mocha --require=tsconfig-paths/register "${REPORTER_ARGS[@]}" \
    "unit/swagger/schemaDetails3.spec.ts" \
    "unit/swagger/schemaDetails31.spec.ts" \
    --exit --timeout 60000
elif [ "$MODE" = "new" ]; then
  npx mocha --require=tsconfig-paths/register "${REPORTER_ARGS[@]}" \
    "unit/swagger/discriminatedUnion.spec.ts" \
    --exit --timeout 60000
else
  echo "Usage: $0 [--output_path <path>] <base|new>" >&2
  exit 1
fi
