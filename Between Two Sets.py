#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    answer_list = []
    answer_list2 = []
    mx = max(a)
    mn = min(b)
    for i in range(mx, mn+1, mx):
        answer_list.append(i)
        answer_list2.append(i)

    for answer in answer_list:
        for a_item in a:
            if answer % a_item != 0:
                answer_list2.remove(answer)

    answer_list = answer_list2.copy()

    for answer in answer_list:
        for b_item in b:
            if b_item % answer != 0:
                answer_list2.remove(answer)
                break
    return len(answer_list2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
