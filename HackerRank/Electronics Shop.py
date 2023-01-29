#!/bin/python3

import os
import sys
import math
#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards.sort(reverse = True)
    drives.sort(reverse = True)
    maxx = -1
    print(keyboards, drives)
    for i in range(0, len(keyboards)):
        for j in range(0, len(drives)):
            print(keyboards[i], drives[j])
            if b - (keyboards[i] + drives[j]) >= 0:
                if (keyboards[i] + drives[j]) > maxx:
                    maxx = (keyboards[i] + drives[j])
                    print(maxx)
    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
