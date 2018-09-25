#!/bin/bash
# demo of error handling

echo "Change to a directory and list the contents"
DIRECTORY=$1

# Check if user passed an argument
if [ "$#" = "0" ]; then
    echo "Please pass an argument"
    echo "Usage : errorhandling.sh <directory>"
    exit 1
else
    cd $DIRECTORY 2> /dev/null
fi

# Using if
if [ "$?" = "0" ]; then
    ls -la
else 
    echo "Directory not found"
    exit 99
fi
