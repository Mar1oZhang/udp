#udp_server.py
import socket

def udp_server(host, port):
    #host表示服务器绑定的主机地址，port表示服务器监听的端口号
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    #打印服务器已经开始监听的消息
    print(f"Server listening on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        #file_name = data.decode('utf-8')
        file_name='./ab.txt'
        with open(file_name, 'wb') as file:
        #打开文件以进行写入二进制数据的操作
            while True:
                data, client_address = server_socket.recvfrom(1024)
                if data=="finished".encode():
                #检查是否接收到了特定的结束标志，即客户端发送的"finished"字符串的编码。如果收到结束标志，关闭文件，打印成功接收的消息，并跳出内层循环
                    file.close()
                    print(f"File '{file_name}' received successfully")
                    break
                file.write(data)
                print(data.decode())
                

if __name__ == "__main__":
#启动UDP服务器，监听在本地主机的12345端口上  这是服务器脚本的入口点
    udp_server('127.0.0.1', 12345)

