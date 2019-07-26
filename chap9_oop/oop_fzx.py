# 私有变量
# 如果想让它们成为私有变量，可以在变量前加上双下画线'_'

class Animal(object):
    '''定义动物类'''

    def __init__(self, age, sex, weight):
        self.age = age
        self.sex = sex
        self.__weight = weight

    def eat(self):
        self.__weight += 0.05
        # 私有方法
        self.__run()
        print('eat...')

    def run(self):
        self.__weight -= 0.01
        print('run...')

    # 定义属性，通过setter,getter访问器访问
    @property  # getter
    def weight(self):
        return self.__weight

    @weight.setter  # setter
    def weight(self, weight):
        self.__weight = weight


a1 = Animal(2, 0, 10.0)
print("a1体重：{0:0.2f}".format(a1.weight))
a1.weight = 123.45
print("a1体重：{0:0.2f}".format(a1.weight))
