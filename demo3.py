# 可变与不可变
# 不可变：  值改变，地址也发生改变了，说明此类型是不可变   int  str  tuple
# 可变:  值改变了，但是地址没有改变   可变的类型      list  dict  set


'''
  小整数对象池
  字符串驻留区

'''
a = 1
print(id(a))
a = 2
print(id(a))

name = 'admin'
print(id(name))
name = 'admin1'
print(id(name))

b = 2
print(id(b))
print(a == b)

n = 'admin1'
print(name == n)

list1 = [1, 2, 3]
print(id(list1))

list1.append(5)

print(list1)
print(id(list1))




