# 量词
'''
量词的使用
？     0次或1次
*      0次或多次
+      1次或多次
{n}    n次
{n,m}  [n,m）次
{n,}   至少出现n次
'''

import re

m = re.search(r'\d?', '87654321')  # 匹配8
print(m)

m1 = re.search(r'\d?', 'ABC')  # 匹配""
print(m1)

m2 = re.search(r'\d*', '8765432')  # 匹配所有
print(m2)

m3 = re.search(r'\d*', 'ABC')  # 匹配""
print(m3)

m4 = re.search(r'\d+', '87654321')  # 匹配所有
print(m4)

m5 = re.search(r'\d+', 'ABC')  # 不匹配
print(m5)

m6 = re.search(r'\d{8}', '87654321')  # 匹配所有
print(m6)

m7 = re.search(r'\d{8}', 'ABC')  # 不匹配
print(m7)

m8 = re.search(r'\d{4,5}', '87654321')  # 匹配前5个
print(m8)

m9 = re.search(r'\d{9，}', '87654321')  # 不匹配
print(m9)

# 贪婪量词，懒惰量词
greedy_m = re.search(r'\d{5,8}', '87654321')  # 匹配多的
print(greedy_m)

lazy_m = re.search(r'\d{5,8}?', '87654321')  # 匹配少的
print(lazy_m)
