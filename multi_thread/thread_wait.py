import threading
import time

# 等待线程结束采用join()方法。

value = 0


def thread_body():
    global value
    print("ThreadA 开始...")
    for n in range(2):
        print("ThreadA执行...")
        value += 1
        time.sleep(1)
    print('ThreadA结束..')


def main():
    print('主线程开始..')
    t1 = threading.Thread(target=thread_body, name="ThreadA")
    t1.start()
    # 应用场景：一个线程依赖另一个线程的结果
    t1.join()
    print('value = {0}'.format(value))
    print('主线程结束')


if __name__ == '__main__':
    main()
