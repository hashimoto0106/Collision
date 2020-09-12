# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:14:17 2020

@author: PC
"""

import scipy
import numpy as np
import matplotlib.pyplot as plt

# 標準偏差を変えた例
x = np.linspace(-10,10,100)
stdvs = [1.0, 2.0, 3.0, 4.0]
fig = plt.figure()
ax = fig.add_subplot(111)

for s in stdvs:
    ax.plot(x, scipy.stats.norm.pdf(x,scale=s), label='stdv=%.1f' % s)
ax.set_xlabel('x')
ax.set_ylabel('p(x)')
ax.set_title('Normal Distribution')
ax.legend(loc='best', frameon=False)
ax.grid(True)


# 平均を変えた例
x = np.linspace(-10,10,100)
mus = [0.0, 1.0, 2.0, 5.0]
fig = plt.figure()
ax = fig.add_subplot(111)

for mu in mus:
    ax.plot(x, scipy.stats.norm.pdf(x,loc=mu), label='mean=%.1f' % mu)
ax.set_xlabel('x')
ax.set_ylabel('p(x)')
ax.set_title('Normal Distribution')
ax.legend(loc='best', frameon=False)
ax.grid(True)
