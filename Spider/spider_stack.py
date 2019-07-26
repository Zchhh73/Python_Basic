import urllib.request
import hashlib
from bs4 import BeautifulSoup
import datetime
import os
import re
from Spider.stock_db import insert_hisq_data

url = 'https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'


def validateUpdate(html):
    '''
    验证数据是否更新，更新返回True，未更新返回False
    :param html:
    :return:
    '''
    # 创建md5对象
    md5obj = hashlib.md5()
    md5obj.update(html.encode(encoding='utf-8'))
    md5code = md5obj.hexdigest()
    print(md5code)

    # 对md5码操作
    old_md5code = ''
    f_name = 'md5.txt'
    if os.path.exists(f_name):
        with open(f_name, 'r', encoding='utf-8') as f:
            old_md5code = f.read()

    if md5code == old_md5code:
        print('数据没有更新！')
        return False
    else:
        # 将新的md5写入文件
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(md5code)
        print('数据更新')
        return True


req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    html = data.decode()
    sp = BeautifulSoup(html, 'html.parser')
    div = sp.select('div#quotes_content_left_pnlAJAX')
    divstring = div[0]

    if validateUpdate(divstring):
        trlist = sp.select('div#quotes_content_left_pnlAJAX table tbody tr')
        data = []
        for tr in trlist:
            trtext = tr.text.strip('\n\r')
            if trtext == '':
                continue
            rows = re.split(r'\s+', trtext)
            # print(rows)

            fields = {}
            fields['Date'] = rows[1]
            fields['Open'] = float(rows[2])
            fields['High'] = float(rows[3])
            fields['Low'] = float(rows[4])
            fields['Close'] = float(rows[5])
            fields['Volume'] = int(rows[6].replace(',', ''))
            data.append(fields)

        for row in data[1:]:
            row['Symbol'] = 'AAPL'
            insert_hisq_data(row)
