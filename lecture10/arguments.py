#!/usr/bin/env python3

import sys

# Main Execution

def main(arguments=sys.argv[1:]) -> None:           # Review: default arguments
    print(sys.argv)                                 # Review: slicing
    print(sys.argv[1:])

    print(len(arguments))                           # Review: print number of elements

    print(arguments[0])                             # Discuss: indices
    print(arguments[-1])

    arguments.append('hat')                         # Review: adding to list
    print(arguments)

    print('hat' in arguments)                       # Discuss: search

    for index, argument in enumerate(arguments, 1): # Discuss: looping, enumerate
        print(index, argument)

    while arguments:
        argument = arguments.pop(0)                 # Discuss: queue/pop
        print(argument)

    if not arguments:                               # Discuss: check if empty
        print('Empty')

if __name__ == '__main__':                          # Review: import guard
    main()
