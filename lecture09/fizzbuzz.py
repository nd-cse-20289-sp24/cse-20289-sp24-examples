#!/usr/bin/env python3

import sys

# Functions

def fizzbuzz(start: int=1, stop: int=100) -> list[str]:
    '''
    >>> fizzbuzz(1, 5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    >>> fizzbuzz(12, 15)
    ['Fizz', '13', '14', 'FizzBuzz']
    '''
    # Version 1: add docstring
    # Version 2: add type annotations
    # Version 3: return list (for unit testing)
    results = []
    for number in range(start, stop + 1):
        if number % 3 == 0 and number % 5 == 0:
            results.append('FizzBuzz')
        elif number % 3 == 0:
            results.append('Fizz')
        elif number % 5 == 0:
            results.append('Buzz')
        else:
            results.append(str(number)) # Demonstrate: Fails mypy w/out conversion
    return results

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    # Version 1: no checks (mypy failure)
    '''
    start = arguments[0]
    stop  = arguments[1]
    '''

    # Version 2: try/except
    '''
    try:
        start = int(arguments[0])
    except IndexError:
        start = 1

    try:
        stop = int(arguments[1])
    except IndexError:
        stop = 100
    '''

    # Version 3: ternary
    start = int(arguments[0]) if len(arguments) >= 1 else 1
    stop  = int(arguments[1]) if len(arguments) >= 2 else 100

    for word in fizzbuzz(start, stop):
        print(word)

if __name__ == '__main__':
    main()
