'''
浅拷贝和深拷贝区别：
   对于不可变类型来说，发生改变不会影响拷贝的那一份。

  浅拷贝中的可变类型变量是共享，只要一个发生改变则另一个也跟着发生改变
  深拷贝中 的可变类型是各自拥有一份，其中一个发生改变对另外的不会产生影响

哪些是浅拷贝？
 copy.copy()
 list1.copy()
 切片操作

'''
import copy

list1 = ['一帆', 20, ['红烧肉', '炖猪蹄', '啤酒']]

list2 = copy.copy(list1)

print(id(list1), id(list2))
print(list1, list2)

list1[0] = '王一帆'

print(list1, list2)
list1[2].append('羊肉串')

print(list1, list2)

print('*' * 50)

list3 = copy.deepcopy(list1)
print(id(list1), id(list3))

print(list1, list3)

list3[1] = 21
print(list1, list3)

list3[2].remove('炖猪蹄')

print(list1, list3)

#
# list1.copy()
# {'1':'aa'}.copy()

list4 = [1, 2, 3, [4, 5]]

list5 = list4[::]

list6 = list4

print(list4, list5, list6)

print(id(list4), id(list5), id(list6))

list5[3].append(8)

print(list4, list5, list6)
