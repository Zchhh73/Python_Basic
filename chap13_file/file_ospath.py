# os.path()
'''
os.path.abspath(path)  返回path的绝对路径
os.path.basename(path) 返回path路径的基础名部分
os.path.dirname(path)  返回path路径中目录部分。
os.path.exists(path)   判断path文件是否存在。
os.path.isfile(path)   如果path是文件，则返回True
os.path.isdir(path)    如果path是目录，则返回True
os.path.getatime(path) 返回最后一次的访问时间
os.path.getmtime(path) 返回最后修改时间
os.path.getctime(path) 返回创建时间
os.path.getsize(path)  返回文件大小
'''

import os.path
from datetime import datetime

f_name = 'test.txt'
af_name = 'D:\pycodes\python_basic\chap13_file\\test.txt'

#返回基础名部分
basename = os.path.basename(af_name)
filename = basename.strip().split('.')[0]
print(filename)
print(basename)

#返回路径中目录部分
dirname = os.path.dirname(af_name)
every_dir = dirname.strip().split('\\')
print(dirname)
print(every_dir)

#返回绝对路径
print(os.path.abspath(f_name))

#返回文件大小
print(os.path.getsize(f_name))

#返回访问时间
atime = datetime.fromtimestamp(os.path.getatime(f_name))
print(atime)

print(os.path.isfile(dirname))
print(os.path.isdir(dirname))
print(os.path.isfile(f_name))
print(os.path.isdir(f_name))
print(os.path.exists(f_name))

