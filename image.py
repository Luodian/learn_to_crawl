#-*- coding:utf-8 -*-
import re
import requests



def dowmloadPic(html,keyword):
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)

    print '找到关键词:'+keyword+'的图片，现在开始下载图片...'
    for each in pic_url:
        print '正在下载第'+str(i+1)+'张图片，图片地址:'+str(each)
        try:
            pic= requests.get(each, timeout=10)
        except p:
            print '当前图片无法下载'
            continue
        string = 'pictures\\'+keyword+'_'+str(i+ '.jpg'
        #resolve the problem of encode, make sure that chinese name could be store
        fp = open(string.decode('utf-8').encode('cp936'),'wb')
        fp.write(pic.content)
        fp.close()
        i += 1



if __name__ == '__main__':
    word = raw_input("Input key word: ")
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1495029212467_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1495029212467%5E00_703X638&word=%E5%B0%8F%E9%BB%84%E4%BA%BA'
    result = requests.get(url)
    dowmloadPic(result.text,word)