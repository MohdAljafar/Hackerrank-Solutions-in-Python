#!/bin/python3

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

def diagonalDifference(arr, n):
    # Write your code here
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += arr[i][i]
    for j in range(n):
        sum2 += arr[j][(n-1)-j]
    if sum1 > sum2:
        return sum1-sum2
    else:
        return sum2-sum1 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
