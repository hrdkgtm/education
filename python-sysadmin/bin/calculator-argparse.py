#!/usr/bin/env python3
# Demonstration of using the argparse module
# Calculate integers

import argparse

# Setting up the parameter parser
parser = argparse.ArgumentParser(prog="clac", description="The CLI Calculator")
parser.add_argument('firstint', type=int, help='The first number')
parser.add_argument('secondint', type=int, help='The second number')
parser.add_argument('--exponent', '-e', type=int, help='The second number')
parser.add_argument('--version', '-v', action='version', version='%(prog)s %(description)s - v0.1')

# declaring the args
args = parser.parse_args()
# Error handling 101
# If the exponential option is specified
try:
    type(args.exponent) is float
except TypeError as err:
    print(f"{err}")
else:
    if args.exponent:
        result = (args.firstint + args.secondint) ** args.exponent
        print(result)
    else:
        result = args.firstint + args.secondint
        print(result)

# The calculator
# print(args.firstint + args.secondint)
