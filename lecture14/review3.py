#!/usr/bin/env python3

# List Comprehension

numbers = range(0, 10)

doubled = [n*2 for n in numbers]

selected = [d for d in doubled if not d % 4]

for s in selected:
    print(s)
