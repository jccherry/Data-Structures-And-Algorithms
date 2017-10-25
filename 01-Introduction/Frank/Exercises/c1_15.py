#! /bin/env python3

### C-1.15 Write a Python function that takes a sequence of numbers and determines
### if all the numbers are different from each other (that is, they are distinct).

def distinct(l):
    already = []
    for item in l.items():
        if item in already:
            return False
        already += item
    return True
