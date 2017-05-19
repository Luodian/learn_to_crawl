#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import json
import requests
import urllib2
import sys
from bs4 import BeautifulSoup
import socket
import time
import os

global pic_counter
pic_counter = 0

socket.setdefaulttimeout(5)

def download(url, num_retries = 2):

    print "Downloading: ", url
    headers = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"}
    
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

def match_pic(json_data,filepath):
    global pic_counter
    for info in json_data['imgs']:
        try:
            print 'Save file at ', filepath + str(pic_counter) + '.png'
            file = open(filepath + str(pic_counter) + '.jpg', 'wb')
            pic_counter += 1
            time.sleep(0.2)
            file.write(requests.get(info['objURL'] ,stream = True).content)
            file.close()
        except socket.timeout as e:
            print "Timeout"
        except Exception as err:
            time.sleep(1)
            print 'Exception'
    return


def crawl_pic(keyword, amount = 100, filepath = None):
    pn = 0
    while pn < amount:
        url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + keyword + '&cg=girl&pn=' + str(
                pn) + '&rn=30&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
        url.decode('utf-8').encode('gbk')
        try:
            headers = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"}
            req = urllib2.Request(url=url, headers=headers)
            page = urllib2.urlopen(req)
            data = page.read().decode('utf-8')
        except UnicodeDecodeError as e:
            print "Error url: ",url
            time.sleep(1)
        except socket.timeout as e:
            print "Timeout"
        else:
            json_data = json.loads(data)
            match_pic(json_data,filepath)
            time.sleep(1)
            print "pn = ",pn,"Next page"
            pn += 30
            print "pn = ",pn,"Next page"
        finally:
            page.close()


    print "Download finish"
    return


if __name__ == '__main__':
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
    except:
        pass

    print sys.getdefaultencoding()
    keyword = "美国队长"
    if not os.path.exists("./" + keyword):
        os.mkdir("./" + keyword)

    filepath = "./" + keyword + '/'
    crawl_pic(keyword,1000,filepath)
    # test(bdimgurl)


# def test(url):
#     url.decode('utf-8').encode('gbk')

#     page = download(url)
#     # page = urllib2.urlopen(url).read()

#     # try:
#     # soup = BeautifulSoup(page,'lxml')
#     # href_list = soup.find_all('a',class_ = 'pc')

#     # line = '''<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E5%A4%8F%E7%9B%AE%E5%8F%8B%E4%BA%BA%E5%B8%90&pn=40&gsm=0"><span class="pc" data="right">3</span></a>'''
#     # line_match = re.findall('<a href=".*?"><span class="pc" data="right">.*?</span></a>',line)
#     # print 'line',line_match

#     href_list = re.findall('<a href="(.*?)"><span class="pc" data="right">(.*?)</span></a>',page)
#     print href_list
#     for each in href_list:
#         print each.get('href')

#         # href = td.get('href')
#         # print button_id
#     # except:
#     #     print 'Error'
#     
#     # def bfs(url):
#     url.decode('utf-8').encode('gbk')
#     i = 0
#     Q = [url]
#     vis = set()
#     while Q != []:
#         # extract the head element
#         cur_url = Q.pop(0)

#         # start to download a new page
#         if cur_url not in vis:
#             html = download(cur_url)
#             pic_url_list = re.findall('"objURL":"(.*?)",', html, re.S)
#             vis.add(cur_url)
#             for each in pic_url_list:
#                 try:
#                     pic = requests.get(each, timeout=10)
#                 except requests.exceptions.ConnectionError:
#                     print "Downloading error"
#                     continue
#                 file_path = str(i) + '.jpg'
#                 print "Save file path is : ",file_path
#                 file = open(file_path, 'w')
#                 file.write(pic.content)
#                 file.close()
#                 i += 1

#             # tree = lxml.html.fromstring(html)
#             # print tree
#             # td = tree.cssselect('body.flip > div#page > a')
#             # print next_page_url
#             # for each in next_page_url:
#             #     print each
#             #     if each not in vis:
#             #         vis.add(each)
#             #         Q.append(each)
