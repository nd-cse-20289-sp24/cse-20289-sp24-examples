#!/usr/bin/env python3

from typing      import Iterator, Optional
from collections import namedtuple
from dataclasses import dataclass

# Structures                                    # Review: singly linked list

'''
Node = namedtuple('Node', 'data next')          # Review: named tuple
'''

@dataclass
class Node:                                     # Discuss: Data class
    data: str = ''
    next: Optional['Node'] = None

# Functions (Iterative)

'''                                             # Discuss: Iterative (List)
def slist_data(head: Optional[Node]) -> list[str]:
    data = []
    curr = head
    while curr:
        data.append(curr.data)
        curr = curr.next
    return data
                                                # Discuss: Recursion (List)
def slist_reverse(head: Node) -> list[str]:
    return slist_reverse_r(head.next, head)
                                                # Discuss: Helper Function
def slist_reverse_r(curr: Optional[Node], prev: Node) -> list[str]:
    if curr is not None:                        # Recursive case
        data = slist_reverse_r(curr.next, curr)
    else:                                       # Base case
        data = []

    return data + [prev.data]                   # Discuss: Concatenating lists
'''

# Functions (Generators)
                                                # Discuss: Iterative (Generator)
def slist_data(head: Optional[Node]) -> Iterator[str]:
    curr = head
    while curr:
        yield curr.data
        curr = curr.next
                                                # Discuss: Recursion (Generator)
def slist_reverse(head: Node) -> Iterator[str]:
    return slist_reverse_r(head.next, head)
                                                # Discuss: Helper Function
def slist_reverse_r(curr: Optional[Node], prev: Node) -> Iterator[str]:
    if curr is not None:                        # Discuss: yield from
        yield from slist_reverse_r(curr.next, curr)

    yield prev.data

# Main Execution

def main():
    slist = Node('a', Node('b', Node('c', Node('d', None))))

    for item in slist_data(slist):
        print(item)

    print()

    for item in slist_reverse(slist):
        print(item)

if __name__ == '__main__':
    main()
