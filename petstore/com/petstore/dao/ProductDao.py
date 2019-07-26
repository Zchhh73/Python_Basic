# coding=utf-8

from petstore.com.petstore.dao.base_dao import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findall(self):
        '''查找所有'''
        products = []
        try:
            with self.conn.cursor() as cursor:
                sql = 'select productid,category,cname,ename,image,listprice,unitcost,descn from products'
                cursor.execute(sql)
                result_set = cursor.fetchall()
                for row in result_set:
                    product = {}
                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listproce'] = row[5]
                    product['unitcost'] = row[6]
                    product['descn'] = row[7]
                    products.append(product)
        finally:
            self.close()
        return products

    def findbycat(self, catname):
        '''按分类查找'''
        products = []
        try:
            with self.conn.cursor() as cursor:
                sql = 'select productid,category,cname,ename,image,listprice,unitcost,descn from products where category=%s'
                cursor.execute(sql, catname)
                result_set = cursor.fetchall()
                for row in result_set:
                    product = {}
                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listproce'] = row[5]
                    product['unitcost'] = row[6]
                    product['descn'] = row[7]
                    products.append(product)
        finally:
            self.close()

        return products

    def findbyid(self, productid):
        '''按商品ID查找'''
        product = None
        try:
            with self.conn.cursor() as cursor:
                sql = 'select productid,category,cname,ename,image,listprice,unitcost,descn from products where productid=%s'
                cursor.execute(sql, productid)
                row = cursor.fetchone()
                if row is not None:
                    product = {}
                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listproce'] = row[5]
                    product['unitcost'] = row[6]
                    product['descn'] = row[7]
        finally:
            self.close()

        return product


if __name__ == '__main__':
    dao = ProductDao()
    product2 = dao.findbycat('鸟类')
    print(product2)
