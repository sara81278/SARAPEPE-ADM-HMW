#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    sortedS = sorted([c for c in s])
    counter = Counter(sortedS) 
    for letter, count in counter.most_common(3):
        print(letter, count, sep = ' ')
