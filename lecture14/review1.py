#!/usr/bin/env python3

# Imperative

numbers = range(0, 10)

doubled = []
for n in numbers:
    doubled.append(n * 2)

selected = []
for d in doubled:
    if not d % 4:
        selected.append(d)

for s in selected:
    print(s)
