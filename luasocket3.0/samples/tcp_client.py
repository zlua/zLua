# client

import socket

address = ('127.0.0.1', 8080)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

s.send('hihi')
s.send('hihi\n')
s.send('hihi')
s.send('hihi\n')

s.close()

