# -*- coding: utf-8 -*-
import scrapy
from proxy_fetcher.items import ProxyFetcherItem
import time
import re

class GoubanjiaSpider(scrapy.Spider):
    name = "goubanjia"
    allowed_domains = ["goubanjia.com"]
    start_urls = (
            'http://www.goubanjia.com/free/gngn/index.shtml',
            'http://www.goubanjia.com/free/gnpt/index.shtml',
            'http://www.goubanjia.com/free/gwgn/index.shtml',
            'http://www.goubanjia.com/free/gwpt/index.shtml',
    )

    def parse(self, response):
        hidden = re.compile(r'<([a-z0-9]*)\s+style\s*=\s*(\'|")display\s*:\s*none;\2>([^<]*)</\1>', re.S)
        pattern = re.compile(r'<([a-z0-9]*)[^>]*>([^<]*)</\1>', re.S)
        for row in response.xpath('//table//tr'):
            tds = row.xpath('td')
            if len(tds) == 10:
                item = ProxyFetcherItem()
                ip_str = ''.join(tds[0].xpath('./child::*').extract())
                ip_str = re.sub(hidden, '', ip_str)
                parts = re.findall(pattern, ip_str)
                item['ip'] = ''.join([part[1] for part in parts])
                item['port'] = ''.join(tds[1].xpath('text()').extract())
                item['opacity'] = ''.join(tds[2].xpath('a/text()').extract())
                item['protocol'] = ''.join(tds[3].xpath('a/text()').extract()).split(',')[0].lower()
                item['ttl'] = ''
                item['address'] = ''.join(tds[4].xpath('a/text()').extract())
                item['crawl_time'] = int(time.time())
                item['source'] = self.name
                yield item
