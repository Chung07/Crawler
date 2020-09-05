#拓元首頁所有演出
import requests
from bs4 import BeautifulSoup
import get.html

# 獲取首頁html
url="https://tixcraft.com"
# print(get.html.GetHtml(url))
root=get.html.GetHtml(url)
all=root.find("ul",class_="nav-menu accessible-megamenu")
activity=all.find("a",string="節目資訊")
#印出節目資訊的網址
# print(url+activity["href"])

#解析全部節目的html
allshow=get.html.GetHtml(url+activity["href"])
# print(allshow)

#印出全部節目
showlist=allshow.find("tbody")
showname=showlist.find_all("a")
for buy in showname:
    print(buy.text)
