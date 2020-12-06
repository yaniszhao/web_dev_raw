"""
使用第三方库完成模板渲染
"""

import socket

def f1(request):
    import pymysql
    # 创建连接,获得数据
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='yanis', passwd='1', db='django_test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select dev_id, dev_name, dev_desc from device_table')
    dev_list = cursor.fetchall()
    cursor.close()
    conn.close()

    #print(dev_list)
    """
    [
    {'dev_id': 1, 'dev_name': 'dev1', 'dev_desc': '设备1'}, 
    {'dev_id': 2, 'dev_name': 'dev2', 'dev_desc': '设备2'}, 
    {'dev_id': 3, 'dev_name': 'dev3', 'dev_desc': '设备3'}, 
    {'dev_id': 4, 'dev_name': 'dev4', 'dev_desc': None}, 
    {'dev_id': 5, 'dev_name': 'dev5', 'dev_desc': '设备5'}, 
    {'dev_id': 6, 'dev_name': 'dev6', 'dev_desc': None}
    ]
    """
    #print(type(dev_list[0]['dev_id'])) #int
    #print(type(dev_list[0]['dev_name'])) #str
    #print(type(dev_list[0]['dev_desc'])) #str
    #print(type(dev_list[3]['dev_desc']))  # NoneType


    # 模板渲染（模板+数据）
    f = open('../resource/test06_devlist.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()
    # 基于第三方工具实现的模板渲染
    from jinja2 import Template
    template = Template(data)
    data = template.render(xxxxx=dev_list)
    return data.encode('utf-8')

routers = [
    ('/devlist.html', f1),
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