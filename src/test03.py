"""
根据url的不同，做路由选择，形成一个框架
"""

import socket

def f1(request):
    """
    处理用户请求，并返回相应的内容
    :param request: 用户请求的所有信息
    :return:
    """
    f = open('../resource/test03_index.html','rb')
    data = f.read()
    #print(type(data)) #bytes
    f.close()
    return data

def f2(request):
    f = open('../resource/test03_article.html','rb')
    data = f.read()
    f.close()
    return data

routers = [
    ('/xxx', f1),
    ('/ooo', f2),
]

if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('127.0.0.1',8080))
    sock.listen(5)
    print("ready.")
    while True:
        conn, address = sock.accept()
        data=conn.recv(8096)
        data = str(data, encoding='utf-8')
        #data=bytes('sdlfhlsajf', encoding='utf-8')

        header, body = data.split('\r\n\r\n')
        temp_list = header.split('\r\n')
        method, url, protocal = temp_list[0].split(' ')

        #若不加这个200 OK，在ie能成功一次，但是chrome上一次都不成功
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

        func_name = None
        for item in routers:
            if item[0] == url:
                func_name = item[1]
                break

        if func_name:
            response = func_name(data)
        else:
            response = b"404"

        conn.send(response)
        conn.close()