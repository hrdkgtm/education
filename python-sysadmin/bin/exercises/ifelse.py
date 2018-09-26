#!/usr/bin/env python3
# A script that has a dictionary

# Declaring Variables
user = dict([('admin',True),('active',True),('name','Kevin')])

if user['admin'] and user['active']:
    prefix = "ACTIVE - (ADMIN)"
elif user['active']:
    prefix = "ACTIVE"
elif user['admin']:
    prefix = "(ADMIN)"

endstring = prefix + " - " + user['name']
print(endstring)
    
