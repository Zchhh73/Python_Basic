# URL(Uniform Resource Locator)统一资源定位器
import urllib.request
import urllib.parse

''' 
打开网站
with urllib.request.urlopen("http://www.baidu.com") as response:
    读取数据，字节序列数据
    data = response.read()
    转化为字符串
    html = data.decode()
    print(html)
'''

# 发送GET请求
url = 'http://www.51work6.com/service/mynotes/WebService.php'
params_dict = {'email': '13671292697@163.com', 'type': 'JSON', 'action': 'query'}
params_str = urllib.parse.urlencode(params_dict)
print(params_str)

# url = url + '?' + params_str
# print(url)

# req = urllib.request.Request(url)
# with urllib.request.urlopen(req) as response:
#   data = response.read()
#  json_data = data.decode()
#  print(json_data)

# 发送POST请求
# 转化为字节序列对象
params_bytes = params_str.encode()

req = urllib.request.Request(url, data=params_bytes)
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    print(json_data)
