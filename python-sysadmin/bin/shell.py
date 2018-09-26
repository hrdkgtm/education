
#!/usr/bin/env python3
#!/usr/bin/env python3
# Demonstration of running commands in python

import subprocess

ls = subprocess.run(['ls','-l'], stderr=subprocess.PIPE, stdout=subprocess.PIPE,)

print("Trying to list out the current directory and reverse it...")


print("Standard output : ")
print(ls.stdout)
print(type(ls.stdout))
print("Standard output decoded")
print(ls.stdout.decode())
print(type(ls.stdout.decode()))