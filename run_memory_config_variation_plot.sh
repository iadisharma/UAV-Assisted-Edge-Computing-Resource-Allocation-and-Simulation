#!/bin/bash

### NOTE: run main_file.py only when fraction_testing_mode = True
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${SCRIPT_DIR}/.venv/bin/python"
if [ ! -x "$PYTHON_BIN" ]; then
    PYTHON_BIN="$(command -v python3 || command -v python)"
fi

main_file_path="${SCRIPT_DIR}/main_file.py"
store_memory_config_script_path="${SCRIPT_DIR}/comparative_plots/memory_config_fraction/accumulation_script.py"
data_path="${SCRIPT_DIR}/comparative_plots/memory_config_fraction/accumulated_points_dict.json"

i=0
while [ $i -le 10 ];
do
	# set fraction_testing_mode=True in environment
	"$PYTHON_BIN" "$main_file_path"
	echo 
	"$PYTHON_BIN" "$store_memory_config_script_path"
	i=$((i+1))
done
