#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    string_lenght = len(s)
    count_a = s.count('a')
    no_of_a = (n // string_lenght) * count_a
    remainder = n % string_lenght
    for i in range(remainder):
        if s[i] == 'a':
            no_of_a += 1

    return no_of_a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
