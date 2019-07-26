# Python 函数的返回值也是比较灵活的， 主要有三种形式：无返回值、单一返回值和多返回

# 无返回值
def show_info(sep=":", **info):
    print("------info------")
    for key, value in info.items():
        print('{0}{2}{1}'.format(key, value, sep))


result1 = show_info('->', name='Tony', age=18, sex=True)
print(result1)


def sum(*numbers, multiple=1):
    if len(numbers) == 0:
        return
    total = 0.0
    for number in numbers:
        total += number
    return total * multiple


print(sum(multiple=2))


# 多返回值
def position(dt, speed):
    posx = speed[0] * dt
    posy = speed[1] * dt
    return (posx, posy)

move = position(60.0,(10,-5))
print('物体位移：（{0},{1}）'.format(move[0],move[1]))



