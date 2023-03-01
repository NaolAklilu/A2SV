#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def arrayManipulation(n, queries):
    dic = defaultdict(int)
    for query in queries:
        dic[query[0]-1] += query[2]
        dic[query[1]] -= query[2]
        
    sortedKeys = sorted(dic.keys())
    
    prefix = [dic[sortedKeys[0]]]
    maxQuery = prefix[0]
    for i in range(1, len(sortedKeys)):
        prefix.append(dic[sortedKeys[i]] + prefix[i-1])
        maxQuery = max(maxQuery, prefix[i])
    
    return maxQuery
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
