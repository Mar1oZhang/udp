# client.py
import socket

#file_path  表示要传输的文件路径
def udp_client(host, port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 从文件路径中提取文件名，使用文件路径中的斜杠（/）分隔，取最后一个元素作为文件名
    file_name = file_path.split("/")[-1]
    client_socket.sendto(file_name.encode('utf-8'), (host, port))

    # 发送文件内容
    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.sendto(data, (host, port))
            data = file.read(1024)

    print(f"File '{file_name}' sent successfully")
    client_socket.sendto("finished".encode(), (host, port))
    #发送一个标志着文件传输结束的字符串（"finished"）编码后的数据到服务器

if __name__ == "__main__":
    udp_client('127.0.0.1', 12345, './file.txt')