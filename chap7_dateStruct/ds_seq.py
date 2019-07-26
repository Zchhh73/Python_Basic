#索引操作
'''
序列中第一个元素的索引是0 ，其他元素的索引是第一个元素的偏移量。
有正偏移量，称为正值索号；
也有负偏移量，称为负值索引。
正值索引的最后一个元素索引是“序列长度-1”
'''
a = 'Hello'
'''
print(a[0])
print(a[1])
print(a[4])

print(a[-1])
print(a[-3])

print(max(a))
print(min(a))
print(len(a))

print(a*3)

a += " "
a += 'World'
print(a)
'''

print(a[1:3])
print(a[:3])
print(a[0:3])
print(a[0:])
print(a[0:5])
print(a[:])
print(a[1:-1])


print(a[1:5])
#步长
print(a[1:5:2])