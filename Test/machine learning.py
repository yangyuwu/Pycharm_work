#!/usr/bin/env python
# -*--coding:utf-8 -*-
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

y = numpy.median(speed)
print(y)

speed2 = [99,86,87,88,86,103,87,94,78,77,85,86]
z = numpy.median(speed2)
print(z)

from scipy import stats
speed3 = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x3 = stats.mode(speed3)
print(x3)

x = numpy.std(speed)
print(x)

import numpy
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)

xxx = numpy.std(speed)

print(xxx)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)


xd = numpy.percentile(ages, 90)

print(xd)

'''
实例
创建一个包含 250 个介于 0 到 5 之间的随机浮点数的数组：

'''
import numpy

x = numpy.random.uniform(0.0, 5.0, 250)

print(x)

'''
直方图
为了可视化数据集，我们可以对收集的数据绘制直方图。

我们将使用 Python 模块 Matplotlib 绘制直方图：
'''
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()


import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()


















































































































































































































