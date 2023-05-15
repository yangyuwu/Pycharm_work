'''
Python 基本用法
author:wyy
time: 23/8/2022
W3school python学习教程
学习网址：https://www.w3school.com.cn/python/python_modules.asp
'''

# 内容：Python 实现经典的快速排序算法例子
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]  # 经过查阅得到 “/”是浮点数除法，但是在此程序中需要整除，所以要用“%”或者“//”
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

xxs = quicksort([3,6,8,10,1,2,1])
print(xxs)

# 列表(lists)
xs= [3,1,2,45,5,6]
print(xs)
print(xs[2])
print(xs[-1])

xs[2]='foo' #列表可以包含不同类型的元素
xs.append('bar,bus')  # 添加新元素到列表末端
print(xs)
xs.pop()
print(xs)

# 循环(Loops)
for an in xs:
    print(an)
#想要在循环体内访问每个元素的指针，可以使用内置的枚举(enumerate)函数
for idx,an in enumerate(xs):
    print('#%d:%s' %(idx + 1,an))

nums = [0,1,2,3,4,5]
squares = []
for x in nums:
    squares.append(x**2)
print(squares)
#列表解析(list comprehension)
nums = [0,1,2,3,4,5]
squares = [x**2 for x in nums]
print(squares)
#列表解析也可以包含条件语句
nums = [0,1,2,3,4,5]
even_squares = [x**2 for x in nums if x % 2==0]
print(even_squares)

'''
字典
是 Python 提供的一种常用的数据结构，它用于存放具有映射关系的数据；

为了保存具有映射关系的数据，Python 提供了字典，字典相当于保存了
两组数据，其中一组数据是关键数据，被称为 key；另一组数据可通过 
key 来访问，被称为 value。

由于字典中的 key 是非常关键的数据，而且程序需要通过 key 来访问 value，因此字典中的 key 不允许重复。

程序既可使用花括号语法来创建字典，也可使用 dict() 函数来创建字典。实际上，dict 是一种类型，它就是 Python 中的字典类型。
'''
scores = {'语文': 89, '数学': 92, '英语': 93}
print(scores)
print(scores['语文'])
# 空的花括号代表空的dict
empty_dict = {}
print(empty_dict)
# 使用元组作为dict的key
dict2 = {(20, 30):'good', 30:'bad'}
print(dict2)

for an,legs in scores.items():
    print('%s : %d 分'%(an,legs))

"""
+ 字典解析
  和列表解析类似，字典机械允许你轻松地构造字典，如下：
"""
even_num_to_square = {x: x**2 for x in nums if x % 2 ==0}
print(even_num_to_square)

"""
+ 集合(sets)
  + 集合存放着无序的不同元素，在python中，集合使用花括号表示，
  + 集合添加元素是用**.add(),而不是用**.append(),这个是针对列表的
"""
animals = {'cat','dog','pig','duck','tiger','河马'}
print('河马' in animals)
print('fish' in animals)
animals.add('fish')
print('fish' in animals)
animals.add('Camel')
print('Camel' in animals)

animals.remove('fish')
print(len(animals))
print(animals)

# 集合循环
for idx,animal in enumerate(animals):
    print('%d:%s'%(idx+1,animal))

# 集合解析（Set Comprehension）
from math import sqrt
print({int(sqrt(x)) for x in range(30)})

"""
+ 元组(tuples)
  + 元组是一个（不可改变）有序列表
  + 元组可以像字典一样使用键值对，并且还可以作为集合中的元素，而列表不行
"""
#通过元组创建字典
d = {(x,x+1):x for x in range(10)}
t=(5,6)
print(type(t))
print(d[t])
print(d[(1,2)])

'''
+ 函数(functions)
 + def 来定义函数
'''
def sign(x):
     if x > 0:
         return '正数'
     elif x < 0:
         return '负数'
     else:
         return '零'
for x in [-1,0,2,4,-1]:
    print(sign(x))

def hello(name,loud = False):
    if loud:
        print('HELLO,%s' %name.upper())
    else:
        print('HELLO,%s!' %name)
hello('Bob')
hello('Tracy',loud = True)
hello('Red',loud = False)

"""
+ 类（Classes）
  - 在python中，定义类的语法很直接，如下：
"""
class Greeter:
    # 构造函数
    def __init__(self,name):
        self.name = name  # 创建一个变量实例

    #实例用法
    def greet(self,loud = False):
        if loud:
            print('HELLO,%s' % self.name.upper())
        else:
            print('HELLO,%s!' % self.name)

g = Greeter('Fred')  # 创建一个Greeter类实例
g.greet()            # 调用实例方法，打印“Hello,Fred”
g.greet(loud = True) # 调用实例方法，打印“HELLO,FRED!”

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
      print("Hello my name is " + self.name)

p1 = Person("Bill", 63)

print(p1.name)
print(p1.age)
p1.myfunc()

'''
self 参数
self 参数是对类的当前实例的引用，用于访问属于该类的变量。

它不必被命名为 self，您可以随意调用它，但它必须是类中任意函数的首个参数：

实例
使用单词 mysillyobject 和 abc 代替 self：
'''
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
    print("my age is: %d" % abc.age)

