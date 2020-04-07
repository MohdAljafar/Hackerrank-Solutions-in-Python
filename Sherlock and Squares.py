#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    no_of_squares = 0
    startingvalue = int(a ** .5)
    endingvalue = int(b ** .5)
    for i in range(startingvalue, endingvalue+1):
        if i*i in range(a, b+1):
            no_of_squares += 1
            
        
    return no_of_squares

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
