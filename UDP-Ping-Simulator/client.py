import socket
import time

host = '127.0.0.1'
port = 22222
message = 'this is just a simple message'

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1.0) 

for i in range(4):
    try:
        startTime = time.perf_counter() 
        clientSocket.sendto(message.encode(), (host, port)) 
        
        data, server = clientSocket.recvfrom(1024)
        endTime = time.perf_counter()
        
        rtt = endTime - startTime 
        print('Received response from server:', data.decode())
        print('Round-trip time:', rtt, 'seconds')
    except socket.timeout:
        print('Request timeout')

clientSocket.close()
