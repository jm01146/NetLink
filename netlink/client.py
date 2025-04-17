import socket
import pickle
import struct

class NetClient:
    def __init__(self, server_ip, port=9999):
        self.server_ip = server_ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server_ip, self.port))

    def receive(self):
        data = b""
        payload_size = struct.calcsize(">L")
        while len(data) < payload_size:
            data += self.socket.recv(4096)
        size = struct.unpack(">L", data[:payload_size])[0]
        data = data[payload_size:]
        while len(data) < size:
            data += self.socket.recv(4096)
        return pickle.loads(data[:size])

    def close(self):
        self.socket.close()
