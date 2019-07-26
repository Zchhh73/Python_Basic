import urllib.parse
import urllib.request

url = 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png'

with urllib.request.urlopen(url) as response:
    data = response.read()
    f_name = 'download.png'
    with open(f_name,'wb') as f:
        f.write(data)
        print('文件下载成功。')

