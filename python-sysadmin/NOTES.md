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
- null value for python
- its None, with capital **N**


# Lecture : Working with variables
- `<varname> = <value>`
- function(varname)
- `varname += <anothervalue>`
- if you assign a variable to a value of another variable, when that second variable is changed, the first variable wont change because its not a pointer. all variables assinged as a value.

# Lecture : Lists
- Lists are mutable, means you can manipulate whats inside a list
- list = [val1, 2, val3]
- it is not type specific, so you can assign string and integer in one list

#### Appending
- len() is one function that you can use in lists, to count the total index of the list
- append() is a function we can use to add index to the list
- `+=` also can be used to append indexes to the list

#### Calling a list
- my_list(n) = call index number n of list `my_list`
- my_list[0:1] = call index number 0 until 1 of `my_list`
- my_list[0:4:2] = call index number 0 until 4 with 2 __slices__

#### Removing indexes
- using the remove() function
    - my_list.remove('a') -> will remove the first index found containing 'a' (starting from 0)
- using the pop() function
    - my_list.pop() -> by default will remove AND return the value of the last index
    - my_list.pop(n) -> will remove AND return the value of index n

#### Replacing an index with another value
- my_list[0:2] = ['a', 'b'] -> will replace index number 0 and 1 to 'a' and 'b'
    - read carefully, index number 2 is not replaced


# Lecture : Tuples
- are a fixed width, immutable sequence type. We create tuples using parenthesis (( and )) and at least one comma (,)
- tuple = ("string", 1, 2.0)
- IMMUTABLE, cant be smaller, cant be bigger
- The most common use of tuples is when we need text formatting
    - example
    ```
    print("My name is %s and my age is %s" % ("Dika", 22))
    ```

# Lecture : Dictionary
- It is like what it said, it has a 'key' and a 'value'
- Think like you are looking at an actual dictionary and looking for certain words
- dictionary = {} --> an empty dictionary
- Creating a dictionary
    - dictionary = ['key1': val, 'key2': val2, 'key3': val3]
    - dictionary = dict(key1=val1, key2=val2, key3=val3)
    - dictionary = dict([('key1', 'val1'), ('key2', 'val2'), ('key3', 'val3')]) --> using TUPLES!!
- The keys have to be **unique**

#### Working with a dictionary
- list all keys
    - dictionary.keys()
    - list(dictionary.keys())
- list all values
    - dictionary.values()
    - list(dictionary.ages())
- what is the value that is inside key1
    - dictionary['key1'] -> this will do that for you
- add a new key
    - dictionary['key4'] = val4
- Delete
    - del dictionary['key4']
    - be careful with del as you can delete the whole dictionary with it [del dictionary]
- Popping
    - dictionary.pop('key4')


# Lecture : Conditionals and Comparisons
- We need to compare a same type. e.g int with int
- For characters, it is case sensitive, and each character have specific values

```
=========================================
            CONDITIONALS
=========================================
< less than
> more than
== equals
!= not equals
>= greater than and equals
<= lesser than and equals
==========================================
x in [x,y,z] --> check whether x in the list
x not in [x,y,z] --> check whether x not in the list
```

#### The if statement
```
if <condition>:
    <command>
elif <condition>:
    <command>
else:
    <command>
```
- you dont always need to specify the else, or even the elif


# Lecture : Loop
- see bin/nested-loop.py for more details and demonstration
- Remember that the boolean (True/False) will always be true if you dont specify the condition
- `continue` will throw you out of the loop/statement and start over from the top
- `break` will throw you out from the loop, like `continue` and **STOP**

