#!/bin/python3

#You are given two arrays: A and B.
#Your task is to compute their inner and outer product.

import numpy as np

A=list(map(int,input().split()))
B=list(map(int,input().split()))

print(np.inner(A,B))
print(np.outer(A,B))
