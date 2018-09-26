#!/usr/bin/env python3

count=0
while count <= 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We are counting!! {count}")
    count += 1

# This will output 1-9
