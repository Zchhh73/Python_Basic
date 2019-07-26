# coding:utf-8

# TCP socket编程
'''
Socket是网络上的两个程序，通过一个双向的通信连接实现数据的交换。这个双向链路的一端称为一个Socket。
Socket 通常用来实现客户端和服务端的连接

服务器编程方法:
socket.bind(address):绑定地址和端口
socket.listen(backlog):监听端口，backlog最大连接数
socket.accept():等待客户端连接。返回（conn.address）conn为socket对象，address为客户端地址
'''

import socket

# 创建socket，par1位地址类型，par2为通讯类型（TCP，UDP）
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))
s.listen()
print('服务器启动..')

# 等待连接
conn, address = s.accept()
# 连接成功打印
print(address)

# 从客户端接受数据
data = conn.recv(1024)
print('从客户端接受消息：{0}'.format(data.decode()))

#给客户端发送数据
conn.send('你好'.encode())

conn.close()
s.close()
