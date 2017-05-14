import urllib2
import whois
import builtwith
import os


def getwho(url):
    return whois.whois(url)


def getbuiltwith(url):
    return builtwith.parse(url)


def download(url, user_agent = 'wswp', num_retries = 2):
    print "Downloading: ", url
    headers = ["User-agent", user_agent]
    request = urllib2.Request(url, headers = headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print "Download error: ", e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html

if __name__ == "__main__":
    html = download("http://www.meetup.com/")
    file = open("/Users/luodian/Desktop/test.html","w")
    file.writelines(html)

