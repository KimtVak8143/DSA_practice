# Capitalize
# !/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.


def solve(s):
    # # Approach 1
    # return s.title()

    # # Approach 2
    # new = ' '.join(map(str.capitalize, s.split(' ')))
    # return new

    # Approach 3
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
