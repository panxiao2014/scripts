import socket
import sys

HOST = sys.argv[1]
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(b'Hello, world')
  data = s.recv(1024)

print('Received', repr(data))
