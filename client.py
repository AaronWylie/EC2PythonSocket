import socket

# You run this second
# This will go on Jetson Nano

# AF_INET = IPv4, SOCK_STREAM = TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ec2 public ip --> 18.188.146.161
client.connect(('18.188.146.161', 1256))

file = open('apple.jpg', 'rb')
image_data = file.read(4096)

while image_data:
    client.send(image_data)
    image_data = file.read(4096)

file.close()
client.close()
