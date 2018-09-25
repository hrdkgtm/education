#!/bin/bash
# demo of variable scopes

# Declaring global variables
GLOBALVAR="Globally Visible"

# Defining functions
# Sample function for variable scope
funExample (){
    # Function-local variable
    LOCALVAR="Locally visible"

    echo "From funExample, the local var is $LOCALVAR"
    echo "and the global var is $GLOBALVAR"
}

# Script - Start
clear

echo "Now I am started"
echo "I know that GLOBALVAR is $GLOBALVAR"
echo "I dont know what the LOCALVAR is? trying? $LOCALVAR"
echo 
echo "Now I am calling my function"
echo
funExample
echo
echo " now i know that LOCALVAR is = $LOCALVAR"
