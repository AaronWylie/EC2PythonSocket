import socket

# You Run this first
# this will go on EC2 server
# AF_INET = IP, SOCK_STREAM = TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# replace'IP' with EC2 Private IP
server.bind(('IP', 1325)) 
server.listen()

client_socket, client_address = server.accept()
file = open('apple_SENT_9.jpg', "wb")
image_chunk = client_socket.recv(4096)  # stream-based protocol

while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(4096)

file.close()
client_socket.close()


