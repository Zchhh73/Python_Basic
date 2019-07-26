import pymysql
from petstore.com.petstore.dao.base_dao import BaseDao


class OrderDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findall(self):
        '''查找所有'''
        orders = []
        try:
            with self.conn.cursor() as cursor:
                sql = 'select orderid,userid,orderdate from orders'
                cursor.execute(sql)
                result_set = cursor.fetchall()
                for row in result_set:
                    order = {}
                    order['orderid'] = row[0]
                    order['userid'] = row[1]
                    order['orderdate'] = row[2]
                    orders.append(order)
        finally:
            self.close()

        return orders

    def create(self,order):
        '''创建订单'''
        try:
            with self.conn.cursor() as cursor:
                sql = 'insert into orders(orderid,userid,orderdate,status,amount) values(%s,%s,%s,%s,%s)'
                affectedcount = cursor.execute(sql,order)
                print('成功插入{0}条数据'.format(affectedcount))
                self.conn.commit()
        except pymysql.DatabaseError as e:
            self.conn.rollback()
            print(e)
        finally:
            self.close()

