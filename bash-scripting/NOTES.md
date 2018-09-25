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
        - / = divide
        - \* = multiply --> notice that we need to escape so it sees it as math operation and not a wildcard
        - + - = u know what it means
        - % = modulus
        -
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
- How to handle a non-zero error code in your script
- Remember that available custom exit code is < 200
- using if
    - if [ "$?" = "0" ]; then execute the command -> if it is a zero exit code then execute the command

# Simple Functions
- functions cant be empty
- Usage :
    ```
    functionName () {
    command
    }
    functionName2 () { command ; }
