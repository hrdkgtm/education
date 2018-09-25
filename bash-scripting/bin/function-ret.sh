#!/bin/bash
# demo of function return and exit

# Global var declare
YES=0
NO=1
FIRST=$1
SECOND=$2
THIRD=$3

# Function definitions
## check the command line for any arguments
funcCheckArgs (){
    #did we get three
    if [[ ! -z "$THIRD" ]]; then # -z is for checking if the condition is zero/null
        echo "We got three arguments"
        return $YES
    else
        echo "We did not get three arguments"
        return $NO
    fi
}

# Start of script
funcCheckArgs
RETVAL=$?

## did we get three?
if [[ "$RETVAL" -eq "$YES" ]]; then
    echo "We receiver three parameters and they are :"
    echo "Param 1: $FIRST"
    echo "Param 2: $SECOND"
    echo "Param 3: $THIRD"
    echo
else
    echo "Please give 3 arguments"
    echo "Usage: functions-ret.sh [arg1] [arg2] [arg3]"
    exit 90
fi
