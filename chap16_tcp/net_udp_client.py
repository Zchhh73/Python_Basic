import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 8888)
s.sendto(b'Hello Server',server_address)

data,_ = s.recvfrom(1024)
print('从服务器接收消息：{}'.format(data.decode()))

s.close()
