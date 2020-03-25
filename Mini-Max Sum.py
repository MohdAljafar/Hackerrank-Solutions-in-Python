#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    a = min(arr)
    max_lst = arr[:]
    max_lst.remove(a)
    b = max(arr)
    min_lst = arr[:]
    min_lst.remove(b)
    min_lst_sum = 0
    max_lst_sum = 0
    for i in min_lst:
        min_lst_sum += i

    for j in max_lst:
        max_lst_sum += j

    print(min_lst_sum, max_lst_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
