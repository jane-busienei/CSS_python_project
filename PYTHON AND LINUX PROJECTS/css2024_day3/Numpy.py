# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 04:11:06 2024

@author: Neno
"""
import numpy as np
import matplotlib.pyplot as plt
#Using python
#for i in range(1,11):
 #   print(i)
# using numpy- arrange
#for i in np.arange(1,11):
#    print(i)
squares = []
#for i in range(6,1):
#   squares.append(i**2)
#print(squares)

#x = np.arange(1,6)
#y = x**2
#print(y)

#print("the shape of x is:", x.shape)
#print("the shape of y is:", y.shape)
#print(x*y)
#plt.plot(x,y, "r*")
#print(x.dot(y))

alist = [1, 2, 5, 6, 15, 22]
data = np.array(alist)
print(data)
#reshape to 2 rows and 3 columns
data2 = data.reshape([2,3])
data3 = np.reshape(data2,[2,3])
print(data2)
print(data3)

alist2 = [[1,2,5], [6,15,22]]
data4 = np.matmul(data2.T, data3)
print("alist2 is:", alist2)
print("data4 is:", data4)