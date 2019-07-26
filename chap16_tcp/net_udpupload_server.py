import socket

HOST = '127.0.0.1'
PORT = 8888

filename = 'test1.txt'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print('服务器启动...')

    buffer = []
    while True:
        data, _ = s.recvfrom(1024)
        if data:
            flag = data.decode()
            if flag == 'bye':
                break
            buffer.append(data)
        else:
            continue
    b = bytes().join(buffer)
    with open(filename, 'w') as f:
        f.write(b.decode())

    print("服务器接收完成！")
