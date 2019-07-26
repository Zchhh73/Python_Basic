import socket

HOST = ''
PORT = 8888

filename = 'img.jpg'

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(10)
    print("服务器启动。。。")


    while True:
        with s.accept()[0] as conn:
            buffer = []
            #反复接受数据
            while True:
                data = conn.recv(1024)
                if data:
                    #加到缓冲区
                    buffer.append(data)
                else:
                    break
            #合并
            b = bytes().join(buffer)
            with open(filename,'wb') as f:
                f.write(b)

            print('服务器接受完成。')