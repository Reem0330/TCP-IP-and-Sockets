$ ipython
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.6.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import socket

In [2]: client_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

In [3]: client_socket.connect(('127.0.0.1',50000))

In [4]: client_socket.sendall(b'Hello??')

In [5]: client_socket.recv(64)
Out[5]: b'yes? Cen you hear me?!'

In [6]: client_socket.sendall(b'Excellent!')

In [7]: client.close()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-1ef8b845d8fa> in <module>
----> 1 client.close()

NameError: name 'client' is not defined

In [8]: client_socket.close()

In [9]:
