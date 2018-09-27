# List of useful modules

## os

This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module. For creating temporary files and directories see the tempfile module, and for high-level file and directory handling see the shutil module.

Functions:

    - getenv()
    - geteuid()
    - getgid()
    - getgroups()
    - getuid()
    - uname()

## subprocess

<https://docs.python.org/3/library/subprocess.html>

The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions:

Functions :

    - run('commands', 'options', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

## shutil

<https://docs.python.org/3/library/shutil.html>

The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files, see also the os module.

Functions :

    - which()
    - chown()
    - copytree()
    - copy()
    - move()
    -

## glob

<https://docs.python.org/3/library/glob.html>

The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order. No tilde expansion is done, but *, ?, and character ranges expressed with [] will be correctly matched. This is done by using the os.scandir() and fnmatch.fnmatch() functions in concert, and not by actually invoking a subshell. Note that unlike fnmatch.fnmatch(), glob treats filenames beginning with a dot (.) as special cases. (For tilde and shell variable expansion, use os.path.expanduser() and os.path.expandvars().)

## json

<https://docs.python.org/3/library/json.html>

JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired by JavaScript object literal syntax (although it is not a strict subset of JavaScript [1] ).

Functions :

    - dump()
    - load()

## re : regular expressions

