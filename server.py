import socket
import select

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8008

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((SERVER_HOST, SERVER_PORT))
srv.listen(10)

srv.setblocking(False)
FOR_READ = [srv]
FOR_WRITE = []
BUFFER = {}

while True:

    R, W, ERR = select.select(FOR_READ, FOR_WRITE, FOR_READ)

    for r in R:
        if r is srv:
            client, addr = srv.accept()
            client.setblocking(False)
            FOR_READ.append(client)

        else:
            try:
                data = r.recv(2 ** 16)
            except ConnectionResetError:
                r.close()
            else:
                data = data.decode("utf-8")
                FOR_WRITE.append(r)
                BUFFER[r] = data
                FOR_READ.remove(r)

                for r in FOR_READ:
                    if r != srv:
                        r.sendall(data.encode('utf-8'))
                        FOR_WRITE.append(r)
                        FOR_READ.remove(r)

    for w in W:
        FOR_READ.append(w)
        FOR_WRITE.remove(w)
