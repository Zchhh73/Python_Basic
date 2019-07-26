# lambda表达式Lambda 表达式本质上是一种匿名函数
# 医名函数也是函数，有函数类型，也可以创建函数对象。

# 结构：lambda 参数列表 ： Lambda体

def calculate_fun(opr):
    if opr == '+':
        return lambda a, b: (a + b)
    else:
        return lambda a, b: (a - b)


f1 = calculate_fun('+')
f2 = calculate_fun('-')

print('10 + 5 = {0}'.format(f1(10, 5)))
print('10 - 5 = {0}'.format(f2(10, 5)))

# filter()，它可以对可迭代对象的元素进行过滤。
users = ['zch', 'wsp', 'll', 'llz']
users_filter = filter(lambda u: u.startswith('z'), users)
print(list(users_filter))

number_list = range(1, 11)
number_filter = filter(lambda it: it % 2 == 0, number_list)
print(list(number_filter))

# map()、映射操作使用map()函数，它可以对可迭代对象的元素进行变换，
students = ['zch', 'wsp', 'll', 'llz']
students_map = map(lambda u: u.upper(), users)
print(list(students_map))

# reduce()聚合操作会将多个数据聚合起来输出单个数据，聚合操作中最基础的是归纳函数reduce(),
# reduce()函数会将多个数据按照指定的算法积累叠加起来，最后输出一个数据。
from functools import reduce

a = (1, 2, 3, 4)
a_reduce = reduce(lambda acc, i: acc + i, a)
print(a_reduce)
