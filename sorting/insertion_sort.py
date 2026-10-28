#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    
    n=n-1
    while arr[n] < arr [n-1] and n>0:
        tmp = arr[n]
        arr[n] = arr[n-1]
        for i in arr:
            print(str(i), end=" ")
        arr[n-1] = tmp
        n=n-1
        print()
    for i in arr:
        print(str(i), end=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
