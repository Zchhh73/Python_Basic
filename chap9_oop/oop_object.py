# 跟类--object
# __str()__:返回该对象的字符串表示
# _eq__(other):其他对象是否相等

# __str()__为了日志输出等处理方便，所有的对象都可以输出自己的描述信息
# 可以重写__str__()方法。

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        template = 'Person [name = {0},age = {1}]'
        s = template.format(self.name, self.age)
        return s


person = Person('Tony', 18)
print(person)

# __eq__()为了比较两个Person 对象是否相等,则需要
# 重写__eq__()方法

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        template = 'Person [name = {0},age = {1}]'
        s = template.format(self.name, self.age)
        return s
    '''
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False
    '''
p1 = Person('Tony',18)
p2 = Person('Zch',24)

print(p1 ==p2)