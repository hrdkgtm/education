#!/bin/bash
# Demo of simple infobox with dialog and ncurses

# Global variables declaration
INFOBOX=${INFOBOX=dialog}
TITLE="Default"
MESSAGE="Some messages"
XCOORD=10
YCOORD=40

# Function Declaration
## Display the infobox with our message
funcDisplayInfo (){
    $INFOBOX --title "$1" --infobox "$2" "$3" "$4"
    sleep "$5"
}

# Start of script
if [ "$1" == "shutdown" ]; then
    funcDisplayInfo "WARNING!" "WE ARE SHUTTINGDOWN THE SYSTEM" "$XCOORD" "$YCOORD" "3"
    echo "Shutting down!"
else
    funcDisplayInfo "Information..." "You are not doing anything" "11" "21" "3"
    echo "booooooooo"
fi

