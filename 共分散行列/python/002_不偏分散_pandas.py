# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:39:38 2020
http://ailaby.com/python_cov/
@author: PC
"""
from pandas import DataFrame
 
df = DataFrame([[1,2],[2,4],[3,6]])
#-----------
#    0  1
# 0  1  2
# 1  2  4
# 2  3  6
#-----------

matrix = df.cov()
print(matrix)
#-----------
#    0  1
# 0  1  2
# 1  2  4
#-----------