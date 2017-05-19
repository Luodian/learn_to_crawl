#Chapter 1

1. [re.findall作用]("http://blog.csdn.net/cashey1991/article/details/8875213")
2. [sitemap作用]("https://zh.wikipedia.org/wiki/%E7%B6%B2%E7%AB%99%E5%9C%B0%E5%9C%96")
3. [sitemap详细说明](https://www.sitemaps.org/protocol.html#escaping "https://www.sitemaps.org/protocol.html#escaping")
4. [python函数的作用顺序]
```python
def f1():
    f2()

def f2():
  print "blah"

f1()

# 这段代码是合法的，虽然在f1里调用了后面才定义的f2
# 弄清楚这个，需要了解python里函数定义的原理：
# 函数里的语句在函数定义时并不执行，只有在该function being called的时候才执行
```

5.  [正则表达式]("http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html")
6.  re.findall
    findall函数返回的总是正则表达式在字符串中所有匹配结果的列表list，此处主要讨论列表中“结果”的展现方式，即findall中返回列表中每个元素包含的信息。
7.  [路径拼接]("http://www.cnblogs.com/shijiaoyun/p/4863813.html")
8.  # list.pop(obj=list[-1])
    # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值



