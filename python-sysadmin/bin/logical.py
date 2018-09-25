#!/usr/bin/python3.7
# Demonstrate how logical operations work

#assign name to an empty value
name=""
age=24

if not name: # check if name is empty
    print("no Name given")

if name or age:
    print("You have 1 value either in name or age")


# Try or in another usage
last=""
last_name = last or "Doe" # This will continue until the boolean value is True, in this case, it is "Doe"
print(last_name)
