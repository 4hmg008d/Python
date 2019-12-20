#!/usr/local/bin/env python3
# -*- coding:utf-8 -*-


import urllib.request

# send request and get response
response = urllib.request.urlopen("http://www.baidu.com/")

# the response support class methods in Python
html = response.read()

print(html)
