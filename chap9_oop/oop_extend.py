# 继承性
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        template = 'Person [name = {0}, age = {1}]'
        s = template.format(self.name, self.age)
        return s


# 继承
class Student(Person):

    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school


# 重写方法
class Animal(object):

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age
        self.sex = sex
        self.weight = weight

    def eat(self):
        self.weight += 0.05
        print('吃...')

    def run(self):
        print('跑..')


class Dog(Animal):

    def eat(self):
        self.weight += 0.1
        print('狗狗吃...')


a1 = Dog(2, 0, 10.0)
a1.eat()
a1.run()


# 多继承
# 这个方案是， 当子类实例调用一个方法时，先从子类中查找，如果没有找到则查找父类。
# 父类的查找顺序是按照子类声明的父类列表从左到右查找，如果没有找到再找父类的父类，依次查找下去。
class ParentClass1:
    def run(self):
        print('ParentClass1 run...')


class ParentClass2:
    def run(self):
        print('ParentClass2 run...')


# 多继承方法
class SubClass1(ParentClass1, ParentClass2):
    pass


class SubClass2(ParentClass2, ParentClass1):
    pass


class SubClass3(ParentClass1, ParentClass2):
    def run(self):
        print('SubClass3 run...')


sub1 = SubClass1()
sub1.run()
sub2 = SubClass2()
sub2.run()
sub3 = SubClass3()
sub3.run()
