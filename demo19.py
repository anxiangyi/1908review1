'''
匿名函数:
   lambda 匿名函数
   1. 函数比较简单的时候
   2. 函数作为参数 ---》高阶函数： sorted()  max()   min()  filter()  map()

   格式： lambda 参数列表 ： 返回值
'''

func = lambda x, y: x + y

print(func)

result = func(1, 2)
print(result)

result = (lambda x, y, z: x + y - z)(1, 2, 3)
print(result)

list1 = [('d', 20), ('b', 15), ('c', 19), ('a', 22)]

result = sorted(list1)
print(result)

result = sorted(list1, key=lambda x: x[1], reverse=True)
print(result)

result = max(list1, key=lambda x: x[1])
print(result)

# 类型转换：

s = 'admin'
list2 = list(s)
# print(list2)
#
# print(str(list2))  #'['a', 'd', 'm', 'i', 'n']'
# print(''.join(list2))
#
# list2.reverse()
#
# print(list2)

print(list2[::-1])

tuple1 = (1, 3, 5, 7)

print(tuple1[::-1])

print('-----------')
for i in range(7,-1,-2):
    print(i)


import shutil

shutil.rmtree('c:/foo')