#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    numberOfPeopleThatLikedIt=5//2
    shares = 5
    for i in range(1,n):
        shares = (shares//2)*3
        numberOfPeopleThatLikedIt += (shares//2)
        print(numberOfPeopleThatLikedIt)
    return numberOfPeopleThatLikedIt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
