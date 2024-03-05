#!/usr/bin/env python3

import concurrent.futures
import functools
import os
import re

# Constants

ROUNDS   = 5
VERSIONS = (
    ('iterative'    , '-i'),
    ('functional'   , '-f'),
    ('comprehension', '-l'),
    ('generator'    , '-g'),
)

# Functions

def benchmark_once(flag):
    command = f'seq 10000000 | measure ./odds.py {flag} 2>&1 > /dev/null'
    return map(float, re.findall(r'([0-9\.]+)', os.popen(command).read()))

def benchmark(name, flag):
    seconds_total = []
    memory_total  = []

    # Version 1: Sequential
    '''
    for _ in range(ROUNDS):
        seconds, memory = benchmark_once(flag)
        seconds_total.append(seconds)
        memory_total.append(memory)
    '''

    # Version 2: Parallel
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for seconds, memory in executor.map(benchmark_once, [flag]*ROUNDS):
            seconds_total.append(seconds)
            memory_total.append(memory)

    seconds_average = sum(seconds_total) / ROUNDS
    memory_average  = sum(memory_total)  / ROUNDS
    print(f'{name:>15}: {seconds_average:8.2f}s {memory_average:8.2f}MB')

# Main Execution

def main():
    '''
    # Version 1: Sequential
    for name, flag in VERSIONS:
        benchmark(name, flag)
    '''

    # Version 2: Parallel
    with concurrent.futures.ProcessPoolExecutor() as executor:
        names = [v[0] for v in VERSIONS]
        flags = [v[1] for v in VERSIONS]
        executor.map(benchmark, names, flags)

if __name__ == '__main__':
    main()
