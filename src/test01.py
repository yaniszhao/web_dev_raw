"""
最简单的框架
"""
import socket
sock = socket.socket()
sock.bind(('127.0.0.1',8080))
sock.listen(5)
print("ready.")
while True:
    connection, address = sock.accept()
    data=connection.recv(8096)

    print(data)
    """
    b'GET / HTTP/1.1\r\n
    Accept: text/html, application/xhtml+xml, image/jxr, */*\r\n
    Accept-Language: zh-CN\r\n
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like ecko\r\n
    Accept-Encoding: gzip, deflate\r\n
    Host: 127.0.0.1:8080\r\n
    Connection: Keep-Alive\r\n\r\n'
    """

    #若不加这个200 OK，在ie能成功一次，但是chrome上一次都不成功
    connection.send(b"HTTP/1.1 200 OK\r\n\r\n")
    connection.send(b"123456")
    connection.close()