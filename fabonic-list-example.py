# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 07:44:47 2018

@author: SUNIL
"""

b=[0,1]
for i in range(1,10):
    b.append(b[-2]+b[-1])
print (b)