#coding utf-8

import threading

#当前线程对象
t = threading.current_thread()
# 打印
print(t.name)
print(threading.active_count())

t1 =threading.main_thread()
print(t1.name)