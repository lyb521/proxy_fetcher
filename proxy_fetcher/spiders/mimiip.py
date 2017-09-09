# -*- coding: utf-8 -*-
import scrapy
from proxy_fetcher.items import ProxyFetcherItem
import time

class MimiipSpider(scrapy.Spider):
    name = "mimiip"
    allowed_domains = ["mimiip.com"]
    start_urls = (
        'http://www.mimiip.com/gngao/',
        'http://www.mimiip.com/gnpu/',
        'http://www.mimiip.com/gntou/',
        'http://www.mimiip.com/hw',
    )

    def parse(self, response):
        for row in response.xpath('//table/tr'):
            tds = row.xpath('td')
            if len(tds) == 7:
                item = ProxyFetcherItem()
                item['ip'] = ''.join(tds[0].xpath('text()').extract())
                item['port'] = ''.join(tds[1].xpath('text()').extract())
                item['address'] = ''.join(tds[2].xpath('text()').extract()).strip('\r\n ')
                item['opacity'] = ''.join(tds[3].xpath('text()').extract())
                item['protocol'] = ''.join(tds[4].xpath('text()').extract()).lower()
                item['ttl'] = ''
                item['crawl_time'] = int(time.time())
                item['source'] = self.name
                yield item
