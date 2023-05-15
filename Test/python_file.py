#!/usr/bin/env python
# -*--coding:utf-8 -*-
'''
Python 文件处理
author:wyy
time: 23/8/2022
W3school python文件处理
学习网址：https://www.w3school.com.cn/python/python_modules.asp
'''
f = open("demofile.txt","r")

print(f.read(5))
print(f.readline())
print(f.readline())

print(f.read())

print('******************************************************************************')
'''
通过循环遍历文件中的行，您可以逐行读取整个文件：
'''
f = open("demofile.txt", "r")
for x in f:
  print(x)

print(f.readline())
f.close()

print('******************************************************************************')
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# 追加后，打开并读取该文件：
f = open("demofile2.txt", "r")
print(f.read())

print('******************************************************************************')
#ff = open("myfile.txt", "x")  # 创建名为 "myfile.txt" 的文件：
fff = open("myfile.txt", "a") # 将内容追加到文件中：
fff.write("Now the file has more content!") # 写入内容

# 写入后，打开并读取该文件：
f = open("myfile.txt", "r")
print(f.read())


'''
删除文件
'''
import os
os.remove("demofile2.txt")



















































