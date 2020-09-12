# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 22:07:58 2020

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

#関数に投入するデータを作成
x = y = np.arange(-20, 20, 0.5)
X, Y = np.meshgrid(x, y)

z = np.c_[X.ravel(),Y.ravel()]

#二次元正規分布の確率密度を返す関数
def gaussian(x):
    #分散共分散行列の行列式
    det = np.linalg.det(sigma)
    print(det)
    #分散共分散行列の逆行列
    inv = np.linalg.inv(sigma)
    n = x.ndim
    print(inv)
    return np.exp(-np.diag((x - mu)@inv@(x - mu).T)/2.0) / (np.sqrt((2 * np.pi) ** n * det))



mu = np.array([0,0])  #2変数の平均値を指定
sigma = np.array([[1,0],[0,1]])  #2変数の分散共分散行列を指定

Z = gaussian(z)
shape = X.shape
Z = Z.reshape(shape)

#二次元正規分布をplot
fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
plt.show()
