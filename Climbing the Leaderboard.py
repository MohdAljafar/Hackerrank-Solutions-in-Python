#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    for i in alice:
        index = bisect.bisect(scores, i)
        yield len(scores)+1-index

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    scores = list(set(scores))
    scores.sort()

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
