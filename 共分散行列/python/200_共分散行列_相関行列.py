# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:50:56 2020
https://www.ydc.co.jp/column/0002/20180820-1.html
@author: PC
"""

import numpy as np


X = np.array([
[6, 1, 0],
[4, 0, 7],
[7, 8, 1],
[6, 5, 4]
])

# 標本数
n = X.shape[0]
print('標本数')
print(n)

# 平均
Xbar = np.mean(X, axis=0)
print('平均')
print(Xbar)

# 偏差
D = X - Xbar
print('偏差')
print(D)

# 共分散行列
S = D.T.dot(D)/n

# 共分散行列の対角成分を切り出し
v = np.diag(S)

# 標準偏差
s = np.sqrt(v)

# 相関係数
R = S/s[:, None]/s[None, :]

np.set_printoptions(precision=3)
print('共分散行列')
print(S)
print('共分散行列の対角成分')
print(v)
print('標準偏差')
print(s)
print('相関行列')