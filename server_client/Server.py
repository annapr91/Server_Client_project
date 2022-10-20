from .AbstrClass import BaseInterface
import socket
import select


class Server(BaseInterface):
    FOR_READ = []


    def creating_server(self):
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srv.bind((self.SERVER_HOST, self.SERVER_PORT))
        self.srv.listen(10)

        self.srv.setblocking(False)
        self.FOR_READ.append(self.srv)




    # def creating_select(self):
    #
    #     self.R, self.W, self.ERR = select.select(Server.FOR_READ, Server.FOR_WRITE, Server.FOR_READ)


    def for_reading(self):
        R, _, _ = select.select(Server.FOR_READ, [], [])

        for r in R:
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
                    for conn in Server.FOR_READ:
                        if conn != self.srv and conn != r:
                            conn.sendall(data.encode('utf-8'))




