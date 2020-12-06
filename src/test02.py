"""
可以根据url返回不同的信息
"""
import socket
sock = socket.socket()
sock.bind(('127.0.0.1',8080))
sock.listen(5)
print("ready.")
while True:
    conn, address = sock.accept()
    data=conn.recv(8096)

    print("#################################################")
    #print(data)
    """
    b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
    """
    """
    b'GET /favicon.ico HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36\r\nAccept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-Mode: no-cors\r\nSec-Fetch-Dest: image\r\nReferer: http://127.0.0.1:8080/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'
    """

    data = str(data, encoding='utf-8')
    #data=bytes('sdlfhlsajf', encoding='utf-8')
    print("#################################################")
    print(data)
    """
    GET / HTTP/1.1
    Host: 127.0.0.1:8080
    Connection: keep-alive
    Cache-Control: max-age=0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    """
    """
    GET /favicon.ico HTTP/1.1
    Host: 127.0.0.1:8080
    Connection: keep-alive
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36
    Accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: no-cors
    Sec-Fetch-Dest: image
    Referer: http://127.0.0.1:8080/
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    """

    header, body = data.split('\r\n\r\n')
    temp_list = header.split('\r\n')
    method, url, protocal = temp_list[0].split(' ')
    print("#################################################")
    #print(header)
    print(temp_list)
    print(method)
    print(url)
    print(protocal)

    #若不加这个200 OK，在ie能成功一次，但是chrome上一次都不成功
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

    if url == '/':
        conn.send(b"123456")
        print('send /')
    elif url == '/xxx':
        conn.send(b"xxx")
        print('send /xxx')
    else:
        conn.send(b"unknown url")
        print('send unknown url')
    conn.close()