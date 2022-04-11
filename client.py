import socket

# You run this second
# This will go on Jetson Nano (Or any local device)

# AF_INET = IPv4, SOCK_STREAM = TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Replace 'IP' with EC2 Public IP address
client.connect(('IP', 1325))

file = open('apple.jpg', 'rb')
image_data = file.read(4096)

while image_data:
    client.send(image_data)
    image_data = file.read(4096)

file.close()
client.close()
