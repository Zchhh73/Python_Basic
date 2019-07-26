# 构造方法
# 。一init一（）方法也属于魔法方法。定义时它的第一个参数应该是self，其后的参数才是用来初始化实例变量的。
# 调用构造方法时不需要传入self。

class Animal(object):

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age
        self.sex = sex
        self.weight = weight

    # 实例方法
    def eat(self):
        self.weight += 0.5
        print('eat...')

    def run(self):
        self.weight -= 0.01
        print('run')


a1 = Animal(2, 0, 10.0)
a2 = Animal(1, weight=5.0)
a3 = Animal(1, sex=0)

print('a1年龄：{0}'.format(a1.age))
print('a2体重：{0}'.format(a2.weight))
print('a3性别：{0}'.format('雌性' if a3.sex == 0 else '雄性'))

print('a1体重：{0:0.2f}'.format(a1.weight))
a1.eat()
print('a1体重：{0:0.2f}'.format(a1.weight))
a1.run()
print('a1体重：{0:0.2f}'.format(a1.weight))


# 类方法
class Account:
    interest_rate = 0.0668

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt

    #静态方法
    '''
    类方法需要绑定类，静态方法不需要绑定类， 
    静态方法与类的相合度更加松散
    '''
    @staticmethod
    def interest_with(amt):
        return Account.interest_by(amt)

interest1 = Account.interest_by(12000.0)
print('计算利息:{0:.4f}'.format(interest1))
interest2 = Account.interest_with(12000.0)
print('计算利息:{0:.4f}'.format(interest2))


