import pymysql
import datetime


def insert_hisq_data(row):
    '''在股票历史价格表中传入数据'''

    # 1.建立连接
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 database='nasdaq',
                                 charset='utf8')
    try:
        # 创建游标对象
        with connection.cursor() as cursor:
            # 执行sql
            sql = "insert into historicalquote(HDate,Open,High,Low,Close,Volume,Symbol) values('{0}',%(Open)s,%(High)s,%(Low)s,%(Close)s,%(Volume)s,%(Symbol)s)".format(
                datetime.datetime.strptime(row['Date'], '%m/%d/%Y'))
            affectedcount = cursor.execute(sql, row)
            print('影响的数据行数：{0}'.format(affectedcount))
            # 提交数据库事务
            connection.commit()
    except pymysql.DatabaseError as error:
        # 回滚数据库事务
        connection.rollback()
        print(error)
    finally:
        connection.close()
