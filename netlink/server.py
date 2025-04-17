import socket
import pickle
import struct

class NetServer:
    def __init__(self, host="0.0.0.0", port=9999):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"[NetServer] Listening on {host}:{port}")
        self.conn, self.addr = self.socket.accept()
        print(f"[NetServer] Connected by {self.addr}")

    def send(self, data):
        raw = pickle.dumps(data)
        size = struct.pack(">L", len(raw))
        self.conn.sendall(size + raw)

    def close(self):
        self.conn.close()
        self.socket.close()
