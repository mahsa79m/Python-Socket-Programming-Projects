import socket
import random

host = '127.0.0.1'
port = 22222

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((host, port))

print('Server is listening on {}:{}'.format(host, port))

while True:
    connection, address = serverSocket.recvfrom(1024)
    print('Received message from', address)

    if random.choice([True, False]):
        response = 'HEY CLIENT!'
        serverSocket.sendto(response.encode(), address)
        print('Responded to', address)
    else:
        print('No response sent to', address)
