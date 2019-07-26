# 函数式编程（ functional pro gramming）与面向对象编程一样都是一种编程范式，
# 函数式编程也称为面向函数的编程。

# 函数类型
def calculate_fun(opr):
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    if opr == '+':
        return add
    else:
        return sub


f1 = calculate_fun('+')
f2 = calculate_fun('-')
print('10 + 5 = {0}'.format(f1(10,5)))
print('10 - 5 = {0}'.format(f2(10,5)))
