#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s.startswith("12") and s.endswith("AM"):
        s = s.replace(s[0:2], '00')
        return s[:8]
    elif s.endswith("AM"):
        return s[:8]
    elif s.startswith("12") and s.endswith("PM"):
        return s[:8]
    elif s.endswith("PM"):
        s1 = int(s[:2])
        s1 += 12
        print(s1)
        s = str(s[:8])
        s = s.replace(s[:2], str(s1))
        return s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
