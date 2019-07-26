import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             database='MyDB',
                             charset='utf8')

# 有条件查询
# select name,userid from user where userid > ? order by userid
'''
try:
    with connection.cursor() as cursor:
        # 执行sql操作
        sql = 'select name,userid from user where userid > %(id)s'
        cursor.execute(sql, {'id': 0})
        # 提取结果集
        result_set = cursor.fetchall()
        for row in result_set:
            print('id : {0}-name:{1}'.format(row[1], row[0]))
finally:
    connection.close()
'''
#   无条件查询
try:
    with connection.cursor() as cursor:
        sql = 'select max(userid) from user'
        cursor.execute(sql)

        #提取一条数据
        row = cursor.fetchone()

        if row is not None:
            print('最大用户id:{0}'.format(row[0]))
finally:
    connection.close()
