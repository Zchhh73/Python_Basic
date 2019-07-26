# 文件操作

# 打开文件
# 参数；r   只读打开文件
#      w   写入打开文件 会覆盖
#      x   独占创建，创建+写入
#      a   追加模式，追加文件末尾
#      b   二进制模式
#      t   文本模式

f = open('test.txt', 'w+')
f.write('World')

f = open('test.txt', 'r+')      #读
f.write('Hello')                #覆盖World

f = open('test.txt', 'a')
f.write(' ')

fname = r'D:\pycodes\python_basic\chap13_file\test.txt'
f = open(fname, 'a+')
f.write('World')


