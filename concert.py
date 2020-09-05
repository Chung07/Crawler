import urllib.request as req
import bs4

#取得內容
url="https://tixcraft.com/ticket/area/20_TarcySu/7596"
data=req.urlopen(url).read().decode("utf-8")
# print(data)

#解析
root=bs4.BeautifulSoup(data,"html.parser")
#列出價位及販售情形
seats=root.find("div",class_="zone area-list")
seats2=seats.find_all("li")
for seat in seats2:
    print(seat.text)

#把結果寫入檔案
# seats=root.find("div",class_="zone area-list")
# seats2=seats.find_all("li")
# with open("ticket/seats.txt",mode="w",encoding="utf-8") as file:
#     for seat in seats2:
#         file.write(seat.text+"\n")



