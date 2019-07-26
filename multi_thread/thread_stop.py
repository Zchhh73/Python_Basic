import threading
import time

isrunning = True


def thread_body():
    while isrunning:
        print('下载中...')
        time.sleep(5)
    print('下载完成')


def main():
    t1 = threading.Thread(target=thread_body)
    t1.start()
    command = input("请输入停止指令：")
    if command == 'exit':
        global isrunning
        isrunning = False


if __name__ == '__main__':
    main()
