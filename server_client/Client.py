import socket
import sys

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8008

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((SERVER_HOST, SERVER_PORT))
client_sock.setblocking(False)
while True:
        for line in sys.stdin:

            client_sock.send(line.encode('utf-8'))
            try:
                    res = client_sock.recv(2**16)
            except BlockingIOError:
                    continue

            else:
                    print(res.decode('utf-8'))