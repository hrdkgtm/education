#!/usr/bin/python3.7
# Demo

count=0
while count < 10:
        if count % 2 == 0:
            count += 1
            continue
        print(f"We are counting!! {count}")
        count += 1
        break

print(count)
