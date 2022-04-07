#TCPEchoClient.py

import socket

host = '203.250.133.88'
port = 10206
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print("connecting to {} port {}" .format(host,port))
sock.connect(server_address)

message = input("Enter message : ")
message = bytes(message, encoding='utf-8')

try:
    sock.sendall(message)
    data = sock.recv(BUFF_SIZE)
    print("received form server: {}".format(data.decode()))

except Exception as e:
    print("Exception: {}".format(str(e)))

sock.close()