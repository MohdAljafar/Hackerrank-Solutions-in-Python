#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    hi_score = scores[0]
    hi_score_times = 0
    low_score = scores[0]
    low_score_times = 0
    for score in scores:
        if score > hi_score:
            hi_score = score
            hi_score_times += 1
        if score < low_score:
            low_score = score
            low_score_times += 1
    return hi_score_times, low_score_times

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
