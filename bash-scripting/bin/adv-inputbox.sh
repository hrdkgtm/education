#!/bin/bash
# demo of advanced ncurses UI - the inputbox

# GLOBAL VARIABLE DECLARATIONS
INPUTBOX=${INPUTBOX=dialog}
TITLE="Default"
MESSAGE="Some Message"
XC=20
YC=40
USERINPUT=input.tmp

# FUNCTIONS DEFINITION
## Display the input box
funcInputBox () {
    $INPUTBOX --title "$1" --inputbox "$2" "$3" "$4" 2> $USERINPUT
}


# START OF SCRIPT
funcInputBox "Display File Name" "Which file in the current directory do you want to display?" $XC $YC

if [[ "`cat $USERINPUT`" != "" ]]; then
    cat "`cat $USERINPUT`"  ### why is this confusing? because we want to read the file that is DEFINED inside the $USERINPUT and not the CONTENTS OF $USERINPUT
else
    echo "nothing to do"
fi
rm $USERINPUT # general housekeeping
