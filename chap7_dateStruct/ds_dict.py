# 字典是可迭代的、可变的DS，通过键访问元素 键-值对
# create
dict1 = {102: 'zch', 103: "ll", 104: "llz"}
print(len(dict1))
print(dict1)
dict2 = dict(zip([102, 103, 104], ['zch', 'll', 'llz']))
print(dict2)
dict3 = dict(S101='zch', S102='ll', S103='llz')
print(dict3)

# update
'''
print(dict1[102])
dict1[101] = 'wsp'
print(sorted(dict1))
del dict1[101]
print(dict1)
print(dict1.pop(104))
print(dict1)
'''
# find
print(dict1.get(102))

print(dict1.get(101, 'aa'))

print(dict1.items())

print(dict1.keys())
print(dict1.values())

print(102 in dict1)
print(101 in dict1)

# 遍历
print('-------遍历键--------')
for student_id in dict1.keys():
    print('学号：' + str(student_id))

print('--------遍历值--------')
for student_name in dict1.values():
    print('姓名：' + student_name)

print('--------遍历键值对--------')
for stu_id, stu_name in dict1.items():
    print('学号{0}-学生{1}'.format(stu_id, stu_name))

# 字典推导式
input_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
output_dict = {k: v for k, v in input_dict.items() if v % 2 == 0}
print(output_dict)

keys = [k for k,v in input_dict.items() if v % 2 == 0]
print(keys)
