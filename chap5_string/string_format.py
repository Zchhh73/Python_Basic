name = 'zch'
age = 18
money = 1234.567
s =  '他的年龄是{0}岁。'.format(age)
print(s)
s1 = '{0}的年龄是{1}岁。'.format(name,age)
print(s1)
s2 = '{1}的年龄是{0}岁。'.format(age,name)
print(s2)
s3 = '{n}的年龄是{a}岁。'.format(n=name,a=age)
print(s3)

s4 = '{0}的年龄是{1:5d}岁。'.format(name,age)
print(s4)
s5 = '{0}今天的收入是是{1:f}元。'.format(name,money)
print(s5)
s6 = '{0}的年龄是{1:.2f}元。'.format(name,money)
print(s6)
s7 = '{0}的年龄是{1:4.3f}元。'.format(name,money)
print(s7)
