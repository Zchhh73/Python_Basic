import pymysql


# 读数据
def read_max_userid():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 database='MyDB',
                                 charset='utf8')
    try:
        with connection.cursor() as cursor:
            sql = 'select max(userid) from user'
            cursor.execute(sql)

            # 提取一条数据
            row = cursor.fetchone()

            if row is not None:
                return row[0]
    finally:
        connection.close()


# 插入操作
def insert_userid():
    maxid = read_max_userid()
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 database='MyDB',
                                 charset='utf8')
    try:
        with connection.cursor() as cursor:
            sql = 'insert into user(userid,name) values(%s,%s)'
            nextid = maxid + 1
            name = 'LLH' + str(nextid)
            cursor.execute(sql, (nextid, name))
            connection.commit()
            print('数据插入成功！')
    except pymysql.DatabaseError:
        connection.rollback()
    finally:
        connection.close()


# 更新修改数据
def update_data():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 database='MyDB',
                                 charset='utf8')
    try:
        with connection.cursor() as cursor:
            sql = 'update user set name = %s where userid > %s'
            affectedcount = cursor.execute(sql, ('WSP', 2))
            print('影响的数据行数：{0}'.format(affectedcount))
            connection.commit()
    except pymysql.DatabaseError as e:
        connection.rollback()
        print(e)
    finally:
        connection.close()


# 查看数据库中数据
def findall_data():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 database='MyDB',
                                 charset='utf8')
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


# 删除数据
def delete_data():
    maxid = read_max_userid()
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 database='MyDB',
                                 charset='utf8')
    try:
        with connection.cursor() as cursor:
            sql = 'delete from user where userid = %s'
            affectedcount = cursor.execute(sql, (maxid))
            print('影响的数据行数：{0}'.format(affectedcount))
            connection.commit()

    except pymysql.DatabaseError as e:
        connection.rollback()
        print(e)
    finally:
        connection.close()


if __name__ == "__main__":
    delete_data()
    findall_data()
