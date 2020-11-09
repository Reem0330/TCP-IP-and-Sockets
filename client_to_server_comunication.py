$ ipython
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.6.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import socket

In [2]: socket.getaddrinfo('hasthelargehadroncolliderdestroyedtheworldyet.com', 'http')
Out[2]:
[(<AddressFamily.AF_INET: 2>,
  <SocketKind.SOCK_STREAM: 1>,
  0,
  '',
  ('216.92.96.71', 80))]

In [3]: client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

In [4]: client.connect(('216.92.96.71', 80))

In [5]: msg = "GET / HTTP/1.1\r\n"

In [6]: msg += "Host: hasthelargehadroncolliderdestroyedtheworldyet.com\r\n\r\n"

In [7]: msg = msg.encode('utf8')

In [8]: msg
Out[8]: b'GET / HTTP/1.1\r\nHost: hasthelargehadroncolliderdestroyedtheworldyet.com\r\n\r\n'

In [9]: client.sendall(msg)

In [10]: response = client.recv(64)

In [11]: print(response)
b'HTTP/1.1 200 OK\r\nDate: Mon, 09 Nov 2020 14:51:54 GMT\r\nServer: Ap'

In [12]: msg1 = "GET / HTTP/1.1\r\nHost: jaschilz.net\r\n\r\n".encode('utf8')

In [13]: msg2 = b"GET / HTTP/1.1\r\nHost: jaschilz.net\r\n\r\n"
    ...:

In [14]: client.sendall('regular old py3 unicode string')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-237cc4393a65> in <module>
----> 1 client.sendall('regular old py3 unicode string')

TypeError: a bytes-like object is required, not 'str'

In [15]: client.close()

In [16]:
