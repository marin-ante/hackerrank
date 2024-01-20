#!/bin/python3

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird

import math
import os
import random
import re
import sys

def is_even(num):
    return num % 2 == 0

if __name__ == '__main__':
    n = int(input().strip())

    if is_even(n):
        if n in list(range(6, 21)):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
