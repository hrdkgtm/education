# DISCLAIMER
This is a notes derived from linuxacademy.com course called "Python 3 Scripting for System Administrator" by Keith Thompson

Prerequisites in the machine :
- git
- wget
- words (/usr/share/dict/words
- lsof
- text editor


# HISTORY AND BENEFITS OF PYTHON
- Created by Guido van Rossun at 1991
- Used and supported by tech giants like **Google** and **Youtube**
- It is an *Object Oriented* **Scripting** Language
- Functional concepts (not included in the course)
- Whitespace delimited with pseudo-code like syntax
    - Makes python code aesthetically pleasing
- Used across a variety of diciplines
- Runs on all major OS, most Linux distro comes with python out-of-the-box
- As of this note is written (25-09-2018), python is ranked 3 in TIOBE index (most searched programming language)


# What's the deal with Python 3?
- Python 3 was released in 2008, it was created for a very specific reason
- in 2020 python 2 wont be supported anymore.
https://wiki.python.org/moin/Python2orPython3
https://docs.python.org/3/whatsnew/3.0.html
- differentiates between text and data, for example when specifying file and a text


#### Introduction to REPL (Read Evaluate Print Loop) for rapid experimentation
- just run the python binary from the command line, and you will get thrown into the python interpreter
- Double quotes (") and single quotes (') doesnt matter like bash

#### Creating and Running python scripts
- #!/usr/bin/python3.7 -> use accordingly to your python binary

#### Using comments
- format
    ```
    # this is a comment
    command # this is also a comment
    """
    This is not a comment,
    This is a multiline string
    Dont use me as a comment
    """
    ```

# Lecture : Strings
- Remember that python doesnt care about double and single quotes
- You can do math operations on string!!!
    ```
    "Ha" * 4
    ```
    this will output : "HaHaHaHa"
- A string is a sequence of characters, in python you can assign a function to that string
    ```
    "helloolleh".find('e')
    "helloolleh".find('ll')
    "helloOLLEH".lower()
    ```
    this command will output
    - 1
    - 2
    - helloolleh
    because you operate a function to the string

# Lecture : Numbers (int and float)
- Strings and numbers are immutable
- Math Operations
    ```
    +  is a substitute
    -  is a substraction
    *  is a multiplication
    /  is a division
    //  is a floor division, means it rounded down
    %  is a modulus
    **  is an exponent
    ```
- When a float is operated with an integer, it will return a **float**
    - 2.0 * 2 = 4.0

#### How to convert types
- say you have "1" assigned to variable, that will be seen as a `string` type
- you want to convert it into an int, then you can do
    ```
    int("1")
    ```
    to parse it into an integer type

# Lecture : Booleans and None
#### Boolean
- `True` and `False`
- Everything has a boolean value to it.
- the bool() function
    - bool({}) = False
    - bool("") = False
    - bool("Literally anything you want") = True

#### None
- like null
- its None, with capital **N**
