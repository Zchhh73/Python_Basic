# 编译正则表达式
# 编译的正则表达式可以重复使用，这样能减少正则表达式的解析和验证，提高效率。

import re

p = r'\w+@163\.com'

regex = re.compile(p)
text = "zch's email is 13671292697@163.com"
m = regex.search(text)
print(m)

p1 = r'[Jj]ava'
regex = re.compile(p1)
text2 = 'I like Java and java'
match_list = regex.findall(text2)
print(match_list)

match_iter = regex.finditer(text2)
for m in match_iter:
    print(m.group())

p2 = r'\d+'
regex = re.compile(p2)
text = 'AB1234CD56EF78GH'
match_list = regex.findall(text)
for num in match_list:
    print(num)

clist = regex.split(text)
print(clist)

# 忽略大小写
p3 = r'(Java).*(python)'
regex = re.compile(p3, re.I)

m1 = regex.search('I like Java and python.')
print(m1)

m2 = regex.search('I like JAVA and python.')
print(m2)

m3 = regex.search('I like Java and Python.')
print(m3)

# re.dotall匹配换行符
p4 = r'.+'
regex = re.compile(p4, re.DOTALL)
m = regex.search('hello\nworld')
print(m)
