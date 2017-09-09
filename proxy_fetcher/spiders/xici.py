# -*- coding: utf-8 -*-
import scrapy
from proxy_fetcher.items import ProxyFetcherItem
import time

class XiciSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["www.xicidaili.com"]
    start_urls = (
        'http://www.xicidaili.com/',
    )

    def parse(self, response):
        for row in response.xpath('//table/tr'):
            tds = row.xpath('td');
            if len(tds) == 8:
                item = ProxyFetcherItem()
                item['ip'] = ''.join(tds[1].xpath('text()').extract())
                item['port'] = ''.join(tds[2].xpath('text()').extract())
                item['address'] = ''.join(tds[3].xpath('text()').extract())
                item['opacity'] = ''.join(tds[4].xpath('text()').extract())
                item['protocol'] = ''.join(tds[5].xpath('text()').extract()).lower()
                item['ttl'] = ''.join(tds[6].xpath('text()').extract())
                item['crawl_time'] = int(time.time())
                item['source'] = self.name
                yield item
