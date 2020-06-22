# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:44:50 2020
https://qiita.com/harmegiddo/items/09e5ec2dc1f0bdb7e1e9
@author: PC
"""

import numpy as np

A = np.array([
              [80, 20, 50], # math
              [100, 30, 80], # science
              [50, 50, 50] # lang
              ])

print(np.var(A[0])) # xx
print(np.var(A[1])) # yy
print(np.var(A[2])) # zz

# xy = yx
a = A[0] - np.mean(A[0])
b = A[1] - np.mean(A[1])
print("---------")
print( 1/3 * np.dot(a, b.T)) 
print(np.cov(A, bias=True))
