# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:23:56 2020
https://qiita.com/supersaiakujin/items/71540d1ecd60ced65add
@author: PC
"""

import scipy
import numpy as np
import matplotlib.pyplot as plt


# case1
x,y = np.meshgrid(np.linspace(-10,10,100),np.linspace(-10,10,100))
pos = np.dstack((x,y))
mean = np.array([2.5, 3.3])  #2変数の平均値を指定
cov  = np.array([[1.0,0.0],[0.0,1.0]])  #2変数の分散共分散行列を指定
z = scipy.stats.multivariate_normal(mean,cov).pdf(pos)

fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal')
ax.contourf(x,y,z)
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('pdf')


# case2
x,y = np.meshgrid(np.linspace(-10,10,100),np.linspace(-10,10,100))
pos = np.dstack((x,y))
mean = np.array([2.5, 3.3])  #2変数の平均値を指定
cov  = np.array([[5.0,1.0],[1.0,2.0]])  #2変数の分散共分散行列を指定
z = scipy.stats.multivariate_normal(mean,cov).pdf(pos)

fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal')
ax.contourf(x,y,z)
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('pdf')
