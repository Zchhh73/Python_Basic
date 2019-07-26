# 分组 189
import re

p = r'(121){2}'
m = re.search(p, '121121abcabc')
print(m)
print(m.group())
print(m.group(1))

p2 = r'(\d{3,4})-(\d{7,8})'
m1 = re.search(p2, '010-88530786')
print(m1)
print(m1.group())
print(m1.groups())
'''
# 分组命名
p3 = r'(?P<area_code>\d{3,4})-(?P<phone-code>\d{7,8})'
m2 = re.search(p3, '010-88530786')
print(m2.group(1))
print(m2.group(2))
'''

# 反向引用
# 称为捕获分组。捕获分组的匹配子表达式结果被暂时保存到内存中,以备表达式或其他程序引用，
# 这个过程称为“捕获”,捕获结果可以通过组编号或组名进行引用。
p3 = r'<([\w]+)>.*</([\w]+)>'
m3 = re.search(p3, '<a>abc</a>')
print(m3)
m4 = re.search(p3, '<a>abc</b>')
print(m4)

p4 = r'<([\w]+)>.*</\1>'
m5 = re.search(p4, '<a>zch</a>')
m6 = re.search(p4, '<a>zch</b>')
print(m5, m6)

# 非捕获分组
# 有时并不想引用子表达式的匹配结果，不想捕获匹配结果，
# 只是将小括号作为一个整体进行匹配，此时可以使用非捕获分组，
# 在组开头使用“?:”可以实现非捕获分组。

s = 'img1.jpg,img2.jpg,img3.bmp'

#捕获分组
p = r'\w+(\.jpg)'
mlist = re.findall(p,s)
print(mlist)

#非捕获分组
p = r'\w+(?:\.jpg)'
mlist = re.findall(p,s)
print(mlist)