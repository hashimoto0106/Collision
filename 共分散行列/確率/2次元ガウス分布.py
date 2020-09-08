# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 21:55:09 2020

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# 2次元のメッシュの座標とその座標での値をしまう3次元の変数を用意
N = 60
X = np.linspace(-4, 4, N)
Y = np.linspace(-4, 4, N)
X, Y = np.meshgrid(X, Y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y

# 平均
mu_multi = np.array([0., 0.])
print(mu_multi)

#　分散共分散行列
Sigma_multi = np.array([[ 1.0 , -0.5],
                        [-0.5,  1.5]])

# 確率密度関数
F = multivariate_normal(mu_multi, Sigma_multi)
p_multi = F.pdf(pos)
cset = plt.contourf(X, Y, p_multi )

# 標本
s_multi = np.random.multivariate_normal(mu_multi, Sigma_multi, 100)
plt.scatter(s_multi[:,0], s_multi[:,1])
