#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import urllib2
import lxml

def download(url, user_agent = 'wswp', num_retries = 2):
    print "Downloading: ", url
    headers = {"User-agent": user_agent}
    request = urllib2.Request(url, headers = headers)
    try:
        html = urllib2.urlopen(request).read()

    except urllib2.URLError as e:
        print "Download error: ", e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries - 1)
    return html

def save_pic(keyword):
    url = "https://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word=" + keyword + "&ct=201326592&ic=0&lm=-1&width=&height=&v=index"
    url.decode('utf-8').encode('gbk')
    i = 0
    html = download(url)

    pic_url_list = re.findall('"objURL":"(.*?)",', html, re.S)

    for each in pic_url_list:
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print "Downloading error"
            continue
        file_path = str(i) + '.jpg'
        print "Save file path is : ",file_path
        file = open(file_path, 'w')
        file.write(pic.content)
        file.close()
        i += 1


if __name__ == '__main__':
    save_pic("夏目友人帐")