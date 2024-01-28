#!/bin/python3

#You are given two arrays and A and B. Both have dimensions of NxN.
#Your task is to compute their matrix product.

import numpy

N = int(input())
A = numpy.array([input().split() for _ in range(N)],int)
B = numpy.array([input().split() for _ in range(N)],int)

print(numpy.dot(A,B))
