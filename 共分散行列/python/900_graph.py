# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:30:34 2020
https://qiita.com/Seiji_Tanaka/items/5c8041dbd7da1510fbe9
@author: PC
"""

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import math

# データ数　上げると精度が上がる
N = 10 ** 5

# 乱数の生成
x1 = np.random.normal(0, 1, N)
x2 = np.random.normal(0, 3, N)

# 二つの乱数列の結合　それぞれ異なるパラメータを設定したいため後から結合する
x = np.vstack([x1, x2])

# 回転前の分布の表示　この時点ではx軸方向かy軸方向へ平べったい楕円形
# plt.scatter(x[0][:], x[1][:])

# xの分布の回転　これによって一般系の2次元正規分布に変形
theta = np.pi / 4
rot = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]], np.float32)
x = np.dot(rot, x)

# グラフ
plt.scatter(x[0][:], x[1][:])
plt.grid()
plt.xlabel('X1')
plt.ylabel('X2')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()

# 共分散行列の計算
V_x1 = np.dot(x[0][:].T, x[0][:]) / N - (np.sum(x[0][:]) / N)**2
Cov_x1x2 = np.dot(x[1][:].T, x[0][:]) / N - (np.sum(x[1][:]) / N)*(np.sum(x[0][:]) / N)
Cov_x2x1 = np.dot(x[0][:].T, x[1][:]) / N - (np.sum(x[0][:]) / N)*(np.sum(x[1][:]) / N)
V_x2 = np.dot(x[1][:].T, x[1][:]) / N - (np.sum(x[1][:]) / N)**2
V_X = np.array([[V_x1, Cov_x1x2], [Cov_x2x1, V_x2]], np.float32)

# 共分散行列の固有値と固有ベクトルの表示
print("共分散行列")
print(V_X)

w, v = LA.eig(V_X)
print("共分散行列の固有値")
print(w)

print("共分散行列の固有ベクトル")
print(v)

print("誤差楕円長半径")
ellipse_a = math.sqrt(abs(w[0]))
print(ellipse_a)

print("誤差楕円短半径")
ellipse_b = math.sqrt(abs(w[1]))
print(ellipse_b)
