#json解码
import json

with open('data2.json','r') as f:
    py_dict = json.load(f)
    py_list_a = py_dict['a']
    py_list_age = py_dict['age']
    print(py_dict)
    print(py_list_a)
    print(py_list_age)