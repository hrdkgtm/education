#!/usr/bin/env python3
# A simple script with a function that can prompt user for a message end echo it accordingly

message = input("Please enter a message to echo : ")
count = input("How many times to echo? ")



def echo(message, count):
    try:
        count = int(count)
    except TypeError as tErr:
        print("Must be an integer")
    else:
        x = 1
        while x <= count:
            print(f"{message} - {x}")
            x += 1

echo(message,count)