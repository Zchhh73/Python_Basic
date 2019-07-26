# datetime
# datetime 模块对time 模块进行了封装，提供了高级API.

import datetime

dt = datetime.datetime(2019, 6, 18, 18, 23, 34)
print(dt)

date = datetime.datetime.today()
print(date)

date1 = datetime.datetime.now()
print(date1)

date2 = datetime.datetime.utcnow()
print(date2)

d = datetime.date(2018, 2, 28)
print(d)

# 日期时间计算

date3 = datetime.date.today()
delta = datetime.timedelta(10)
d += delta
print(d)

# 时区
from datetime import datetime, timezone, timedelta

utc_dt = datetime(2018, 7, 3, 5, 0, 0, tzinfo=timezone.utc)
print(utc_dt)
