# 释放资源
# 可以使用finally 代码块或w地as 自动资源管理
# 无论try 正常结束还是except 异常结束都会执行finally代码块

import datetime as dt


def read_date_from_file(filename):
    try:
        file = open(filename)
        in_date = file.read()
        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except ValueError as e:
        print('处理ValueError异常')
        print(e)
    finally:
        file.close()


date = read_date_from_file('readme.txt')
print('日期 = {0}'.format(date))
