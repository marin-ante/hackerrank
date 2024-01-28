#!/bin/python3

#You are given the coefficients of a polynomial P.
#Your task is to find the value of P at point x.

import numpy as np

coeffs = list(map(float,input().split()))
x = float(input())

print(np.polyval(coeffs,x))
