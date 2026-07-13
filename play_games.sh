#!/bin/bash

# Terminal Games Launcher Script
# This script provides an easy way to run the terminal games collection

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Python is not installed. Please install Python 3 to run these games."
    exit 1
fi

# Run the game launcher
cd "$SCRIPT_DIR"
$PYTHON_CMD -m games.launcher
