# -*- coding: utf-8 -*-
import scrapy
from proxy_fetcher.items import ProxyFetcherItem
import time
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Ip3366Spider(scrapy.Spider):
    name = "ip3366"
    allowed_domains = ["ip3366.net"]
    start_urls = (
            'http://www.ip3366.net/free/?stype=1',
            'http://www.ip3366.net/free/?stype=2',
            'http://www.ip3366.net/free/?stype=3',
            'http://www.ip3366.net/free/?stype=4',
    )

    def parse(self, response):
        response = response.replace(body=response.body.decode(response.encoding,'ignore'))
        for row in response.xpath('//table/tbody/tr'):
            tds = row.xpath('td')
            if len(tds) == 7:
                item = ProxyFetcherItem()
                item['ip'] = ''.join(tds[0].xpath('text()').extract())
                item['port'] = ''.join(tds[1].xpath('text()').extract())
                item['opacity'] = ''.join(tds[2].xpath('text()').extract())
                item['protocol'] = ''.join(tds[3].xpath('text()').extract()).lower()
                item['address'] = ''.join(tds[5].xpath('text()').extract()).strip('\r\n ')
                item['ttl'] = ''
                item['crawl_time'] = int(time.time())
                item['source'] = self.name
                yield item