import urllib.request
import os
import re

url = 'http://p.weather.com.cn/'


def findallimageurl(htmlstr):
    '''
    从html中查找匹配的字符串
    :param htmlstr:
    :return:
    '''
    # 定义正则表达式
    pattern = r'http://\S+(?:\.png|\.jpg)'
    return re.findall(pattern, htmlstr)


def getfilename(urlstr):
    '''
    截取图片名
    :param urlstr:
    :return:
    '''
    pos = urlstr.rfind('/')
    return urlstr[pos + 1:]


url_list = []
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    url_list = findallimageurl(htmlstr)

for imagesrc in url_list:
    req = urllib.request.Request(imagesrc)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        # 过滤小于10KB的图片
        if len(data) < 1024 * 100:
            continue

        if not os.path.exists('download'):
            os.mkdir('download')

        filename = getfilename(imagesrc)
        filename = 'download/' + filename
        # 保存到本地
        with open(filename, 'wb') as f:
            f.write(data)
    print('下载图片：', filename)
