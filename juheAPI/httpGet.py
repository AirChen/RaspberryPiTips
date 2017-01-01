# -*- coding:utf-8 -*-
# File: http_put.py
import json
import urllib2
import time

def http_get():
    d = time.strftime('%Y-%m-%d')
    url='http://japi.juhe.cn/calendar/day?date=2016-6-23&key=9272715137e15526b9c907f3e0e8b929'
    print url
    request = urllib2.Request(url)
    request.get_method = lambda:'POST'           # 设置HTTP的访问方式
    request = urllib2.urlopen(request)
    return request.read()

resp = http_get()
data = json.loads(resp)
print data['result']['data']['weekday']

#print unicode(resp,'utf-8')
#print resp
#file = open('out.jpg','wb')
#file.write(resp)
#file.close()
