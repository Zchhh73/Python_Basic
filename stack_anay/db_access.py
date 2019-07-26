import pymysql

def findall_hisq_data(symbol):
    '''根据ID差历史数据'''
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 database='nasdaq',
                                 charset='utf8')

    data = []
    try:
        with connection.cursor() as cursor:
            sql = 'select HDate,Open,High,Low,Close,Volume,Symbol from historicalquote where Symbol = %s'
            cursor.execute(sql,[symbol])
            resultset = cursor.fetchall()
            for row in resultset:
                fields={}
                fields['Date'] = row[0]
                fields['Open'] = float(row[1])
                fields['High'] = float(row[2])
                fields['Low'] = float(row[3])
                fields['Close'] = float(row[4])
                fields['Volume'] = row[5]
                data.append(fields)

    except pymysql.DatabaseError as error:
        print('数据查询失败' + error)
    finally:
        connection.close()
    return data

if __name__ == '__main__':
    data = findall_hisq_data('AAPL')
    print(data)