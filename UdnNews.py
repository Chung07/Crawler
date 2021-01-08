#聯合新聞網新聞標題
import get.html

# 獲取首頁html
url="https://udn.com/news/breaknews/1"
# print(get.html.GetHtml(url))

root=get.html.GetHtml(url)
# bknews=root.find("section",class_='cate-list_subheader')

#印出幻燈片
# top=root.find("section",class_="slide-holder")
# slide=top.find("div",class_="slide-section slide picture")
# print(slide)

#印出新聞分類
# cat=root.find("header",class_="header")
# nav=cat.find("nav",class_="navigation")
# print(nav.text)

#新聞子分類
# subcat=root.find("section",class_="cate-list__subheader")
# subcat_mode=subcat.find("a",class_="active")
# print(subcat_mode.text)

#印出即時新聞標題
left=root.find("section",class_="thumb-news cate-list context-box")
news=left.find("div",class_="context-box__content story-list__holder story-list__holder--full")
news_text=news.find_all("div",class_="story-list__text")
# print(news_text)
for head in news_text:
    print(head.h2.text)


