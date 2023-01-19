#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
                
    return count, arr

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    count, newArr = countSwaps(arr)
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(arr[0]))
    print("Last Element: " + str(arr[-1]))
