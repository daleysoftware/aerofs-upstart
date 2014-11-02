#!/bin/bash
# Wrapper script for python, for easier execution via URL.
set -eu
TEMP_FILE="/tmp/quick-install.py"
trap "rm -f $TEMP_FILE; exit" SIGHUP SIGINT SIGTERM
curl -sL https://bit.ly/1EbB3EN > $TEMP_FILE
python $TEMP_FILE
rm -f $TEMP_FILE
