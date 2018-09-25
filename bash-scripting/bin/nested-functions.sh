#!/bin/bash
# Demo of nested functions and some abstraction

# Exit if no argument passed
if [ "$#" = "0" ]; then
    echo "Please pass an argument"
    echo "Usage : function-params.sh <your_name>"
    exit 1
fi

# Declaring global variables
GENDER=$1

# Funtion definitions
## create a human being
funcHuman (){
    ARMS=2
    LEGS=2
    funcMale (){
        BEARD=1
        echo "This is a man, he has $ARMS arms and $LEGS legs, with $BEARD beard"
    }
    funcFemale (){
        BEARD=0
        echo "This is a woman, she has $ARMS arms and $LEGS legs, and $BEARD beard"
    }
}

# Start of script
clear
echo "Determining your characteristics based on your argument"
echo

if [[ $GENDER == "male" ]]; then
    funcHuman
    funcMale
else
    funcHuman
    funcFemale
fi

