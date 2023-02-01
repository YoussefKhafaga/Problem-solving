#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    time = ""
    dict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"tweleve", 13:"thirteen", 14:"fourteen", 15:"quarter", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 21:"twenty one", 22:"twenty two", 23:"twenty three", 24:"twenty four", 25:"twenty five", 26:"twenty six", 27:"twenty seven", 28:"twenty eight", 29:"twenty nine", 30:"half"}
    if m == 0:
        time += dict[h]
        time += " o' clock"
    else:
        if m == 1:
            time = "one minute past " + dict[h]
            return time
        elif m == 59:
            time = "one minute to " + dict[h]
            return time
        elif m > 30:
            m = 60 - m
            if m == 15:
                time = "quarter to " + dict[h+1]
                return time
            time = dict[m] + " minutes to " + dict[h+1]
        elif m < 30:
            if m == 15:
                time = "quarter past " + dict[h]
                return time
            time += dict[m] + " minutes past " + dict[h]
        else:
            time = "half past " + dict[h]
    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
