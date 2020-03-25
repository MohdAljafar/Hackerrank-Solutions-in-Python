#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bCharged = b
    bill.pop(k)
    bActual = reduce(lambda x, y: x+y, bill)//2
    if bCharged == bActual:
        print("Bon Appetit")
    else:
        print(bCharged-bActual)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
