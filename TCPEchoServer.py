#!/usr/bin/python3

import socket

host = '0.0.0.0'
port = 10206
BUFF_SIZE = 128
BACKLOG = 5

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host,port)
conn_sock.bind(server_address)

conn_sock.listen(BACKLOG)

while True:
    print("wating for request...")
    data_sock, address = conn_sock.accept()
    print("echo request from {} port {}" .format(host,port))
    message = data_sock.recv(BUFF_SIZE)

    if message:
        print("recevied message: {}\n" .format(message.decode()))
        data_sock.sendall(message)

    data_sock.close()
