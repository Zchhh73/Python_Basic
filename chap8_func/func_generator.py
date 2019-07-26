# 生成器
# 在一个函数中经常使用return关键字返回数据，但是有时候会使用yield 关键字返回数据。
# 使用yield关键字的函数返回的是一个生成器（generator）对象， 生成器对象是一种可法代对象。

'''
def square(num):
    n_list = []

    for i in range(1, num + 1):
        n_list.append(i * i)

    return n_list

for i in square(5):
    print(i,end=" ")
'''


def square2(num):
    for i in range(1, num + 1):
        yield i * i


n_seq = square2(6)
print(n_seq.__next__())
print(n_seq.__next__())
print(n_seq.__next__())
print(n_seq.__next__())
print(n_seq.__next__())
print(n_seq.__next__())

# 生成器函数通过yield返回数据，与return不同的是， return 语句一次返回所有数据，函数调用结束
# 而yield只返回一个元素数据，函数调用不会结束，只是暂停，直到＿next__()方法被调用，程序继续执行yield 语句之后的代码

'''
生成器特别适合用于选历一些大序列对象，
它无须将对象的所有元素都载入内存后才开始进行操作，
仅在迭代至某个元素时才会将该元素载入内存。
'''