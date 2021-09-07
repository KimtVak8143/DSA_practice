#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the 'staircase' function below.
# The function accepts INTEGER n as parameter.


def staircase(n):   # Method 1
    # Write your code here
    for x in range(1, n + 1):
        print(" " * (n - x) + "#" * x)


def staircase1(n):   # Method 2
    for i in range(1, n + 1):
        print(("#" * i).rjust(n))


def stair(n):    # Method 3
    print(*[" " * (n - i - 1) + "#" * (i + 1) for i in range(n)], sep='\n')


def staircase2(n):   # Method 4
    for m in range(n):
        print((n - m - 1) * ' ' + (m + 1) * '#')


if __name__ == '__main__':
    n = int(input().strip())

    staircase2(n)
