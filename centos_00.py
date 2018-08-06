#豆瓣音乐专区

import requests

from lxml import html
url="https://music.douban.com/"#需要爬去的网址

page=requests.Session().get(url)

result=tree.xpath("//tr//a/text()")

result=tree.xpath("//tr//a/@href")

result=tree.xpath("//tr[last()]//a/@href")

print(result)
print(result1)
print(result2)
