# 定义
def rectangle_area(width, height):
    area = width * height
    return area


r_area = rectangle_area(100.0, 50.0)
print("100*50的长方形面积是：{0:.2f}".format(r_area))


def triangle_area(width, height):
    area = 0.5 * width * height
    print('{0}*{1}三角形面积是：{2}'.format(width, height, area))


print(triangle_area(2.0, 4.0))
print(triangle_area(width=6.0, height=6.0))


# 默认参数值

def make_coffee(name='卡布奇诺'):
    return "制作一杯{}咖啡。".format(name)


coffee1 = make_coffee("拿铁")
coffee2 = make_coffee()
print(coffee1, coffee2)


# *可变参数
def sum(*numbers, multiple=1):
    total = 0.0
    for number in numbers:
        total += number
    return total * multiple


print(sum(100, 200, 500, 100, multiple=2))
double_tuple = (50.0, 60.0, 0.0)
print(sum(30, 50, *double_tuple, multiple=2))


# **可变参数, **可变参数必须在正规参数之后
def show_info(sep=":", **info):
    print("------info------")
    for key, value in info.items():
        print('{0}{2}{1}'.format(key, value, sep))


print(show_info('->', name='Tony', age=18, sex=True))
print(show_info(student_name='zch',student_id='1000'))

