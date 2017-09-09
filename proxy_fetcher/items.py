# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyFetcherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip = scrapy.Field() #ip地址
    port = scrapy.Field()   #端口号
    address = scrapy.Field()    #物理地址
    opacity = scrapy.Field()  #匿名度
    protocol = scrapy.Field()   #协议，http或https
    ttl = scrapy.Field()    #生存时间,至今存活时间
    delay = scrapy.Field()  #响应速度
    speed = scrapy.Field()  #下载速度KB/s
    verify_time = scrapy.Field()    #验证时间
    crawl_time = scrapy.Field() #采集时间
    source = scrapy.Field() #采集来源
