import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 80))

server.listen()

while True:
    client, addr = server.accept()
    client.send("Hello Wordl".encode())
    print(client.recv(1024).decode())
    client.close()