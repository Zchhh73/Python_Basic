# 类的定义
class Animal(object):
    '''定义动物类'''

    def __init__(self, age, sex, weight):
        self.age = age
        self.sex = sex
        self.weight = weight


animal = Animal(2, 1, 10.0)

print('年龄：{0}'.format(animal.age))
print('性别：{0}'.format('雄性' if animal.sex == 0 else '雌性'))
print('体重：{0}'.format(animal.weight))


class Account:
    interest_rate = 0.0668  # 类变量，与实例无关

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

account = Account('zch',200000.0)
print('账户名：{0}'.format(account.owner))
print('存款：{0}'.format(account.amount))
print('利率：{0}'.format(Account.interest_rate))
print('ac1利率:{0}'.format(account.interest_rate))
print('ac1实例所有变量:{0}'.format(account.__dict__))