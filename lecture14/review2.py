#!/usr/bin/env python3

# Functional

numbers = range(0, 10)

doubled = map(lambda n: n*2, numbers)

selected = filter(lambda d: not d % 4, doubled)

for s in selected:
    print(s)
