#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${SCRIPT_DIR}/.venv/bin/python"
if [ ! -x "$PYTHON_BIN" ]; then
    PYTHON_BIN="$(command -v python3 || command -v python)"
fi

accumulation_script_path="${SCRIPT_DIR}/comparative_plots/bandwidth_comparison_plot_folder/accumulation_script.py"
plot_script_path="${SCRIPT_DIR}/comparative_plots/bandwidth_comparison_plot_folder/plot_script.py"

"$PYTHON_BIN" "$accumulation_script_path"
"$PYTHON_BIN" "$plot_script_path"
