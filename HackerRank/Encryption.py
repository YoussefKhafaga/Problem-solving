#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    result = ""
    n = len(s)
    s = s.split()
    s = s[0]
    rows = math.floor(math.sqrt(n))
    columns = math.ceil(math.sqrt(n))
    if rows * columns < n:
        rows = columns
    grid = [[0 for i in range(columns)] for j in range(rows)]
    k = 0
    for i in range(0, rows):
        for j in range(0, columns):
            if k == n:
                break
            grid[i][j] = s[k]
            k += 1
    k = 0
    for i in range(0, columns):
        for j in range(0, rows):
            if grid[j][i] == 0:
                continue
            result += grid[j][i]
            k += 1
        result += " "
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
