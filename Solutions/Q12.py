#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def timeConversion(s):
    # Write your code here
    str1 = s
    h, m, sec = map(str, str1[:-2].split(':'))
    x = str1[-2:]
    if x == 'PM':
        if h == '12':
            h = '12'
        else:
            h = str(int(h) + 12)
    else:
        if h == '12':
            h = '00'

    return h + ':' + m + ':' + sec


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
