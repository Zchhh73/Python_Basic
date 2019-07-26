import random

# random模块
# （0,1）的随机数
print('(0,1)的随机数')
for i in range(0, 10):
    x = random.random()
    print(x)

print('(0,5)的随机数')
for i in range(0, 10):
    x = random.randrange(5)
    print(x, end=" ")
print('\n')
print('(5,10)的随机数')
for i in range(0, 10):
    x = random.randrange(5, 10)
    print(x, end=" ")
