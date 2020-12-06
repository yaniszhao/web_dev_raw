"""
最简单的动态网页，使用模板渲染，每次返回的是不同的时间
"""

import socket

def f1(request):
    f = open('../resource/test04_article.html','r', encoding='utf-8') #‘r’读出的是字符串，要加编码格式
    data = f.read()
    #print(type(data)) #str
    f.close()
    import time
    ctime = time.time()
    data = data.replace('@@sw@@', str(ctime))
    return bytes(data, encoding='utf-8')

routers = [
    ('/xxx', f1),
    #('/ooo', f2),
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