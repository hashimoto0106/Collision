# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:56:56 2020

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
#import seaborn
from scipy.stats import norm

# 標準正規分布
mu = 0  # 平均
sigma = 1  # 標準偏差 ( = 分散^{1/2} )

x = np.linspace(-5, 5)
# 確率密度関数
p = norm.pdf(x, mu, sigma)
print(sum(p))
plt.plot(x, p)
# 標本
#s = np.random.normal(mu, sigma, 500)
#count, bins, ignored = plt.hist(s, normed=True)
