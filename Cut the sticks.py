#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    while arr != []:
        yield len(arr)
        shortest_lenght = min(arr)
        arr = list(map(lambda x: x-shortest_lenght, arr))
        for _ in range(arr.count(0)):
            arr.remove(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
