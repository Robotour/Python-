import requests
import re

def get_web():
    url = "http://www.17k.com/list/1315078.html"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    r = requests.get(url,headers=headers)
    r.encoding="utf-8"

    htmls = re.findall('<a target="_blank" href="(.*?)" title="字数：.*?;更新日期:.*?">',r.text)
    return htmls

webs = get_web()
def get_content():
    for web in webs:
        url ="http://www.17k.com" + web
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        r = requests.get(url,headers=headers)
        r.encoding="utf-8"
        content_lists = re.findall('&#12288;&#12288;(.*?)<br /><br />',r.text)

        for content in content_lists:
            print(content)

get_content()
print("这是修改的内容")
