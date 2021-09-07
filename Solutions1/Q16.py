#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.


def plusMinus(arr):
    # Write your code here
    l = len(arr)
    sump, sum0, sumn = 0, 0, 0
    for x in range(l):
        if arr[x] > 0:
            sump += 1
        elif arr[x] == 0:
            sum0 += 1
        else:
            sumn += 1

    print("{:.6f}".format(sump / l))
    print("{:.6f}".format(sumn / l))
    print("{:.6f}".format(sum0 / l))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
