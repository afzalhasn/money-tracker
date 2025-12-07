#!/usr/bin/env bash
set -euo pipefail

# Run the Phase A regression suite before starting the server.
pytest backend/app/tests/phase_a

exec uvicorn app.main:app --host 0.0.0.0 --port 8000
