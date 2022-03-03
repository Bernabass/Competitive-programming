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
    new_arr=arr[:-1]
    e=arr[-1]
    for i in range(len(arr)-2,-1,-1):
        if e<new_arr[i]:
            new_arr.insert(i,new_arr[i])
            print(' '.join(map(str,new_arr)))
        else:
            new_arr.insert(i+1,e)
            print(' '.join(map(str,new_arr)))
            break
        new_arr=arr[:-1]
    else:
        new_arr.insert(0,e)
        print(' '.join(map(str,new_arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
