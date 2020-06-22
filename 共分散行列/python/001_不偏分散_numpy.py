# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:39:38 2020
http://ailaby.com/python_cov/
@author: PC
"""
import numpy as np

a = np.array([[1,2],[2,4],[3,6]])
#---------------------------
# array([[1, 2],
#        [2, 4],
#        [3, 6]])
#---------------------------

# 不偏分散（bias=0）
matrix = np.cov(a, rowvar=0, bias=0)
print(matrix)
#---------------------------
# array([[ 1.,  2.],
#        [ 2.,  4.]])
#---------------------------