#!/usr/bin/env sh
# Linux / macOS launcher: finds a Python interpreter and hands over to start.py,
# which checks the virtual environment, installs what is missing and starts
# the simulation or the computer.   Try:  ./start.sh help
cd "$(dirname "$0")" || exit 1

for candidate in "$PYTHON" python3 python; do
    [ -n "$candidate" ] || continue
    if command -v "$candidate" >/dev/null 2>&1; then
        exec "$candidate" start.py "$@"
    fi
done

echo "[start] error: no Python interpreter found on the PATH." >&2
echo "        Install Python 3.10 or newer (https://www.python.org, or your package manager:" >&2
echo "        apt install python3 python3-venv / dnf install python3 / brew install python)." >&2
exit 1
