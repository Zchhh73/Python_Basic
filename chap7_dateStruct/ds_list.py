# 列表具有可变性，可以追加，插入，删除和替换
a = [10]
# print(type(a))
# print(list((10, 20, 30, 40)))

student_list = ['zch', 'llz']
'''
追加元素
student_list.append("ll")
print(student_list)
student_list += ['wsp','lyh']
print(student_list)
student_list.extend(['jm','hyb'])
print(sorted(student_list))


# 插入元素
student_list.insert(1, 'll')
print(student_list)

# 替换元素
student_list[0] = 'hyb'
print(student_list)

# 删除元素
student_list.remove('ll')
print(student_list)

student_list.pop(0)
print(student_list)

# 倒置列表
b = [21, 32, 43, 54]
b.reverse()
print(b)

#复制列表
c = b.copy()
print(c)
#清空列表
b.clear()
print(b)
#统计次数
c.append(21)
print(c.count(21))

#查找索引
print(student_list.index('ll'))
'''
#列表推导式
#0-9偶数的平方数列
n_list = []
for x in range(10):
    if x % 2 == 0:
        n_list.append(x ** 2)
print(n_list)

m_list = [x**2 for x in range(100) if x % 2 == 1]
print(m_list)