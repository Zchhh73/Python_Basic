a = ('Hello', 'World', 1, 2, 3)

'''
print(a[1])
print(a[1:3])
print(a[2:])
print(a[:2])


str1, str2, n1, n2, n3 = a
str1, str2, *n = a
print(str1, str2, n1, n2, n3)
print(*n)
'''
# 遍历元组
a = (21, 32, 43, 54)
for item in a:
    print(item)
print('-------------')
#enumrate(a)可以获得元组对象，有两个元素，索引和数值
for i, item in enumerate(a):
    print('{0} - {1}'.format(i,item))