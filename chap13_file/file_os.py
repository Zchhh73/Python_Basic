# os模块
# os.rename(src,dst) 修改文件名,src是源文件,dst是目标文件，它们都可以是相对当前路径或绝对路径表示的文件。
# os.remove(path) 删除path所指的文件
# os.mkdir(path) 创建path所指的目录
# os.rmdir(path) 删除path所指的目录
# os.walk(top) 遍历top所指的目录树，返回值是一个三元组（目录路径，目录列表名，文件名列表）
# os.listdir(dir) 列出指定目录中的文件和子目录。
# os.curdir 获得当前目录。
# os.pardir 获得当前父目录。

import os
f_name = 'test.txt'
copy_f_name = 'copy1.txt'

with open(f_name,'r') as f:
    b = f.read()
    with open(copy_f_name,'w') as copy_f:
        copy_f.write(b)
    try:
        os.rename(copy_f_name,'copy2.txt')
    except OSError:
        os.remove('copy2.txt')
print(os.listdir(os.curdir))
print(os.listdir(os.pardir))

try:
    os.mkdir('subdir')
except OSError:
    os.rmdir('subdir')

for item in os.walk('.'):
    print(item)