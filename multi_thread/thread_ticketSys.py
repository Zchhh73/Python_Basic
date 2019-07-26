# 模拟销售机票系统

import threading
import time


class TicketDB:
    def __init__(self):
        self.ticket_count = 5

    def get_ticket_count(self):
        return self.ticket_count

    def sell_ticket(self):
        time.sleep(1)
        print("第{0}号票已经售出".format(self.ticket_count))
        self.ticket_count -= 1


db = TicketDB()


def thread1_body():
    global db
    while True:
        curr_ticket_count = db.get_ticket_count()
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            break


def thread2_body():
    global db
    while True:
        curr_ticket_count = db.get_ticket_count()
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            break


def main():
    t1 = threading.Thread(target=thread1_body)
    t1.start()
    t2 = threading.Thread(target=thread2_body)
    t2.start()


if __name__ == '__main__':
    main()
