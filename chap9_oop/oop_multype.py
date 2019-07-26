# 多态性
# 两个前提条件：第一.继承;多态发生一定是子类和父类之间；
# 第二.重写;子类重写了父类的方法。

class Figure:
    def draw(self):
        print('绘制...')


class Ellipse(Figure):
    def draw(self):
        print('绘制椭圆...')


class Triangle(Figure):
    def draw(self):
        print('绘制Triangle')


f1 = Figure()
f1.draw()

f2 = Ellipse()
f2.draw()

f3 = Triangle()
f3.draw()

# 类型检查
print(isinstance(f1, Triangle))
print(isinstance(f2, Triangle))
print(isinstance(f3, Triangle))
print(isinstance(f2, Figure))

# 子类检查
print(issubclass(Ellipse, Triangle))
print(issubclass(Ellipse, Figure))
print(issubclass(Triangle, Ellipse))


# 鸭子类型
# 在动态语言中有一种类型检查称为“鸭子类型”
# 鸭子类型不关注变量的类型，而是关注变量具有的方法

class Animal(object):
    def run(self):
        print('动物跑..')


class Dog(Animal):
    def run(self):
        print('狗狗跑..')


class Car:
    def run(self):
        print('汽车跑..')


def go(animal):
    animal.run()


go(Animal())
go(Dog())
go(Car())
