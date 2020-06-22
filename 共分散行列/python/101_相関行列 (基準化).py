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
              [40, 50, 40] # lang
              ])

print(np.corrcoef(A))
print("---------")
idx = 0
idy = 0
num = 3
a_v = np.sqrt( 1/num * np.sum(np.power( (A[idx] - np.mean(A[idx])), 2 ) ) )
b_v = np.sqrt( 1/num * np.sum(np.power(  (A[idy] - np.mean(A[idy])), 2 ) ) )
a = (A[idx] - np.mean(A[idx]))
b = (A[idy] - np.mean(A[idy]))
cor = 1/num * (np.dot(a, b.T))
print(cor / (a_v * b_v))
