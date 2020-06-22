# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:35:49 2020
https://phst.hateblo.jp/entry/2020/01/22/000000
@author: PC
"""

import numpy as np


# 計測における誤差解析入門 9.2の例題より
data = np.array([[35, 50], [31, 55], [33, 51], [32, 53], [34, 51]])
print("data:", data)

# 平均値を求める
mu = np.mean(data, axis=0)
print("mean:", mu)

# 分散共分散行列を求める(データ数が少ないので不偏分散のbiasを1にする)
cov = np.cov(data, rowvar=0, bias=1)
print("cov:", cov)

# x+yの標準偏差を求める
print("std_(x+y)", np.std([x+y for x, y in zip(data[:, 0], data[:, 1])])**2)

# 再現性を出すためにseedを固定する
np.random.seed(0)

# MCでデータを生成する
values = np.random.multivariate_normal(mu, cov, 10000)

# MCで生成したデータの分散σ^2を求める
print("MC std_x    :", np.std(values[:, 0])**2) # 期待値は2
print("MC std_y    :", np.std(values[:, 1])**2) # 期待値は3.2
print("MC std_(x+y):",
np.std([data+b for a, b in zip(values[:, 0], values[:, 1])])**2) # 期待値は0.4
