# 线程间通信，线程之间存在依赖关系。需互相协调完成任务。
# Condition实现线程间通信问题。

# 生产消费线程
import threading
import time
import random

condition = threading.Condition()


class Stack:
    def __init__(self):
        self.pointer = 0
        # -1代表没有数据
        self.data = [-1, -1, -1, -1, -1]

    # 压栈方法
    def push(self, c):
        global condition
        condition.acquire()
        # 堆栈已满，不能压栈
        while self.pointer == len(self.data):
            # 等待其他线程将数据出栈
            condition.wait()
        # 通知线程数据出栈
        condition.notify()
        # 数据压栈
        self.data[self.pointer] = c
        self.pointer += 1
        condition.release()

    # 出栈方法
    def pop(self):
        global condition
        condition.acquire()
        # 无数据，不能出栈
        while self.pointer == 0:
            # 等待其他线程将数据压栈
            condition.wait()
        # 通知其他线程将数据压栈
        condition.notify()
        self.pointer -= 1
        data = self.data[self.pointer]
        condition.release()
        return data


stack = Stack()


def producer_thread_body():
    global stack
    for i in range(0, 10):
        stack.push(i)
        print('生产：{0}'.format(i))
        time.sleep(1)


def consumer_thread_body():
    global stack
    for i in range(0, 10):
        x = stack.pop()
        print('消费:{0}'.format(x))
        time.sleep(1)


def main():
    producer = threading.Thread(target=producer_thread_body)
    producer.start()
    consumer = threading.Thread(target=consumer_thread_body)
    consumer.start()


if __name__ == '__main__':
    main()
