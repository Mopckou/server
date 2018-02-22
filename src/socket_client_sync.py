import socket
from . import socket_client
class SocketClientSync(object):

    def __init__(self, address='localhost', port=8888):
        self.address = address
        self.port = port

    def make_tcp_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.address, self.port))
        return s

    def recieve_time(self, socket_):
        payload = socket_.recv(1024)
        socket_.close()
        return 'Received time is {}'.format(payload.decode('ascii'))

def process(address='localhost', port=8888):
    client = SocketClientSync(address, port)
    con = client.make_tcp_socket()
    print(client.recieve_time(con))