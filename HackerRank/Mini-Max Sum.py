#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minn = 0
    maxx = 0
    arr2 = arr.copy()
    for i in range(0, 4):
        max1 = max(arr)
        maxx += max1
        arr.remove(max1)
        min1 = min(arr2)
        minn += min1
        arr2.remove(min1)
    print (minn, maxx)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
