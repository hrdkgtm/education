#!/bin/bash
# override/trap the system exit and execute a custom function

# GLOBAL VARIABLE
TMPFILE="tmpfile.txt"
TMPFILE2="tmpfile2.txt"


# Traps
trap 'funcMyExit' EXIT # Trapping exit code 90

# FUNCTION DECLARATION
## Run this exit instead of the default exit when called
funcMyExit (){
    echo "Exit is overriden..."
    echo "Cleaning up the temp files..."
    rm -r tmpfil*.txt
    exit 55
}


# START OF SCRIPT
echo "Write something to tmp file for later use..." > $TMPFILE
echo "Writing temp file number 2" > $TMPFILE2

echo

echo "Trying to copy the tempfiles"
cp -rf $1 copied$1 2> /dev/null

if [[ "$?" == "0" ]]; then
    echo "Done"
else
    echo "Something is wrong"
    exit 90
fi
