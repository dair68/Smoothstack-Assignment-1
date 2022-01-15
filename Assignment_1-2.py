# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:03:50 2022

@author: Grant Huang

Work for assignent 1-1 in Smoothstack
"""

import math

total = 50 + 50
print("50 + 50 = " + str(total))

difference = 100 - 10
print("100 - 10 = " + str(difference))

#%%

#syntax error
#sum1 = 30 +* 6
#print("30 +* 6 = " + str(sum1))

comparison = 6 ^ 6
print("6 ^ 6 = " + str(comparison))

product = 6**6
print("6**6 = " + str(product))

sum2 = 6 + 6 + 6 + 6 + 6 + 6
print("6 + 6 + 6 + 6 + 6 + 6 = " + str(sum2))

#%%

print("Hello World")
print("Hello World : 10")

#%%

import math

data = input("input data: \n").split()

p = int(data[0])
r = int(data[1])
l = int(data[2])

#print("P=" + str(p))
#print("R=" + str(r))
#print("L=" + str(l))

#M = P[c(1 +c)^L]/[(1 + c)^L - 1] for c = R/100*1/12
c = r/100*1/12
m = p*(c*(1 + c)**l)/((1 + c)**l - 1)
print("\nanswer:")
print(math.ceil(m))

