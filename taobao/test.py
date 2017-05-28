# -*-coding:utf-8-*-
import re
import requests
from lxml import etree
import re
import sys


url = 'https://s.taobao.com/search'
payload = {'q': 'python'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
resp = requests.get(url, headers = headers, params = payload)
# print resp.text

# urlopen_resp = urllib2.urlopen(url).read()
# print urlopen_resp
# file = open("a.txt","w")
# file.write(str(resp.text.encode('utf-8')))

# resp = resp.text

# resp = etree.HTML(resp)
# hrefs = resp.xpath("//div[contains(@class, 'items')]")
# hrefs = resp.xpath('//a/@href')

print (resp.url)
resp.encoding = 'utf-8'
detail_urls = re.findall(r'"nick":"([^"]+)"',resp.text,re.I)

file = open('a.txt', 'w', encoding = 'utf-8')

# print (detail_urls)

for href in detail_urls:
	# href.encode('utf-8').decode('gbk')
	# file.write(str(href))
    print (href)

file.close()
