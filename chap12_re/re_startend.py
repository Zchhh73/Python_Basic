# 3. 开始与结束字符
#      ^     $

import re

p1 = r'\w+@zhangchenhan\.com'
p2 = r'^\w+@zhangchenhan\.com$'

text = "Zch's email is z_ch9573@zhangchenhan.com."
m1 = re.search(p1, text)
print(m1)

m2 = re.search(p2, text)
print(m2)

email = 'z_ch9573@zhangchenhan.com'
m3 = re.search(p2, email)
print(m3)
