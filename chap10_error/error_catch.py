#捕获异常
import datetime as dt

def read_date(in_date):
    try:
        date = dt.datetime.strptime(in_date,'%Y-%m-%d')
        return date
    except ValueError as e:
        print('处理ValueError异常')
        print(e)

str_date = '2019-06-18'
print('日期 = {0}'.format(read_date(str_date)))


