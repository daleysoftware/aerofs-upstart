#!/bin/bash
# Wrapper script for python, so execution via URL is easier.
set -eu

TEMP_FILE="/tmp/quick-install.py"
trap "rm -f $TEMP_FILE; exit" SIGHUP SIGINT SIGTERM

echo ">> Downloading setup scripts..."
curl -sL https://raw.githubusercontent.com/mpillar/aerofs-upstart/master/quick-install.py > $TEMP_FILE

echo ">> Launching setup utility..."
echo
python $TEMP_FILE

rm -f $TEMP_FILE
