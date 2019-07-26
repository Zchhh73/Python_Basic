import socket

filename = 'test.txt'
HOST = '127.0.0.1'
PORT = 8888
server_address = (HOST,PORT)

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    with open(filename,'r') as f:
        while True:
            data = f.read(1024)
            if data:
                s.sendto(data.encode(),server_address)
            else:
                s.sendto(b'bye',server_address)
                break

        print('客户端上传数据完成。')
