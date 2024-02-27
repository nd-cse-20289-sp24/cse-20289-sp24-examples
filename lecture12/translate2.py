#!/usr/bin/env python3

# curl -sL https://yld.me/raw/f3z1 | cut -d , -f 3 | grep -Eo '^B.*' | sort

import csv
import requests

response   = requests.get('https://yld.me/raw/f3z1')
data       = response.text.splitlines()
last_names = []
for netid, first_name, last_name, phone_number in csv.reader(data):
    if last_name.startswith('B'):
        last_names.append(last_name)

for last_name in sorted(last_names):
    print(last_name)

# Alternative(s)

last_names = [ln for _, _, ln , _ in csv.reader(data) if ln.startswith('B')]

for last_name in sorted(last_names):
    print(last_name)
