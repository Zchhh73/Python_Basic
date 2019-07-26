# 字符类
# 正则表达式中可以使用字符类，一个字符类定义一组字符，
# 其中的任－字符出现在输入字符串中即匹配成功

import re

p = r'[Jj]ava'
p1 = r'[^0123456789]'

m1 = re.search(p, 'I like Java and Python.')
print(m1)

m2 = re.search(p, 'I like JAVA and Python')
print(m2)

m3 = re.search(p, 'I like java and python')
print(m3)

# 字符串取反前加^
m4 = re.search(p1, '1000')
print(m4)

m5 =re.search(p1,'Python 3')
print(m5)

#区间
m6 = re.search(r'[A-Za-z0-9]','A10.3')
print(m6)

m7 = re.search(r'[0-25-7]','A3489C')
print(m7)

#预定义字符类
'''
.           匹配任意一个字符
\\          匹配反斜杠＼字符
\n          匹配换行
\r          匹配回车
\f          匹配换页符
\t          匹配水平制表符
\v          匹配垂直制表符
\s          匹配一个空格符，等价于［\t\n\r\f\v]
\S          匹配一个非空格符,等价于［^\s]
\d          匹配一个数字字符，等价于[0-9]
\D          匹配一个非数字字符，等价于［^0-9］
\w          匹配任何语言的单词字符,数字和下画线"_"等字符
\W          等价于［^\w]

'''
p = r'\D'
m = re.search(p,'1000')
print(m)

m = re.search(p,'Python 3')
print(m)

text = '你们好Hello'
m = re.search(r'\w',text)
print(m)
