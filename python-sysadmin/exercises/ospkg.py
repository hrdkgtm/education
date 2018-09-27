#!/usr/bin/env python3
# Using the os package and environment variables

import os
from math import pi

digits = os.getenv('DIGITS')
if digits:
    print("PI" * int(digits))
else:
    print(f"The first 10 float point of pi = {pi:.10f}") # https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals