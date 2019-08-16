#lilah gives a str which will be repeated for infinite times. then given int n to consider first n elements. outputis no of a's in those n elements
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    c=s.count('a')
    c=c*int(n/len(s))
    x=s[0:n%len(s)]
    return(c+x.count('a'))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
