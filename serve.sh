#!/bin/bash

echo "Starting local server on port 8000..."
echo "Open http://localhost:8000 in your browser to view the site."
echo "Press Ctrl+C to stop the server."

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 -m http.server
elif command -v python &> /dev/null; then
    python -m http.server
else
    echo "Error: Python is not installed. Please install Python to run this server."
    exit 1
fi 