#!/bin/bash
# demo of dialog box with confirmation button

# SETTING GLOBAL VAR
## DEFAULTS
MSGBOX=${MSGBOX=dialog}
TITLE="Default"
MESSAGE="Some Message"
XC=20
YC=30

# FUNCTION DEFINITION
## Display the message box with our message
funcDisplayMsg () {
    $MSGBOX --title "$1" --msgbox "$2" "$3" "$4"
}

# START OF SCRIPT
if [[ "$1" == "shutdown" ]]; then
    funcDisplayMsg " WARNING!! " "Please press OK when you are ready to shut down" "$XC" "$YC"
    echo "Shutting down now...."
else
    funcDisplayMsg " nothing " "null" "$XC" "$YC"
    echo "meh..."
fi

