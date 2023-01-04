import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("8uown.localtonet.com", 80))


print(client.recv(1024).decode())
client.send("Hey Server".encode())