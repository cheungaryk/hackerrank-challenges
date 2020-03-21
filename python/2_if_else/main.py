#!/bin/python3
#
# https://www.hackerrank.com/challenges/py-if-else/problem

# If n is even and in the inclusive range of 6 to 20, print "Weird"
# If n is even and greater than 20, print "Not Weird"

import math
import os
import random
import re
import sys

def check_weirdness(n):
    """
    if n is odd, return "Weird"
    if n is even and in the inclusive range of 6 to 20, return "Weird"

    if n is even and in the inclusive range of 2 to 5, return "Not Weird"
    if n is even and greater than 20, return "Not Weird"
    """
    if n < 1 or n > 100:
        return "Not Applicable"

    return "Not Weird" if n % 2 == 0 and (2 <= n <= 5 or n > 20) else "Weird"

if __name__ == '__main__':
    n = int(input().strip())
    result = check_weirdness(n)
    print(result)
