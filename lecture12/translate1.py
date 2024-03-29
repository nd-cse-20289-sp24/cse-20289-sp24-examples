#!/usr/bin/env python3

'''
Translate: cat /etc/passwd | cut -d : -f 1 | grep d$ | wc -l
'''

import csv

# Translation

count = 0
for line in open('/etc/passwd'):
    user = line.rstrip().split(':')[0]
    if user.endswith('d'):
        count += 1

print(count)

# Alternative

users = csv.reader(open('/etc/passwd'), delimiter=':')
print(sum(1 for user in users if user[0].endswith('d')))
