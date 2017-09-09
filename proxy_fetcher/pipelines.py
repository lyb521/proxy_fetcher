# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import hashlib

from scrapy import log
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import time
import MySQLdb
import MySQLdb.cursors
import filter

class ProxyFetcherPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool
        self.filter = filter.IPChecker()

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8mb4',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._insert_proxy, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    def _insert_proxy(self, conn, item, spider):
        if item['protocol'] not in ('http', 'https'):
            raise DropItem("Protocol not suitable: %s" % item['protocol'])

        items = self.filter.check(item)
        print items
        if not items:
            raise DropItem("Not available: %s" % item['ip'])

        iphash = self._get_hash_key(items)
        # print iphash
        conn.execute("SELECT * from xb_proxy WHERE 	iphash = '%s'" % iphash)
        ret = conn.fetchone()
        if not ret:
            sql = "INSERT INTO xb_proxy(iphash, ip, port, address, opacity, protocol, ttl, delay, speed, verify_time,crawl_time, source) \
                   VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s',%f, %f, %d, %d, '%s')" % \
                  (iphash, items['ip'], items['port'], items['address'],items['opacity'], items['protocol'], items['ttl'],
                   items['delay'], items['speed'], items['verify_time'], items['crawl_time'], items['source'])
            try:
                conn.execute(sql)
            except:
                print sql
    #
    def _get_hash_key(self,item):
        return hashlib.md5(item['ip'].encode('utf-8')).hexdigest()

    # 异常处理
    def _handle_error(self, failue, item, spider):
        log.err(failue)
