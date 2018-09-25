# HISTORY
- Shells are command line interpreters, begin with the first unix shell back in 1971, called the V6 shell.
- The bourne shell was introduced in 1977 by Stephen Bourne, at Bell Labs fot V7 UNIX.
- From this Bourne Shell later give birth to many other shells like bash, ksh, zsh, etc.

THE BOURNE AGAIN SHELL
- Bash is fully compatible with the bourne shell
- Introduces _functions, regexp, associative arrays_.
- Licensed under GPL rather than the BSD license like the bourne shell.

# BASH FILES
## .bash_profile
- Main difference between this and bashrc is, bash_profile only sourced when you log in. Where bashrc sourced everytime you run another terminal.
- a profile for every user. the global profile exists in /etc/profile
- the ideal place to set up custom path PATH=$PATH:$HOME/bin
- these profile 'files' are actually a script within itself so you usually can run it.

## .bashrc
- it is run before the shell actually comes out.
- basically a dotfiles, boring stuffs.

## bash_history
- a file storing history of commands that been executed with bash.
- newest at the bottong, oldest at the top, not numbered like zsh
- there is an environment variable dalled $HISTCONTROL which controlling how history behaves, like for instance *ignoredup* which will ignore duplicates
    - in environment variables, the delimiter is (:)
    -  for example PATH=$PATH:$HOME/bin
    -  another example HISTCONTROL=$HISTCONTROL:ignoredups:ignorespace
- _ignorespace_ will not record any command that starts with ' ' (space)

## bash_logout
- a file that will be run everytime you logout from the shell
- can have interesting interactions with bash_login for example
    - bash_login will backup the .bashrc into .bashrc.orig
    - bash_logout will overwrite the .bashrc with the .bashrc.orig and delete the .bashrc.orig for good practice and keep things persistent


# WHAT MAKES A SHELL SCRIPT?
- shebang bin shell --- this specifies the interpreter to read the script
- executable mode --- chmod +x

# EXPORTS
-  remember that if you run a command to be the environment, for instance "export today=`date`", the date will be only a statuc output that is generated _when the environment is set_


# COMMAND SUBSTITUTION
- use backticks (`)
- or $(command)
- remember that alias does not translate to subshells by default, if you want it to expand you can enable it by 'shopt -o expand_aliases'
- when using aliases, this is also known as dynamically substituting value with a command, with variable, it is statix as it is set when you set the variable.

# ERROR CODES
- with set -e = script will exit immidiately everytime there is a non-zero exit code
- there are various exit code, and you can specify it with whatever you want in the script and handles those accordingly within the script.


# MATHS IN SHELL
- expr = known as _expression_
    - example expr 2 + 2
    - SPACES MATTER!!!1
    - operations :
        - `/` = divide
        - `\*` = multiply --> notice that we need to escape so it sees it as math operation and not a wildcard
        - `+ -` = u know what it means
        - `%` = modulus
    - this follows order of precedence, which means multiplication done first before substitution
    - can grouped with () with an escape
        - example expr \(2 + 2 \) \* 5
        - this will output 20

# GLOBAL AND LOCAL VARIABLES
- _printenv_ = a part of GNU coreutils to print the global environment that is set in our system
- set = environment that is specific to current session

# Debugging your script
- Using set -x 
    - put the "set -x" before the line that you want to debug
    - to output the commands as they are executed
    - unset with +x (set +x)

# Error Handling
- see bin/errorhandling.sh
- How to handle a non-zero error code in your script
- using if
    - if [ "$?" = "0" ]; then execute the command -> if it is a zero exit code then execute the command

# Functions
## Simple Functions
- functions cant be empty
- IT IS NOT AN OBJECT!!
- You *cant* call a function if it is not defined yet, like if you define a function at the bottom of the script
- Usage :
    ```
    functionName () {
    command
    }
    functionName2 () { command ; }
    ```
- Its one of a best/good practice to structure your commands inside a function
    - see functionsctructure.sh inside bin

## Function with parameters
- see bin/function-params.sh
- Function can take parameter, just like scripts in general, they behave the same way in taking an argument

## Nested Functions
- see bin/nested-function.sh (this is just an example, dont get mad because of gender issues)
- Like what its called, it is a function inside a function

## Function return and exit
- see bin/function-ret.sh
- return value is like the exit code of the script, without actually exitting
- for example `return 4` will pass a 4 return value outside the function
- to read it outside the function, use `$?`


# Variable Scope
- see bin/variable-scope.sh
- Global variable declared in the script can be read inside a function
- Local variable defined inside a function can be read from the script *ONLY IF* the function already called
- Try to define accordingly and not defining all things in global variables

# The dialog box
- Create dialog box, ncurses based

## The Infobox
- A method of popping up a ncurses dialog box
- install the `dialog` package to be able to create an infobox
- man 1 dialog

### Dialog
- see bin/simpleinfobox.sh
- simple dialog box to notify
- `dialog --title [] --infobox [message] [xcoordinate] [ycoordinate]

### MessageBox for Confirmation
- see bin/confirmationbox.sh
- simple confirmation box with "OK" button
- `dialog --title [] --msgbox [message] [xcoordinate] [ycoordinate]`

### Advanced UI - Building a menu system
- see bin/adv-msgbox.sh
- using the case statement, we can catch user input and act accordingly
- `dialog --title [] --menu [Message above options] [xcoord] [ycoord] [number of menus] [menu number1] [message] [menu numberN] [message] 2> [file]`
- the dialog will write user choices in standard error, thats why we redirect the option to a file and then later on will read that option using the *case* statement
- remember to remove the choice file afterwards for good practice, or no if you want to see how it plays.

### Advanced UI - The Input Box
- see bin/adv-inputbox.sh
- `dialog --title [] --inputbox [Message on top of inputbox] [xc] [yc] 2> [tmp inputfile]`
- Like the menu, dialog will take user input and output it in stderr, so we redirect it into a temp file and remove it afterwards

# Overriding Events - traps
- see bin/override.sh
- Learn how to override the exit/signal with traps
- remember traps
    - `trap 'command' [SIGNAL]`
    - some signals = `SIGHUP SIGKILL SIGTERM EXIT`
    - trapping an EXIT will execute the command when an exit is trapped (Equivalent to signal number 0)
    - man 1p trap

# Checking Parameters
- see bin/param-check-if.sh and bin/param-check-robust
- The script will demonstrate how we can check parameters that is passed with the script
- There is two mentioned way in the course which is usinf _if_ and the other one

# Building a document generator
- see bin/makedoc.sh
- the #!/bin/bash is just basically will run bash, and reading the proceeding command as its input
- as you can see in the `makedoc.sh` we are creating another script that is called `scipt_listing` that will use *less* as its interpreter
- what `script_listing` do is basically taking the content of itself into the `less` program which will display the content in a pager
- this script is an example on how we can create a script to dynamically create another script that we can run and adjust to our needs
- this script utilizes the IFS environment and reading a filename based on line for the wile loop.
