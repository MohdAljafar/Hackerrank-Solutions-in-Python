#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    jumping_clouds = []
    i = 0
    while True:
        i += k
        if i > (len(c)-1):
            i -= len(c)
        jumping_clouds.append(c[i])
        if i == 0:
            break
    for j in jumping_clouds:
        if j == 0:
            energy -= 1
        else:
            energy -= 3
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
