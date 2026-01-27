#!/bin/bash

# Ensure we are in the app directory
cd /app

echo "--- Mega Hello World Runner ---"
echo "Initializing environment..."

# Run the python runner
python3 runner.py "$@"
