#!/usr/bin/env bash
# Run development server (Unix/macOS). Usage: ./run_dev.sh
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="$SCRIPT_DIR/.venv/bin/python"
if [ ! -x "$PY" ]; then
  PY="python"
fi

export DEBUG=True
export SECRET_KEY="${SECRET_KEY:-dev-secret-key}"

echo "Running migrations..."
"$PY" manage.py migrate

echo "Starting development server (DEBUG=$DEBUG)"
"$PY" manage.py runserver
