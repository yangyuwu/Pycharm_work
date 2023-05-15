#!/usr/bin/env python
# -*--coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

a= np.array([2,2,3])
print(type(a))
print(a.shape)
print(a[0])
print(a[2])
print(a)
a[0] = 5
print(a)

b=np.array([[1,2,3],[2,4,5],[4,5,6]])
print(b)
aa=np.zeros((2,2))
bb=np.ones((3,3))
print(aa)
print(bb)

print('***************************************************')
x = np.arange(0,3*np.pi,0.1)
print(x)
y = np.sin(x)
print(y)
plt.plot(x,y)

plt.show()

print('***************************************************')
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')

plt.title('Sin and Cos')
plt.legend(['Sine','Cosine'])
plt.show()






