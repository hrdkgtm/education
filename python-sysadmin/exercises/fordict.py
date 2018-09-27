#!/usr/bin/env python3
# A script that has a dictionary

# Declaring Variables
users = [
        {'admin': True, 'active': True, 'name': 'Kevin'},
        {'admin': False, 'active': True, 'name': 'Pleb'},
        {'admin': True, 'active': False, 'name': 'God'},
        ]

# for loop iterating through the dictionary
for iteration in users:
    if iteration['admin'] and iteration['active']:
        prefix = "ACTIVE - (ADMIN) "
        print(f"{prefix} {iteration['name']}")
    elif iteration['admin'] and not iteration['active']:
        prefix = "(ADMIN) "
        print(f"{prefix} {iteration['name']}")
    else:
        prefix = "ACTIVE - "
        print(f"{prefix} {iteration['name']}")
