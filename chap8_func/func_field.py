# 函数变量作用域
# 全局变量
x = 20


def print_value():
    x = 10
    print('func中x={0}'.format(x))
    return 1


print(print_value())
print('全局变量下= {0}'.format(x))

print('--------------------')
def print2_value():
    global x
    x = 10
    print('func中x={0}'.format(x))


print(print2_value())
print('全局变量下= {0}'.format(x))
