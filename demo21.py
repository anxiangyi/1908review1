'''
 os模块：
  os：

  os.path:

'''
import os
import sys

# os.mkdir('bbb')
# os.chdir('aaa')
#
# with open('test1.py','w') as ws:
#     pass

# os.rmdir('aaa')

# import shutil
#
# shutil.rmtree('aaa')

# print(sys.path)

print(os.listdir('./'))

result = os.path.isdir('demo21.py')
print(result)
# sys.path.insert(0,'')

path = os.path.abspath(__file__)  # 获取文件的绝对路径
print(path)

path1 = os.path.dirname(path)  # 获取当前文件的文件夹
print(path1)

result = os.path.join('./', 'demo21.py')  # 拼接
print(result)

result = os.path.split(path)  # 获取文件名
print(result[1])

result = os.path.splitext(path)  # 获取扩展名
print(result)

# python demo21.py 1
import sys

print(sys.argv) # 执行文件时参数

print(sys.path)  # 获取程序执行时查找路径

print(os.environ)  # 获取当前电脑的环境变量
print(os.environ.get('PATH'))