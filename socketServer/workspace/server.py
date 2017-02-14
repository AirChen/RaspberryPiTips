# -*- coding: utf-8 -*-
import socket
import urllib2
import json
import time
from poster.streaminghttp import register_openers
from poster.encode import multipart_encode

def http_put():
    url='http://api.heclouds.com/bindata?device_id=4661834&datastream_id=pic'
    
    f = open('img.jpeg','rb')
    b = f.read()
    f.close()
    
    request = urllib2.Request(url,b)
    request.add_header('api-key', 'Y8gdH8Mim1wCfgHBEIK2TRQWE9o=')
    request.get_method = lambda:'POST'
    request = urllib2.urlopen(request)
    return request.read()

def http_put_uuid(uuid):
    url='http://api.heclouds.com/devices/4661834/datapoints'
    d = time.strftime('%Y-%m-%dT%H:%M:%S')
    print d
    values={'datastreams':[{"id":"uuid","datapoints":[{"at":d,"value":uuid}]}]}
    
    jdata = json.dumps(values)                  # 对数据进行JSON格式化编码
    request = urllib2.Request(url, jdata)
    request.add_header('api-key', 'Y8gdH8Mim1wCfgHBEIK2TRQWE9o=')
    request.get_method = lambda:'POST'           # 设置HTTP的访问方式
    request = urllib2.urlopen(request)
    return request.read()

if __name__=="__main__":
        print "Server is starting"  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        sock.bind(('localhost', 8001))  #配置soket，绑定IP地址和端口号  
        sock.listen(5) #设置最大允许连接数，各连接和server的通信遵循FIFO原则  
        print "Server is listenting port 8001, with max connection 5"   
        while True:  #循环轮询socket状态，等待访问  
                  
                connection,address = sock.accept()    
                try:    
                        connection.settimeout(50000)
                        while True:  
                                buf = connection.recv(1024)    
                                print "Get value " +buf  
                                if buf == '1':    
                                    print "send image"
                                    resp = http_put()
                                    a = eval(resp)
                                    aa = a.get('data')
                                    uuid = aa.get('index')
                                    print uuid
                                    result = http_put_uuid(uuid)
                                    print result
                                    connection.sendall(uuid)
                                
                                elif buf!='0':    
                                    connection.sendall('please go out!')   
                                    print "send refuse"  
                                else:   
                                    print "close"  
                                    break  #退出连接监听循环  
                except socket.timeout:  #如果建立连接后，该连接在设定的时间内无数据发来，则time out  
                         print 'time out'  
  
                print "closing one connection" #当一个连接监听循环退出后，连接可以关掉  
                connection.close()
