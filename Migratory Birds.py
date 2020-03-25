#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count = arr.count(arr[0])
    lst = []
    for i in arr:
        if arr.count(i) > count:
            count = arr.count(i)
    for j in range(1,6):
        if arr.count(j) == count:
            lst.append(j)
    if lst != []:
        lst.sort()
        return lst[0]
    elif lst == []:
        return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
