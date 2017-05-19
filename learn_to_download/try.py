import requests
import urllib2

# re = requests.get("http://www.baidu.com")

html = urllib2.urlopen("http://www.baidu.com").read()

print html