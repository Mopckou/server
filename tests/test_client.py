import pytest, pytest_socket, time
import src

class SocketMock(object):
    def recv(self, bytes):
        return time.ctime(1519255913.9968698).encode('utf-8')

    def close(self):
        print('Close')


def make_mock_socket():
    return SocketMock()

def test_decode():
    'byte-string' == b'byte-string'.decode('ascii')


def test_recieved():
    client = src.socket_client_sync.SocketClientSync('localhost', 8888)
    ret = client.recieve_time(
        make_mock_socket()
    )
    assert ret == 'Received time is Thu Feb 22 02:31:53 2018'