p1 = Person("Tracy", 60)
p1.myfunc()
#print(p1.age)

p1.age = 40
p1.myfunc()
#print(p1.age)

'''
Python Lambda:
lambda 函数是一种小的匿名函数。

lambda 函数可接受任意数量的参数，但只能有一个表达式。

'''
x = lambda a : a + 10  # 接受一个参数，一个表达式
print(x(5))

sx = lambda a, b : a * b  # 接受两个参数，一个表达式
print(sx(5, 6))

tx = lambda a, b, c : a + b + c  # 接受三个参数，一个表达式
print(tx(5, 6, 2))

'''
为何使用 Lambda 函数？
当您把 lambda 用作另一个函数内的匿名函数时，会更好地展现 lambda 的强大能力。
假设您有一个带一个参数的函数定义，并且该参数将乘以未知数字：
'''
def myfunc(n):
  return lambda a : a * n
'''
使用该函数定义来创建一个总是使所发送数字加倍的函数：
'''
mydoubler = myfunc(2)
'''
使用相同的函数定义来创建一个总是使您发送的数字增加三倍的函数：
'''
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))


def my_function(country = "China"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# 递归
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results：")
tri_recursion(6)

'''
什么是模块？
请思考与代码库类似的模块。
模块是包含一组函数的文件，希望在应用程序中引用。

创建模块
如需创建模块，只需将所需代码保存在文件扩展名为 mymodule.py 的文件中：
'''
import mymodule
mymodule.greeting('Bill')
a = mymodule.person1["age"]
print(a)

'''
重命名模块
您可以在导入模块时使用 as 关键字创建别名：
'''
import mymodule as mx
b = mx.person1["country"]
print(b)

import platform
xx = platform.system()
print(xx)

'''
使用 dir() 函数
有一个内置函数可以列出模块中的所有函数名（或变量名）。dir() 函数：
'''
x = dir(platform)
print(x)
y = dir(mx)
print(y)

'''
从模块导入
您可以使用 from 关键字选择仅从模块导入部件。
实例
名为 mymodule 的模块拥有一个函数和一个字典：
仅从模块导入 person1 字典：
'''
from mymodule import person1
print (person1["age"])

import datetime

t = datetime.datetime.now()
print(t)

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

print('**********************************************************************')

'''
JSON 是用于存储和交换数据的语法。
JSON 是用 JavaScript 对象表示法（JavaScript object notation）编写的文本。
Python 中的 JSON
Python 有一个名为 json 的内置包，可用于处理 JSON 数据。
'''
import json
# 一些 JSON:
jx =  '{ "name":"Bill", "age":63, "city":"Seatle"}'

# 解析 x:
y = json.loads(jx)

# 结果是 Python 字典：
print(y["age"])

'''
把 Python 转换为 JSON
若有 Python 对象，则可以使用 json.dumps() 方法将其转换为 JSON 字符串。

实例
把 Python 转换为 JSON：
'''
import json

# Python 对象（字典）：
x = {
  "name": "Bill",
  "age": 63,
  "city": "Seatle"
}

# 转换为 JSON：
y = json.dumps(x)

# 结果是 JSON 字符串：
print(y)
print('**********************************************************************')
import json

x = {
  "name": "Bill",
  "age": 63,
  "married": True,
  "divorced": False,
  "children": ("Jennifer","Rory","Phoebe"),
  "pets": None,
  "cars": [
    {"model": "Porsche", "mpg": 38.2},
    {"model": "BMW M5", "mpg": 26.9}
  ]
}

print(json.dumps(x))

json.dumps(x, indent=4)
json.dumps(x, indent=4, sort_keys=True)
print(json.dumps(x))

print('**********************************************************************')
'''
RegEx 或正则表达式是形成搜索模式的字符序列。
RegEx 可用于检查字符串是否包含指定的搜索模式。

RegEx 模块
Python 提供名为 re 的内置包，可用于处理正则表达式。

实例
检索字符串以查看它是否以 "China" 开头并以 "country" 结尾：
'''
import re

txt = "China is a great country"
rx = re.search("^China.*country$", txt)
print(rx)
x = re.findall("a", txt)
print(x)

ssx = re.search("\s", txt)

print("The first white-space character is located in position:", ssx.start())

sub_x = re.sub("\s", "9", txt)
print(sub_x)

# 打印匹配的字符串部分。
# 正则表达式查找以大写 "C" 开头的任何单词：
x = re.search(r"\bC\w+", txt)
print(x.group())

'''
format
为了确保字符串按预期显示，我们可以使用 format() 方法对结果进行格式化。
'''
price = 52
txet = "The price is {} dollars"
print(txet.format(price))
print('**********************************************************************')
quantity = 3
itemno = 567
price = 52
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

'''
索引号
您可以使用索引号（花括号 {0} 内的数字）来确保将值放在正确的占位符中：
'''

quantity = 3
itemno = 567
price = 52
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# 此外，如果要多次引用相同的值，请使用索引号：
age = 63
name = "Bill"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

'''
命名索引
您还可以通过在花括号 {carname} 中输入名称来使用命名索引，但是在传递参数值 txt.format(carname = "Ford") 时，必须使用名称：
'''
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Porsche", model = "911"))






































































































