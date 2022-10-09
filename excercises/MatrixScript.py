#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

res = ''

for i in range(m):
    s = ''.join([row[i] for row in matrix])
    s = re.sub('(?<=[0-9a-zA-Z])+[^0-9a-zA-Z]+(?=[0-9a-zA-Z])', ' ', s)
    res += s
res = re.sub('(?<=[0-9a-zA-Z])+[^0-9a-zA-Z]+(?=[0-9a-zA-Z])', ' ', res)
print(res)
