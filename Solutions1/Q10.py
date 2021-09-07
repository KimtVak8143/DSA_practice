#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    maxum = sum(arr)-arr[0]
    minum = sum(arr)-arr[-1]
    print("{} {}".format(minum, maxum))


if __name__ == '__main__':

    arr = list(map(int, input("Enter 5 Numbers ").rstrip().split()))

    miniMaxSum(arr)
