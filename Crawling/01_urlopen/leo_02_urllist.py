#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request
import random

url = "https://baike.baidu.com/item/%E6%8A%93%E5%8C%85/9929103"

# 可以是User-Agent列表，也可以是代理列表
ua_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]

# 在User-Agent列表里随机选择一个User-Agent
user_agent = random.choice(ua_list)

# 构造一个请求
request = urllib.request.Request(url)

# add_header()方法 添加/修改 一个HTTP报头
request.add_header("User-Agent", user_agent)

# get_header() 获取一个已有的HTTP报头的值，注意只能是第一个字母大写，其他的必须小写
print(request.get_header("User-agent"))

with urllib.request.urlopen(url) as response:
    the_page = response.read().decode('utf-8')

print(the_page)

with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(the_page)
