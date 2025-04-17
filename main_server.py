from netlink.server import NetServer
import time

server = NetServer()

for i in range(5):
  data = {"message": f"Hello from Transmitter {i}", "timestamp": time.time()}
  print(f"[Server] Sending: {data}")
  server.send(data)
  time.sleep(1)

server.close()
