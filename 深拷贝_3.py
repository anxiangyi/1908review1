'''
copy.deepcopy()

两个列表中可变类型会各自使用各自（只要使用深拷贝，可变类型就会新建一份放到备份列表）
备份列表中的可变类型地址与原列表中的可变类型的地址是不同的。

而浅拷贝： 原列表与备份列表使用的是同一个可变类型的地址

不可变类型与浅拷贝相同
'''

import copy

list1 = ['郭德纲', 50, ['岳云鹏', '张云雷', '孟鹤堂']]

list2 = copy.deepcopy(list1)
# 31849352 31883464
print(id(list1), id(list2))
print(list1)
print(list2)

for i in list1:
    print(id(i), end='\t')

print('')
for i in list2:
    print(id(i), end='\t')

print('')

print('*' * 50)
list1[2].append('郭麒麟')
print(list1)
print(list2)

for i in list1:
    print(id(i), end='\t')

print('')
for i in list2:
    print(id(i), end='\t')

print('')

print('*' * 50)

list1[0] = '于谦'
list2[1] = 60

print(list1)
print(list2)

for i in list1:
    print(id(i), end='\t')

print('')
for i in list2:
    print(id(i), end='\t')

# list2 = list1[:]
