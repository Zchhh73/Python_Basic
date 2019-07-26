import json

py_dict = {'name': 'zch', 'age': 24, 'sex': True}
py_list = [1, 3]
py_tuple = ('A', 'B', 'C')

py_dict['a'] = py_list
py_dict['b'] = py_tuple

# print(py_dict)

# 编码过程
json_obj = json.dumps(py_dict, indent=4)  # 缩进4空格
print(json_obj)

json_obj = json.dumps(py_dict)
print(json_obj)

# 写入文件中
with open('data1.json', 'w') as f:
    json.dump(py_dict, f)

with open('data2.json', 'w') as f:
    json.dump(py_dict, f, indent=4)
