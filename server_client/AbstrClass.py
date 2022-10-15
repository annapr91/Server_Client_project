from abc import ABC, abstractmethod
import socket

class BaseInterface(ABC):
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8008

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # def __int__(self, SERVER_HOST, SERVER_PORT):
    #      self.SERVER_HOST = SERVER_HOST
    #      self.SERVER_PORT = SERVER_PORT


    @abstractmethod
    def creating_server(self):
        ...

