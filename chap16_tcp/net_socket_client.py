import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务器
s.connect(('127.0.0.1',8888))

#发送数据
s.send(b"Hello Server,I'm Client!")
data = s.recv(1024)
print('从服务器接受消息：{0}'.format(data.decode()))

s.close()
