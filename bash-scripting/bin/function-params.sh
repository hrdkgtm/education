#!/bin/bash
# demo of functional parameter

# Exit if no argument passed
if [ "$#" = "0" ]; then
    echo "Please pass an argument"
    echo "Usage : function-params.sh <your_name>"
    exit 1
fi

# Declare a global variable
USERNAME=$1

# FUNCTION DEFS
## Calculate age in days
funcAgeInDays (){
    echo "Hello $USERNAME, You are $1 Years Old."
    echo "That means you are $[ $1 * 365 ] days old... roughly"
}

# START OF SCRIPT
clear

read -p "Enter your age: " USERAGE
# Calculate the user age in days by passing the $USERAGE variable that is read
funcAgeInDays $USERAGE
