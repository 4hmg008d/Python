#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse

url = "http://www.baidu.com/s"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/79.0.3945.88 Safari/537.36 "
}

keyword = input("请输入需要查询的关键字： ")

wd = {"wd" : keyword}

# 通过urllib.urlencode() 参数是一个dict类型
wd = urllib.parse.urlencode(wd)

# 拼接完整的url
fullurl = url + "?" + wd
#print(fullurl)

# 构造请求对象
request = urllib.request.Request(fullurl, headers = headers)


with urllib.request.urlopen(request) as response:
    the_page = response.read().decode('utf-8')

print(the_page)
print(response.geturl())
