import socket

s = socket.socket()

s.bind(('localhost',9999))
s.listen(3)

print('Waiting for connections')

while True:
    c, caddr = s.accept()
    name = c.recv(1024).decode()

    print(f"Connected with {caddr} and user {name}")
    c.send(bytes("Welcome to Socket Server","utf-8"))

    c.close()

