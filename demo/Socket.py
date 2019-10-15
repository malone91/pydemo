import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8888))
sock.sendall(b"hello")
print(sock.recv(1024))
sock.close()