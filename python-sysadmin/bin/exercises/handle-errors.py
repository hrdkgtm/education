#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='The file name to read from')
parser.add_argument('line_number', type=int, help='The line number to read from the file')

params = parser.parse_args()

try:
    with open(params.file_name, 'r') as f:
        result = f.readlines(params.line_number)
        linez = result[params.line_number - 1]
except IndexError as err:
    print(f"Error, the line number is out of range")
else:
    print("This is the line that you want to read")
    print(linez)
