#!/usr/local/bin/env python3
# -*- coding:utf-8 -*-


import urllib.request


ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/79.0.3945.88 Safari/537.36"
}

# 构造请求对象并发送请求，服务器响应相应的类文件对象
request = urllib.request.Request("http://www.baidu.com/", headers=ua_headers)

response = urllib.request.urlopen(request)

# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
html = response.read()

# 返回HTTP的响应码，成功返回2xx，服务器页面出错返回4xx，服务器问题返回5xx
print(response.getcode())

# 返回实际数据的URL，防止重定向问题
print(response.geturl())

# 返回服务器相应的HTTP报头
print()