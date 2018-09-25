#!/bin/bash
# demo of advanced ncurses UI for menu


# GLOBAL VARIABLE DECLARATION
MENUBOX=${MENUBOX=dialog}
CHOICE="userchoice"

# FUNCTION DEFINITIONS
## The function to display simple menu
funcMenuBox () {
    $MENUBOX --title "[ M A I N  M E N U ]" --menu "Use UP/DOWN Arrow to Move and Select or the number accordingly" 15 45 4 1 "Display Hello World" 2 "Display Goodbye World" 3 "Display Hostname" X "Quit" 2> $CHOICE
}


# START OF SCRIPT
funcMenuBox
case "`cat $CHOICE`" in
    1) echo "Hello World!!!";;
    2) echo "Goodbye World...";;
    3) echo $HOST ;;
    X) echo "Exit" ;;
esac
rm $CHOICE
