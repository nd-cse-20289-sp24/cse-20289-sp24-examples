#!/usr/bin/env python3

# List

def triples(sequence):
    ts = []
    for i in sequence:
        ts.append(i * 3)
    return ts

# Generator

def triples(sequence):
    for i in sequence:
        yield i * 3

# Main Execution

for i in triples([1, 2, 3]):
    print(i)
