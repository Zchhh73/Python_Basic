#集合是一种可迭代的，无序的，不能包含重复元素的DS，不能通过序号访问，不能有重复
'''
a = {'zch','ll','llz'}
print(a)
print(len(a))
print(set((10,20,20,30,40,50)))
b = set()
print(type(b))

student_list = {'zch','ll','llz'}
student_list.add("hyb")
print(student_list)
student_list.remove('zch')
print(student_list)
#重复删除不会报错
student_list.discard('zch')
print(student_list)

student_list.pop()
print(student_list)

student_list.clear()
print(student_list)

#遍历
student_set = {'zch','ll','llz'}
for item in student_set:
    print(item)
print('---------------')
for i,item in enumerate(student_set):
    print("{0}-{1}".format(i,item))
'''

#不可变集合frozenset
student_set = frozenset({'zch','sq','ls'})
print(student_set)

#集合推导式
n_list = {x for x in range(100) if x % 2 ==0 if x % 5 ==0}
print(n_list)

input_list = [2,3,2,4,5,6,6,6,6]
n_list = [x ** 2 for x in input_list]
n_set = {x ** 2 for x in input_list}
print(n_list)
print(n_set)


