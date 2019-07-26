import threading
import time

event = threading.Event()


class Stack:
    def __init__(self):
        self.pointer = 0
        self.data = [-1, -1, -1, -1, -1]

    def push(self, c):
        global event
        while self.pointer == len(self.data):
            event.wait()
        # 通知线程将数据出栈
        event.set()
        # 压栈
        self.data[self.pointer] = c
        self.pointer += 1

    def pop(self):
        global event
        # 无数据
        while self.pointer == 0:
            event.wait()
        event.set()
        self.pointer -= 1
        data = self.data[self.pointer]
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
