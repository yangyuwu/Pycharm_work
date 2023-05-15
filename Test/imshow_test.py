#!/usr/bin/env python
# -*--coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt
# 读取图片
img = cv2.imread('test.jpg', 0)

plt.subplot(2,2,1)
plt.imshow(img)
plt.title('pic 1')

plt.subplot(2,2,2)
plt.imshow(img, cmap='Greens_r')
plt.title('pic 2')

plt.subplot(2,2,3)
plt.imshow(img, cmap='Blues_r')
plt.title('pic 3')
plt.xticks([])#加备注信息，可以省略
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(img, cmap='gray')
plt.title('pic 4')
plt.xticks([])
plt.yticks([])

plt.savefig('plt.png')#保存图片
plt.show()



