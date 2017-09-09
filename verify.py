#!/usr/bin/python
# coding=utf-8
import math

from proxy_fetcher.filter import IPChecker
import config
import httplib
import json
import os
import MySQLdb.cursors
import time
from config import *
import urllib
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def connect():
    return MySQLdb.connect(
        user=configs['db']['user'],
        passwd=configs['db']['passwd'],
        host=configs['db']['host'],
        db=configs['db']['database'],
        charset=configs['db']['charset']
    )


verifier = IPChecker()

if __name__ == '__main__':
    conn = connect()
    cursor = conn.cursor()
    table = configs['db']['table_prefix'] + "proxy"
    cursor.execute("SELECT count(*) as count from "+table)
    ret = cursor.fetchone()
    total = ret[0]
    pagesize = 100
    page = math.ceil(total / pagesize)
    i = 0
    while i <= page:
        conn.close()
        offset = i * pagesize
        conn = connect()
        cursor = conn.cursor()
        sql = "SELECT iphash, ip, port, protocol from "+table+" limit %d,%d" % (offset, pagesize)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            times = int(time.time())
            item = {}
            iphash = row[0]
            item['ip'] = row[1]
            item['port'] = row[2]
            item['protocol'] = row[3]
            items = verifier.check(item)
            print items
            if items:
                print "UPDATE " + table + " SET verify_time = %d WHERE iphash='%s'" % (times, iphash)
                cursor.execute("UPDATE " + table + " SET verify_time = %d WHERE iphash='%s'" % (times, iphash))
            else:
                print "DELETE FROM " + table + " WHERE iphash='%s'" % iphash
                cursor.execute("DELETE FROM " + table + " WHERE iphash='%s'" % iphash)
            conn.commit()
        i += 1