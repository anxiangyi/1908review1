'''
可变:  list  set  dict
不可变: str int float bool tuple
 浅拷贝:
   1.list2 = list1.copy()
   2. import copy
      list3 = copy.copy(list1)
 复制原列表中一模一样的内容到一块新的地址中


 可变类型共用的是一个地址，无论哪一方对可变类型进行了添加或者删除操作，地址都不会发生改变，只不过地址变化
 不可变类型一开始的时候使用的也都是相同的地址，只要不可变类型中有发生改变，哪个列表发生改变
 则地址改变，对另一个列表没有元素地址改变。



'''
import copy

list1 = ['郭德纲', 50, ['岳云鹏', '张云雷', '孟鹤堂']]
# 备份
list2 = list1.copy()
# list3 = list1.copy()
list3 = copy.copy(list1)


print(id(list1), id(list2),id(list3))
print(list1)
print(list2)
print(list3)

for i in list1:
    print(id(i), end='\t')

print('')
for i in list2:
    print(id(i), end='\t')

print('')
for i in list3:
    print(id(i), end='\t')

# print()
# print('*' * 50)
#
# list1[0] = '于谦'
#
# list2[1] = 60
#
# for i in list1:
#     print(id(i), end='\t')
#
# print('')
# for i in list2:
#     print(id(i), end='\t')
#
# print()
# print('*' * 50)
#
# list1[2].append('郭麒麟')
#
# for i in list1:
#     print(id(i), end='\t')
#
# print('')
# for i in list2:
#     print(id(i), end='\t')


