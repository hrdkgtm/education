#!/bin/bash
# demo of functions within a shell script structure

# script or global vars
CMDLINE=$1

# Defining function
function1 () {
    echo "I am function number 1"
    echo "Therefore I am called"
}

# calling
echo "Calling function1"
function1
echo
echo "Calling function2"
function2

# Demonstrating late function defining
function2 (){
    echo "I am function number 2"
    echo "Therefore I am called"
}

# retry to call the function
echo "Second try to call function2"
function2
