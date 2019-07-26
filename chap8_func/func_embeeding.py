#嵌套函数

def calculate(n1,n2,opr):
    multiple = 2

    #定义相加
    def add(a, b):
        return (a + b) * multiple

    def sub(a,b):
        return (a -b) * multiple

    if opr == '+':
        return add(n1,n2)
    else:
        return sub(n1,n2)

print(calculate(10,5,'+'))