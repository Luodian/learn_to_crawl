import urllib2
import whois
import builtwith
import itertools
import re


def getwho(url):
    return whois.whois(url)


def getbuiltwith(url):
    return builtwith.parse(url)


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

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    # download each link
    for link in links:
        html = download(link)


# 遍历ID的方式进行sitemap的爬取
# maximum number of consecutive download errors allowed
max_errors = 5
# current number of consecutive download errors allowed
num_errors = 0

def easy_download():
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d', % page
        html = None
        if hstml is None:
            num_errors ++
            if (num_errors >= max_errors):
                break
        else:
            num_errors = 0


if __name__ == "__main__":
    # html = download("http://www.meetup.com/")
    # file = open("/Users/luodian/Desktop/test.html", "w")
    # file.writelines(html)
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')

