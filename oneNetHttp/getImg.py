# -*- coding:utf-8 -*-
# File: http_put.py

import urllib2
def http_put():
    url='http://api.heclouds.com/bindata/1100353_1466653327429_img_data'
    request = urllib2.Request(url)
    request.add_header('api-key', 'BMoXY9INkS=l0Iiow=Zo4bqjqLE= ')
    request.get_method = lambda:'GET'           # 设置HTTP的访问方式
    request = urllib2.urlopen(request)
    return request.read()

resp = http_put()
#print resp
file = open('out.jpg','wb')
file.write(resp)
file.close()
