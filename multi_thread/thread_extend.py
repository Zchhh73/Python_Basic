import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    def run(self):
        t = threading.current_thread()
        for n in range(5):
            print('第{0}次执行进程{1}'.format(n,t.name))
            time.sleep(1)
        print('线程{0}执行完成！'.format(t.name))

def main():
   t1 = MyThread()
   t1.start()
   t2 = MyThread(name='Mythread')
   t2.start()

if __name__ == '__main__':
    main()
