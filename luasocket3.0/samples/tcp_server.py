# server

import socket
ocal_port = 8282

address = ('127.0.0.1', 8080)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the old state of the SO_REUSEADDR option
sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

# Enable the SO_REUSEADDR option
sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 ) 

new_state = sock.getsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR )

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(address)
srv.listen(5)

ss, addr = srv.accept()
print 'got connected from', addr

ra = ss.recv(40960)
print "|" + ra + "|"

ss.close()
srv.close()
