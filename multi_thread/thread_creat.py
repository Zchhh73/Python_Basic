'''
创建线程的两个要素：
(1)线程对象
(2)线程体
    提供线程体的方式：
    (1) 自定义函数
    (2) 继承Thread的run(),run()为线程体
'''

# 自定义函数
import threading
import time


def thread_body():
    t = threading.current_thread()
    for n in range(5):
        print('第{0}次执行线程{1}\n'.format(n, t.name))
        time.sleep(1)
    print('线程{0}执行完成!'.format(t.name))


def main():
    t1 = threading.Thread(target=thread_body,name='FirstThread')
    t1.start()

    t2 = threading.Thread(target=thread_body, name='MyThread')
    t2.start()


if __name__ == '__main__':
    main()
