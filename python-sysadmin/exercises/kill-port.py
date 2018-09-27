#!/usr/bin/env python3
# A script that has a dictionary
import argparse
from subprocess import run, PIPE
import os

# Declaring Variables
parser = argparse.ArgumentParser(prog='prkilz', description='kill process that is listening to the port')
parser.add_argument('port_number', help='The port that you want to check and kill (probably)')
args = parser.parse_args()

lsof = run(['lsof', '-n', f'-i4TCP:{args.port_number}'], stdout=PIPE, stderr=PIPE)
lineout = lsof.stdout.decode().splitlines()

def kill_process(pid, user):
    if user == "y":    
        # os.kill(pid, 9) #what we would actually do
        print(f"killing {pid}...")
    else:
        print("okay")


for list in lineout:
    PROC = [x for x in list.split()]
    if PROC[1] == "PID":
        continue
    else:
        USERINPUT = input(f"{PROC[0]} is listening on port {args.port_number}. kill? (y/n) :")
        kill_process(PROC[1], USERINPUT)