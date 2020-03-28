#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    heighest = 0
    for character in word:
        ascii_value = ord(character)
        index_in_h = ascii_value - 97
        if h[index_in_h] > heighest:
            heighest = h[index_in_h]
    return heighest * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
