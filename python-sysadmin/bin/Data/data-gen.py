#!/usr/bin/env python3.6

import os
import random
import json
import argparse

parser = argparse.ArgumentParser(prog="Data Generator")
parser.add_argument('--count', '-c', type=int, default=100, help='specify the number of files to be generated')

params = parser.parse_args()

words = [word.strip() for word in open('/usr/share/dict/words', 'r').readlines()]

for identifier in range(params.count):
    amount = random.uniform(1, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        json.dump(content, f)