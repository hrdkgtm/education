#!/bin/bash
# 


# The more robust way to do it
# This will check if there are 3 arguments passed, and we can pass the arguments specified to the echo
# this script will also exit with a error code 1.
: ${3?"USAGE : param-check.sh $1[arg1] $2[arg2] [arg3]"}

