#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    total_accepted_people = 0
    accepted_people = 0
    people = 5
    for _ in range(n):
        accepted_people = people//2
        people = accepted_people*3
        total_accepted_people += accepted_people

    return total_accepted_people

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
