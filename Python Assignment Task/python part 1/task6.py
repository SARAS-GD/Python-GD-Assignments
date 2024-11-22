"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> tuple[int, int]:
    min_val = float("inf")
    max_val = float("-inf")
   
    
    with open(filename, 'r') as file:
        for line in file:
            value = int(line.strip())
            if value < min_val:
                min_val = value
            if value > max_val:
                max_val = value
    
    return min_val, max_val

print(get_min_max("/Users/srajuv/Desktop/Python-GD-Assignments/problem6.txt"))

