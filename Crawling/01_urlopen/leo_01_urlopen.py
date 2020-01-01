#!/usr/local/bin/env python3
# -*- coding:utf-8 -*-


import urllib.request

ua_headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"    
}


# send request and get response
request = urllib.request.Request("http://www.baidu.com/", headers = ua_headers)

response = urllib.request.urlopen(request)

# the response support class methods in Python
html = response.read()

print(html)
