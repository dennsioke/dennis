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

if [ -n "$OUTPUT_PATH" ]; then
  mkdir -p "$(dirname "$OUTPUT_PATH")"
  OUTPUT_PATH="$(cd "$(dirname "$OUTPUT_PATH")" && pwd)/$(basename "$OUTPUT_PATH")"
fi

export NODE_ENV=tsoa_test

(cd packages/runtime && yarn build)
(cd packages/cli && yarn build)

cd tests

npx ts-node --require=tsconfig-paths/register ./prepare.ts

REPORTER_ARGS=(--reporter=spec)
if [ -n "$OUTPUT_PATH" ]; then
  REPORTER_ARGS=(--reporter=xunit --reporter-option output="$OUTPUT_PATH")
fi

MOCHA_EXIT=0
if [ "$MODE" = "base" ]; then
  npx mocha --require=tsconfig-paths/register "${REPORTER_ARGS[@]}" \
    "unit/swagger/schemaDetails3.spec.ts" \
    "unit/swagger/schemaDetails31.spec.ts" \
    --exit --timeout 60000 || MOCHA_EXIT=$?
elif [ "$MODE" = "new" ]; then
  npx mocha --require=tsconfig-paths/register "${REPORTER_ARGS[@]}" \
    "unit/swagger/discriminatedUnion.spec.ts" \
    --exit --timeout 60000 || MOCHA_EXIT=$?
else
  echo "Usage: $0 [--output_path <path>] <base|new>" >&2
  exit 1
fi

exit $MOCHA_EXIT
