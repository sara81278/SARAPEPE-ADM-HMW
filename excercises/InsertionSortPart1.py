#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    key = arr[n-1]
    i = n-1
    while i-1 >= 0 and  key < arr[i-1]:
        arr[i] = arr[i-1]
        [print(j, end = ' ') for j in arr]
        i -= 1
        print()
    arr[i] = key
    [print(j, end=' ') for j in arr]

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
