# 枚举类
# 定义枚举类
import enum


class WeekDays(enum.Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 10


day = WeekDays.FRIDAY
print(day)
print(day.value)
print(day.name)


# 限制枚举类
# 为了使枚举类常量成员只能使用整数类型，可以使用enum.IntEnum作为枚举父类。
# 为了防止常量成员值重复，可以为枚举类加上＠enum.unique 装饰器。
@enum.unique
class Numbers(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    TEN = 10


num = Numbers.ONE
print(num)
print(num.value)
print(num.name)

#使用枚举类
if day == WeekDays.MONDAY:
    print('working...')
elif day == WeekDays.FRIDAY:
    print('studying')
