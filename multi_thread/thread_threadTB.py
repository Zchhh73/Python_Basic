import threading
import time


class TicketDB:
    def __init__(self):
        self.ticket_count = 5

    def get_ticket_count(self):
        return self.ticket_count

    def sell_ticket(self):
        time.sleep(1)
        print('第{0}号票已经售出'.format(self.ticket_count))
        self.ticket_count -= 1


db = TicketDB()
# 创建lock对象，互斥锁
lock = threading.Lock()


def thread1_body():
    global db, lock
    while True:
        #实现锁定
        lock.acquire()
        curr_ticket_count = db.get_ticket_count()
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            #解锁
            lock.release()
            break
        lock.release()
        time.sleep(1)

def thread2_body():
    global db,lock
    while True:
        lock.acquire();
        curr_ticket_count = db.get_ticket_count()
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            lock.release()
            break
        lock.release()
        time.sleep(1)


def main():
    t1 = threading.Thread(target=thread1_body)
    t1.start()
    t2 = threading.Thread(target=thread2_body)
    t2.start()

if __name__ == '__main__':
    main()

