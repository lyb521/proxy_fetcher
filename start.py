#!/usr/bin/python

from twisted.internet import reactor,defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from proxy_fetcher.spiders.xici import XiciSpider
from proxy_fetcher.spiders.ipbus import IpbusSpider
from proxy_fetcher.spiders.mimiip import MimiipSpider
from proxy_fetcher.spiders.kdl import KdlSpider
from proxy_fetcher.spiders.goubanjia import GoubanjiaSpider
from proxy_fetcher.spiders.ip3366 import Ip3366Spider

runner = CrawlerRunner(get_project_settings())
dfs = set()
dfs.add(runner.crawl(XiciSpider))
dfs.add(runner.crawl(MimiipSpider))
dfs.add(runner.crawl(IpbusSpider))
dfs.add(runner.crawl(KdlSpider))
dfs.add(runner.crawl(GoubanjiaSpider))
dfs.add(runner.crawl(Ip3366Spider))

defer.DeferredList(dfs).addBoth(lambda _: reactor.stop())
reactor.run()
