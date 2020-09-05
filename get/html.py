#解析網頁html
import requests
from bs4 import BeautifulSoup

def GetHtml(url):
    req=requests.get(url).text
    root=BeautifulSoup(req,"html.parser")
    return root

