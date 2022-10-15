from .AbstrClass import BaseInterface
import socket
import select


class Server(BaseInterface):
    FOR_READ = []
    FOR_WRITE = []
    BUFFER = {}

    def creating_server(self):
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srv.bind((self.SERVER_HOST, self.SERVER_PORT))
        self.srv.listen(10)

        self.srv.setblocking(False)
        self.FOR_READ.append(self.srv)

    def creating_select(self):
        self.R, self.W, self.ERR = select.select(Server.FOR_READ, Server.FOR_WRITE, Server.FOR_READ)
        return self.R, self.W, self.ERR

    def for_reading(self):
        for r in self.creating_select()[0]:
            if r is self.srv:
                client, addr = self.srv.accept()
                client.setblocking(False)
                Server.FOR_READ.append(client)

            else:
                try:
                    data = r.recv(2 ** 16)
                except ConnectionResetError:
                    r.close()
                else:
                    data = data.decode("utf-8")
                    Server.FOR_WRITE.append(r)
                    self.BUFFER[r] = data
                    Server.FOR_READ.remove(r)

                    for r in Server.FOR_READ:
                        if r != self.srv:
                            r.sendall(data.encode('utf-8'))
                            Server.FOR_WRITE.append(r)
                            Server.FOR_READ.remove(r)

    def for_writing(self):
        for w in Server.FOR_WRITE:
            Server.FOR_READ.append(w)
            Server.FOR_WRITE.remove(w)
