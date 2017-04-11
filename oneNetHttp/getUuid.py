# -*- coding:utf-8 -*-

import urllib2
def http_get():
	url='http://api.heclouds.com/devices/1100353/datapoints?%20datastream_id=001%202&start=2016-06-23T11:00:00&end=2016-06-23T11:45:00'
	request = urllib2.Request(url)
	request.add_header('api-key', 'BMoXY9INkS=l0Iiow=Zo4bqjqLE= ')
	request.get_method = lambda:'GET'           # 设置HTTP的访问方式
	request = urllib2.urlopen(request)
	return request.read()

resp = http_get()
print resp
