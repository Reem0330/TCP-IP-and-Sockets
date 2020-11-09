In [1]: import socket

In [2]: server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

In [3]: server_socket.bind(('127.0.0.1',50000))

In [4]: server_socket.listen(1)

In [5]: connection, client_address = server_socket.accept()

In [6]: connection.recv(64)
Out[6]: b'Hello??'

In [7]: connection.sendall(b'yes? Cen you hear me?!')

In [8]: connection.recv(64)
Out[8]: b'Excellent!'

In [9]: server_socket.close()
