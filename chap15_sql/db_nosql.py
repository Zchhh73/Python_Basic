# 非关系型数据库的存储。
# coding:utf-8

# dbm数据存储方式类似于字典数据结构，通过键写入或读取数据。
import dbm

with dbm.open('mydb','c') as db:
    db['name']  = 'tony'
    print(db['name'].decode())

    age = int(db.get('age',b'18').decode())
    print(age)

    if 'age' in db:
        db['age'] = '20'

    del db['name']