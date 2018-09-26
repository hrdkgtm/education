#!/usr/bin/env python3
# Demonstrating for loop with a dictionary

users=dict([('dika','admin'), ('bob','pleb'), ('john','killer')])

for name, role in users.items(): # This will unpack the dictionary users and assign it to name and role accordingly to its value
    print(f"Username : {name}") # then print it
    print(f"Role : {role}")
    print()
