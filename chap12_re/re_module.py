# re模块
import re

# search()、match()
p = r'\w+@163\.com'

text = "Zch's email is 13671292697@163.com"
m = re.search(p, text)
print(m)

m = re.match(p, text)
print(m)

email = '13671292697@163.com'

s = re.search(p, email)
print(s)

s1 = re.match(p, email)
print(s1)

print('match对象几个方法：')
print(s1.group())
print(s1.start())
print(s1.end())
print(s1.span())

# findall()和finditer()函数
# findall()在输入字符串中查找所有匹配内容,如果匹配成功,则返回match列表对象.
# finditer()如果匹配成功,则返回容纳match的可选代对象，
p1 = r'[Jj]ava'
text = 'I like Java and java.'
match_list = re.findall(p1, text)
print(match_list)

match_iter = re.finditer(p1, text)
for m in match_iter:
    print(m.group())

# 字符串分割
p2 = r'\d+'
text = 'AB1234CD56EF'

clist = re.split(p2, text)
clist1 = re.split(p2, text, maxsplit=1)
clist2 = re.split(p2, text, maxsplit=2)

print(clist)
print(clist1)
print(clist2)

# 字符串替换
p2 = r'\d+'
text1 = 'ABCD12EF34GH56'
replace_text = re.sub(p2, ' ', text1)
replace_text1 = re.sub(p2, ' ', text1, count=1)
replace_text2 = re.sub(p2, ' ', text1, count=2)
print(replace_text)
print(replace_text1)
print(replace_text2)

