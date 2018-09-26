#!/usr/bin/env python3
# Simple demonstration of the os library

from os import name, environ, getenv, getpid

username = environ['USER']
os_name = name
print(f"You are running a {os_name.upper()} operating system")
print(f"Your default shell is in {environ['SHELL']}")
print(f"You have an environment USER={username}")


knowledge = getenv("KNOWLEDGE", "NOTSET")
if not knowledge.startswith("NOT"):
    print(f"KNOWLEDGE environment is {knowledge}")
else:
    print()
    print("You havent set the KNOWLEDGE variable, try running this command with a format: ")
    print("KNOWLEDGE=<your_name> ./os-environment.py")
    print()
