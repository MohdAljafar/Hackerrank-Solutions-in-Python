#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    no_of_apples = 0
    no_of_oranges = 0
    for i in apples:
        if a+i >= s and a+i <= t:
            no_of_apples += 1
    for j in oranges:
        if b+j <= t and b+j >= s:
            no_of_oranges += 1
    print(no_of_apples)
    print(no_of_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
