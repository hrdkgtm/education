#!/usr/bin/env python3.6

import os
import glob
import json
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory exists")
 
subtotal = 0.0

for path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
        destination = path.replace('new', 'processed')
        shutil.move(path, destination)
        print(f"moved '{path}' to '{destination}'")

print(f"Subtotal : ${subtotal:.2f}")
print(f"Subtotal rounded : ${round(subtotal, 2)}")