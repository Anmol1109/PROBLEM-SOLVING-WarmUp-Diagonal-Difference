#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += arr[i][i]
        s2 += arr[-i-1][i]
    return abs(s1 - s2)
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
