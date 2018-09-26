#!/usr/bin/env python3
# Simple script to demonstrate how to import a time library

# Libraries
# import time
from time import localtime, strftime, mktime

# Start of script
start_time = localtime()

print(f"Stopwatch started at {strftime('%X', start_time)}")
input("Press ENTER to stop the stop watch")

## Declaring stop time after the script stopped
stop_time = localtime()
total_time = mktime(stop_time) - mktime(start_time)

print(f"Stopwatch stopped at {strftime('%X', stop_time)}")
print(f"Total time wasted of your life running this script = {total_time} (s)")
