import requests
from bs4 import BeautifulSoup

response = requests.get(
    url='http://www.autohome.com.cn/news/'
)
response.encoding = "gbk"

# convert text into object, then can use method
soup = BeautifulSoup(response.text, features = "html.parser")
target = soup.find(id = "auto-channel-lazyload-article")

# find all li and store in a list
li_list = target.find_all_next("li")

# find all "a" tabs, then print their 'href' and 'h3', if they exist
for i in li_list:
    a = i.find("a")
    if a:
        print(a.attrs.get('href'))
        txt = a.find('h3')
        print(txt)

with open("Car.html", "w") as f:
    f.write(response.text)