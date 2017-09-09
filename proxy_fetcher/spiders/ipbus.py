# -*- coding: utf-8 -*-
import scrapy
from proxy_fetcher.items import ProxyFetcherItem
import time

class IpbusSpider(scrapy.Spider):
    name = "ipbus"
    allowed_domains = ["ip84.com"]
    start_urls = (
            'http://ip84.com/gn',
            'http://ip84.com/pn',
            'http://ip84.com/tm',
            'http://ip84.com/gw',
    )

    def parse(self, response):
        for row in response.xpath('//table/tr'):
            tds = row.xpath('td')
            if len(tds) == 7:
                item = ProxyFetcherItem()
                item['ip'] = ''.join(tds[0].xpath('text()').extract())
                item['port'] = ''.join(tds[1].xpath('text()').extract())
                item['address'] = ''.join(tds[2].xpath('a/text()').extract())
                item['opacity'] = ''.join(tds[3].xpath('text()').extract())
                item['protocol'] = ''.join(tds[4].xpath('text()').extract()).lower()
                item['ttl'] = ''
                item['crawl_time'] = int(time.time())
                item['source'] = self.name
                yield item
