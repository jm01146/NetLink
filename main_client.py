# Client End Code (Receiver)
from netlink.client import NetClient

client = NetClient("x.x.x.x")  # Replace with actual IP of Linux server

while True:
    try:
        data = client.receive()
        print(f"[Client] Received: {data}")
    except Exception as e:
        print(f"[Client] Error: {e}")
        break

client.close()
