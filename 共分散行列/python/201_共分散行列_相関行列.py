# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:50:56 2020
https://www.ydc.co.jp/column/0002/20180820-1.html
@author: PC
"""

import numpy as np


X = np.array([[6, 1, 0],[4, 0, 7],[7, 8, 1],[6, 5, 4]])

# 分散共分散行列
S = np.cov(X, rowvar=0, ddof=0)

# 相関行列
R = np.corrcoef(X,rowvar=0)

np.set_printoptions(precision=3)
print('共分散行列')
print(S)
print('相関行列')
print(R)
